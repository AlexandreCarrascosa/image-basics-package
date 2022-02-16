import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def _plot_histogram(hist, colors):
        
    for key, value in hist.items():
        
        key = int(key)
        
        plt.fill(value,
                    color = colors[key],
                    label = f'Channel {key}',
                    alpha = 0.5)       

    plt.xlim([0, 256])
    plt.grid(True)
            
    plt.legend()
    plt.show()

