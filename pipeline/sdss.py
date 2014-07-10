from survey import *
class SDSS(Survey):
    def __init__(self,name='SDSS',bands=['u','g','r','i','z'],color_bands=['g','r','i'],best_band='r',pixel_size=0.396):
        Survey.__init__(self,name,bands,color_bands,best_band,pixel_size)

