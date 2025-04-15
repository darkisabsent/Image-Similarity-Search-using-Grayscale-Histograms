# Image Similarity Search using Grayscale Histograms

## Description
This project is a Python-based implementation of an image similarity search system. It uses **grayscale histograms** to describe images and calculates the **Euclidean distance** between histograms to determine similarity. The system indexes a collection of images and allows users to query the most similar images to a given input image.

## Features
- Indexes images in a directory by calculating their grayscale histograms.
- Finds the most similar images to a query image based on histogram similarity.
- Outputs the top N most similar images, sorted by similarity.

## How It Works
1. **Grayscale Histogram Calculation**:
   - Each image is converted to grayscale.
   - A histogram is computed to represent the distribution of pixel intensities (0-255).
2. **Indexing**:
   - All images in the specified directory are indexed by their histograms.
3. **Similarity Search**:
   - The histogram of the query image is compared to the indexed histograms using the **Euclidean distance**.
   - The closest matches are returned as the most similar images.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/darkisabsent/Image-Similarity-Search-using-Grayscale-Histograms.git
   pip install -r requirements.txt
   python run.py
