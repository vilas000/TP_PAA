# Guia Completo do Projeto - Problema da Mochila 0-1

## 📋 Visão Geral

Este projeto implementa e avalia empiricamente três algoritmos para resolver o **Problema da Mochila 0-1 com duas restrições** (peso e volume):
- **Programação Dinâmica (DP)**
- **Backtracking**
- **Branch-and-Bound (B&B)**

---

## 🔄 Fluxo de Funcionamento Completo
```

### 2. **Fluxo de Execução Individual** (`main.py`)

```
┌─────────────────┐
│  main.py        │
│  (entrada)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ file_reader.py  │ ← Lê arquivo .txt
│                 │   Formato: W V (primeira linha)
│                 │           peso volume valor (demais linhas)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Algoritmos:    │
│  - DP           │
│  - Backtracking │
│  - B&B          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Resultado:     │
│  - Valor máximo │
│  - Itens        │
│  - Tempo        │
└─────────────────┘
```

**Como funciona:**
1. `main.py` recebe o nome do arquivo de entrada e opcionalmente o algoritmo
2. `file_reader.py` lê e parseia o arquivo, retornando `(W, V, items)`
3. O(s) algoritmo(s) selecionado(s) processa(m) a instância
4. Os resultados são exibidos formatados

### 3. **Fluxo de Avaliação Empírica** (`evaluator.py`)

```
┌──────────────────────┐
│ instance_generator.py│ ← Gera 10 instâncias por configuração
│                      │   (n_items, W, V)
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   instances/         │ ← Diretório com arquivos .txt
│   n5_W10_V10_inst1   │
│   n5_W10_V10_inst2   │
│   ...                │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   evaluator.py       │ ← Processa cada instância
│                      │   Executa os 3 algoritmos
│                      │   Mede tempo de execução
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   results.csv        │ ← Resultados em CSV
│   (estatísticas)     │
└──────────┬───────────┘
           │
           ▼
┌────────────────────────┐
│ analisar_resultados.py │ ← Análise estatística
│                        │   Médias, medianas, gráficos
└────────────────────────┘
```

**Como funciona:**
1. `instance_generator.py` cria múltiplas instâncias de teste
2. `evaluator.py` processa todas as instâncias com os 3 algoritmos
3. Resultados são salvos em `results.csv`
4. `analisar_resultados.py` analisa e exibe estatísticas

---

## 🚀 Como Executar

### **Opção 1: Execução Individual (Teste Rápido)**

```bash
# Testar com arquivo de exemplo (todos os algoritmos)
python main.py exemplo.txt

# Testar apenas um algoritmo específico
python main.py exemplo.txt dp
python main.py exemplo.txt backtracking
python main.py exemplo.txt bnb
```

**Saída esperada:**
```
Capacidade da mochila: peso=10, volume=9
Número de itens: 4

Programação Dinâmica:
Lucro máximo: 30
Itens selecionados: [1, 2]
Detalhes dos itens:
  Item 1: peso=3, volume=4, valor=14
  Item 2: peso=4, volume=2, valor=16
Peso total: 7
Volume total: 6
Tempo de execução: 0.000123 segundos
...
```

### **Opção 2: Avaliação Empírica Completa**

```bash
# Passo 1: Gerar instâncias de teste
python instance_generator.py

# Passo 2: Executar avaliação (pode demorar alguns minutos)
python evaluator.py instances results.csv

# Passo 3: Analisar resultados
python analisar_resultados.py results.csv
```

**O que acontece:**
- **Passo 1**: Cria 100 instâncias (10 configurações × 10 instâncias cada)
- **Passo 2**: Executa os 3 algoritmos em todas as instâncias (300 execuções)
- **Passo 3**: Exibe estatísticas comparativas

---

## 📊 Detalhamento dos Algoritmos

### **1. Programação Dinâmica** 

**Como funciona:**
- Usa uma tabela 3D `dp[w][v]` = valor máximo com peso ≤ w e volume ≤ v
- Preenche a tabela iterativamente considerando cada item
- Complexidade: **O(n × W × V)** em tempo e espaço

**Vantagens:**
- ✅ Sempre encontra solução ótima
- ✅ Eficiente para instâncias médias

**Desvantagens:**
- ❌ Consome muita memória para W e V grandes
- ❌ Pode ser lento se W×V for muito grande

### **2. Backtracking** 

**Como funciona:**
- Explora todas as combinações possíveis recursivamente
- Usa podas para evitar caminhos inviáveis
- Complexidade: **O(2^n)** no pior caso

**Vantagens:**
- ✅ Simples de implementar
- ✅ Usa podas para melhorar desempenho

**Desvantagens:**
- ❌ Pode ser muito lento para n > 25
- ❌ Explora muitos caminhos desnecessários

### **3. Branch-and-Bound** 

**Como funciona:**
- Usa uma fila de prioridade para explorar nós promissores primeiro
- Calcula um "bound" (limite superior) para cada nó
- Poda nós cujo bound é menor que a melhor solução atual
- Ordena itens por razão valor/peso e valor/volume

**Vantagens:**
- ✅ Geralmente mais rápido que backtracking puro
- ✅ Usa heurísticas inteligentes

**Desvantagens:**
- ❌ Ainda pode ser lento para instâncias muito grandes
- ❌ Implementação mais complexa

---

## 📈 Análise de Resultados

O arquivo `results.csv` contém:
- `arquivo`: Nome do arquivo de instância
- `n_items`: Número de itens
- `W`, `V`: Capacidades da mochila
- `instancia`: Número da instância (1-10)
- `algoritmo`: DP, Backtracking ou Branch-and-Bound
- `valor_maximo`: Valor da solução encontrada
- `num_itens_selecionados`: Quantidade de itens na solução
- `tempo_execucao`: Tempo em segundos
- `sucesso`: True/False

**O script `analisar_resultados.py` calcula:**
- Tempo médio, mediano, mínimo e máximo por algoritmo
- Desvio padrão dos tempos
- Análise por tamanho de instância
- Verificação de consistência (todos devem encontrar o mesmo valor máximo)

---

## 🔍 Verificação de Funcionamento

### **Teste Rápido:**

```bash
# 1. Teste básico
python main.py exemplo.txt

# 2. Verifique se todos os algoritmos encontram o mesmo valor máximo
# (isso deve acontecer, pois todos são exatos)
```

### **Teste Completo:**

```bash
# 1. Gere instâncias pequenas primeiro (edite instance_generator.py)
# 2. Execute evaluator.py
# 3. Verifique results.csv
# 4. Execute analisar_resultados.py
```

---

## ⚠️ Observações Importantes

1. **Formato de arquivo**: Use **tabulação** (`\t`) para separar valores, não espaços
2. **Tempo de execução**: Backtracking pode demorar muito para n > 25
3. **Memória**: DP pode consumir muita memória para W×V > 1.000.000
4. **Consistência**: Todos os algoritmos devem encontrar o mesmo valor máximo (verifique com `analisar_resultados.py`)

---

## 📝 Formato de Entrada

```
W	V
peso1	volume1	valor1
peso2	volume2	valor2
...
```

**Exemplo (`exemplo.txt`):**
```
10	9
6	3	10
3	4	14
4	2	16
2	5	9
```

---

## 🎯 Próximos Passos Sugeridos

1. Execute `python main.py exemplo.txt` para testar
2. Gere instâncias: `python instance_generator.py`
3. Execute avaliação: `python evaluator.py`
4. Analise resultados: `python analisar_resultados.py`
