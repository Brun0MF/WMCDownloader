# WMCDownloader
An easy way to download multiple images from Wikimedia Commons.
This library was initially designed to collect images that would be used in training neural networks.
Just indicate the search term and the maximum amount of images and it will start collecting.

## Usage:
**It is not available in PIP. It is necessary to transfer the file and place it in the main folder.**

```python

import WMCDownloader as wmcd

wmcd.download_images("Cats", max_images=10)

```

## Available Functions
**download_images(**{Search Term(String)} **)**

