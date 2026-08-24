import cv2
# Automatic image stitching using OpenCV's Stitcher class
def stitch_images(image_paths):
    # Load images
    images = [cv2.imread(p )  for p in image_paths]

    #Create stitcher and stitch
    stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
    
    status, pano = stitcher.stitch( images)
    # Check for errors
    if status != cv2.Stitcher_OK:
        print("Stitching failed. Error code:", status)
        return None

    return pano

# Run the stitching if this file is executed directly
if __name__== "__main__":
    # Images in order from left to right
    image_paths = [
        "images/1.jpg",
        "images/2.jpg",
        "images/3.jpg"
    ]

    pano = stitch_images(image_paths)

    if pano is not None :
        cv2.imwrite("output/final_auto_panorama.png", pano)
        print("Panorama saved to")
    else:
        print("Could not generate panorama.")
