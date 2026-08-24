import cv2
# Visualization utilities for keypoints and matches
def visualize_keypoints(img, keypoints, path):
    out = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0))
    cv2.imwrite(path, out)
 # Visualize matches between two images   
def visualize_matches(imgA, kp1, imgB, kp2, matches, path):
    out = cv2.drawMatches(imgA, kp1, imgB, kp2, matches, None,
                          flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imwrite(path, out)
 # Visualize inlier matches after RANSAC   
def visualize_inliers(imgA, kp1, imgB, kp2, inliers, path):
    out = cv2.drawMatches(imgA, kp1, imgB, kp2, inliers, None,
                          flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
    cv2.imwrite(path, out)
