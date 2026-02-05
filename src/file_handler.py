import os

class FileHandler:
    def __init__(self):
        pass

    def listar_arquivos(self, path_):
        '''
        Lista apenas aqrquivos .txt de uma pasta

        Args:
            path_ (str): Caminho absoluto da pasta

        Returns:
            list: lista com nomes dos arquivos .txt

        Complexidade: O(n)
        '''
        texts = []
        for arquivo in os.listdir(path_):
            file_path = os.path.join(path_, arquivo)
            if os.path.isfile(file_path) and file_path.endswith(".txt"):
                texts.append(arquivo)
        return texts
        
    def ler_arquivo(self, caminho_arquivo):

        ''' 
        Lê conteúdo do arquivo .txt

        Args:
            caminho_arquivo (str): caminho absoluto do arquivo .txt

        Returns:
            string: Conteúdo completo do arquivo
        '''

        if not os.path.exists(caminho_arquivo):
            raise ValueError(f"Pasta não encontrada: {caminho_arquivo}") 
        
        with open(caminho_arquivo, "r", encoding = 'utf-8') as f:
            return f.read()

    def ler_todos_arquivos(self, path_):
        ''' 
        Lê conteúdo de todos arquivos .txt 

        Args:
            path_ (str): caminho absoluto da pasta

        Returns:
            dict: cada nome do arquivo ligado ao seu respectivo conteúdo 
        '''


        dict_txt = {}
        textos = self.listar_arquivos(path_)
        
        for texto in textos:
            caminho_completo = os.path.join(path_, texto)
            dict_txt[texto] = self.ler_arquivo(caminho_completo)
        return dict_txt

