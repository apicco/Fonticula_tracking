from trajalign.traj import Traj
from trajalign.average import load_directory
from matplotlib import pyplot as plt
from scipy.stats import median_absolute_deviation as mad
from scipy.stats import ttest_ind as ttest
from scipy.stats import mannwhitneyu as utest

import numpy as np
import seaborn as sns
import os

print(  '../Snakes/5s_int-10%FRAP-5s012/snakes_1_2/Trajectories/' )
path =  '../Snakes/5s_int-10%FRAP-5s012/snakes_1_2/Trajectories/'
ts = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

print(  '../Snakes/5s_int-10%FRAP-5s011/Snake_1/Trajectories/' )
path =  '../Snakes/5s_int-10%FRAP-5s011/Snake_1/Trajectories/'
tmp =  load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_int-10%FRAP-5s010/Snake_Left/Trajectories/' )
path =  '../Snakes/5s_int-10%FRAP-5s010/Snake_Left/Trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_int-10%FRAP-5s010/Snake_Right/Trajectories/' )
path =  '../Snakes/5s_int-10%FRAP-5s010/Snake_Right/Trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-10%_5sint_005/trajectories/' )
path =  '../Snakes/5s_488FRAP-10%_5sint_005/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-10%_5sint_006/snake_right/trajectories/' )
path =  '../Snakes/5s_488FRAP-10%_5sint_006/snake_right/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-10%_5sint_006/snake_top_left/trajectories/' )
path =  '../Snakes/5s_488FRAP-10%_5sint_006/snake_top_left/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-10%_5sint_007a/trajectories/' )
path =  '../Snakes/5s_488FRAP-10%_5sint_007a/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-10%_5sint_007b/Snake_left/trajectories/' )
path =  '../Snakes/5s_488FRAP-10%_5sint_007b/Snake_left/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-10%_5sint_007b/Snake_right/trajectories/' )
path =  '../Snakes/5s_488FRAP-10%_5sint_007b/Snake_right/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-10%_5sint_007c/Snake_left/trajectories/' )
path =  '../Snakes/5s_488FRAP-10%_5sint_007c/Snake_left/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-10%_5sint_007c/Snake_right/trajectories/' )
path =  '../Snakes/5s_488FRAP-10%_5sint_007c/Snake_right/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-100%_5sint_000/Snake_left/trajectories/' )
path =  '../Snakes/5s_488FRAP-100%_5sint_000/Snake_left/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print(  '../Snakes/5s_488FRAP-100%_5sint_000/Snake_right/trajectories/' )
path =  '../Snakes/5s_488FRAP-100%_5sint_000/Snake_right/trajectories/'
tmp = load_directory( path , # snake (collective)
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula snakes"
		)

for t in tmp : ts.append( t )

print( len( ts ) )

# single cells data

print(  '../Single_cells_on_snake_movie/trajectories/' )
path =  '../Single_cells_on_snake_movie/trajectories/'
tc = load_directory( path ,  # single cell
		pattern = 'x' ,
		comment_char = "%%" , 
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		dt = 5 , 
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		notes = "fonticula single cells"
		)

filter_length = 15
scale_snakes = 6.45 / 20 

def extract_velocities( t ) :

	v = []
	D = []
	v_step = []
	
	l = len( t ) 
	for i in range( l ) :
	
		# select only trajectories long enough for a reliable msd analysis
		if len( t[ i ] ) >= filter_length :
		
			v_tmp , D_tmp , m = t[ i ].msdfit( sel = 6 , scale = scale_snakes , return_data = True )
	
			# if diffusion D is negative, something went wrong, dump this trajectory
			if D_tmp[ 0 ] > 0 :
				
				v.append( v_tmp[ 0 ] )
				D.append( D_tmp[ 0 ] )
	
				#compute the individual speed steps
				for j in range( len( t[ i ] ) -1 ) :
	
					d = np.sqrt( ( t[ i ].coord()[ 0 ][ j ] - t[ i ].coord()[ 0 ][ j + 1 ] ) ** 2 + ( t[ i ].coord()[ 1 ][ j ] - t[ i ].coord()[ 1 ][ j + 1 ] ) ** 2 ) * scale_snakes 
					v_step.append( d / float( t[ i ].annotations()[ 'delta_t' ] ) ) 
	
	return v , D , v_step

# ------------------ PLOTS --------------------

color_lobose = '#f00f0f'
color_filose = '#0e9594'
color_collective = '#ff9500'
color_singlecell = '#562c2c'
alpha = 0.7 
figsize = ( 6.5 , 5.5 )

# plot histograms for filose and lobose

exec( open( "../60x_liquid_culture/60x-phase for tracking01/filo-lobo-speeds.py").read() ) #this file is now named Lobose_Filose_velocities.py in the repsitory

# plot speeds 

f , ax = plt.subplots( 1 , 1 , figsize = figsize )

ax.hist( v_l_step , density = False , log = False , color = color_lobose , label = 'Lobose' , alpha = alpha )
ax.hist( v_f_step , density = False , log = False , color = color_filose , label = 'Filose' , alpha = alpha )
ax.set_xlabel( '$\\mu m/s$' , fontsize = 20 )
ax.set_ylabel( 'Frequency' , fontsize = 20 )
ax.set_title( 'Velocity (during exposure time)' , fontsize = 20 )
ax.set_xlim( 0 , 1.3 )
ax.legend( fontsize = 20 )

plt.savefig( 'Filose_VS_Lobose_cells_speed.pdf' )


# plot velocities 

f , ax = plt.subplots( 1 , 1 , figsize = figsize )

ax.hist( v_l , density = False , log = False , color = color_lobose , label = 'Lobose' , alpha = alpha )
ax.hist( v_f , density = False , log = False , color = color_filose , label = 'Filose' , alpha = alpha )
ax.set_xlabel( '$\\mu m/s$' , fontsize = 20 )
ax.set_ylabel( 'Frequency' , fontsize = 20 )
ax.set_title( 'Velocity (during trajectory time)' , fontsize = 20 )
ax.set_xlim( 0 , 0.3 )
ax.legend( fontsize = 20 )

plt.savefig( 'Filose_VS_Lobose_cells_velocity.pdf' )

# compute average velocity

velocity_lobose = []
velocity_lobose.append( np.nanmedian( v_l ) )
vm = mad( np.log( v_l ) , nan_policy = 'omit' )#, scale = 'normal' )
velocity_lobose.append( velocity_lobose[ 0 ] * vm / np.sqrt( len( v_l ) ) )

velocity_filose = []
velocity_filose.append( np.nanmedian( v_f ) )
vm = mad( np.log( v_f ) , nan_policy = 'omit' )#, scale = 'normal' )
velocity_filose.append( velocity_filose[ 0 ] * vm / np.sqrt( len( v_f ) ) )


# plot average velocity summary

f , ax = plt.subplots( 1 , 1 , figsize = figsize )

ax.bar( 0 , velocity_lobose[ 0 ] , color = color_lobose , alpha = alpha , label = 'Lobose' )
ax.errorbar( 0 , velocity_lobose[ 0 ] , velocity_lobose[ 1 ] , color = color_lobose , ls = '' , marker = '' , capsize = 10 )
ax.bar( 1 , velocity_filose[ 0 ] , color = color_filose , alpha = alpha , label = 'Filose' )
ax.errorbar( 1 , velocity_filose[ 0 ] , velocity_filose[ 1 ] , color = color_filose , ls = '' , marker = '' , capsize = 10 )
ax.plot( [ 0 , 1 ] , [ 0.142 , 0.142 ] , color = 'black' )
ax.text( 0.51 , 0.14 , '$****$' , fontsize = 24 , ha = 'center' )
ax.set_ylabel( '$\\mu m/s$' , fontsize = 20 )
ax.set_ylim( 0 , 0.155 )
ax.set_xticklabels( [ ] )
ax.set_xticks( [ ] )
ax.set_title( 'Median velocity (during trajectory time)' , fontsize = 20 )
ax.legend( fontsize = 20 )

plt.savefig( 'Filose_VS_Lobose_cells_velocity_summary.pdf' )

print( 'is the Filose and Lobose velocity the same?' )
print( 'velocity ttest' )
tt = ttest( v_l , v_f , nan_policy = 'omit' )
print( tt ) 
print( 'velocity utest' )
ut = utest( v_l , v_f , alternative = 'two-sided' )
print( ut ) 

#----------------------------------------------------------------------------------------------------------

# plot collectives vs single cells

vc , Dc , vc_step = extract_velocities( tc ) # single cell
vs , Ds , vs_step = extract_velocities( ts ) # snake (collective)

print( len( vs ) )

f , ax = plt.subplots( 1 , 1 , figsize = figsize )

ax.hist( vs_step , density = False , log = False , color = color_collective , label = 'Collectives' , alpha = alpha )
ax.hist( vc_step , density = False , log = False , color = color_singlecell , label = 'Single cells' , alpha = alpha )
ax.set_xlabel( '$\\mu m/s$' , fontsize = 20 )
ax.set_ylabel( 'Frequency' , fontsize = 20 )
ax.set_title( 'Velocity (during exposure time)' , fontsize = 20 )
ax.set_xlim( 0 , 1.3 )
ax.legend( fontsize = 20 )

plt.savefig( 'collectives_VS_single_cells_speed.pdf' )

# plot velocities

f , ax = plt.subplots( 1 , 1 , figsize = figsize )

ax.hist( vs , density = False , log = False , color = color_collective , label = 'Collectives' , alpha = alpha )
ax.hist( vc , density = False , log = False , color = color_singlecell , label = 'Single cells' , alpha = alpha )
ax.set_xlabel( '$\\mu m/s$' , fontsize = 20 )
ax.set_ylabel( 'Frequency' , fontsize = 20 )
ax.set_title( 'Velocity (during trajectory time)' , fontsize = 20 )
ax.set_xlim( 0 , 0.3 )
ax.legend( fontsize = 20 )

plt.savefig( 'collectives_VS_single_cells_velocity.pdf' )


# compute average speed

speed_snake = []
speed_snake.append( np.nanmedian( vs_step ) )
sm = mad( np.log( vs_step ) , nan_policy = 'omit' )#, scale = 'normal' )
speed_snake.append( speed_snake[ 0 ] * sm )

print( speed_snake )

speed_cell = []
speed_cell.append( np.nanmedian( vc_step ) )
sm = mad( np.log( vc_step ) , nan_policy = 'omit' )#, scale = 'normal' )
speed_cell.append( speed_cell[ 0 ] * sm )

print( speed_cell )

# compute average velocity

velocity_snake = []
velocity_snake.append( np.nanmedian( vs ) )
vm = mad( np.log( vs ) , nan_policy = 'omit' )#, scale = 'normal' )
velocity_snake.append( velocity_snake[ 0 ] * vm / np.sqrt( len( vs ) ) )

diffusion_snake = []
diffusion_snake.append( np.nanmedian( Ds ) )
Dm = mad( np.log( Ds ) , nan_policy = 'omit' )#, scale = 'normal' )
diffusion_snake.append( diffusion_snake[ 0 ] * Dm  / np.sqrt( len( Ds ) ) )

print( 'velocity collective' )
print( velocity_snake )
print( 'n: ' + str( len( vs ) ) )
print( 'diffusion collective' )
print( diffusion_snake )
print( 'n: ' + str( len( Ds ) ) )

velocity_cell = []
velocity_cell.append( np.nanmedian( vc ) )
vm = mad( np.log( vc ) , nan_policy = 'omit' )#, scale = 'normal' )
velocity_cell.append( velocity_cell[ 0 ] * vm / np.sqrt( len( vc ) ) )

diffusion_cell = []
diffusion_cell.append( np.nanmedian( Dc ) )
Dm = mad( np.log( Dc ) , nan_policy = 'omit' )#, scale = 'normal' )
diffusion_cell.append( diffusion_cell[ 0 ] * Dm  / np.sqrt( len( Dc ) ) )

print( 'velocity single cell' )
print( 'n: ' + str( len( vc ) ) )
print( velocity_cell )
print( 'diffusion single cell' )
print( diffusion_cell )
print( 'n: ' + str( len( Dc ) ) )

# plot average velocity for snake and single cells

f , ax = plt.subplots( 1 , 1 , figsize = figsize )

ax.bar( 0 , velocity_snake[ 0 ] , color = color_collective , alpha = alpha , label = 'Collectives' )
ax.errorbar( 0 , velocity_snake[ 0 ] , velocity_snake[ 1 ] , color = color_collective , ls = '' , marker = '' , capsize = 10 )
ax.bar( 1 , velocity_cell[ 0 ] , color = color_singlecell , alpha = alpha , label = 'Single cells' )
ax.errorbar( 1 , velocity_cell[ 0 ] , velocity_cell[ 1 ] , color = color_singlecell , ls = '' , marker = '' , capsize = 10 )
ax.plot( [ 0 , 1 ] , [ 0.203 , 0.203 ] , color = 'black' )
ax.text( 0.51 , 0.20 , '$****$' , fontsize = 24 , ha = 'center' )
ax.set_ylabel( '$\\mu m/s$' , fontsize = 20 )
ax.set_ylim( 0 , 0.22 )
ax.set_xticklabels( [ ] )
ax.set_xticks( [ ] )
ax.set_title( 'Median velocity (during trajectory time)' , fontsize = 20 )
ax.legend( fontsize = 20 )

plt.savefig( 'collectives_VS_single_cells_velocity_summary.pdf' )

# stats

print( 'velocity ttest' )
tt = ttest( vs , vc , nan_policy = 'omit' )
print( tt ) 
print( 'velocity utest' )
ut = utest( vs , vc , alternative = 'two-sided' )
print( ut ) 
print( 'speed utest' )
ut_step = utest( vs_step , vc_step , alternative = 'two-sided' )
print( ut_step ) 


