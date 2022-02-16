import cv2
import plotly.graph_objects as go
import numpy as np

'''
Use this module to plot images using
Plotly library!!

'''
def calc_histogram(image):
    '''
    Use this function to calculate histogram, for
    images with 03 channels RGB.
    
    You need to give a array like image.    
    '''
    assert isinstance(image, (list, np.ndarray)), "Oh no, I can't read this, need be a array-like!"
    
    channels = ['r', 'g', 'b']
    for i, col in enumerate(channels):
        yield cv2.calcHist(
            [image], 
            [i], 
            None, 
            [256], 
            [0, 256]
            )
        
def normalize_data(x):
    normalized = (x-min(x))/(max(x)-min(x))
    return normalized


def _plotly_plot(image, channels, colors):
    
    fig = go.Figure()
    
    for channel in range(channels):
        fig.add_trace(
            go.Histogram(x = image[..., channel].ravel(), opacity=0.5,
                         marker_color = colors[channel],
                         name = f'Channel {channel}'
                         )
        )
        
    fig.update_layout(height=800)
    fig.show()
