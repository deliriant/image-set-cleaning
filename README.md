# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This mini script scans recursively through a directory of images and removes the ones below a certain preset threshold of hight and width.
Then it resizes the images that did not get discarded, into the average height and the average width of this same group of images that passed the dimension thresholds to normalize the set.

## Getting Started <a name = "getting_started"></a>

Clone the script to your working directory where your directory of images is located and run.

### Prerequisites

You might have to install tqdm package if you don't already have it (progress bar package).

## Usage <a name = "usage"></a>

python3 preprocessing.py
