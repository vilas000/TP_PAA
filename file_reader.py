"""
Módulo para leitura de arquivos de entrada do Problema da Mochila 0-1.
"""


def read_instance(filename):
    """
    Lê uma instância do problema da mochila de um arquivo.
    
    Formato esperado:
    - Primeira linha: W V (peso máximo e volume máximo)
    - Demais linhas: peso volume valor (separados por tabulação ou espaços)
    
    Args:
        filename: Caminho para o arquivo de entrada
        
    Returns:
        tuple: (W, V, items) onde items é uma lista de tuplas (peso, volume, valor)
        
    Raises:
        FileNotFoundError: Se o arquivo não existir
        ValueError: Se o formato do arquivo for inválido
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
        
        if len(lines) < 2:
            raise ValueError("Arquivo deve ter pelo menos 2 linhas (W V e pelo menos 1 item)")
        
        # Primeira linha: W e V (aceita espaços ou tabs)
        first_line = lines[0].strip().split()
        if len(first_line) < 2:
            raise ValueError("Primeira linha deve conter W e V separados por espaço ou tabulação")
        
        W = int(first_line[0])
        V = int(first_line[1])
        
        if W <= 0 or V <= 0:
            raise ValueError("W e V devem ser positivos")
        
        # Demais linhas: itens (aceita espaços ou tabs)
        items = []
        for i, line in enumerate(lines[1:], start=2):
            parts = line.strip().split()  # Aceita espaços ou tabs
            if len(parts) < 3:
                print(f"Aviso: Linha {i} ignorada (formato inválido: esperado 'peso volume valor')")
                continue
            
            try:
                peso = int(parts[0])
                volume = int(parts[1])
                valor = int(parts[2])
                
                if peso <= 0 or volume <= 0 or valor <= 0:
                    print(f"Aviso: Linha {i} ignorada (valores devem ser positivos)")
                    continue
                
                items.append((peso, volume, valor))
            except ValueError:
                print(f"Aviso: Linha {i} ignorada (valores não numéricos)")
                continue
        
        if not items:
            raise ValueError("Nenhum item válido encontrado no arquivo")
        
        return W, V, items
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{filename}' não encontrado")
    except ValueError as e:
        raise ValueError(f"Erro ao ler arquivo '{filename}': {e}")
