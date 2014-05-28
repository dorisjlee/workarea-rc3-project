import montage_wrapper as montage
import os
import shutil

DEBUG = True
CUTOFF =False 

run=1239
camcol=3
field=128

ra=139.463333333       
dec= -0.279166666667
radius= 1.73780082875

# run=3015
# camcol=4
# field=327

# ra=163.129583333
# dec= 7.22444444444
# radius=  0.758577575029*2
bands=['u','g','r','i','z']
for ele in bands:
	band =ele
	out = "frame-"+str(band)+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)
	os.system("wget http://data.sdss3.org/sas/dr10/boss/photoObj/frames/301/"+str(run)+"/"+ str(camcol) +"/"+out+".fits.bz2")
	os.system("bunzip2 "+out+".fits.bz2")
	
	out2 = "frame-"+str(band)+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field-1)
	os.system("wget http://data.sdss3.org/sas/dr10/boss/photoObj/frames/301/"+str(run)+"/"+ str(camcol) +"/"+out2+".fits.bz2")
	os.system("bunzip2 "+out2+".fits.bz2")
	os.mkdir (band)
	os.chdir(band)
	os.mkdir ("raw")
	os.mkdir ("projected")
	os.chdir("..")
	shutil.move(out+".fits",band+"/raw/" )
	shutil.move(out2+".fits",band+"/raw/" )
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
# Superimposing R,G,B image mosaics into JPEG

os.system("mJPEG -red "+ "SDSS_frame-"+"i"+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)+ "cropped.fits "+ " 50% max gaussian-log \
        -green  SDSS_frame-"+"r"+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)+"cropped.fits "+" 50% max gaussian-log \
        -blue SDSS_frame-"+"g"+"-00"+str(run)+"-"+str(camcol)+"-0"+str(field)+"cropped.fits "+ " 50% max gaussian-log \
        -out 139_50%min.jpg")
if (DEBUG) : print ("Completed Mosaic")