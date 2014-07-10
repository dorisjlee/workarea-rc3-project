#Data object is an abstract class for accessing raw data from survey and feed it into program in the appropraite format.
'''
Instance Attributes:
    - str raw : unprocessed raw data in CSV or HTML format
    - str processed: processed data in desirable format (list?, or just text file and do readline())
    - Useful quantities parse columns into list and store as attributes(?) 
'''
import survey
import mast
import gator
abstract class Server():
    def __init__(raw,):
        self.raw = raw
        #self.processed = self.process()
	
	#Optional 
    def process():
        #Processing data
        '''
        Implemented by Catalog 
        '''
        #return null
    
    abstract def query ()
    abstract def getData()
    def printInfo():

