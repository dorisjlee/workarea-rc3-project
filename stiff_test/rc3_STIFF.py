import montage_wrapper as montage
import os
import shutil
from math import floor
DEBUG = True
CUTOFF =False 

run=5087
camcol=2
field=266

ra= 193.472083333 
dec=26.4438888889
radius=  2.45470891569

bands=['u','g','r','i','z']
for ele in bands:
	band =ele
	out = "frame-"+str(band)+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)
	os.system("wget http://data.sdss3.org/sas/dr10/boss/photoObj/frames/301/"+str(run)+"/"+ str(camcol) +"/"+out+".fits.bz2")
	os.system("bunzip2 "+out+".fits.bz2")
	out2 = "frame-"+str(band)+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field-1).zfill(4)
	os.system("wget http://data.sdss3.org/sas/dr10/boss/photoObj/frames/301/"+str(run)+"/"+ str(camcol) +"/"+out2+".fits.bz2")
	os.system("bunzip2 "+out2+".fits.bz2")
	out3 = "frame-"+str(band)+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field+1).zfill(4)
	os.system("wget http://data.sdss3.org/sas/dr10/boss/photoObj/frames/301/"+str(run)+"/"+ str(camcol) +"/"+out3+".fits.bz2")
	os.system("bunzip2 "+out3+".fits.bz2")
	os.mkdir (band)
	os.chdir(band)
	os.mkdir ("raw")
	os.mkdir ("projected")
	os.chdir("..")
	shutil.move(out+".fits",band+"/raw/" )
	shutil.move(out2+".fits",band+"/raw/" )
	shutil.move(out3+".fits",band+"/raw/" )
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
	montage.mSubimage("SDSS_"+out+".fits","SDSS_"+out+".fits",ra,dec,0.05)
	shutil.move("SDSS_"+out+".fits",os.getcwd()[:-11] )#if change to :-11 then move out of u,g,r,i,z directory, may be more convenient for mJPEG
	if (DEBUG) : print ("Completed Mosaic for " + band)
	os.chdir("../..")
# Superimposing R,G,B image mosaics into JPEG
# os.system("mJPEG "+ " -t 20  \ "+ 
# 		" -red "+ "SDSS_frame-"+"i"+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)+ ".fits "+ " 1s max gaussian-log \
#         -green  SDSS_frame-"+"r"+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)+".fits "+" 1s max gaussian-log \
#         -blue SDSS_frame-"+"g"+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)+".fits "+ " 2s max gaussian-log \
#         -out "+str(floor(ra))+"_"+str(floor(dec))+"_tcolor_10_min1s_max_final.jpg")
# Using STIFF 

os.system("stiff "+" SDSS_frame-"+"i"+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)+ ".fits "+ " SDSS_frame-"+"r"+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)+".fits "+ " SDSS_frame-"+"g"+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)+".fits "+ "  -c stiff.conf  " +"  -OUTFILE_NAME  "+str(floor(ra))+"_"+str(floor(dec))+"_COLORSAT_5_MAX_MAN_3  -COLOUR_SAT  5 -MAX_TYPE MANUAL -MAX_LEVEL 3")
#for b in bands:
	#os.system("rm -r "+b+"/")
	#we want to keep the fit files, but for testing purposes Python will throw file-already-exist error , if we dont delete them.
	#os.system("rm -r " + "SDSS_frame-"+b+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)+ ".fits" )
if (DEBUG) : print ("Completed Mosaic")