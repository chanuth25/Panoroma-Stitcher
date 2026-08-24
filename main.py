import cv2
from stitcher import ImageStitcher

#MAKE SURE IMAGES ARE LEFT TO RIGHT OR CODE WILL NOT RUN PROPERLY
def main():
    stitcher = ImageStitcher(output_dir="output")
# Load images
    img1= cv2.imread("images/IMG_2740.jpg")
    img2 = cv2.imread("images/IMG_2741.jpg")
    img3 = cv2.imread("images/IMG_2742.jpg")
    img4= cv2.imread("images/img4.jpg")
    img5 = cv2.imread("images/img5.jpg")
    img6 = cv2.imread("images/img6.jpg")
# Check if images are loaded
    if img1 is None or img2 is None or img3 is None:
        print("Error: One or more images could not be loaded. Please check the file paths.")
        return
# Stitch images pairwise
    print("\n Stitching 1 +2 ")
    s12 = stitcher.stitch_pair(img1,img2, "12")
# Stitch the result with the third image
    print("\n Stitching (1+2) + 3 ")
    final = stitcher.stitch_pair(s12 , img3, "123")
# Save final panorama
    cv2.imwrite("output/final_panorama123.png",final)
    print("\n Panorama saved")

# Stitch images pairwise
    print("\n Stitching 4 +5 ")
    s45 = stitcher.stitch_pair(img4,img5, "45")
# Stitch the result with the third image
    print("\n Stitching (4+5) + 6 ")
    final = stitcher.stitch_pair(s45 , img6, "456")
# Save final panorama
    cv2.imwrite("output/final_panorama456.png",final)
    print("\n Panorama saved")

if __name__ == "__main__":
    main()
