# Sheep Detection Project

This repository contains several scripts based on the pipeline proposed by [Ankan Ghosh](https://learnopencv.com/moving-object-detection-with-opencv/).

## Purpose

The purpose of this project is the smart detection of sheep movement in static scenes, using a straightforward approach of background removal and thresholding.

## Description

This project applies the pipeline to videos of sheep, where the camera is positioned overhead, capturing their backs. The goal is to detect when a sheep is in the scene to start recording and stop recording as soon as the sheep leaves the scene.

## Features

- Motion detection using background subtraction.
- Application of thresholding for object segmentation.
- Identification and counting of sheep in the scene.
- Automatic start and stop of video recording based on the presence of sheep.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Anth0nYM/sheep-detection.git
    cd sheep-detection
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Scripts

- ``crop.py``: Crop videos
- ``video.py``: Detect movement from a static scenario
