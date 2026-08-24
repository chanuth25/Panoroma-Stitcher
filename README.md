# Panorama Stitcher

A Python computer-vision application that automatically creates panoramic images from overlapping photographs. The project implements a **manual image-stitching pipeline using SIFT, FLANN, homography estimation, and RANSAC**, along with an alternative implementation using OpenCV's built-in panorama stitcher.

The project also generates visualizations of detected keypoints, feature matches, and RANSAC inliers to demonstrate how the images are aligned.

## ✨ Features

* 🔍 **SIFT Feature Detection** — Detects distinctive keypoints and extracts feature descriptors.
* 🔗 **FLANN Feature Matching** — Efficiently matches features between overlapping images.
* 🎯 **Lowe's Ratio Test** — Filters out unreliable and ambiguous feature matches.
* 📐 **Homography Estimation** — Determines the geometric transformation between images.
* 🛡️ **RANSAC** — Removes outlier matches and produces a more reliable homography.
* 🖼️ **Image Warping & Stitching** — Aligns images onto a common canvas to create a panorama.
* ✂️ **Automatic Cropping** — Removes unnecessary black borders from the final panorama.
* 📊 **Visualizations** — Generates keypoint, feature-match, and inlier visualizations.
* ⚡ **Automatic Stitching** — Includes an alternative implementation using OpenCV's `Stitcher` class.

---

## 🧠 How It Works

The manual stitching pipeline follows these main steps:

```text
Input Images
     │
     ▼
SIFT Feature Detection
     │
     ▼
Feature Descriptors
     │
     ▼
FLANN Feature Matching
     │
     ▼
Lowe's Ratio Test
     │
     ▼
RANSAC Homography Estimation
     │
     ▼
Image Warping
     │
     ▼
Image Blending
     │
     ▼
Black Border Cropping
     │
     ▼
Final Panorama
```

### 1. Feature Detection

SIFT (**Scale-Invariant Feature Transform**) detects distinctive points in each image and generates descriptors that can be used to identify the same features across different photographs.

### 2. Feature Matching

A **FLANN-based matcher** compares descriptors between overlapping images to find potential corresponding features.

### 3. Ratio Test

Lowe's ratio test filters out ambiguous matches by comparing the distance between the best and second-best matches.

### 4. Homography Estimation

The remaining matches are used to calculate a **homography matrix**, which describes how one image should be transformed to align with another.

### 5. RANSAC

**RANSAC** identifies and removes incorrect feature matches (outliers), resulting in a more reliable homography.

### 6. Warping and Stitching

The images are warped onto a shared canvas and combined to produce a single panoramic image.

### 7. Cropping

Black regions created during image warping are detected and removed from the final panorama.

---

## 📂 Project Structure

```text
panorama-stitcher/
│
├── main.py                 # Runs the manual pairwise stitching pipeline
├── stitcher.py             # ImageStitcher implementation
├── sticher_auto.py         # Automatic OpenCV stitching pipeline
├── visualize.py            # Keypoint and feature-match visualization
├── requirements.txt        # Python dependencies
│
├── images/                 # Input images
│
└── output/                 # Generated panoramas and visualizations
```

> **Note:** `sticher_auto.py` is the current filename in the project. For consistency, it could be renamed to `stitcher_auto.py`.

---

## 🛠️ Technologies

* **Python**
* **OpenCV**
* **NumPy**
* **SIFT**
* **FLANN**
* **RANSAC**
* **Homography**

---

## 📋 Requirements

* Python **3.8+**
* OpenCV
* NumPy
* A sequence of overlapping photographs

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/panorama-stitcher.git
cd panorama-stitcher
```

### 2. Create a virtual environment

Creating a virtual environment is recommended:

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🖼️ Input Images

Create an `images` directory:

```bash
mkdir images
```

Place your overlapping photographs inside the directory.

The current manual pipeline expects:

```text
images/
├── IMG_2740.jpg
├── IMG_2741.jpg
├── IMG_2742.jpg
├── img4.jpg
├── img5.jpg
└── img6.jpg
```

The images should be:

* Taken with sufficient overlap.
* Ordered from **left to right**.
* Similar enough for SIFT to identify common features.

### Automatic Stitching

The automatic OpenCV pipeline currently expects:

```text
images/
├── 1.jpg
├── 2.jpg
└── 3.jpg
```

Update the image paths in the script if you want to use different filenames.

---

## ▶️ Running the Project

### Manual Stitching Pipeline

Run:

```bash
python main.py
```

The manual pipeline processes the images pairwise and generates panoramic results.

Example outputs:

```text
output/
├── final_panorama123.png
├── final_panorama456.png
└── ...
```

It also generates visualizations showing:

* SIFT keypoints
* Feature matches
* RANSAC inliers
* Intermediate stitching results

### Automatic Stitching

OpenCV's built-in panorama stitcher can be run with:

```bash
python sticher_auto.py
```

The resulting panorama is saved as:

```text
output/final_auto_panorama.png
```

---

## 📊 Output Visualizations

The project generates visualizations to help understand the computer-vision pipeline.

### Keypoints

Shows the features detected by SIFT in each image.

### Feature Matches

Displays corresponding features identified between overlapping images.

### RANSAC Inliers

Shows the matches that were considered reliable when calculating the homography.

These visualizations make it easier to evaluate how successfully the images are being aligned.

---

## ⚠️ Important Notes

* Input photographs need sufficient overlap for successful feature matching.
* Images should generally be captured from a similar viewpoint.
* Input images should be ordered from left to right.
* Poor lighting, motion blur, or large changes in viewpoint can reduce matching accuracy.
* The manual pipeline currently uses specific image filenames, so update the paths in `main.py` when using different images.
* Make sure the `output/` directory exists before running the scripts if it is not created automatically.

---

## 🎯 Project Objective

The goal of this project was to explore fundamental **computer-vision techniques for panoramic image generation** by implementing the major steps of an image-stitching pipeline rather than relying solely on a pre-built panorama solution.

The project demonstrates practical applications of:

* Feature detection
* Feature description
* Feature matching
* Outlier rejection
* Homography estimation
* Perspective transformation
* Image stitching

---

## 🔮 Future Improvements

Potential improvements include:

* Automatically detecting and loading images from the `images/` directory.
* Supporting an arbitrary number of input images.
* Automatically ordering images based on feature overlap.
* Improving seam blending between images.
* Adding a graphical user interface.
* Adding command-line arguments for input/output directories.
* Renaming `sticher_auto.py` to `stitcher_auto.py`.
* Adding automated tests for the stitching pipeline.

---

## 👤 Author

**Chanuth Pathirana**

Computer Engineering — Software Engineering
Toronto Metropolitan University

---

## 📄 License

This project was developed as an academic/portfolio project.
