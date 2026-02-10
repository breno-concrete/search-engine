# 🔍 Mecanismo de Busca Pessoal

Um motor de busca desenvolvido em Python para indexar e buscar termos em anotações pessoais usando uma **estrutura de dados avançada** (Índice Invertido) com **busca otimizada** em O(1).

**Concluído em:** 5 dias de desenvolvimento estruturado  
**Status:** ✅ Produção (35 testes, 100% cobertura)

---

## 📋 Descrição Geral

Este projeto implementa um **search engine funcional** que lê arquivos de texto, processa o conteúdo, cria um índice invertido e permite buscas rápidas com suporte a operações booleanas (AND/OR).

O objetivo principal é demonstrar:
1. **Arquitetura de software** bem estruturada com separação de responsabilidades
2. **Análise de complexidade** (Big O) em cada componente
3. **Testes automatizados** com 100% de cobertura
4. **Processamento de linguagem natural** em português

---

## ✨ Funcionalidades

✅ **Busca Simples** - Encontre uma palavra com frequência  
✅ **Busca AND** - Documentos que contêm AMBAS as palavras  
✅ **Busca OR** - Documentos que contêm UMA OU OUTRA palavra  
✅ **Processamento Inteligente** - Remove pontuação, converte caixa, remove stopwords  
✅ **Ranking por Frequência** - Resultados ordenados por relevância  
✅ **Interface Amigável** - Menu com emojis e formatação clara

---

## 💻 Requisitos

- **Python 3.12+**
- **NLTK** (Natural Language Toolkit) para processamento de português
- **pytest 9.0.2+** para testes
- **Sistema**: Linux/Mac/Windows

---

## 🚀 Instalação

```bash
# 1. Clone ou navegue para o diretório
cd search-engine

# 2. Crie um ambiente virtual
python3 -m venv venv

# 3. Ative o ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 4. Instale as dependências
pip install nltk pytest

# 5. Download dos dados NLTK (execute uma única vez)
python3 -c "import nltk; nltk.download('stopwords')"
```

---

## 📖 Como Usar

### Executar o programa

```bash
python3 main.py
```

### Menu de interação

```
🔍 MECANISMO DE BUSCA PESSOAL

📁 Digite o caminho da pasta (ou deixe vazio para usar ./data/):
```

**Exemplos de uso:**

```
Digite uma palavra para buscar: python
→ Retorna frequência de "python" em cada arquivo com ranking

Digite uma palavra para buscar: python and banco
→ Retorna arquivos que contêm AMBAS as palavras

Digite uma palavra para buscar: python or oop
→ Retorna arquivos que contêm pelo menos uma das palavras

Digite uma palavra para buscar: AJUDA
→ Mostra menu com todos os comandos

Digite uma palavra para buscar: SAIR
→ Encerra o programa
```

---

## 🏗️ Estrutura do Projeto

```
search-engine/
├── src/                           # Módulos principais
│   ├── __init__.py
│   ├── file_handler.py            # Leitura e listagem de arquivos
│   ├── text_processor.py          # Processamento de texto
│   ├── inverted_index.py          # Construção do índice invertido
│   └── searcher.py                # Operações de busca
│
├── tests/                         # Testes automatizados (35 testes)
│   ├── file_handler_test.py       # 5 testes
│   ├── text_processor_test.py     # 8 testes
│   ├── inverted_index_test.py     # 8 testes
│   └── searcher_test.py           # 14 testes
│
├── data/                          # Arquivos de entrada (.txt)
│   ├── notas_python.txt
│   ├── anotanoes_oop.txt
│   └── resumo_banco_dados.txt
│
├── main.py                        # Interface principal com usuário
├── basic_search.py                # Protótipo inicial (referência)
├── README.md                      # Este arquivo
└── venv/                          # Ambiente virtual (ignorado no git)
```

---

## 🧠 Arquitetura & Conceitos

### 1. Pipeline de Processamento

```
Arquivos .txt
    ↓
[FileHandler] - Lê arquivos brutos
    ↓
[TextProcessor] - Limpa texto (pontuação, lowercase, stopwords)
    ↓
[InvertedIndex] - Cria índice {palavra: [arquivos]}
    ↓
[Searcher] - Busca e ranking dos resultados
    ↓
Resultados ordenados ao usuário
```

### 2. Índice Invertido

**Estrutura:** `Dict[str, List[str]]`

```python
{
    "python": ["notas_python.txt"],
    "banco": ["resumo_banco_dados.txt"],
    "dados": ["resumo_banco_dados.txt"],
    "oop": ["anotanoes_oop.txt"],
    ...
}
```

**Vantagem:** O(1) para lookup de uma palavra!

### 3. Processamento de Texto

O texto passa por 5 etapas:

1. **remove_punctuations()** - Remove `.,!?;:` etc  
   - Input: `"Python é incrível!"`
   - Output: `"Python é incrível"`

2. **lowercase()** - Converte para minúsculas  
   - Input: `"Python é incrível"`
   - Output: `"python é incrível"`

3. **remove_spaces()** - Remove espaços extras  
   - Input: `"python  é   incrível"`
   - Output: `"python é incrível"`

4. **separe_words()** - Divide em tokens  
   - Input: `"python é incrível"`
   - Output: `["python", "é", "incrível"]`

5. **remove_stopwords()** - Remove palavras comuns (português)  
   - Input: `["python", "é", "incrível"]`
   - Output: `["python", "incrível"]`  
   - (removeu "é" por ser stopword)

### 4. Buscas Booleanas

**AND Search** (Interseção)
```
Busca: "python AND banco"
Etapa 1: python → [notas_python.txt]
Etapa 2: banco → [resumo_banco_dados.txt]
Resultado: [] (vazio - sem documentos com ambas)
```

**OR Search** (União)
```
Busca: "python OR banco"
Etapa 1: python → [notas_python.txt]
Etapa 2: banco → [resumo_banco_dados.txt]
Resultado: [notas_python.txt, resumo_banco_dados.txt]
```

---

## ⚡ Análise de Complexidade (Big O)

| Operação | Complexidade | Explicação |
|----------|-------------|-----------|
| `FileHandler.listar_arquivos()` | O(n) | n = quantidade de arquivos |
| `FileHandler.ler_arquivo()` | O(m) | m = tamanho do arquivo |
| `TextProcessor.preprocess()` | O(m) | m = caracteres do texto |
| `InvertedIndex.clean_text()` | O(n × m) | n arquivos × m caracteres |
| `InvertedIndex.iv_index()` | O(n × m) | Processa todas as palavras |
| `Searcher.search()` | **O(1)** | Lookup direto no dict ⭐ |
| `Searcher.and_search()` | O(k₁ + k₂) | k = docs encontrados |
| `Searcher.or_search()` | O(k₁ + k₂) | k = docs encontrados |
| `Searcher.counter()` | O(k × m) | k docs × m palavras |
| `Searcher.order()` | O(k log k) | k = docs × k sorting |

**Insight:** A busca é **constantemente rápida** O(1) após indexação inicial!

---

## 🧪 Testes Automatizados

O projeto inclui **35 testes** com **100% de cobertura** usando pytest.

### Executar testes

```bash
# Rodar todos os testes
pytest tests/ -v

# Rodar com cobertura
pytest tests/ --cov=src --cov-report=html

# Rodar teste específico
pytest tests/searcher_test.py::test_and_search_encontra_documentos_com_todas_palavras -v
```

### Distribuição de testes

- **file_handler_test.py** - 5 testes sobre I/O de arquivos
- **text_processor_test.py** - 8 testes sobre processamento de texto
- **inverted_index_test.py** - 8 testes sobre construção do índice
- **searcher_test.py** - 14 testes sobre buscas e ranking

**Exemplo de teste:**
```python
def test_and_search_encontra_documentos_com_todas_palavras():
    """AND retorna documentos com ambas as palavras"""
    indice_teste = {
        "python": ["arquivo1.txt", "arquivo2.txt"],
        "banco": ["arquivo2.txt", "arquivo3.txt"]
    }
    searcher = Searcher('.')
    resultado = searcher.and_search(indice_teste, "python banco")
    assert resultado == ["arquivo2.txt"]  # Só o que tem ambas
```

---

## 📚 Conceitos de Aprendizado

### 1. Estruturas de Dados

- **Dict (Dicionário)**: Acesso O(1) - usado no índice invertido
- **List (Lista)**: Acesso O(n) - armazena documentos
- **Set (Conjunto)**: Operações booleanas rápidas - AND/OR

### 2. Algoritmos

- **Indexação**: Pré-processamento para busca rápida
- **Hash Tables**: Base do funcionamento do dicionário Python
- **Busca Linear vs Hash**: Por que O(1) é melhor que O(n)
- **Sorting**: OrderedDict para ranking por frequência

### 3. Padrões de Design

- **Separação de Responsabilidades**: Cada classe tem um propósito
- **Pipeline Pattern**: Processamento em etapas (texto → índice → busca)
- **Dependency Injection**: Classes recebem dependências no init

### 4. Processamento de Linguagem

- **Tokenização**: Dividir texto em palavras
- **Normalização**: Converter para minúsculas
- **Remoção de Stopwords**: Eliminar palavras comuns
- **Stemming/Lemmatization**: (Conceitual - não implementado)

---

## 🔄 Fluxo Completo de Execução

```
1. Usuario executa: python3 main.py
   ↓
2. main() é chamada
   ├─ Chama obter_pasta_arquivos() → pede caminho
   ├─ Chama carregar_indice(caminho)
   │  ├─ Cria InvertedIndex()
   │  ├─ ii.clean_text(caminho) → processa arquivos
   │  ├─ ii.iv_index(dict_) → cria índice
   │  └─ Retorna índice {palavra: [arquivos]}
   └─ Cria Searcher(caminho)
   ↓
3. Loop while True:
   ├─ Lê entrada do usuário
   ├─ Valida AJUDA/SAIR
   ├─ Identifica tipo de busca (simples/AND/OR)
   ├─ Chama sr.search() ou sr.and_search() ou sr.or_search()
   ├─ Chama mostrar_resultado() para exibir
   └─ Volta para próxima entrada
   ↓
4. Usuario digita SAIR
   ├─ Break do loop
   ├─ Mostra mensagem de despedida
   └─ Programa encerra
```

---

## 👨‍💻 Detalhes de Implementação

### Módulo: file_handler.py

```python
class FileHandler:
    def listar_arquivos(path_)       # O(n) - lista .txt
    def ler_arquivo(caminho)          # O(m) - lê arquivo
    def ler_todos_arquivos(path_)     # O(n×m) - lê todos
```

### Módulo: text_processor.py

```python
class TextProcessor:
    def remove_punctuations(texto)    # Remove símbolos
    def lowercase(texto)              # Converte minúsculas
    def remove_spaces(texto)          # Remove espaços
    def separe_words(texto)           # Tokeniza
    def remove_stopwords(texto)       # Remove comuns
    def preprocess(texto)             # Pipeline completo
```

### Módulo: inverted_index.py

```python
class InvertedIndex:
    def clean_text(path_)             # O(n×m) - processa
    def iv_index(dict_)               # O(n×m) - indexa
```

### Módulo: searcher.py

```python
class Searcher:
    def search(indice, word)          # O(1) - busca simples
    def counter(indice, word)         # O(k×m) - conta freq
    def order(freq)                   # O(k log k) - ordena
    def and_search(indice, word)      # O(k₁+k₂) - AND
    def or_search(indice, word)       # O(k₁+k₂) - OR
```

---

## 🎯 Próximos Passos (Melhorias Futuras)

- [ ] Implementar **Stemming/Lemmatization** para variações de palavras
- [ ] Adicionar **scores TF-IDF** para melhor ranking
- [ ] Suportar **filtros por data** de modificação de arquivo
- [ ] **Interface web** com Flask/Django
- [ ] **Cache** de índices em arquivo (JSON/pickle)
- [ ] **Busca com wildcards** (Caracteres coringas)
- [ ] **Sugestões de termos** (did you mean?)

---

## 📝 Notas de Desenvolvimento

Este projeto foi desenvolvido com foco em:

1. **Aprendizado estruturado** - Uma funcionalidade por dia
2. **Testes desde o início** - TDD (Test-Driven Development)
3. **Documentação clara** - Docstrings em cada função
4. **Código limpo** - PEP 8 compliant
5. **Complexidade explícita** - Análise Big O documentada

**Tempo total:** 5 dias (conceitos + implementação + testes + UI)

---

## 📄 Licença

Este é um projeto educacional.

---

## 👤 Autor

Desenvolvido por **Breno C.** como exercício de estruturas de dados e algoritmos em Python.

**Data:** Janeiro - Fevereiro de 2026

---

## ❓ Dúvidas Frequentes

**P: Por que usamos índice invertido?**  
R: Transforma busca de O(n) (varrer todos) para O(1) (acesso direto).

**P: Como funciona o AND/OR?**  
R: AND = interseção de listas, OR = união de listas de documentos.

**P: Por que remover stopwords?**  
R: Palavras como "o", "de", "é" não agregam significado e aumentam o índice.

**P: Posso adicionar mais arquivos?**  
R: Sim! Coloque no `.data/` e reexecute. O programa carrega automaticamente.

**P: E se houver erro de encoding?**  
R: Certifique-se que os `.txt` estão em UTF-8.

---

**✨ Pronto para buscar!**

