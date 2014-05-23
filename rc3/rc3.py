#http://skyserver.sdss3.org/dr8/en/help/browser/browser.asp?n=RC3&t=U
# Doing the i band still for the 1st rc3 object in that list
#     - Trying to find a more formal way to deal with directory structure
#      - Things I have to iterate through: 
#          - All ~23000 galaxies
#          - all bands

import montage_wrapper as montage
import os
import shutil

#cd /Users/doris/Desktop/GSoC2014/workarea-rc3-project/rc3/rc3-g/
DEBUG = True 

obj = 2 #loop through all the objects
band = "u"                #loop through u,g,i,r,z
loc = str(0.03625) + " " + str(-6.374722222222222)              #concatenate RA, DEC into a string
w = 2* 1.5488166189124812#equals height 
out = "rc3_"+ band + "_"+ str(obj) #concat str filename

if (DEBUG) : print("Creating mosaic for obj"+str(obj) +" , "+ band + "band.")

os.mkdir(out)
os.chdir(out)
#make a directory and go in before you pull all your data files
os.mkdir("raw")
    #consider making raw directory for the data 
    #https://docs.python.org/2/library/tempfile.html#tempfile.mkdtemp



#pull in all your data files inside the raw directory
montage.mArchiveList("SDSS",band, loc, w, w, out+".tbl")



os.chdir("raw")


if (DEBUG): print ("Retreiving raw FITS from remote archive")
montage.mArchiveExec("../"+out+".tbl") #Keeps saying that url not found because you changed into raw so it can't find the .tbl file (which is outside)
#doing "cd .. "
os.chdir(os.getcwd()[:-3]) #current path minus "raw"
montage.mImgtbl("raw","images.tbl")
montage.mHdr(loc , w,out+".hdr")

os.mkdir("projected")
os.chdir("raw")
if (DEBUG): print ("Reprojecting images")
montage.mProjExec("../images.tbl","../"+out+".hdr","../projected", "stats.tbl") #,debug=True)



os.chdir(os.getcwd()[:-3]) #cdd 
#creating a table of projected images
montage.mImgtbl("projected","pimages.tbl")


#mAdd coadds the reprojected images using the FITS header template and mImgtbl list.
os.chdir("projected")
montage.mAdd("../pimages.tbl","../"+out+".hdr","SDSS_"+out+".fits")



shutil.move("SDSS_"+out+".fits",os.getcwd()[:-9] )

if (DEBUG) : print ("Completed Mosaic")

os.chdir(os.getcwd()[:-9])
#Removing intermediate directories "raw" and "projected" after 
shutil.rmtree('projected')
shutil.rmtree('raw')
