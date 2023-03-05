import pandas as pd
from datetime import datetime
import numpy as np
import MetaTrader5 as mt5
import pytz
from tabulate import tabulate
import inspect


class Dados():
    def __init__(self, user: str, password: str):
        self.conectar(user, password)

    def conectar(self, user, password):
        try:
            if not mt5.initialize():
                print("Falha ao conectar ao MetaTrader 5")
                mt5.shutdown()
                return False
    
            authorized = mt5.login(user, password)
            if not authorized:
                print("Falha ao autorizar a conexão com a conta", user)
                return False
    
            return True
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
    
    def get_profit(self):
        try:
            print('------------------------------')
            print('Informações da Conta')
            print('------------------------------')
            account_info = mt5.account_info()._asdict()
            my_list = list(account_info.items())
            print(tabulate(my_list, headers=['nome','valor'], tablefmt="grid"))
            return account_info
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
        
    def get_symbol_info(self, symbol):
        try:
            print('------------------------------')
            print('Informaçãoes do Simbolo')
            print('------------------------------')
            symbol_info = mt5.symbol_info(symbol)
            symbol_info = symbol_info._asdict()
            my_list = list(symbol_info.items())
            print(tabulate(my_list, headers=['nome','valor'], tablefmt="grid"))
            return symbol_info
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
        
    def get_symbol_book(self, symbol):
        try:
            print('------------------------------')
            print('Profudindade do Mercado')
            print('------------------------------')
            symbol_book = mt5.market_book_add(symbol)._asdict()
            my_list = list(symbol_book.items())
            print(tabulate(my_list, headers=['nome','valor'], tablefmt="grid"))
            return symbol_book
        except Exception as e:
            print(f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}")
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
    
    def get_symbols(self, search:str=''):
        try:
            print('------------------------------')
            simbolos = mt5.symbols_get()
            for index in range(mt5.symbols_total()):
                ticket = simbolos[index].name
                if (search in ticket):
                    print(index, ticket)
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"

    def get_ticks(self,symbol: str, start_day: int,end_day ,month: int,year: int):
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
            ticks_ = mt5.copy_ticks_range(symbol, utc_from, utc_to, mt5.COPY_TICKS_ALL)
            # Convertemos para pandas dataframe
            ticks_ = pd.DataFrame(ticks_)
            # transformar timestamp em segundos
            ticks_['time']=pd.to_datetime(ticks_['time'],unit='s')
            # ticks_.set_index('time',inplace=True)
            return ticks_
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
    
    def convert_time(self):
        '''
        To convert it into a usable signal is to use sin and cos
        Returns
        -------
        Date time convert sin and cos
        '''
        try:
            date_time = pd.to_datetime(self.base1.pop('date'), format='%Y.%m.%d %H:%M:%S')
            timestamp_s = date_time.map(datetime.datetime.timestamp)
            day = 24*60*60
            self.base1['date'] = date_time
            self.base1['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
            self.base1['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
        
    def select_symbol(self, symbol):
        try:
            selected=mt5.symbol_select(symbol,True)
            if not selected:
                print("Failed to select EURCAD, error code =",mt5.last_error())
            self.get_symbol_info(symbol)

        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"

    def comprar(self, symbol, volume):
        try:
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_BUY,
                "price": mt5.symbol_info_tick(symbol).ask,
                "deviation": 20,
                "magic": 123456,
                "comment": "Minha ordem de compra",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC
            }
    
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print("Erro ao comprar", symbol, ":", result.comment)
            else:
                print("Compra de", volume, "de", symbol, "realizada com sucesso")
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"

    def vender(self, symbol, volume):
        try:
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_SELL,
                "price": mt5.symbol_info_tick(symbol).bid,
                "deviation": 20,
                "magic": 123456,
                "comment": "Minha ordem de venda",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC
            }
    
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print("Erro ao vender", symbol, ":", result.comment)
            else:
                print("Venda de", volume, "de", symbol, "realizada com sucesso")
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            
# testes

if __name__ == '__main__':
    
    login = '********'
    password = '*********'
    symbol = 'WINJ23'
    conexao = Dados(login, password)
    conexao.get_symbols(symbol)
    conexao.get_profit()
    conexao.get_symbol_info(symbol)
    conexao.get_symbol_book(symbol)
