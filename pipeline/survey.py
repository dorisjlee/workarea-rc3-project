# __Survey__ implements the abstract methods in the __Data__  class. It can also call on  appropriate methods from Gator or MAST data class. For the program to work properly, survey must have capabilities which is covered by the folowing method.
from server import *
class Survey():
    def __init__(name):
        self.name=name
        # Preset defaults for the specific survey
        self.bands = []
    	self.color_bands= []
    	self.best_band=[]
    	self.pixel_size= -1
        self.data_server=_initServer(name)
        # Mosaic Program Settings
        self.sextractor_params={} 
        self.montage_params={}
        self.stiff_params={}
    # def search(query,database):

    def _initServer(name):
        #Type Dispatching
        if (self.name =='2MASS'):
            self.data_server=2MASS()
        else if (name =='GALEX'):
            self.data_server=GALEX()
        else: #Generic
            print ("Unsupported survey type")
            self.data_server= self 
        
