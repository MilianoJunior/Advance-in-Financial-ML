# -*- coding: utf-8 -*-
"""
consider a classe:
<code>
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
            return f"Error: {inspect.currentframe().f_code.co_name}, {e}"
    
    def get_profit(self):
        try:
            account_info = mt5.account_info()._asdict()
            my_list = list(account_info.items())
            print(tabulate(my_list, headers=['nome','valor'], tablefmt="grid"))
            return account_info
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e}"
    
    def get_symbols(self, search:str=''):
        try:
            print('------------------------------')
            simbolos = mt5.symbols_get()
            for index in range(mt5.symbols_total()):
                ticket = simbolos[index].name
                if (search in ticket):
                    print(index, ticket)
        except Exception as e:
            return f"Error: {inspect.currentframe().f_code.co_name}, {e}"

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
            return f"Error: {inspect.currentframe().f_code.co_name}, {e}"
    
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
            return f"Error: {inspect.currentframe().f_code.co_name}, {e}"

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
            return f"Error: {inspect.currentframe().f_code.co_name}, {e}"

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
            return f"Error: {inspect.currentframe().f_code.co_name}, {e}"
<code>


complete a classe com o dict para gerar novos métodos:
    metatrader_methods = {
        'initialize': 'Estabelece a conexão com o terminal MetaTrader 5',
        'login': 'Conecta-se a uma conta de negociação com os parâmetros especificados',
        'shutdown': 'Fecha a conexão estabelecida anteriormente com o terminal MetaTrader 5',
        'version': 'Retorna a versão do terminal MetaTrader 5',
        'last_error': 'Retorna informações sobre o último erro',
        'account_info': 'Obtém informações atuais sobre a conta de negociação',
        'terminal_info': 'Obtém o estado e os parâmetros do terminal MetaTrader 5 conectado',
        'symbols_total': 'Obtém o número total de instrumentos financeiros no terminal MetaTrader 5',
        'symbols_get': 'Obtém todos os instrumentos financeiros do terminal MetaTrader 5',
        'symbol_info': 'Obtém informações sobre o instrumento financeiro especificado',
        'symbol_info_tick': 'Obtém o último tick do instrumento financeiro especificado',
        'symbol_select': 'Seleciona o símbolo na janela MarketWatch ou remove o símbolo deste janela',
        'market_book_add': 'Faz com que o terminal MetaTrader 5 receba eventos sobre mudanças no livro de ofertas para o símbolo especificado',
        'market_book_get': 'Retorna uma tupla desde BookInfo contendo os registros do livro de ofertas para o símbolo especificado',
        'market_book_release': 'Cancela a subscrição do terminal MetaTrader 5 para receber eventos sobre alterações no livro de ofertas para o símbolo especificado',
        'copy_rates_from': 'Recebe barras do terminal MetaTrader 5, a partir da data especificada',
        'copy_rates_from_pos': 'Recebe barras do terminal MetaTrader 5, a partir do índice especificado',
        'copy_rates_range': 'Recebe barras a partir do terminal MetaTrader 5, no intervalo de datas especificado',
        'copy_ticks_from': 'Recebe ticks do terminal MetaTrader 5, a partir da data especificada',
        'copy_ticks_range': 'Recebe ticks a partir do terminal MetaTrader 5, no intervalo de datas especificado',
        'orders_total': 'Obtém o número de ordens ativas',
        'orders_get': 'Obtém ordens ativas com a capacidade de filtrar por símbolo ou ticket',
        'order_calc_margin': 'Retorna o tamanho da margem na moeda da conta para a operação de negociação especificada',
        'order_calc_profit': 'Retorna o valor do lucro na moeda da conta para a operação de negociação especificada',
        'order_check': 'Verifica que há fundos suficientes para realizar a operação de negociação requerida',
        'order_send': 'Envia do terminal para o servidor de negociação uma solicitação para concluir uma operação de negociação',
        'positions_total': 'Obtém o número de posições abertas',
        'positions_get': 'Obtém posições abertas com a capacidade de filtrar por símbolo ou bilhete',
        'history_orders_total': 'Obtém o número de ordens no histórico de negociação no intervalo especificado',
        'history_orders_get': 'Obtém ordens do histórico de negociação com a capacidade de filtrar por bilhete ou posiçãocapitalize',
        'history_deals_total':'Obtém o número de transações no histórico de negociação no intervalo especificado',
        'history_deals_get':'Obtém transações do histórico de negociação com a capacidade de filtrar por bilhete ou posição'
        }
"""

