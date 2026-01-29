"""
Gerador de instâncias para o Problema da Mochila 0-1.
"""

import random
import os


def generate_instance(n_items, W, V, seed=None, min_peso=1, max_peso=10, 
                     min_volume=1, max_volume=10, min_valor=1, max_valor=20):
    """
    Gera uma instância aleatória do problema da mochila.
    
    Args:
        n_items: Número de itens
        W: Capacidade máxima de peso
        V: Capacidade máxima de volume
        seed: Semente para reprodutibilidade
        min_peso, max_peso: Limites para peso dos itens
        min_volume, max_volume: Limites para volume dos itens
        min_valor, max_valor: Limites para valor dos itens
        
    Returns:
        tuple: (W, V, items) onde items é uma lista de tuplas (peso, volume, valor)
    """
    if seed is not None:
        random.seed(seed)
    
    items = []
    for _ in range(n_items):
        peso = random.randint(min_peso, max_peso)
        volume = random.randint(min_volume, max_volume)
        valor = random.randint(min_valor, max_valor)
        items.append((peso, volume, valor))
    
    return W, V, items


def save_instance(filename, W, V, items):
    """
    Salva uma instância em um arquivo no formato esperado.
    
    Args:
        filename: Nome do arquivo
        W: Capacidade máxima de peso
        V: Capacidade máxima de volume
        items: Lista de tuplas (peso, volume, valor)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"{W}\t{V}\n")
        for peso, volume, valor in items:
            f.write(f"{peso}\t{volume}\t{valor}\n")


def generate_test_instances(output_dir="instances"):
    """
    Gera múltiplas instâncias de teste para avaliação empírica.
    
    Cria 10 instâncias para cada combinação de parâmetros.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Configurações de teste
    configs = [
        # (n_items, W, V)
        (5, 10, 10),
        (10, 20, 20),
        (15, 30, 30),
        (20, 40, 40),
        (25, 50, 50),
        (30, 60, 60),
        (35, 70, 70),
        (40, 80, 80),
        (45, 90, 90),
        (50, 100, 100),
    ]
    
    for n_items, W, V in configs:
        for instance_num in range(1, 11):
            seed = hash(f"{n_items}_{W}_{V}_{instance_num}") % (2**32)
            _, _, items = generate_instance(n_items, W, V, seed=seed)
            
            filename = os.path.join(output_dir, f"n{n_items}_W{W}_V{V}_inst{instance_num}.txt")
            save_instance(filename, W, V, items)
            print(f"Gerada: {filename}")
    
    print(f"\nTodas as instâncias foram geradas em '{output_dir}'")


if __name__ == "__main__":
    generate_test_instances()
