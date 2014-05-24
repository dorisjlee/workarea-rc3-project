# Ra:135.15
# Dec: 50.6769444444
# Run:2074
# Camcol:3
# Field:112
# frame-u-002074-3-0112
# out = "frame-"+band+"-00"+run+"-0"+field


import montage_wrapper as montage
import os
import shutil

DEBUG = True 

run=1239
camcol=3
field=128
band ='i'
out = "frame-"+str(band)+"-00"+str(run)+"-0"+str(field)
ra=139.463333333       
dec= -0.279166666667
radius= 1.73780082875
os.mkdir (band)
os.chdir(band)
shutil.move(out+".fits",band )
if (DEBUG) : print("Creating mosaic for " +" "+ band + "band.")

montage.mImgtbl("raw","images.tbl")
montage.mHdr(str(ra)+" "+str(dec),radius,out+".hdr")
if (DEBUG): print ("Reprojecting images")
#Sometimes you can't find the files and result in images.tbl => empty doc
#need to put data file inside raw AND unzip it so that Montage detect that it is a fit file
os.chdir("raw")
montage.mProjExec("../images.tbl","../"+out+".hdr","../projected", "../stats.tbl") 
os.chdir("..")
montage.mImgtbl("projected","pimages.tbl")
#mAdd coadds the reprojected images using the FITS header template and mImgtbl list.
os.chdir("projected")
montage.mAdd("../pimages.tbl","../"+out+".hdr","SDSS_"+out+".fits")

#shutil.move("SDSS_"+out+".fits",os.getcwd()[:-9] )
#
if (DEBUG) : print ("Completed Mosaic")
# #Setup:
# 	#manually create "raw" and "projected" directory
# 	#place the u,g,r,i,z files inside "raw" dir

# # Ra:135.15
# # Dec: 50.6769444444
# # Run:2074
# # Camcol:3
# # Field:112
# # frame-u-002074-3-0112
# # out = "frame-"+band+"-00"+run+"-0"+field


# import montage_wrapper as montage
# import os
# import shutil

# DEBUG = True 

# run=2074
# camcol=3
# field=112
# band ='u'
# out = "frame-"+str(band)+"-00"+str(run)+"-0"+str(field)
# ra=135.15
# dec= 50.6769444444
# radius=2.29086765277

# if (DEBUG) : print("Creating mosaic for " +" , "+ band + "band.")

# montage.mImgtbl("raw","images.tbl")
# montage.mHdr(str(ra)+" "+str(dec),radius,out+".hdr")
# if (DEBUG): print ("Reprojecting images")
# montage.mProjExec("images.tbl",out+".hdr","projected", "stats.tbl") 
# montage.mImgtbl("projected","pimages.tbl")
# #mAdd coadds the reprojected images using the FITS header template and mImgtbl list.
# os.chdir("projected")
# montage.mAdd("../pimages.tbl","../"+out+".hdr","SDSS_"+out+".fits")

# shutil.move("SDSS_"+out+".fits",os.getcwd()[:-9] )

# if (DEBUG) : print ("Completed Mosaic")








