import numpy as np
import xarray as xr

#-----------------------------------------------
def preprocess(dataset):
    '''A function to preprocess input data so dimensions are labelled 'time', 'level', 'lat', 'lon', levels are ordered from surface to top of atmosphere, latitudes are ordered from south to north and longitudes from west to east.'''
 
    return

#-----------------------------------------------
def regrid(dataarray, interpolation):
    '''A function to horizontally regrid data, given a target grid. Can specify bilinear, nearest neighbour, conservative or cubic.'''

    return

#----------------------------------------------- 
def check_units(dataset):
    '''A function to check whether each required variable is in the correct units for calculating moist static energy budget terms, and convert the units if not.'''

    return

 #-----------------------------------------------  
