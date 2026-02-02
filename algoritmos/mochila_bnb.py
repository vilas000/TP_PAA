"""
Implementação do Problema da Mochila 0-1 usando Branch-and-Bound.
"""

import time
from queue import PriorityQueue


class No:
    """Nó da árvore de busca para Branch-and-Bound."""
    
    def __init__(self, nivel, peso, volume, valor, limite, itens_selecionados):
        self.nivel = nivel
        self.peso = peso
        self.volume = volume
        self.valor = valor
        self.limite = limite  # Bound (Limite Superior)
        self.itens_selecionados = itens_selecionados
    
    def __lt__(self, outro):
        # Invertemos a lógica padrão para que a fila priorize o maior valor
        return self.limite > outro.limite


def calcular_limite(no, W, V, itens):
    """
    Calcula o limite superior (bound) para um nó usando relaxamento linear.
    Assume que podemos pegar frações de itens (Mochila Fracionária).
    NOTA: A lista 'itens' já deve vir ordenada por densidade da função principal.
    """
    if no.peso > W or no.volume > V: # Caso o peso e volume atuais naquele nó descumpram as restrições, interromper execução
        return 0

    itens_restantes = itens[no.nivel:] # Pega os itens restantes a partir do nível atual

    # --- CÁLCULO DO BOUND APENAS PARA O PESO (Relaxa Volume) ---
    # Ordenar os itens restantes pela densidade de PESO (Valor / Peso)
    # Lambda: Valor (x[2]) / Peso (x[0])
    itens_restantes.sort(key=lambda x: x[2]/x[0] if x[0] > 0 else float('inf'), reverse=True)
    
    bound_w = no.valor
    peso_atual = no.peso
    
    for p, v, val in itens_restantes:
        if peso_atual + p <= W:
            peso_atual += p
            bound_w += val
        else:
            # Item não cabe inteiro, entao pegar fração baseada no PESO
            espaco_livre = W - peso_atual
            if p > 0:
                fracao = espaco_livre / p
                bound_w += val * fracao
            break # Encheu o peso, para aqui


    # --- CÁLCULO DO BOUND APENAS PARA O VOLUME (Relaxa Peso) ---
    # Ordenar os itens restantes pela densidade de VOLUME (Valor / Volume)
    # Lambda: Valor (x[2]) / Volume (x[1])
    itens_restantes.sort(key=lambda x: x[2]/x[1] if x[1] > 0 else float('inf'), reverse=True)
    
    bound_v = no.valor
    volume_atual = no.volume
    
    for p, v, val in itens_restantes:
        if volume_atual + v <= V:
            volume_atual += v
            bound_v += val
        else:
            # Item não cabe inteiro, então pegar fração baseada no VOLUME
            espaco_livre = V - volume_atual
            if v > 0:
                fracao = espaco_livre / v
                bound_v += val * fracao
            break # Encheu o volume, para aqui

    # O Limite Verdadeiro é o MINIMO entre as duas restrições.
    return min(bound_w, bound_v)
    

def solucao_inicial(n, W, V, itens):
    peso_g = 0
    volume_g = 0
    valor_g = 0
    solucao_g = []

    for i in range(n):
        p_i, v_i, val_i = itens[i] # Estes itens já estão ordenados pela melhor razão
        
        if peso_g + p_i <= W and volume_g + v_i <= V:
            peso_g += p_i
            volume_g += v_i
            valor_g += val_i
            solucao_g.append(i) # Guardamos o índice interno (da lista ordenada)

    # Inicializamos as variáveis globais com essa solução gulosa
    # Ao invés de começar com 0, já começamos com um valor alto!
    melhor_valor = valor_g
    melhor_solucao = solucao_g[:]
    return melhor_valor, melhor_solucao


def mochila_bnb(W, V, itens):
    """
    Resolve o problema da mochila 0-1 com duas restrições usando Branch-and-Bound.
    
    Args:
        W: Capacidade máxima de peso
        V: Capacidade máxima de volume
        itens: Lista de tuplas (peso, volume, valor)
        
    Returns:
        tuple: (valor_maximo, itens_selecionados, tempo_execucao)
    """
    
    tempo_inicio = time.time() # Início da medição de tempo 
    n = len(itens) # Número de itens
    
    # 1. PRÉ-PROCESSAMENTO: Ordenação por Densidade (Guloso)
    # Calcula a razão valor/custo (média entre peso e volume) para cada item
    itens_com_razao = []
    for i, (peso, volume, valor) in enumerate(itens):

        if peso > 0:
            razao_peso = valor / peso
        else:
            razao_peso = 0

        if volume > 0:
            razao_volume = valor / volume
        else:
            razao_volume = 0

        razao = (razao_peso + razao_volume) / 2

        
        # Guardamos o índice original 'i' para reconstruir a resposta depois
        itens_com_razao.append((razao, i, peso, volume, valor))
    
    # Ordena do maior para o menor (reverse=True)
    itens_com_razao.sort(reverse=True)
    
    # Cria a lista de itens reordenada e um mapa para recuperar os índices originais
    itens_ordenados = []
    mapa_indices = {}
    
    for novo_indice, (_, indice_original, peso, volume, valor) in enumerate(itens_com_razao):
        itens_ordenados.append((peso, volume, valor))
        mapa_indices[novo_indice] = indice_original
    
    # Substituímos a lista original pela ordenada para usar no algoritmo
    itens = itens_ordenados
    

    # 1.1. SOLUÇÃO GULOSA (inicial)
    melhor_valor, melhor_solucao = solucao_inicial(n, W, V, itens)

    # 2. INICIALIZAÇÃO DA BUSCA
    fila_prioridade = PriorityQueue()
    
    # Cria o nó raiz (nível 0, vazio) passando a lista 'itens' (que já está ordenada)
    limite_raiz = calcular_limite(No(0, 0, 0, 0, 0, []), W, V, itens)
    raiz = No(0, 0, 0, 0, limite_raiz, [])
    
    fila_prioridade.put(raiz)
    
    # 3. LOOP PRINCIPAL (Best-First Search)
    while not fila_prioridade.empty():
        no = fila_prioridade.get()
        
        # PODA 1: Se o potencial (limite) deste nó é pior que o melhor valor
        # que já garantimos, não adianta expandir.
        if no.limite < melhor_valor:
            continue
        
        # Verifica se chegamos numa folha (todos itens processados) ou fim da linha, e compara as soluções
        if no.nivel == n:
            if no.valor > melhor_valor:
                melhor_valor = no.valor
                melhor_solucao = no.itens_selecionados.copy()
            continue
        
        # --- EXPANSÃO DOS FILHOS ---
        
        # Filho 1: NÃO incluir o item atual
        limite_sem_item = calcular_limite(
            No(no.nivel + 1, no.peso, no.volume, no.valor, 0, no.itens_selecionados),
            W, V, itens
        )
        
        if limite_sem_item >= melhor_valor: # Verifica se é promissor
            no_sem_item = No(
                no.nivel + 1,
                no.peso,
                no.volume,
                no.valor,
                limite_sem_item,
                no.itens_selecionados.copy()
            )
            fila_prioridade.put(no_sem_item)
        
        # Filho 2: INCLUIR o item atual (se couber)
        peso_i, volume_i, valor_i = itens[no.nivel]
        novo_peso = no.peso + peso_i
        novo_volume = no.volume + volume_i
        
        if novo_peso <= W and novo_volume <= V:
            novo_valor = no.valor + valor_i
            nova_solucao = no.itens_selecionados + [no.nivel]
            
            limite_com_item = calcular_limite(
                No(no.nivel + 1, novo_peso, novo_volume, novo_valor, 0, nova_solucao),
                W, V, itens
            )
            
            if limite_com_item >= melhor_valor: # Verifica se é promissor
                no_com_item = No(
                    no.nivel + 1,
                    novo_peso,
                    novo_volume,
                    novo_valor,
                    limite_com_item,
                    nova_solucao
                )
                fila_prioridade.put(no_com_item)
                
                # Atualiza o melhor valor global se encontramos um candidato válido melhor
                if novo_valor > melhor_valor:
                    melhor_valor = novo_valor
                    melhor_solucao = nova_solucao.copy()
    
    # 4. FINALIZAÇÃO
    # Converte os índices da lista ordenada de volta para os índices originais do problema
    itens_selecionados_originais = sorted([mapa_indices[i] for i in melhor_solucao])
    tempo_execucao = time.time() - tempo_inicio
    
    return melhor_valor, itens_selecionados_originais, tempo_execucao