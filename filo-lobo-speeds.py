from trajalign.traj import Traj
from matplotlib import pyplot as plt
from matplotlib import gridspec as gspec
import numpy as np

f = {} # filos
l = {} # lobos
n = {} # n.c.

path = '/Users/andreapicco/Google Drive/RESEARCH/FONTICULA/Fonticula-speeds/60x_liquid_culture/60x-phase for tracking01/'

def plot_the_msd( d , file_name ) :

	p = np.poly1d( d[ 'p' ] )
	
	fig = plt.figure()
	plt.errorbar( d[ 'x' ] , d[ 'y' ] , yerr = d[ 'err' ] , ls = '' , marker = 's' )
	plt.plot( d[ 'x' ] , p( d[ 'x' ] ) , label = "$y = {:.2f} x ** 2 + {:.2f} x $".format( d[ 'p' ][ 0 ] , d[ 'p' ][ 1 ] ) )
	plt.xlabel( '$\\Delta t$' )
	plt.ylabel( '$MSD$ $(\\mu m^2)$' )
	plt.legend()
	plt.savefig( file_name )
	plt.close()


# -------- LOBOS ---------
# movie 005

l[ 0 ] = Traj( movie = '005.tif' )
l[ 0 ].load( path + '005/trajectories/trajectory_label_1.txt' )
l[ 0 ] = l[ 0 ].extract( range( 0 , 50 ) )

l[ 1 ] = Traj( movie = '005.tif' )
l[ 1 ].load( path + '005/trajectories/trajectory_label_4.txt' )
l[ 1 ] = l[ 1 ].extract( range( 0 , 50 ) )

l[ 2 ] = Traj( movie = '005.tif' )
l[ 2 ].load( path + '005/trajectories/trajectory_label_6.txt' )
l[ 2 ] = l[ 2 ].extract( range( 0 , 50 ) )

# 006
#B
l[ 3 ] = Traj( movie = '006.tif' , parent='f[ 1 ]' )
l[ 3 ].load( path + '006/trajectories/trajectory_label_15.txt' )
l[ 3 ] = l[ 3 ].extract( range( 33 , 48 ) )
#E
l[ 4 ] = Traj( movie = '006.tif' , parent = 'l[ 5 ]' )
l[ 4 ].load( path + '006/trajectories/trajectory_label_37.txt' )
l[ 4 ] = l[ 4 ].extract( range( 29 , 54 ) )

# 007

l[ 5 ] = Traj( movie = '007.tif' , parent = 'f[ 8 ]' )
l[ 5 ].load( path + '007/trajectories/trajectory_label_9.txt' )
l[ 5 ] = l[ 5 ].extract( range( 14 , 19 ) )

l[ 6 ] = Traj( movie = '007.tif' , parent = 'f[ 8 ]' )
l[ 6 ].load( path + '007/trajectories/trajectory_label_15.txt' )
l[ 6 ] = l[ 6 ].extract( range( 0 , 18 ) )

# 009
#A
l[ 7 ] = Traj( movie = '009.tif' )
l[ 7 ].load( path + '009/trajectories/trajectory_label_11.txt' )
l[ 7 ] = l[ 7 ].extract( range( 0 , 30 ) )
#B
l[ 8 ] = Traj( movie = '009.tif' )
l[ 8 ].load( path + '009/trajectories/trajectory_label_30.txt' )
l[ 8 ] = l[ 8 ].extract( range( 0 , 41 ) )

# 010
#A 
l[ 9 ] = Traj( movie = '010.tif' )
l[ 9 ].load( path + '010/trajectories/trajectory_label_24.txt' )
l[ 9 ] = l[ 9 ].extract( range( 0 , 24 ) )
#B 
l[ 10 ] = Traj( movie = '010.tif' )
l[ 10 ].load( path + '010/trajectories/trajectory_label_39.txt' )
#C
l[ 11 ] = Traj( movie = '010.tif' , parent = 'f[ 17 ]' )
l[ 11 ].load( path + '010/trajectories/trajectory_label_65.txt' )
l[ 11 ] = l[ 11 ].extract( range( 27 , 44 ) )
#D
l[ 12 ] = Traj( movie = '010.tif' )
l[ 12 ].load( path + '010/trajectories/trajectory_label_71.txt' )
l[ 12 ] = l[ 12 ].extract( range( 0 , 48 ) )

# 011

l[ 13 ] = Traj( movie = '011.tif' )
l[ 13 ].load( path + '011/trajectories/trajectory_label_25.txt' )
l[ 13 ] = l[ 13 ].extract( range( 0 , 14 ) )

l[ 14 ] = Traj( movie = '011.tif' )
l[ 14 ].load( path + '011/trajectories/trajectory_label_82.txt' )
l[ 14 ] = l[ 14 ].extract( range( 0 , 35 ) )

l[ 15 ] = Traj( movie = '011.tif' )
l[ 15 ].load( path + '011/trajectories/trajectory_label_178.txt' )

l[ 16 ] = Traj( movie = '011.tif' )
l[ 16 ].load( path + '011/trajectories/trajectory_label_193.txt' )

# 012
#A 
l[ 17 ] = Traj( movie = '012.tif' , parent = 'f[ 19 ]' )
l[ 17 ].load( path + '012/trajectories/trajectory_label_6.txt' )
l[ 17 ] = l[ 17 ].extract( range( 47 , 60 ) )
#B
l[ 18 ] = Traj( movie = '012.tif' )
l[ 18 ].load( path + '012/trajectories/trajectory_label_14.txt' )
#H
l[ 19 ] = Traj( movie = '012.tif' )
l[ 19 ].load( path + '012/trajectories/trajectory_label_49.txt' )

# 013
#D
l[ 20 ] = Traj( movie = '013.tif' )
l[ 20 ].load( path + '013/trajectories/trajectory_label_10.txt' )

# -------- FILOS ---------
# movie 006
#A
f[ 0 ] = Traj( movie = '006.tif' )
f[ 0 ].load( path + '006/trajectories/trajectory_label_6.txt' )
#B
f[ 1 ] = Traj( movie = '006.tif' , parent='f[ 1 ]' )
f[ 1 ].load( path + '006/trajectories/trajectory_label_15.txt' )
f[ 1 ] = f[ 1 ].extract( range( 0 , 33 ) )

f[ 2 ] = Traj( movie = '006.tif' , parent='f[ 1 ]' )
f[ 2 ].load( path + '006/trajectories/trajectory_label_15.txt' )
f[ 2 ] = f[ 2 ].extract( range( 48 , 60 ) )
#C
f[ 3 ] = Traj( movie = '006.tif' )
f[ 3 ].load( path + '006/trajectories/trajectory_label_32.txt' )
#D
f[ 4 ] = Traj( movie = '006.tif' )
f[ 4 ].load( path + '006/trajectories/trajectory_label_36.txt' )
#E
f[ 5 ] = Traj( movie = '006.tif' , parent = 'f[ 5 ]' )
f[ 5 ].load( path + '006/trajectories/trajectory_label_37.txt' )
f[ 5 ] = f[ 5 ].extract( range( 0 , 30 ) ) #Chris said 26, but then there is a gap

f[ 6 ] = Traj( movie = '006.tif' , parent = 'f[ 5 ]' )
f[ 6 ].load( path + '006/trajectories/trajectory_label_37.txt' )
f[ 6 ] = f[ 6 ].extract( range( 54 , 60 ) )

# 007

f[ 7 ] = Traj( movie = '007.tif' )
f[ 7 ].load( path + '007/trajectories/trajectory_label_14.txt' )

f[ 8 ] = Traj( movie = '007.tif' )
f[ 8 ].load( path + '007/trajectories/trajectory_label_9.txt' )
f[ 8 ] = f[ 8 ].extract( range( 0 , 15 ) )

f[ 9 ] = Traj( movie = '007.tif' )
f[ 9 ].load( path + '007/trajectories/trajectory_label_32.txt' )

f[ 10 ] = Traj( movie = '007.tif' )
f[ 10 ].load( path + '007/trajectories/trajectory_label_58.txt' )

# 008
#C
f[ 11 ] = Traj( movie = '008.tif' )
f[ 11 ].load( path + '008/trajectories/trajectory_label_37.txt' )
#D
f[ 12 ] = Traj( movie = '008.tif' , notes ='has cyst attached')
f[ 12 ].load( path + '008/trajectories/trajectory_label_50.txt' )
#E
f[ 13 ] = Traj( movie = '008.tif' )
f[ 13 ].load( path + '008/trajectories/trajectory_label_60.txt' )
#F
f[ 14 ] = Traj( movie = '008.tif' )
f[ 14 ].load( path + '008/trajectories/trajectory_label_65.txt' )
#G
f[ 15 ] = Traj( movie = '008.tif' )
f[ 15 ].load( path + '008/trajectories/trajectory_label_73.txt' )

# 009
#C
f[ 16 ] = Traj( movie = '009.tif' )
f[ 16 ].load( path + '009/trajectories/trajectory_label_43.txt' )

# 010
#C
f[ 17 ] = Traj( movie = '010.tif' , parent = 'f[ 17 ]' )
f[ 17 ].load( path + '010/trajectories/trajectory_label_65.txt' )
f[ 17 ] = f[ 17 ].extract( range( 0 , 28 ) )

f[ 18 ] = Traj( movie = '010.tif' , parent = 'f[ 17 ]' )
f[ 18 ].load( path + '010/trajectories/trajectory_label_65.txt' )
f[ 18 ] = f[ 18 ].extract( range( 44 , len( f[ 18 ] ) ) )

# 012
#A
f[ 19 ] = Traj( movie = '012.tif' , parent = 'f[ 19 ]' )
f[ 19 ].load( path + '012/trajectories/trajectory_label_6.txt' )
f[ 19 ] = f[ 19 ].extract( range( 0 , 47 ) )

# 013
#B
f[ 20 ] = Traj( movie = '013.tif' )
f[ 20 ].load( path + '013/trajectories/trajectory_label_8.txt' )
#C
f[ 21 ] = Traj( movie = '013.tif' )
f[ 21 ].load( path + '013/trajectories/trajectory_label_7.txt' )
#E
f[ 22 ] = Traj( movie = '013.tif' )
f[ 22 ].load( path + '013/trajectories/trajectory_label_24.txt' )

# 014

f[ 23 ] = Traj( movie = '014.tif' )
f[ 23 ].load( path + '014/trajectories/trajectory_label_39.txt' )

f[ 24 ] = Traj( movie = '014.tif' )
f[ 24 ].load( path + '014/trajectories/trajectory_label_61.txt' )

# 016

f[ 25 ] = Traj( movie = '016.tif' )
f[ 25 ].load( path + '016/trajectories/trajectory_label_1.txt' )

f[ 26 ] = Traj( movie = '016.tif' )
f[ 26 ].load( path + '016/trajectories/trajectory_label_103.txt' )

f[ 27 ] = Traj( movie = '016.tif' )
f[ 27 ].load( path + '016/trajectories/trajectory_label_104.txt' )

f[ 28 ] = Traj( movie = '016.tif' )
f[ 28 ].load( path + '016/trajectories/trajectory_label_40.txt' )

f[ 29 ] = Traj( movie = '016.tif' )
f[ 29 ].load( path + '016/trajectories/trajectory_label_68.txt' )

f[ 30 ] = Traj( movie = '016.tif' )
f[ 30 ].load( path + '016/trajectories/trajectory_label_80.txt' )

f[ 31 ] = Traj( movie = '016.tif' )
f[ 31 ].load( path + '016/trajectories/trajectory_label_87.txt' )

f[ 32 ] = Traj( movie = '016.tif' )
f[ 32 ].load( path + '016/trajectories/trajectory_label_89.txt' )

v_f = []
v_f_err = []
D_f = []
D_f_err = []
A_f = []
A_f_err = []
e_f = []
e_f_err = []
v_l = []
v_l_err = []
D_l = []
D_l_err = []
A_l = []
A_l_err = []
e_l = []
e_l_err = []
v_f_step = [ ]
v_l_step = [ ]

msd_sel = 6 

for j in range( len( f ) ) :

	for i in range( len( f[ j ] ) - 1 ) : 
		d_step = np.sqrt( ( f[ j ].coord()[ 0 ][ i ] - f[ j ].coord()[ 0 ][ i + 1 ] ) ** 2 + ( f[ j ].coord()[ 1 ][ i ] - f[ j ].coord()[ 1 ][ i + 1 ] ) ** 2 ) * 6.45 / 60
		v_f_step.append( d_step / float( f[ j ].annotations()[ 'delta_t' ] ) ) 

	v , D , d = f[ j ].msdfit( sel = msd_sel , scale = 6.45/60 , return_data = True )

	print( 'Filos #' + str( j ) )
	print( f[ j ].annotations()[ 'file' ] )
	print( 'v = ' + str( round( v[ 0 ] , 2 ) ) + '; D = ' + str( round( D[ 0 ] , 2 ) ) )
	v_f.append( v[ 0 ] )
	v_f_err.append( v[ 1 ] )
	D_f.append( D[ 0 ] )
	D_f_err.append( D[ 1 ] )
	A_f.append( np.mean( f[ j ].f() ) )
	A_f_err.append( np.mean( f[ j ].f() ) )
	e_f.append( np.mean( f[ j ].ecc() ) )
	e_f_err.append( np.mean( f[ j ].ecc() ) )

	# plot the msd
	plot_the_msd( d ,  f[ j ].annotations()[ 'file' ][:-4] + '_Filos_' + str( j ) + '.pdf' )


for j in range( len( l ) ) :

	for i in range( len( l[ j ] ) - 1 ) : 
		d_step = np.sqrt( ( l[ j ].coord()[ 0 ][ i ] - l[ j ].coord()[ 0 ][ i + 1 ] ) ** 2 + ( l[ j ].coord()[ 1 ][ i ] - l[ j ].coord()[ 1 ][ i + 1 ] ) ** 2 ) * 6.45 / 60
		v_l_step.append( d_step / float( l[ j ].annotations()[ 'delta_t' ] ) ) 
	
	print( 'Lobos #' + str( j ) )
	print( l[ j ].annotations()[ 'file' ] )
	v , D , d = l[ j ].msdfit( sel = msd_sel , scale = 6.45/60 , return_data = True )

	print( 'v = ' + str( round( v[ 0 ] , 2 ) ) + '; D = ' + str( round( D[ 0 ] , 2 ) ) )
	v_l.append( v[ 0 ] )
	v_l_err.append( v[ 1 ] )
	D_l.append( D[ 0 ] )
	D_l_err.append( D[ 1 ] )
	A_l.append( np.mean( l[ j ].f() ) )
	A_l_err.append( np.std( l[ j ].f() ) )
	e_l.append( np.mean( l[ j ].ecc() ) )
	e_l_err.append( np.std( l[ j ].ecc() ) )
	
	# plot the msd
	plot_the_msd( d , l[ j ].annotations()[ 'file' ][:-4] + '_Lobos_' + str( j ) + '.pdf' )
	
fig = plt.figure( figsize = ( 12 , 4 ) )

gs = gspec.GridSpec( nrows = 1 , ncols = 3 )

ax_vD = fig.add_subplot( gs[ 0 , 0 ] )
ax_vA = fig.add_subplot( gs[ 0 , 1 ] )
ax_ve = fig.add_subplot( gs[ 0 , 2 ] )

ax_vD.errorbar( D_f , v_f , xerr = D_f_err , yerr = v_f_err , ls = '' , color = 'red' , marker = 's' , label = "Filos" )
ax_vD.errorbar( D_l , v_l , xerr = D_l_err , yerr = v_l_err , ls = '' , color = 'green' , marker = 's' , label = "Lobos" )

ax_vA.errorbar( A_f , v_f , yerr = v_f_err , ls = '' , color = 'red' , marker = 's' )
ax_vA.errorbar( A_l , v_l , yerr = v_l_err , ls = '' , color = 'green' , marker = 's' )

ax_ve.errorbar( e_f , v_f , yerr = v_f_err , ls = '' , color = 'red' , marker = 's' )
ax_ve.errorbar( e_l , v_l , yerr = v_l_err , ls = '' , color = 'green' , marker = 's' )

ax_vD.set_xlabel( '$D (\\mu m^2/s)$' )
ax_vD.set_ylabel( '$v (\\mu m/s)$' )
ax_vD.legend()
ax_vD.grid()

ax_vA.set_xlabel( '$Area (?)$' )
ax_vA.set_ylabel( '$v (\\mu m/s)$' )
ax_vA.grid()

ax_ve.set_xlabel( '$eccentricity$' )
ax_ve.set_ylabel( '$v (\\mu m/s)$' )
ax_ve.grid()

plt.savefig( 'velocities.pdf' )
plt.close()



