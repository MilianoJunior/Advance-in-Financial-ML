'''
Importando as bibliotecas
'''
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Date_Curators import Date_main
from Features_Analysts.Plots import plots
from Features_Analysts import Indicadores
from tqdm import tqdm
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
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
        Processo KDD :
            Preparação dos dados : processamento
            Mineração dos dados : busca de padrões
            Avaliação e interpretação dos dados : Gerando conhecimento
'''
#--------------------------------------------------
# Preparação dos dados
# integração,limpeza,transformação,redução,discretização.
#--------------------------------------------------
box1 = pd.DataFrame(columns=['valor']) # dataframe para armazenar valores a cada 1000 ticks
box2 = pd.DataFrame(columns=['std','distancia','valor','media','dado1','dado2','label']) # dataframe para armazenar os valores de 1000
# Loop para percorrer vários dias
for i in range(1,26):
    box1 = pd.DataFrame(columns=['valor'])
    ticks = dados.get_ticks(i,i+1, 4, 2021)
    if len(ticks)<1:
        pass
    else:
        for s in tqdm(range(0,len(ticks)-1000)):
            if s%1000 ==0:
                box1 = box1.append({'valor': ticks['last'][s]}, ignore_index=True)
                if len(box1) > 30:
                    # calculando a media
                    media = indicador.SMA(box1.valor.values, 15)
                    # calculando o desvio padrão
                    std = indicador.STD(ticks['last'].values[s-1000:s], 1000)
                    # calculando a diferença entre a media e o último preço
                    distancia = media[-1] - ticks['last'][s]
                    valor = ticks['last'][s+1000] - ticks['last'][s]
                    if valor > 0: 
                        label = 1
                    else:
                        label = 0
                    box2 = box2.append({'std':std[-1],
                                        'distancia':distancia,
                                        'valor':valor,
                                        'media':media[-1],
                                        'dado1':ticks['last'][s],
                                        'dado2':ticks['last'][s+1000],
                                        'label':label}, ignore_index=True)
'''
Verificação visual dos dados
'''
print(box2.head(20))
print(box1.head(20))
# Ticks
graficos.sinal(ticks['bid'][6000:7000].values,ticks['ask'][6000:7000].values,'numero de ticks','bid e ask','gráfico de ticks')
# Distancia da média para o último tick
graficos.hist(box2['distancia'].values, 50,'variação','amplitude','diferença entre a media e o valor atual')
# Ticks a cada 1000 e media desses dados
graficos.sinal(box2['media'].values,box2['dado1'].values,'numero de ticks a cada 1000','preço x media','Média de 25 simples e preço atual')
#--------------------------------------------------
# Mineração dos dados
#   Atividades descritivas:
#           Regras de associação:
#           Agrupamento:
#           Sumarização:
#   Atividades preditivas:
#           Classificação:
#           Regressão:
#           Séries Temporais:
#--------------------------------------------------
#--------------------------------------------------
# Avaliação dos dados
#--------------------------------------------------


        
