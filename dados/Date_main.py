import pandas as pd
from datetime import datetime
import numpy as np
import MetaTrader5 as mt5
import pytz


class data():
    def __init__(self,symbol:str):
        # conecte-se ao MetaTrader 5
        if not mt5.initialize():
            print("initialize() failed")
            mt5.shutdown()
        # consultamos o estado e os parâmetros de conexão
        print(mt5.terminal_info())
        # obtemos informações sobre a versão do MetaTrader 5
        print(mt5.version())
        self.symbol = symbol

    def get_ticks(self,start_day: int,end_day ,month: int,year: int):
        '''
        Upload the data 
        Parameters
        ----------
        symbol : name symbol ticker
        day: corrent day upload
        month: corrent month upload
        year: corrent year upload
        
        Returns
        -------
        base : pandas dataframe

        '''
        # tratamento de exeção para dias não operaveis
        try:
            timezone = pytz.timezone("America/Sao_Paulo")
            # criamos o objeto datatime no fuso horário UTC para que não seja aplicado o deslocamento do fuso horário local
            utc_from = datetime(year, month, start_day, tzinfo=timezone)
            utc_to = datetime(year, month, end_day, tzinfo=timezone)
            # solicitamos ticks de um intervalo
            ticks_ = mt5.copy_ticks_range(self.symbol, utc_from, utc_to, mt5.COPY_TICKS_ALL)
            # Convertemos para pandas dataframe
            ticks_ = pd.DataFrame(ticks_)
            # transformar timestamp em segundos
            ticks_['time']=pd.to_datetime(ticks_['time'],unit='s')
            # ticks_.set_index('time',inplace=True)
            return ticks_
        except ValueError:
            print("Dia não existe")
            return pd.DataFrame(columns=['valor'])
    
    def convert_time(self):
        '''
        To convert it into a usable signal is to use sin and cos
        Returns
        -------
        Date time convert sin and cos
        '''
        date_time = pd.to_datetime(self.base1.pop('date'), format='%Y.%m.%d %H:%M:%S')
        timestamp_s = date_time.map(datetime.datetime.timestamp)
        day = 24*60*60
        self.base1['date'] = date_time
        self.base1['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
        self.base1['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))


        # with open('./dados3.csv', 'rb') as f:
        #     result = chardet.detect(f.read())  # or readline if the file is large
        #     base1 = pd.read_csv('./dados3.csv', encoding=result['encoding'])
        
        # with open('./dados1.csv', 'rb') as f:
        #     result = chardet.detect(f.read())  # or readline if the file is large
        #     base = pd.read_csv('./dados1.csv', encoding=result['encoding'])
        
        # date = pd.DataFrame(columns=['dia','hora','max','min'])
        
        # base3 = base1.day == base.date[0]
        
        # dia = base.date[0]
        # var = []
        # for i in range(len(base)):
        #     if base['date'][i] != dia:
        #         print(i,dia)
        #         temp = base.date[i].split(' ')
        #         date = date.append({'dia':temp[0],
        #                               'hora':temp[1],
        #                               'max':max(var),
        #                               'min':min(var)}, ignore_index=True)
                
        #         var = []
        #         dia = base['date'][i]
        #     else:
        #         var.append(base.venda[i])
        
        # date['dif'] = date['max']-date['min']        