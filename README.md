# Problema da Mochila 0-1 - Implementação e Avaliação Empírica

Este projeto implementa três algoritmos para resolver o **Problema da Mochila 0-1 com duas restrições** (peso e volume):

1. **Programação Dinâmica**
2. **Backtracking** 
3. **Branch-and-Bound** 

## Descrição do Problema

Dado uma mochila com capacidade máxima de **W quilos** e **V litros**, e **n itens** onde cada item **i** tem:
- Peso: `wi`
- Volume: `li`
- Valor: `vi`

O objetivo é **maximizar o valor** transportado na mochila, respeitando as restrições de peso e volume, sem repetir itens.


O arquivo de entrada deve ter o seguinte formato:

```
W	V
peso1	volume1	valor1
peso2	volume2	valor2
...
```

**Exemplo:**
```
10	9
6	3	10
3	4	14
4	2	16
2	5	9
```

Onde:
- Primeira linha: capacidade máxima de peso (W) e volume (V), separados por tabulação
- Demais linhas: peso, volume e valor de cada item, separados por tabulação

## Uso

### Executar uma instância específica

```bash
# Executar todos os algoritmos
python main.py arquivo_entrada.txt

# Executar apenas um algoritmo específico
python main.py arquivo_entrada.txt dp
python main.py arquivo_entrada.txt backtracking
python main.py arquivo_entrada.txt bnb
```

### Gerar instâncias de teste

```bash
python instance_generator.py
```

Isso criará 10 instâncias para cada combinação de parâmetros no diretório `instances/`.

### Avaliação empírica completa

```bash
# Gerar instâncias (se ainda não foram geradas)
python instance_generator.py

# Executar avaliação
python evaluator.py instances results.csv
```

O script `evaluator.py` irá:
1. Processar todas as instâncias em `instances/`
2. Executar os três algoritmos em cada instância
3. Salvar os resultados em `results.csv`
4. Exibir estatísticas resumidas

## Saída

Para cada algoritmo, o programa exibe:
- **Lucro máximo**: Valor total obtido
- **Itens selecionados**: Lista de índices dos itens na mochila
- **Detalhes dos itens**: Peso, volume e valor de cada item selecionado
- **Peso total**: Soma dos pesos dos itens selecionados
- **Volume total**: Soma dos volumes dos itens selecionados
- **Tempo de execução**: Tempo em segundos

## Algoritmos Implementados

### 1. Programação Dinâmica
- **Complexidade**: O(n × W × V)
- **Vantagem**: Garante solução ótima
- **Desvantagem**: Pode ser lento para instâncias grandes

### 2. Backtracking
- **Complexidade**: O(2^n) no pior caso
- **Vantagem**: Simples de implementar
- **Desvantagem**: Pode ser muito lento para muitos itens
- **Otimização**: Inclui podas para melhorar desempenho

### 3. Branch-and-Bound
- **Complexidade**: O(2^n) no pior caso, mas geralmente melhor
- **Vantagem**: Usa bounds para podar ramos da árvore de busca
- **Desvantagem**: Ainda pode ser lento para instâncias muito grandes
- **Otimização**: Ordena itens por razão valor/peso e valor/volume

## Análise de Resultados

O arquivo `results.csv` gerado contém:
- Parâmetros da instância (n_items, W, V)
- Algoritmo usado
- Valor máximo encontrado
- Número de itens selecionados
- Tempo de execução
- Status de sucesso

Você pode usar este arquivo para:
- Comparar o desempenho dos algoritmos
- Analisar o comportamento assintótico
- Identificar qual algoritmo é mais eficiente para diferentes tamanhos de instância

## Requisitos

- Python 3.6 ou superior
- Bibliotecas padrão do Python (sem dependências externas)

## Exemplo de Execução

```bash
# Criar um arquivo de exemplo
echo -e "10\t9\n6\t3\t10\n3\t4\t14\n4\t2\t16\n2\t5\t9" > exemplo.txt

# Executar
python main.py exemplo.txt
```

## Notas

- Todos os algoritmos garantem encontrar a solução ótima
- Os tempos de execução podem variar significativamente dependendo do tamanho da instância
- Para instâncias muito grandes, o Backtracking pode ser muito lento
- A Programação Dinâmica é geralmente a mais eficiente para instâncias de tamanho médio
