import montage_wrapper as montage
import os
import shutil

#ra = ra exact (assume ra as left-right)
#dec = dec exact (assume dec as spanning north-south)

#ra_sdss = ra returned by sdss server , center of that particular run, camcol,field
#dec_sdss


#To be on the safe side, use the radius as lengths of square frame 
while ((abs(ra-ra_sdss)>=radius)||(abs(dec-dec_sdss)>=radius)) :
    #while not enough stuff inside the border
    if abs(ra-ra_sdss)>=radius: #*2:
        #pull in more "horizontal" data
    elif abd(dec - dec_sdss)>=radius:
        #pull in more "vertical" data 
    else: 
        # do nothing, given data is enough

