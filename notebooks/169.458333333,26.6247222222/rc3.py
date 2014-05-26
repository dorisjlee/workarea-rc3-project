##NOT SURE WHY THIS DOESN:T WORK. I'll just rerun on the old file.
import montage_wrapper as montage
import os
import shutil

DEBUG = True
CUTOFF =False
run=5112
camcol=3
field=389

ra=158.147083333   
dec= 65.041
radius= 1.20226443462
bands=['u','g','r','i','z']
for ele in bands:
	band =ele
	out = "frame-"+str(band)+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)
	os.system("wget http://data.sdss3.org/sas/dr10/boss/photoObj/frames/301/"+str(run)+"/"+ str(camcol) +"/"+out+".fits.bz2")
	os.system("bunzip2 "+out+".fits.bz2")
	if (CUTOFF) :
		out2 = "frame-"+str(band)+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field-1)
		os.system("wget http://data.sdss3.org/sas/dr10/boss/photoObj/frames/301/"+str(run)+"/"+ str(camcol) +"/"+out2+".fits.bz2")
		os.system("bunzip2 "+out2+".fits.bz2")
	os.mkdir (band)
	os.chdir(band)
	os.mkdir ("raw")
	os.mkdir ("projected")
	os.chdir("..")
	shutil.move(out+".fits",band+"/raw/" )
	if(CUTOFF): shutil.move(out2+".fits",band+"/raw/" )
	os.chdir(band)
	if (DEBUG) : print("Creating mosaic for " +" "+ band + " band.")
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
	montage.mSubimage("SDSS_"+out+".fits","SDSS_"+out+"cropped.fits",ra,dec,0.05)
	shutil.move("SDSS_"+out+"cropped.fits",os.getcwd()[:-11] )#if change to :-11 then move out of u,g,r,i,z directory, may be more convenient for mJPEG
	if (DEBUG) : print ("Completed Mosaic for " + band)
	os.chdir("../..")
#actually you can just do ".." for "cd .."


#Run this on Bash 
#os.system executes ths line in bash, the python wrapper does not support mJPEG for some strange reason 
  # Superimposing R,G,B image mosaics into JPEG

os.system("mJPEG -blue "+ "SDSS_frame-"+"i"+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)+"cropped.fits "+ "-1s 99.999% gaussian-log \
        -green SDSS_frame-"+"g"+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)+"cropped.fits "+" -1s 99.999% gaussian-log \
        -red SDSS_frame-"+"r"+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)+ "cropped.fits "+" -1s 99.999% gaussian-log \
        -out camcoltest4_cropped.jpg")
if (DEBUG) : print ("Completed Mosaic")