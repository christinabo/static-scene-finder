# static-scene-finder
Find static (unchanged) scenes in a sequence of images.

Given a sequence of images, detect "scenes" or set of consecutive images that are unchanged or are slightly changing.
This is useful to detect static content in a sequence of images.

## How to use
Run the static_scene_finder function on the static_scene_finder.py file, given a folder where your images are kept.

## How it works
Given a set of images:
* Sorts the images according to their date taken (using the EXIF metadata)
* Computes the hashes of pairs of consecutive images using the dhash module
* Computes the Hamming distance of the consecutive hashes
* Given the list of Hamming distances, detects successive numbers (groups) that differ mo more than a given threshold
* Finds the indexes of the images that constitute these groups

Any feedback is appreciated!
