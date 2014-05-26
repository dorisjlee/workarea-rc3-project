
import montage_wrapper as montage
import os
import shutil

DEBUG = True 

run=1239
camcol=3
field=128
band ='z'
out = "frame-"+str(band)+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)
out2 = "frame-"+str(band)+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field-1)
ra=139.463333333       
dec= -0.279166666667
radius= 1.73780082875
os.mkdir (band)
os.chdir(band)
os.mkdir ("raw")
os.mkdir ("projected")
os.chdir("..")
shutil.move(out+".fits",band+"/raw/" )
shutil.move(out2+".fits",band+"/raw/" )
os.chdir(band)
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

shutil.move("SDSS_"+out+".fits",os.getcwd()[:-9] )#if change to :-11 then move out of u,g,r,i,z directory, may be more convenient for mJPEG

if (DEBUG) : print ("Completed Mosaic")

#Run this on Bash
  # Superimposing R,G,B image mosaics into JPEG
  # mJPEG -blue   SDSS_frame-i-001239-3-0128.fits -1s 99.999% gaussian-log \
  #       -green  SDSS_frame-g-001239-3-0128.fits -1s 99.999% gaussian-log \
  #       -red SDSS_frame-r-001239-3-0128.fits -1s 99.999% gaussian-log \
  #       -out camcoltest3_r2r_g2g_b2i.jpg
