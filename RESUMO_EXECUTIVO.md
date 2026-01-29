# 📋 Resumo Executivo - Projeto Mochila 0-1

## 🎯 O Que Este Projeto Faz?

Este projeto resolve o **Problema da Mochila 0-1 com duas restrições** (peso e volume) usando três algoritmos diferentes:
- **Programação Dinâmica** (mais eficiente para instâncias médias)
- **Backtracking** (simples, mas pode ser lento)
- **Branch-and-Bound** (balanceado, usa heurísticas)

---

## 🚀 Como Executar (3 Passos Simples)

### **1. Teste Rápido com Arquivo de Exemplo**
```bash
python main.py exemplo.txt
```
**Resultado:** Executa os 3 algoritmos e mostra qual encontrou o maior valor.

### **2. Gerar Instâncias de Teste**
```bash
python instance_generator.py
```
**Resultado:** Cria 100 arquivos de teste no diretório `instances/`.

### **3. Avaliação Empírica Completa**
```bash
python evaluator.py
python analyze_results.py
```
**Resultado:** Compara os 3 algoritmos em todas as instâncias e gera estatísticas.

---

## 📁 Estrutura do Projeto

```
trabalho_paa/
├── main.py                    ← Execução individual
├── evaluator.py              ← Avaliação completa
├── analyze_results.py         ← Análise estatística
├── instance_generator.py      ← Gera instâncias de teste
├── file_reader.py            ← Lê arquivos de entrada
├── knapsack_dp.py            ← Algoritmo 1: Programação Dinâmica
├── knapsack_backtracking.py  ← Algoritmo 2: Backtracking
├── knapsack_bnb.py           ← Algoritmo 3: Branch-and-Bound
├── exemplo.txt               ← Arquivo de exemplo
└── README.md                 ← Documentação básica
```

---

## 🔄 Fluxo de Dados

```
Arquivo .txt
    ↓
file_reader.py (lê e parseia)
    ↓
Algoritmo escolhido (DP/Backtracking/B&B)
    ↓
Resultado: (valor_maximo, itens_selecionados, tempo)
    ↓
Exibição formatada ou salvamento em CSV
```

---

## 📊 Formato de Entrada

**Arquivo `.txt` com:**
- **Primeira linha:** `W V` (capacidades máximas)
- **Demais linhas:** `peso volume valor` (um item por linha)
- **Separadores:** Espaços ou tabulações (ambos funcionam)

**Exemplo (`exemplo.txt`):**
```
10	9
6	3	10
3	4	14
4	2	16
2	5	9
```

---

## 📈 Saída Esperada

### **Execução Individual (`main.py`):**
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
```

### **Avaliação Empírica (`evaluator.py`):**
- Gera `results.csv` com todos os resultados
- Exibe estatísticas resumidas no terminal

### **Análise (`analyze_results.py`):**
- Estatísticas por algoritmo (média, mediana, desvio padrão)
- Análise por tamanho de instância
- Verificação de consistência

---

## ✅ O Que Foi Melhorado?

1. **✅ Corrigido:** `file_reader.py` agora aceita espaços OU tabulações consistentemente
2. **✅ Adicionado:** Tratamento de erros robusto (arquivo vazio, valores inválidos, etc.)
3. **✅ Criado:** Documentação completa (`GUIA_COMPLETO.md`)
4. **✅ Criado:** Lista de melhorias sugeridas (`MELHORIAS_SUGERIDAS.md`)

---

## 🎓 Para Entender o Comportamento Assintótico

1. **Gere instâncias variadas:**
   - Edite `instance_generator.py` para criar instâncias maiores
   - Exemplo: `(50, 100, 100)`, `(100, 200, 200)`, etc.

2. **Execute a avaliação:**
   ```bash
   python evaluator.py
   ```

3. **Analise os resultados:**
   ```bash
   python analyze_results.py
   ```

4. **Compare os tempos:**
   - **DP:** Cresce com `n × W × V`
   - **Backtracking:** Cresce exponencialmente com `n`
   - **B&B:** Cresce exponencialmente, mas com podas eficientes

---

## ⚠️ Pontos de Atenção

1. **Backtracking pode ser muito lento** para `n > 25`
2. **DP pode consumir muita memória** se `W × V > 1.000.000`
3. **Todos os algoritmos devem encontrar o mesmo valor máximo** (verifique com `analyze_results.py`)

---

## 📚 Documentação Disponível

- **`GUIA_COMPLETO.md`** - Explicação detalhada de todo o fluxo
- **`MELHORIAS_SUGERIDAS.md`** - Lista de melhorias possíveis
- **`README.md`** - Documentação básica do projeto
- **`RESUMO_EXECUTIVO.md`** - Este arquivo (visão geral rápida)

---

## 🎯 Próximos Passos Recomendados

1. ✅ **Teste básico:** `python main.py exemplo.txt`
2. ✅ **Gere instâncias:** `python instance_generator.py`
3. ✅ **Execute avaliação:** `python evaluator.py`
4. ✅ **Analise resultados:** `python analyze_results.py`
5. 📊 **Para melhorias:** Consulte `MELHORIAS_SUGERIDAS.md`

---

## 💡 Dicas

- Use `python main.py arquivo.txt dp` para testar apenas um algoritmo
- O arquivo `results.csv` pode ser aberto no Excel para análise visual
- Para instâncias muito grandes, considere aumentar o timeout no `evaluator.py`

---

**Projeto pronto para uso! 🚀**
