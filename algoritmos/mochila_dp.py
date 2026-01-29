"""
Implementação do Problema da Mochila 0-1 usando Programação Dinâmica.
"""

import time

def mochila_dp(W, V, items): 
    """
    Realiza programação dinâmica utilizando tabela de histórico booleana.
    
    Args:
        W: Capacidade máxima de peso
        V: Capacidade máxima de volume
        items: Lista de tuplas (peso, volume, valor)
        
    Returns:
        tuple: (valor_maximo, itens_selecionados, tempo_execucao)
    """

    start_time = time.time() # Início da medição de tempo 
    n = len(items) # Número de itens

    # 1. Tabela DP (Apenas Valores Numéricos)
    # dp[w][v] = Melhor valor monetário possível com peso w e volume v
    dp = [[0 for _ in range(V + 1)] for _ in range(W + 1)] # Tabela DP inicializada com 0

    # 2. Tabela de Histórico (Para Backtracking)
    # historico[i][w][v] = True se o item 'i' foi escolhido naquele estado
    historico = [[[False for _ in range(V + 1)] for _ in range(W + 1)] for _ in range(n)] # Tabela de histórico inicializada com False

    # --- PROCESSAMENTO ---
    for i in range(n):
        peso_i, volume_i, valor_i = items[i] # Peso, volume e valor do item i

        # Loop Inverso (Peso e Volume)
        for w in range(W, peso_i - 1, -1):
            for v in range(V, volume_i - 1, -1):
                
                # A lógica padrão de decisão. Obtendo o valor sem o item e com o item, afim de verificar se o item é melhor que o anterior.
                valor_sem_item = dp[w][v]
                valor_com_item = dp[w - peso_i][v - volume_i] + valor_i

                if valor_com_item > valor_sem_item:
                    dp[w][v] = valor_com_item
                    historico[i][w][v] = True # Marca o item como escolhido
                else:
                    # Não precisamos fazer nada, historico já inicia como False e o valor dp[w][v] mantém o valor antigo (do item anterior).
                    pass

    valor_maximo = dp[W][V] # Valor máximo encontrado

    # --- RECONSTRUÇÃO (BACKTRACKING) ---
    # Voltamos para descobrir quais itens foram escolhidos.
    itens_selecionados = [] 
    w_atual, v_atual = W, V

    # Vamos do último item até o primeiro (n-1 até 0)
    for i in range(n - 1, -1, -1):
        # Verificamos no histórico: "Eu peguei o item 'i' quando tinha capacidade w_atual/v_atual?"
        if historico[i][w_atual][v_atual]:
            itens_selecionados.append(i) # Salva o índice original, caso o item tenha sido escolhido (True na tabela de histórico).
            
            # Reduz a capacidade disponível, pois "devolvemos" o item
            peso_i, volume_i, _ = items[i]
            w_atual -= peso_i
            v_atual -= volume_i

    # Como andamos de trás para frente, ordenamos a lista final, afim de manter a ordem dos itens escolhidos para uma impressão mais legível.
    itens_selecionados.sort()
    
    tempo_execucao = time.time() - start_time # Tempo de execução
    return valor_maximo, itens_selecionados, tempo_execucao # Retorna o valor máximo, os itens selecionados e o tempo de execução