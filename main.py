import os
from pathlib import Path
from src.file_handler import FileHandler
from src.inverted_index import InvertedIndex
from src.searcher import Searcher



def obter_pasta_arquivos():
    '''
    Obtém o caminho da pasta com os arquivos de busca
    
    Retorna:
        Path: Caminho válido da pasta
    
    Complexidade: O(1)
    '''
    while True:
        entrada = input("📁 Digite o caminho da pasta (ou deixe vazio para usar ./data/): ").strip()

        if entrada == '':
            caminho = Path("./data")
            print(f"✅ Utilizando diretório padrão: {caminho}\n")
        else:
            caminho = Path(entrada)

        if caminho.is_dir():
            return caminho
        else:
            print("❌ Caminho inválido ou não é uma pasta. Tente novamente.\n")


def carregar_indice(caminho_pasta):
    '''
    Carrega e processa os arquivos, criando o índice invertido
    
    Args:
        caminho_pasta (Path): Caminho da pasta com os arquivos
    
    Returns:
        dict: Índice invertido {palavra: [arquivos]}
    
    Complexidade: O(n * m) onde n = arquivos, m = palavras por arquivo
    '''
    ii = InvertedIndex()

    print("\n📦 Carregando e processando arquivos...")

    texto_limpo = ii.clean_text(caminho_pasta)
    indice_inverso = ii.iv_index(texto_limpo)

    print(f"✅ Índice criado com {len(indice_inverso)} palavras únicas\n")

    return indice_inverso

    
def mostrar_resultado(palavra, indice, searcher):
    '''
    Mostra resultados de uma busca simples com frequência
    
    Args:
        palavra (str): Palavra a buscar
        indice (dict): Índice invertido
        searcher (Searcher): Objeto searcher para operações
    
    Complexidade: O(n + k log k) onde n = docs, k = docs encontrados
    '''
    resultado = searcher.search(indice, palavra)
    
    if not resultado:
        print(f"❌ Nenhum resultado encontrado para '{palavra}'\n")
        return

    counter = searcher.counter(indice, palavra)
    ordem = searcher.order(counter)
    
    print(f"\n📊 Resultados para '{palavra}':")
    
    for i, (arquivo, quantidade) in enumerate(ordem.items(), 1):
        print(f"   {i}. {arquivo} ({quantidade} vezes) 🏆" if i == 1 else f"   {i}. {arquivo} ({quantidade} vezes)")
    print()

def mostrar_resultado_generico(arquivo_lista, termo_busca=""):
    '''
    Mostra resultados de busca AND/OR sem frequência
    
    Args:
        arquivo_lista (list): Lista de arquivos encontrados
        termo_busca (str): O termo que foi buscado (para mensagem)
    
    Complexidade: O(n) onde n = número de arquivos encontrados
    '''
    if not arquivo_lista:
        print(f"❌ Nenhum resultado encontrado para '{termo_busca}'\n")
        return

    print(f"\n📊 Arquivos encontrados para '{termo_busca}':")
    
    for i, arquivo in enumerate(arquivo_lista, 1):
        print(f"   {i}. {arquivo}")
    print()


def mostrar_ajuda():
    '''
    Mostra instruções de uso do programa
    
    Complexidade: O(1)
    '''
    print('''
╔════════════════════════════════════════╗
║         COMANDOS DISPONÍVEIS           ║
╚════════════════════════════════════════╝

📝 BUSCA SIMPLES:
   Digite uma palavra normalmente
   Exemplo: python
   
   Mostra frequência em cada arquivo

🔗 BUSCA AND (documentos com AMBAS as palavras):
   Digite com " and " no meio
   Exemplo: python AND banco
   
   Retorna só arquivos que têm as duas palavras

📌 BUSCA OR (documentos com UMA OU OUTRA palavra):
   Digite com " or " no meio
   Exemplo: python OR banco
   
   Retorna arquivos que têm pelo menos uma palavra

❓ AJUDA:
   Digite: ajuda
   
   Mostra este menu

🚪 SAIR:
   Digite: sair
   
   Encerra o programa

════════════════════════════════════════════════════
    ''')


def main():
    '''
    Função principal - orquestra todo o programa
    
    Fluxo:
        1. Obtém pasta do usuário
        2. Carrega e indexa arquivos
        3. Loop infinito de buscas
        4. Encerra quando usuário sair
    
    Complexidade: O(n*m) no carregamento + O(k) por busca
    '''
    print('''
╔════════════════════════════════════════╗
║    🔍 MECANISMO DE BUSCA PESSOAL      ║
╚════════════════════════════════════════╝
    ''')

    # Obter caminho
    caminho = obter_pasta_arquivos()

    # Carregar índice
    indice = carregar_indice(caminho)

    # Criar searcher
    sr = Searcher(caminho)

    # Menu
    print("💡 Digite 'AJUDA' para ver opções disponíveis\n")

    # Loop de busca
    while True:
        entrada = input("🔍 Digite uma palavra para buscar (ou 'SAIR'): ").strip()

        # Validações
        if entrada == '':
            print("⚠️  Digite algo!\n")
            continue

        if entrada == 'SAIR':
            break

        if entrada == 'AJUDA':
            mostrar_ajuda()
            continue

        # Converter para minúsculas para a busca
        entrada_lower = entrada.lower()

        # Busca OR
        if ' or ' in entrada_lower:
            resultado = sr.or_search(indice, entrada_lower)
            mostrar_resultado_generico(resultado, entrada)
            continue

        # Busca AND
        if ' and ' in entrada_lower:
            resultado = sr.and_search(indice, entrada_lower)
            mostrar_resultado_generico(resultado, entrada)
            continue

        # Busca simples
        mostrar_resultado(entrada_lower, indice, sr)

    # Despedida
    print('''
╔════════════════════════════════════════╗
║  👋 Obrigado por usar Search Engine!   ║
║             Até logo! 😊               ║
╚════════════════════════════════════════╝
    ''')


if __name__ == "__main__":
    main()