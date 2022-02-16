from PIL import Image
from PIL.ExifTags import TAGS
import numpy as np
import cv2
import matplotlib.colors as mcolors

from utils.matplot_plots import _plot_histogram
from utils.plotly_plots import _plotly_plot

class ReadImage:
    def __init__(self, path):
        self.image = Image.open(path)
        self.shape = self.as_array().shape
        self.bands = self.image.getbands()
        self.format = self.image.format
    
    def get_metadata(self):
        metadata = self.image.getexif()
        infos = {}
        for tag_id in metadata:
            tag = TAGS.get(tag_id, tag_id)
            data = metadata.get(tag_id)

            if isinstance(data, bytes):
                data = data.decode()
                infos[tag] = data

            else:
                infos[tag] = data

        return infos

    def as_array(self) -> 'np.array':
        return np.array(self.image)    

    def display(self):
        return self.image.show()

    def get_histogram(self):
        
        '''
        Calcule the histogram to the read image        
        '''
        image = self.as_array()

        histogram = {}
        for channel in range(len(self.bands)):
            histogram[channel.__str__()] = cv2.calcHist([image],
                                                        [channel],
                                                        None,
                                                        [256],
                                                        [0, 256]
                                                        )

        self.histogram = histogram
        
        return self

    def plot(self, back='matplotlib', **kwargs):
        
        '''
        Use back parameter to select a library to
        plot, you have two choices:
        -> Matplotlib (default)
        -> Plotly
            
        '''
               
        colors = kwargs.get('colors')
                
        if colors is None:
            from random import shuffle
            colors = list(mcolors.TABLEAU_COLORS.values())
            shuffle(colors)
        
        if back == 'matplotlib':
            
            _plot_histogram(self.histogram, colors)

        else:
            
            channels = len(self.bands)            
            _plotly_plot(self.as_array(), channels, colors)
    
            