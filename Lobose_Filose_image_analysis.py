from matplotlib import pyplot as plt
from skimage.external import tifffile as tiff
from skimage.exposure import rescale_intensity
from skimage.segmentation import watershed , random_walker
from skimage.measure import label , regionprops
from skimage import feature , filters , morphology

from trajalign.traj import Traj
import numpy as np
import os

def tracking( im , labels , path ) :

	os.mkdir( path + '/trajectories/' )

	r = im.shape[ 0 ] # range

	# list all the labels. That is important to define the dataset
	ll = [ l for l in range( 1 , labels.max() + 1 ) if l in labels ]

	# define the dataset
	data = {}
	for l in ll : 
		data[ l ] = np.zeros( shape = ( 5 , r ) , dtype = 'float64' ) + np.nan 

	# track each object labelled in frames ranging from 0 to range( r )
	# and save each element of the trajectory in the dataset
	for i in range( r ) :

		props = regionprops( labels[ i , : , : ] , im[ i , : , : ] )

		for p in props :

			l = p.label
			cm = p.centroid
			area = p.area
			ecc = p.eccentricity

			data[ l ][ 0 , i ] = i # frame number 
			data[ l ][ 1 , i ] = cm[ 1 ] # centroid x
			data[ l ][ 2 , i ] = cm[ 0 ] # centroid y
			data[ l ][ 3 , i ] = ecc # eccentricity
			data[ l ][ 4 , i ] = area # eccentricity

			#print_frame( im , cm , color ) 
	output = {}
	for j in range( len( ll ) ) :

		l = ll[ j ]

		output[ j ] = Traj()
		output[ j ].input_values( 'frames' , data[ l ][ 0 ] ) 
		output[ j ].input_values( 'coord' , [ data[ l ][ 1 ] , data[ l ][ 2 ] ] , unit = 'pxl' ) 
		output[ j ].input_values( 'ecc' , data[ l ][ 3 ] )
		# area is saved under fluorescence intensity
		output[ j ].input_values( 'f' , data[ l ][ 4 ] )

		output[ j ].time( delta_t = 5.03 , unit = 's' )
		output[ j ].save( path + '/trajectories/trajectory_label_' + str( l ) + '.txt' )

	return output

def threshold( im ) :

	t = np.zeros( im.shape , dtype = np.uint ) # thresholded image

	v = filters.threshold_triangle( np.max( im , axis = 0 ) ) 

	t[ im > v ] = 1 
	
	return t 

selem_closing = morphology.ball( 2 ) 
idimage = '016'

im = tiff.imread( idimage + '/' + idimage + '_bkg.tif' )
#im = rescale_intensity( im , in_range = ( 0 , 2**12 - 1 ) , out_range = 'uint16' )

print( 'thresholding' )
t = threshold( im )
print( 'closing' )
tc = morphology.closing( t , selem_closing )
print( 'labelling' )
l = label( tc )

# select the cells. Cells are thresholded regions that are at least
# 100 x 100 pixels wide. Note that the labelling is performed on the 
# 3D stack, so the thresholded region volume is actually bigger than
# 100 x 100 pixels.

print( 'clean labelling' )
good_ids = [ i for i in range( 1 , l.max() + 1 ) if len( l[ l == i ] ) > 10000 ]
gl = np.zeros( shape = l.shape , dtype = l.dtype ) #good label

for i in good_ids :
	gl[ l == i ] = i

print( 'tracking' )
trajectories = tracking( im , gl , idimage + '/' )

