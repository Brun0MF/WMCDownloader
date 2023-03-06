# WMCDownloader
An easy way to download multiple images from Wikimedia Commons.
This library was initially designed to collect images that would be used in training neural networks.
Just indicate the search term and the maximum amount of images and it will start collecting.

## Usage:
> __Note__
> **It is not available in PIP. It is necessary to transfer the file and place it in the main folder.**

### Library

```python

import WMCDownloader as wmcd

wmcd.download_images("Cats", max_images=10)

```
This function takes two arguments, a String with the search term and an Int with the number of images for that term.

For this example, the function will download 10 images of the term "Cats"


### List Downloader

> __Warning__
> **This program needs the library "WMCDownloader" in the same directory.**

```
python WMCListDownloader.py 10 ListExample.txt

```
This program takes two arguments, an Int and a String. The Int represents the number of images per term. The String represents the file path with the list of terms.

For this example, the program will download 10 images of all the terms present in the list of the file "ListExample.txt"
