# Class for interacting with SDSS's SkyServer
import sqlcl

class skyserver(Data):
	#Default constructor

	@Override 
	def getData(query):
		other_rc3s = sqlcl.query("SELECT distinct rc3.pgc,rc3.ra,rc3.dec FROM PhotoObj as po JOIN RC3 as rc3 ON rc3.objid = po.objid  WHERE po.ra between {0}-{1} and  {0}+{1} and po.dec between {2}-{3} and  {2}+{3}".format(str(rc3_ra),str(margin),str(rc3_dec),str(margin))).readlines()
                        

