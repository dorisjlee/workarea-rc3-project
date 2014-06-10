import montage_wrapper as montage
import os
import shutil
from math import trunc
import sqlcl
import sys
#Must run in Python 2
DEBUG = True
n = 0
start=false
output = open("rc3_galaxies_outside_SDSS_footprint.txt",'w')
for line in file("rc3_ra_dec_radius_csv(Final).txt"):
    print line
    # if line =="--------(start here)--------": #Debugging purpose, put this in the rc3(final).txt to start from where you left off (when error)
    #     start=True
    # else: 
    #     if(DEBUG) :print "not yet"
    # if (start):
    #     n +=1
    #     ra = float(line.split()[0])
    #     dec = float(line.split()[1])
    #     radius = float(line.split()[2])/2. #radius = diameter/2
    #     margin = 3*radius
    #     if (DEBUG) : print ("Working on "+str(n)+"th RC3 Galaxy at ("+str(ra)+","+str(dec) +") of radius"+str(radius))
    #     if (DEBUG) : print ("Querying data that lies inside margin")
    #     data =[]
    #     result=sqlcl.query("SELECT distinct run,camcol,field FROM PhotoObj WHERE  ra between " + str(ra) +"-" +str(margin) +" and "+ str(ra) +"+"+ str(margin) +" and dec between "+ str(dec) + "-"+ str(margin)+ " and "+str(dec)+"+"+ str(margin)).readlines()
    #     print result
    #     count =0
    #     for i in result:
    #         if count>1:
    #             list =i.split(',')
    #             list[2]= list[2][:-1]
    #             data.append(list)
    #         count +=1
    #     if len(data)==0:
    #         if (DEBUG):print 'The given ra, dec of this galaxy does not lie in the SDSS footprint. Onto the next galaxy!'#Exit Program.'
    #         output.write(str(ra)+ "     "+ str(dec)+"     "+str(diameter)+"\n")
    #         #sys.exit()
    #         continue
    #     else :
    #         if (DEBUG): 
    #             print ( "Complete Query. These data lies within margin: ")
    #             print (data)
    #     bands=['u','g','r','i','z']
    #     for band in bands:
    #         os.mkdir(band)
    #         os.chdir(band)
    #         os.mkdir ("raw")
    #         os.mkdir ("projected")
    #         os.chdir("raw")
    #         if (DEBUG): print ("Retrieving data from SDSS SAS server for "+ band +"band")
    #         for i in data :  
    #             out = "frame-"+str(band)+"-"+str(i[0]).zfill(6)+"-"+str(i[1])+"-"+str(i[2]).zfill(4)
    #             os.system("wget http://data.sdss3.org/sas/dr10/boss/photoObj/frames/301/"+str(i[0])+"/"+ str(i[1]) +"/"+out+".fits.bz2")
    #             os.system("bunzip2 "+out+".fits.bz2")
    #         # print (os.getcwd())
    #         os.chdir("../")
    #         if (DEBUG) : print("Creating mosaic for " +" "+ band + " band.")
    #         montage.mImgtbl("raw","images.tbl")
    #         montage.mHdr(str(ra)+" "+str(dec),margin,out+".hdr")
    #         if (DEBUG): print ("Reprojecting images")
    #         #Sometimes you can't find the files and result in images.tbl => empty doc
    #         #need to put data file inside raw AND unzip it so that Montage detect that it is a fit file
    #         os.chdir("raw")
    #         montage.mProjExec("../images.tbl","../"+out+".hdr","../projected", "../stats.tbl") 
    #         os.chdir("..")
    #         montage.mImgtbl("projected","pimages.tbl")
    #         #mAdd coadds the reprojected images using the FITS header template and mImgtbl list.
    #         os.chdir("projected")
    #         montage.mAdd("../pimages.tbl","../"+out+".hdr","SDSS_"+out+".fits")
    #         montage.mSubimage("SDSS_"+out+".fits","SDSS_"+band+"_"+str(ra)+"_"+str(dec)+".fits",ra,dec,2*margin) # mSubImage takes xsize which should be twice the margin (margin measures center to edge of image)
    #         shutil.move("SDSS_"+band+"_"+str(ra)+"_"+str(dec)+".fits",os.getcwd()[:-11] )#if change to :-11 then move out of u,g,r,i,z directory, may be more convenient for mJPEG
    #         if (DEBUG) : print ("Completed Mosaic for " + band)
    #         os.chdir("../..")
    #     # Superimposing R,G,B image mosaics into TIFF using STIFF
    #     os.system("stiff "+" SDSS_i_"+str(ra)+"_"+str(dec)+ ".fits "+ " SDSS_r_"+str(ra)+"_"+str(dec)+ ".fits "+" SDSS_g_"+str(ra)+"_"+str(dec)+ ".fits "+ "  -c stiff.conf  " +"  -OUTFILE_NAME  MARGIN_2rad_deg_"+str(ra)+"_"+str(dec)+"_COLORSAT_2_MAX_MAN_5.tiff   -COLOUR_SAT  2 -MAX_TYPE MANUAL -MAX_LEVEL 5")
    #     for b in bands:
    #         os.system("rm -r "+b+"/")
    #         #we want to keep the fit files, but for testing purposes Python will throw file-already-exist error , if we dont delete them.
    #         #os.system("rm -r " + "SDSS_frame-"+b+"-"+str(run).zfill(6)+"-"+str(camcol)+"-"+str(field).zfill(4)+ ".fits" )
    #     if (DEBUG) : print ("Completed Mosaic")
    #     if (DEBUG) : print ("--------------------------------------------------------")
