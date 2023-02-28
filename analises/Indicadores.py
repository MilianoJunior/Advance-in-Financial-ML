import talib

class indicadores():
    def __init__(self,name='indicadores'):
        self.name = name
    #--------------------------------------------------    
    def SMA(self,column,period):
        return talib.SMA(column,timeperiod=period)
    #----------------------------------------------------
    def STD(self,column,period):
        return talib.STDDEV(column, timeperiod=period, nbdev=1)