"""
Script para análise dos resultados da avaliação empírica.
"""

import csv
import statistics
import os


def analisar_resultados(csv_file="results.csv"):
    """
    Analisa os resultados do CSV e gera estatísticas.
    """
    if not os.path.exists(csv_file):
        print(f"Arquivo {csv_file} não encontrado.")
        print("Execute primeiro: python evaluator.py")
        return
    
    results = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    
    if not results:
        print("Nenhum resultado encontrado no arquivo.")
        return
    
    # Agrupa por algoritmo e tamanho da instância
    algorithms = ['DP', 'Backtracking', 'Branch-and-Bound']
    
    print("=" * 80)
    print("ANÁLISE DE RESULTADOS")
    print("=" * 80)
    
    # Estatísticas por algoritmo
    for algo in algorithms:
        algo_results = [r for r in results if r['algoritmo'] == algo and r['sucesso'] == 'True']
        
        if not algo_results:
            print(f"\n{algo}: Nenhum resultado bem-sucedido")
            continue
        
        tempos = [float(r['tempo_execucao']) for r in algo_results]
        valores = [int(r['valor_maximo']) for r in algo_results]
        
        print(f"\n{algo}:")
        print(f"  Instâncias processadas: {len(algo_results)}")
        print(f"  Tempo médio: {statistics.mean(tempos):.6f}s")
        print(f"  Tempo mediano: {statistics.median(tempos):.6f}s")
        print(f"  Tempo mínimo: {min(tempos):.6f}s")
        print(f"  Tempo máximo: {max(tempos):.6f}s")
        if len(tempos) > 1:
            print(f"  Desvio padrão: {statistics.stdev(tempos):.6f}s")
        print(f"  Valor médio obtido: {statistics.mean(valores):.2f}")
    
    # Análise por tamanho da instância
    print("\n" + "=" * 80)
    print("ANÁLISE POR TAMANHO DA INSTÂNCIA")
    print("=" * 80)
    
    sizes = sorted(set([int(r['n_items']) for r in results]))
    
    for size in sizes:
        print(f"\nTamanho: {size} itens")
        size_results = [r for r in results if int(r['n_items']) == size and r['sucesso'] == 'True']
        
        for algo in algorithms:
            algo_size_results = [r for r in size_results if r['algoritmo'] == algo]
            if algo_size_results:
                tempos = [float(r['tempo_execucao']) for r in algo_size_results]
                print(f"  {algo}: tempo médio = {statistics.mean(tempos):.6f}s")
    
    # Verifica consistência dos valores (todos devem encontrar o mesmo valor máximo)
    print("\n" + "=" * 80)
    print("VERIFICAÇÃO DE CONSISTÊNCIA")
    print("=" * 80)
    
    # Agrupa por arquivo
    files = set([r['arquivo'] for r in results])
    inconsistencias = 0
    
    for filename in files:
        file_results = [r for r in results if r['arquivo'] == filename and r['sucesso'] == 'True']
        if len(file_results) > 1:
            valores = [int(r['valor_maximo']) for r in file_results]
            if len(set(valores)) > 1:
                print(f"⚠ Inconsistência em {filename}: valores = {valores}")
                inconsistencias += 1
    
    if inconsistencias == 0:
        print("OK: Todos os algoritmos encontraram o mesmo valor maximo para cada instancia")
    
    print("\n" + "=" * 80)
    print("Análise concluída!")
    print("=" * 80)


if __name__ == "__main__":
    import sys
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "results.csv"
    analisar_resultados(csv_file)
