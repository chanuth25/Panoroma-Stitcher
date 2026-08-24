# Panorama Stitcher

A Python computer-vision project that creates panoramic images by detecting and matching visual features across overlapping photographs. It includes a manual SIFT/FLANN/RANSAC stitching pipeline, OpenCV's automatic panorama stitcher, and utilities for visualizing keypoints and feature matches.

## Repository title

**Panorama Stitcher**

Suggested repository name: `panorama-stitcher`

## Features

- Detects image features with SIFT.
- Matches descriptors with a FLANN-based matcher.
- Filters matches with Lowe's ratio test.
- Estimates image alignment using a RANSAC homography.
- Warps and blends images into a panorama.
- Crops black borders from stitched output.
- Saves keypoint, match, and inlier visualizations.
- Provides an automatic stitching option through OpenCV's `Stitcher` class.

## Project structure

```text
.
├── main.py              # Runs the manual pairwise stitching pipeline
├── stitcher.py          # ImageStitcher implementation
├── sticher_auto.py      # Automatic OpenCV stitching pipeline
├── visualize.py         # Keypoint and match visualization helpers
├── requirements.txt     # Python dependencies
├── images/              # Input images; add this directory locally
└── output/              # Generated panoramas and visualizations
```

## Requirements

- Python 3.8 or newer
- OpenCV
- NumPy
- A sequence of overlapping images, ordered from left to right

Install the dependencies with:

```bash
python -m pip install -r requirements.txt
```

## How to run

### 1. Set up the environment

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/panorama-stitcher.git
cd panorama-stitcher

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# Install dependencies
python -m pip install -r requirements.txt
```

### 2. Prepare input images

Create an `images` directory and add your overlapping photos:

```bash
mkdir -p images
```

Place your images in `images/` and update the filenames in the scripts as needed. The current `main.py` expects:

```text
images/IMG_2740.jpg
images/IMG_2741.jpg
images/IMG_2742.jpg
images/img4.jpg
images/img5.jpg
images/img6.jpg
```

The automatic script (`sticher_auto.py`) expects:

```text
images/1.jpg
images/2.jpg
images/3.jpg
```

### 3. Create the output directory

```bash
mkdir -p output
```

### 4. Run the manual stitching pipeline

```bash
python main.py
```

Outputs:

- `output/final_panorama123.png`
- `output/final_panorama456.png`
- Keypoint, match, and inlier visualizations for each step.

### 5. Run the automatic stitching pipeline

Edit `sticher_auto.py` if you want to change the input image paths, then run:

```bash
python sticher_auto.py
```

Output:

- `output/final_auto_panorama.png`

## Important notes

- Images must overlap sufficiently for reliable feature matching.
- Input images should be ordered from left to right.
- The manual pipeline currently checks that the first three images load successfully; verify all six paths before running both sequences.
- The automatic script filename is `sticher_auto.py` as currently provided; consider renaming it to `stitcher_auto.py` for consistency.

## How it works

1. SIFT detects keypoints and computes descriptors in each image.
2. FLANN finds candidate descriptor matches.
3. Lowe's ratio test removes ambiguous matches.
4. RANSAC estimates a homography between the images.
5. The second image is warped onto a larger canvas.
6. The images are blended and black borders are cropped.
