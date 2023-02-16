"""
This experiment will check the performance of cellpose (0.6.1) on the RPI4.
"""
#import timeit
#from cellpose.model import CellposeModel
import matplotlib.pyplot as plt
import openflexure_microscope_client as ofm_client

microscope = ofm_client.find_first_microscope()
#model = Cellpose()

# Autofocus and acquire an image.
ret = microscope.autofocus()
image = microscope.grab_image_array()

plt.imshow(image[...,0])
plt.show()
#masks, flows, styles, diams = model.eval(image[...,0], diameter=None, channels=[0,0])
#print("done")
