# Image Set Preprocessor

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This mini script / cli tool scans recursively through a directory of images and removes the ones below a certain preset threshold of height and width, then it resizes the images that did not get discarded into the average height and the average width of this same group of images that passed the dimension thresholds to normalize the set.
And the resulting photos are saved in a separate directory while maintaining the same folder structure as the input directory.

## Getting Started <a name = "getting_started"></a>

Clone the script to your working directory where your directory of images is located and run.

### Prerequisites

You might have to install tqdm package if you don't already have it (progress bar package).

## Usage <a name = "usage"></a>

`python3 prep-cli.py <width-threshold> <height-threshold> <source-directory> <output-directory>`

### Example

`python3 prep-cli.py 800 800 Camera Finalized`