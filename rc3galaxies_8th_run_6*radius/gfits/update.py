# Assume you are inside directory (gfits/) where you have pulled all the g band fit files 
# find . -name "SDSS_g_*.fits" -type f -exec cp {} ./gfits \; 
import os
from astropy.io import fits as pyfits
updated = open("rc3_updated.txt",'a') # 'a' for append #'w')
updated.write("ra 		dec 		new_ra 		new_dec 		radius")
os.chdir("..")
gfits=[file for root, dir, files in os.walk("gfits") for file in files]
os.chdir("gfits/")
debug_count=0
#Objects: detected 0        / sextracted 0                      
#> All done (in 0 s)
#[]
#if object detect =0 then break

                
 
                # hdulist[0].header['PGC']="PGC"+pgc
                # hdulist[0].header['NED']=("http://ned.ipac.caltech.edu/cgi-bin/objsearch?objname="+hdulist[0].header['PGC']+"&extend=no&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=RA+or+Longitude&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES")
                # hdulist[0].header['CLEAN']=clean
                # outfile="SDSS_{}_{}_{}.fits".format(band,str(ra),str(dec))
                # hdulist.writeto(outfile)
for file in gfits:
	#print(file)
	#hdulist = pyfits.open(file)
	#ra= hdulist[0].header['RA']
	#dec= hdulist[0].header['DEC']
	if (debug_count<10):
		print (file)
		os.system("sex {} -c default.sex".format(file))
		catalog = open("test.cat",'r')
		#find max radius and treat as if it is rc3
		#Will have to modify this later to account for multiple neighboring large galaxies
		# Maybe by imposing other RC3-like characteristics (brightness..etc?)
		radius = []
		for line in catalog:
			if (line[0]!='#'):
				radius.append(line.split()[1])
		print (radius)
		#print (max(radius)) #breaks if object detected = 0
		#special value that indicate empty list (no object detected by SExtractor)
		radii='@'
		new_ra='@'
		new_dec='@'
		#It seems like I need to "reopen" the file after "using it up" in the above loop
		catalog = open("test.cat",'r')
		if (len(radius)!=0):
			print ("MAX RADIUS: " +str(max(radius)))
		for i in catalog:
			line = i.split()
			print (line)
			print ("here?")
			print (line[0])
			print (line[1])
			print (line[2])
			print (line[3])
			if (line[0]!='#' and line[1]==str(max(radius))):
				#)
				print ('Biggest Galaxy with radius {} pixels!'.format(line[1]))
				radii = line[1]
				# line = line.split()
				# radius = line[1]
				# new_ra= line[2]
				# new_dec = line[3]
				# print (radius,new_ra,new_dec)
				break
		if (radii!='@'):
			print ("Radii : "+ str(radii))
		#print (radius,new_ra,new_dec)
    # updated.write(file + "\n")
	debug_count += 1