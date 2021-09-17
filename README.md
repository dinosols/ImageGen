# ImageGen
Stitches multiple image layers together into one image.

## Run
`usage: stitch.py [-h] <backgrounds_dir> <dinos_dir> <traits_dir> <texture_file> <output_dir>`

## Functionality
Dinosols Image Generator tool combines multiple layers of PNG images together into a single image based on input directories for each layer. The basic ordering of layers (from bottom to top) is as follows:
* Background
* Dinosol colored base
* Traits super-directory containing subdirectories for each type of trait (e.g. scars, glasses, necklace, etc.)
* Texture image applied over the whole image (Dinosols uses a half-tone texture)

The image generation script comprehensively generates resulting PNG images for all combinations of the above but also inserts a None option for each trait so combinations will exist lacking in traits as well.