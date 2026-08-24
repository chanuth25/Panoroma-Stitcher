import cv2
import numpy as np
from visualize import visualize_keypoints, visualize_matches, visualize_inliers

# Image Stitcher Class
class ImageStitcher:
    # Initialize with output directory
    def  __init__ (self, output_dir="output"):
        self.output_dir = output_dir
        self.sift = cv2.SIFT_create()
    # Detect keypoints and compute descriptors
    def  detect_and_compute(self, img):
        keypoints, descriptors = self.sift.detectAndCompute(img, None)
        return keypoints, descriptors
    # Match features between two sets of descriptors
    def match_features(self, desc1, desc2):
        if desc1 is None or desc2 is None:
            print("No descriptors found.")
            return [ ]
        # Convert to float32
        desc1 = np.float32(desc1)
        desc2 = np.float32(desc2)
        
        index_params = dict(algorithm=1, trees=5)
        search_params = dict(checks=50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(desc1, desc2, k=2)
        # Apply Lowe's ratio test
        good = []
        
        # 0.8 ratio failed chnage ratio
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)

        print(f"✔ Good matches: {len(good)}")
        return good
    # Compute homography using RANSAC
    def compute_homography ( self , kp1,  kp2 , matches):
        if len(matches) < 4:
            print("Not enough matches for homography.")
            return None, None

        pts1 = np.float32([kp1[ m.queryIdx].pt for m in matches])
        pts2= np.float32([kp2[m.trainIdx].pt  for m in matches])

        # RANSAC threshold should be increased
        H, mask = cv2.findHomography(pts2, pts1, cv2.RANSAC, 10.0)
        return H, mask
    # #
    def blend_images(self, imgA, warpedB):
        hA, wA = imgA.shape[:2]
        hB, wB = warpedB.shape[:2]

        # Expand imgA to warpedB size
        canvas = np.zeros_like(warpedB)
        canvas[0:hA, 0:wA] = imgA

        ##Mask for where warpedB has valid pixels (not black)
        gray = cv2.cvtColor(warpedB, cv2.COLOR_BGR2GRAY)
        mask = gray > 0

        # Blend
        canvas[mask] = warpedB[mask]

        return canvas
    
    def crop_black(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
        coords = cv2.findNonZero(thresh)
        x, y,  w, h =cv2.boundingRect(coords)
        return img[y:y+h, x:x+w]
    
    
    # Stitch two images together
    def stitch_pair(self, imgA, imgB, tag="pair"):
        kp1, desc1 = self.detect_and_compute(imgA)
        kp2, desc2 = self.detect_and_compute(imgB)
        
        visualize_keypoints(imgA, kp1, f"{self.output_dir}/kp_A_{tag}.png")
        visualize_keypoints(imgB, kp2, f"{self.output_dir}/kp_B_{tag}.png")
    
    
    
        matches = self.match_features(desc1, desc2)
        visualize_matches(imgA, kp1, imgB, kp2, matches, f"{self.output_dir}/matches_{tag}.png")
        H, mask = self.compute_homography(kp1, kp2, matches)
        if H is None:
            print("Homography failed — returning imgA.")
            return imgA

        inliers = [matches[i] for i in range(len(matches)) if mask[i] == 1]
        visualize_inliers(imgA, kp1, imgB, kp2, inliers, f"{self.output_dir}/inliers_{tag}.png")
        # will only work if images are left to right. MAKE SURE IMAGES ARE LEFT TO RIGHT
        height = max(imgA.shape[0], imgB.shape[0])
        width = imgA.shape[1]+ imgB.shape[1]

        warpedB = cv2.warpPerspective(imgB, H, (width, height))
        # Proper blending
        result = self.blend_images(imgA, warpedB)
        # Crop large black areas
        result = self.crop_black(result)
        return result
