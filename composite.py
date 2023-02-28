# -*- coding: utf-8 -*-

composicao = {
    1: {
        'description': 'Adquirir dados',
        'class': 'Data',
        'help': 'é necessário obter dados históricos de mercado, que serão usados para treinar e testar o modelo de aprendizado de máquina. É importante adquirir dados de alta qualidade e em quantidade suficiente para que o modelo possa aprender com precisão.'
    },
    2: {
        'description': 'Limpeza e pré-processamento de dados',
        'class': 'DataPreprocessing',
        'help': 'os dados históricos geralmente contêm ruídos, erros ou dados faltantes. Antes de usá-los para treinar o modelo de aprendizado de máquina, é necessário limpar e pré-processar esses dados para remover esses problemas e garantir que o modelo possa aprender com precisão.'
    },
    3: {
        'description': 'Análise exploratória de dados',
        'class': 'DataExploration',
        'help': 'a análise exploratória de dados é importante para entender as características dos dados, como sua distribuição, correlação, sazonalidade e outras características relevantes. Isso ajuda a identificar padrões nos dados que podem ser úteis para o modelo de aprendizado de máquina.'
    },
    4: {
        'description': 'Seleção de recursos',
        'class': 'FeatureSelection',
        'help': 'é importante selecionar os recursos (ou características) mais relevantes para o modelo de aprendizado de máquina. A seleção de recursos pode ser feita por meio de métodos estatísticos, como análise de correlação, ou por meio de técnicas de aprendizado de máquina, como árvores de decisão ou redes neurais.'
    },
    5: {
        'description': 'Treinamento do modelo',
        'class': 'ModelTraining',
        'help': 'com os dados limpos e pré-processados e os recursos selecionados, é possível treinar o modelo de aprendizado de máquina. É importante ajustar os parâmetros do modelo e testar diferentes algoritmos para encontrar o melhor modelo para o problema em questão.'
    },
    6: {
        'description': 'Avaliação do modelo',
        'class': 'ModelEvaluation',
        'help': 'é necessário avaliar a qualidade do modelo treinado para verificar se ele é capaz de generalizar bem os dados e fazer previsões precisas. A avaliação do modelo pode ser feita por meio de diferentes métricas, como precisão, recall, f1-score e outras.'
    },
    7: {
        'description': 'Implantação do modelo',
        'class': 'ModelDeployment',
        'help': 'depois que o modelo é treinado e avaliado, ele pode ser implantado em um ambiente de negociação ao vivo. É importante monitorar o desempenho do modelo em tempo real e fazer ajustes e atualizações conforme necessário.'
    },
    8: {
        'description': 'Teste de backtesting',
        'class': 'Backtesting',
        'help': 'é importante realizar um teste de backtesting para avaliar o desempenho do modelo usando dados históricos. O backtesting é um método que consiste em simular as decisões de negociação',
        },
    9:{
        'description':'Ajuste de parâmetros',
        'class':'Paremeters',
        'help':'após avaliar o modelo de aprendizado de máquina e identificar seu desempenho usando o backtesting, é possível ajustar os parâmetros do modelo para melhorar ainda mais sua precisão. O ajuste de parâmetros pode ser feito por meio de técnicas de otimização, como busca em grade ou otimização bayesiana.',
       },
    9:{
        'description':'Gerenciamento de risco',
        'class':'RiskManagement',
        'help':'é importante ter um sistema de gerenciamento de risco adequado ao fazer negociações usando aprendizado de máquina. O gerenciamento de risco envolve a definição de limites de perda e a implementação de estratégias para minimizar o risco de perda.',
       },
    10:{
        'description':'Monitoramento',
        'class':'Monitoring',
        'help':'depois que o modelo é implantado em um ambiente de negociação ao vivo, é importante monitorar seu desempenho em tempo real e fazer ajustes e atualizações conforme necessário. O monitoramento e a manutenção contínua ajudam a garantir que o modelo continue a fazer previsões precisas e que o sistema de negociação funcione sem problemas',
       }
}

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
