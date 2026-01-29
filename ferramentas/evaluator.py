"""
Script de avaliação empírica dos algoritmos.
"""

import os
import csv
import time
from file_reader import read_instance
from algoritmos.mochila_dp import mochila_dp
from algoritmos.mochila_backtracking import mochila_backtracking
from algoritmos.mochila_bnb import mochila_bnb


def evaluate_algorithm(algorithm_func, W, V, items, algorithm_name):
    """Avalia um algoritmo e retorna os resultados."""
    try:
        valor_maximo, itens_selecionados, tempo_execucao = algorithm_func(W, V, items)
        return {
            'sucesso': True,
            'valor_maximo': valor_maximo,
            'num_itens_selecionados': len(itens_selecionados),
            'tempo_execucao': tempo_execucao
        }
    except Exception as e:
        print(f"Erro ao executar {algorithm_name}: {e}")
        return {
            'sucesso': False,
            'valor_maximo': 0,
            'num_itens_selecionados': 0,
            'tempo_execucao': 0
        }


def evaluate_instances(instances_dir="instances", output_file="results.csv", timeout=300):
    """
    Avalia todas as instâncias nos três algoritmos.
    
    Args:
        instances_dir: Diretório contendo as instâncias
        output_file: Arquivo CSV de saída com os resultados
        timeout: Timeout em segundos para cada execução
    """
    algorithms = {
        'DP': mochila_dp,
        'Backtracking': mochila_backtracking,
        'Branch-and-Bound': mochila_bnb
    }
    
    results = []
    
    # Lista todos os arquivos de instância
    instance_files = sorted([f for f in os.listdir(instances_dir) if f.endswith('.txt')])
    
    print(f"Encontradas {len(instance_files)} instâncias")
    print("Avaliando algoritmos...\n")
    
    for filename in instance_files:
        filepath = os.path.join(instances_dir, filename)
        
        try:
            W, V, items = read_instance(filepath)
            n_items = len(items)
            
            print(f"Processando: {filename} (n={n_items}, W={W}, V={V})")
            
            # Extrai parâmetros do nome do arquivo
            parts = filename.replace('.txt', '').split('_')
            instance_num = int(parts[-1].replace('inst', ''))
            
            for algo_name, algo_func in algorithms.items():
                start_time = time.time()
                result = evaluate_algorithm(algo_func, W, V, items, algo_name)
                elapsed = time.time() - start_time
                
                if elapsed > timeout:
                    print(f"  ⚠ {algo_name}: Timeout (> {timeout}s)")
                    result['sucesso'] = False
                    result['tempo_execucao'] = timeout
                
                results.append({
                    'arquivo': filename,
                    'n_items': n_items,
                    'W': W,
                    'V': V,
                    'instancia': instance_num,
                    'algoritmo': algo_name,
                    'valor_maximo': result['valor_maximo'],
                    'num_itens_selecionados': result['num_itens_selecionados'],
                    'tempo_execucao': result['tempo_execucao'],
                    'sucesso': result['sucesso']
                })
                
                if result['sucesso']:
                    print(f"  OK {algo_name}: valor={result['valor_maximo']}, tempo={result['tempo_execucao']:.4f}s")
                else:
                    print(f"  FAIL {algo_name}: Falhou")
        
        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")
            continue
    
    # Salva resultados em CSV
    if results:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['arquivo', 'n_items', 'W', 'V', 'instancia', 'algoritmo',
                         'valor_maximo', 'num_itens_selecionados', 'tempo_execucao', 'sucesso']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        
        print(f"\nResultados salvos em '{output_file}'") 
        
        # Estatísticas resumidas
        print("\n=== Estatísticas Resumidas ===")
        for algo_name in algorithms.keys():
            algo_results = [r for r in results if r['algoritmo'] == algo_name and r['sucesso']]
            if algo_results:
                tempos = [r['tempo_execucao'] for r in algo_results]
                print(f"\n{algo_name}:")
                print(f"  Média de tempo: {sum(tempos)/len(tempos):.6f}s")
                print(f"  Tempo mínimo: {min(tempos):.6f}s")
                print(f"  Tempo máximo: {max(tempos):.6f}s")
                print(f"  Instâncias processadas: {len(algo_results)}/{len([r for r in results if r['algoritmo'] == algo_name])}")


if __name__ == "__main__":
    import sys
    
    instances_dir = sys.argv[1] if len(sys.argv) > 1 else "instances"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "results.csv"
    
    evaluate_instances(instances_dir, output_file)
