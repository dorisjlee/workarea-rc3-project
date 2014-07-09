#Data object is an abstract class for accessing raw data from survey and feed it into program in the appropraite format.
#Instance Attributes:
    - str raw : unprocessed raw data in CSV or HTML format
    - str processed: processed data in desirable format (list?, or just text file and do readline())
    - Useful quantities parse columns into list and store as attributes(?) 
class Data(Object):
    def __init__():
	self.raw = raw
	self.processed = self.process()
	
    def process():
	#Processing data
	return null

