# Class for interacting with IPAC's  Gator API 
from  server import Server
import abc
import re
import os
class Gator(Server):
    def __init__(self):
        self.name = 'Gator'
    
    def query (self,query): 
        '''
        Query the server database
        URL query form : http://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-query?parameter1=value1&parameter2=value2&
        '''
        os.system("wget {}http://irsa.ipac.caltech.edu/cgi-bin/Gator/{}{}".format(' "',query,'" '))

    def getData(self,band,ra,dec,margin):	
        '''
        Downloads imaging data from server
        URL query form : http://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-im_sia?
        
        FORMAT image/fits
		Return URIs for image FITS files

		POS=ra,dec &SIZE = margin
        '''
        print ("getData")
        out = "FORMAT=image/fits&band={}&POS={},{}&SIZE={}".format(band,str(ra),str(dec),str(margin))
        os.system("wget -O tbl.xml {}http://irsa.ipac.caltech.edu/cgi-bin/2MASS/IM/nph-im_sia?{}{}".format(' "',out,'" '))
        #Parse XML to find URL of all objects lying inside field 
        with open("tbl.xml") as f:
            n=0
            for line in f:
                # print line
                #The URL is stored in the line two lines after <TR>
                # print line[:4]

                if (line[:4] =="<TR>" or n==1):
                	#passing till 2 lines down <TR>
                	n+=1
                	pass
                elif (n==2):
                	n=0
                	url = line.split('[')[-1].split(']')[0]
                	print(url)
                	print ("wget {}{}{} ".format(' "',url,'" '))
                	os.system("wget {}{}{} ".format(' "',url,'" '))
                	



    #########################
    #    Query Builder		#
    #########################
    def otherRC3(self,ra,dec,margin):
    	'''
    	Given ra,dec, pgc of an RC3 galaxy, return a list of other rc3 that lies in the same margin field.
        Units
        =====
        Search radius (radius): arcsecond
    	'''
        query = "SELECT distinct rc3.pgc,rc3.ra,rc3.dec FROM PhotoObj as po JOIN RC3 as rc3 ON rc3.objid = po.objid  WHERE po.ra between {0}-{2} and  {0}+{2} and po.dec between {1}-{2} and  {1}+{2}".format(str(ra),str(dec),str(margin))
        return self.query(query)
    def runCamcolFieldConverter(self,ra,dec,margin,need_clean=False):
    	'''
    	Given ra,dec ,return a list of run camcol field for the given ra,dec
    	'''
        if (need_clean):
            query = "SELECT distinct run,camcol,field FROM PhotoObj WHERE  CLEAN =1 and ra between {0}-{2} and  {0}+{2}and dec between {1}-{2} and  {1}+{2}".format(str(ra),str(dec),str(margin))
        else:
            query = "SELECT distinct run,camcol,field FROM PhotoObj WHERE  ra between {0}-{2} and  {0}+{2}and dec between {1}-{2} and  {1}+{2}".format(str(ra),str(dec),str(margin))
        return self.query(query)