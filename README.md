# Image Basic Analysis

## Description:

The package Image Basic Analysis have two modules **processing** and **utils**.

### Processing Module

#### This module contain two files:

#### **histogram.py**

- **match:** this function use two image, source/reference, and transform histogram color of source image like reference image.

- **oriented_gradient:** this function take a one image and return a histogram oriented gradient of the image.

**imagereader.py**

Contain a class **ReadImage**, this class return a group of data from image like:

- Shape
- Number of Bands
- Format
- Metadata
- Histogram (can plot or just take values)

And can convert image like a numpy array or just display image

**Utils Module:** contain the functions to plot histogram using imagereader.py in processing module.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Image Basic Analysis

```bash
pip install image_basic
```

## Usage

### histogram.py: match

```python
from image_basic.processing import histogram

source_image = 'path_to_source_image'	# Image that you want transform
reference_image = 'path_to_referece_image' # Image Histogram to use like reference

matched = histogram.match(source_image, reference_image, plot = True)
# If you don't can see the result remove plot argument or put like False (default)
```

### histogram.py: oriented_gradient

``` python	
from image_basic.processing import histogram
from image_basic.processing import imagereader as ir

image = ir.ReadImage('image_path').as_array()
hog_image = histogram.oriented_gradient(image)
# If you want plot the result you can add the plot argument and set like True

```

## Author

Alexandre Carrascosa

## License
[MIT](https://choosealicense.com/licenses/mit/)