# Fonticula_tracking
A collection of the image analysis macros and tracking algorithm used to track Fonticula dynamics. 

_Note that the python script are meant to detail the algorithms but the paths where the data are stored aren't mantained. You should update those to your environment, if you want the scripts to run._

# Tracking of Lobose and Filose dynamics.

We tracked the dynamics of Filose and Lobose single cells in liquid culture imaged with phase-contrast microscopy. In these images, cells appear slightly darker than the surrounding medium, and a bright halo surrounds them, making their thresholding hard. Therefore, we first processed the images so that the cells appear as bright and well-defined shapes that can be easily thresholded and thus tracked. To do so, we converted the images into 32-bit, then we inverted the LUT, and we performed a local background subtraction using a kernel radius of 35 pixels. The local background subtraction made cells stand out as bright shapes, while the LUT inversion made the bright halo look dark, enhancing the boundary of the cell shapes. The resulting images were ideal for thresholding and tracking. _See file Lobose_Filose_macro.txt_.

Cell thresholding and tracking were performed in python, using the Scikit Image library (https://scikit-image.org/). The trajectories were collections of centres of mass positions of the shapes of the thresholded cells over time. We use the Trajalign library (http://apicco.github.io/trajectory_alignment/; Picco and Kaksonen, 2017) to perform trajectory handling and analysis. 

_See files Lobose_Filose_image_analysis.py, Lobose_Filose_velocities.py, and analysis.py for the plotting_.

# Tracking of single cells and collectives. 

We tracked single cells and collectives dynamics by following their vacuole dynamics, which appears dark in the brightfield images acquired with a 20x.  
We used Fiji/ImageJ to perform the tracking.
In Fiji/ImageJ, we converted the images to 32-bit and added a small float (0.01). We then computed the log transform of the image. The small float prevented pixels from 0 intensity to diverge in the log transform. We then inverted the image by multiplication by -1. Now the dark vacuoles appear as bright spots. We background-subtracted the image with a rolling ball algorithm using a kernel radius of 9 pixels. Finally, we performed a Gaussian blur filter with kernel 2 to make vacuoles look more like spots to ease their recognition by the tracking algorithm. 

We tracked spot dynamics with Particle Tracker (Mosaic) using the following parameters: Radius = 7, Cutoff = 0, Percentile = 0.4, Linking range = 3, Displacement = 10. 

_See analysis.py for the velocity quantifications and plotting._

