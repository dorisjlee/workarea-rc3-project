# 2MASS Class can not be named starting with number 
from survey import *
class TwoMass(Survey):
    def __init__(self):
        self.name = '2MASS'
        self.bands=['j','h','k']
        self.color_bands=['j','h','k']
        self.best_band ='j' #not sure about this 
        self.pixel_size = 2.0 #http://www.ipac.caltech.edu/2mass/overview/about2mass.html
        self.data_server = Survey._initServer(self)
        # Mosaic Program Settings
        self.sextractor_params={} 
        self.montage_params={}
        self.stiff_params={}
        # super(SDSS,self).__init__(name,bands,color_bands,best_band,pixel_size,sextractor_params,montage_params,stiff_params)
