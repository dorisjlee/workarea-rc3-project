#Data Acquisition Program
import montage_wrapper as montage
import os
import shutil
#ra = ra exact (ra as left-right)
#dec = dec exact (dec as spanning north-south)

#ra_sdss = ra returned by sdss server , center of that particular run, camcol,field image 
#dec_sdss
ra= 193.472083333 
dec=26.4438888889
diameter=  0.0409118153432 
#units of degrees
ra_sdss= 193.42842	
dec_sdss = 26.50897
radius = diameter/2.
#leaving some empty space around galaxy so that mosaic is not too squished 
#let this be ~2% of the radius of galaxy
border=0.2* radius + radius #from center to edge of picture
#To be on the safe side, use the radius as lengths of square frame 
while ((abs(ra-ra_sdss)>=border) or (abs(dec-dec_sdss)>=border)) :
    #while not enough stuff inside the border
    print (abs(ra-ra_sdss))
    print (abs(dec-dec_sdss))
    if ((ra-ra_sdss)>=radius): #*2:
        print ("pull in more horizontal data")
        if (ra-ra_sdss)>0:
        	print("add 1 field")
        else :
        	print(" minus 1 field")
    elif ((dec - dec_sdss)>=radius):
        print ("pull in more vertical data ")
        if (dec - dec_sdss)>0:
        	print ("add 1 camcol ")
        else:
        	print(" minus 1 camcol")
    else: 
        print ("do nothing, given data is enough")
    #update ra_sdss and dec_sdss to the value at the center of the galaxy
    # ra_sdss = new ra value
    # dec_sdss = new dec value
