"""
Programa principal para resolver o Problema da Mochila 0-1.
"""

import sys

from file_reader import read_instance
from algoritmos.mochila_dp import mochila_dp
from algoritmos.mochila_backtracking import mochila_backtracking
from algoritmos.mochila_bnb import mochila_bnb


def print_solution(algorithm_name, valor_maximo, itens_selecionados, tempo_execucao, items):
    """Imprime a solução formatada."""
    print(f"\n{algorithm_name}:")
    print(f"Lucro máximo: {valor_maximo}")
    print(f"Itens selecionados: {itens_selecionados}")
    print(f"Detalhes dos itens:")
    peso_total = 0
    volume_total = 0
    for idx in itens_selecionados:
        peso, volume, valor = items[idx]
        peso_total += peso
        volume_total += volume
        print(f"  Item {idx}: peso={peso}, volume={volume}, valor={valor}")
    print(f"Peso total: {peso_total}")
    print(f"Volume total: {volume_total}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_entrada> [algoritmo]")
        print("Algoritmos disponíveis: dp, backtracking, bnb, all (padrão: all)")
        sys.exit(1)
    
    filename = sys.argv[1]
    algorithm = sys.argv[2] if len(sys.argv) > 2 else "all"
    
    try:
        W, V, items = read_instance(filename)
        print(f"Capacidade da mochila: peso={W}, volume={V}")
        print(f"Número de itens: {len(items)}")
        
        if algorithm == "dp" or algorithm == "all":
            valor_max, itens_sel, tempo = mochila_dp(W, V, items)
            print_solution("Programação Dinâmica", valor_max, itens_sel, tempo, items)
        
        if algorithm == "backtracking" or algorithm == "all":
            valor_max, itens_sel, tempo = mochila_backtracking(W, V, items)
            print_solution("Backtracking", valor_max, itens_sel, tempo, items)
        
        if algorithm == "bnb" or algorithm == "all":
            valor_max, itens_sel, tempo = mochila_bnb(W, V, items)
            print_solution("Branch-and-Bound", valor_max, itens_sel, tempo, items)
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
