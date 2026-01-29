"""
Implementação do Problema da Mochila 0-1 usando Backtracking.
"""

import time

def mochila_backtracking(W, V, items):
    """
    Resolve o problema da mochila 0-1 com duas restrições usando backtracking.
    
    Args:
        W: Capacidade máxima de peso
        V: Capacidade máxima de volume
        items: Lista de tuplas (peso, volume, valor)
    
    Returns:
        tuple: (valor_maximo, itens_selecionados, tempo_execucao)
    """
    
    start_time = time.time() # Início da medição de tempo
    n = len(items)  # Número de itens

    # Valores inicializados
    melhor_valor = 0  
    melhor_solucao = [] 
    
    def backtrack(indice, peso_atual, volume_atual, valor_atual, solucao_atual): # Chamada para o Backtracking
        nonlocal melhor_valor, melhor_solucao
        
        # Caso base: processou todos os itens, e verifica se o atual valor é o novo melhor
        if indice == n:
            if valor_atual > melhor_valor:
                melhor_valor = valor_atual 
                melhor_solucao = solucao_atual.copy()
            return
        
        # DOIS CAMINHOS PARA A ARVORE DE RECURSÃO: 

        # Não incluir o item atual
        backtrack(indice + 1, peso_atual, volume_atual, valor_atual, solucao_atual)
        
        # Incluir o item atual (se couber)
        peso_i, volume_i, valor_i = items[indice] # Passar os valores do item analisado para 3 variáveis
        if peso_atual + peso_i <= W and volume_atual + volume_i <= V:  # Caso os restrições de PESO e VOLUME sejam seguidas  
            solucao_atual.append(indice) # Adiciono o indice do item ao vetor solucao
            backtrack(indice + 1, peso_atual + peso_i, volume_atual + volume_i,  
                     valor_atual + valor_i, solucao_atual) # Chamada recursiva com o item incluso
            solucao_atual.pop() # Necessario para que um outro caminho possa ser seguido
    
    backtrack(0, 0, 0, 0, []) # Chamada inicial

    tempo_execucao = time.time() - start_time # Tempo de execução
    return melhor_valor, sorted(melhor_solucao), tempo_execucao # Retorna o valor máximo, os itens selecionados e o tempo de execução
