import matplotlib.pyplot as plt
from skimage import exposure
from skimage.exposure import match_histograms
from skimage.transform import resize
from skimage.feature import hog


def match(source, reference, plot = False):
    
    if source.shape != reference.shape:
        print("Shapes are different, resizing reference...")
        reference = resize(reference, source.shape[:2])   
        print("Reference image as resized!!")   
        
    matched = match_histograms(source, 
                               reference
                               )
    
    if plot:
        fig, axs = plt.subplots(1, 3, figsize=(16,8),
                               sharex=True, sharey=True)
        
        for pos, ax in enumerate(axs.flat):
            ax.set_axis_off()
        
        axs[0].imshow(source)
        axs[0].set_title('Source')
        axs[1].imshow(reference)
        axs[1].set_title('Reference')
        axs[2].imshow(matched)
        axs[2].set_title('Result')
        
        plt.show()
    
    
    return matched


def oriented_gradient(image, plot=False):
    
    fd, hog_image = hog(image, orientations=8, 
                        pixels_per_cell=(16,16),
                        cells_per_block=(1, 1),
                        visualize=True,
                        )
    
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 7))
    
    if plot:
        fig, axs = plt.subplots(1, 2, figsize=(16, 8),
                                sharex=True, sharey=True)
        
        for ax in axs.flat:
            ax.axis('off')
            
        axs[0].imshow(image, cmap=plt.cm.gray)
        axs[0].set_title('Original')
        
        axs[1].imshow(hog_image_rescaled, cmap=plt.cm.gray)
        axs[1].set_title('Histogram of Oriented Gradients')
        
        plt.show()
    
    return hog_image_rescaled
    