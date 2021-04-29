'''
Importando as bibliotecas
'''
from Date_Curators import Date_main
from Features_Analysts.Plots import plots
from Features_Analysts import Indicadores
from tqdm import tqdm
import pandas as pd
'''
 Instanciando as classe
'''
dados = Date_main.data('WDO$N')   # Classe para obtenção dos dados
graficos = plots.plot()           # Classe para plotar os gráficos
indicador = Indicadores.indicadores()  # Classe para calcular os indicadores
'''
Engenharia de recursos:

    Média Móvel
    
        Objetivo: calcular a média móvel simples para um intervalo de 1000 ticks
        e encontrar algum fator estatistico que demonstre um padrão.
'''
box1 = pd.DataFrame(columns=['valor']) # dataframe para armazenar valores a cada 1000 ticks
box2 = pd.DataFrame(columns=['std','distancia']) # dataframe para armazenar os valores de 1000
# Loop para percorrer vários dias
for i in range(1,2):
    ticks = dados.get_ticks(i,i+1, 4, 2021)
    graficos.sinal(ticks['bid'][6000:7000].values,ticks['ask'][6000:7000].values,'numero de ticks','bid e ask','gráfico de ticks')
    for s in tqdm(range(len(ticks))):
        if s%1000 ==0:
            box1 = box1.append({'valor': ticks['last'][s]}, ignore_index=True)
            if len(box1) > 30:
                media = indicador.SMA(box1.valor.values, 25)
                std = indicador.STD(ticks['last'].values[s-1000:s], 1000)
                distancia = media[-1] - ticks['last'][s]
                box2 = box2.append({'std':std[-1],
                                    'distancia':distancia}, ignore_index=True)
print(box2.head(20))

graficos.hist(box2['distancia'].values, 50,'variação','amplitude','diferença entre a media e o valor atual')
dif_media = media[30:len(media)] + box2['distancia'].values
graficos.sinal(media[30:len(media)],dif_media,'numero de ticks a cada 1000','preço x media','Média de 25 simples e preço atual')

        
