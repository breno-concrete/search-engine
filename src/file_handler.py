import os

class FileHandler:
    def __init__(self):
        pass

    def listar_arquivos(self, path_):
        texts = []
        for arquivo in os.listdir(path_):
            file_path = os.path.join(path_, arquivo)
            if os.path.isfile(file_path) and file_path.endswith(".txt"):
                texts.append(arquivo)
        return texts
        
    def ler_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, "r", encoding = 'utf-8') as f:
            return f.read()

    def ler_todos_arquivos(self, path_):
        dict_txt = {}
        textos = self.listar_arquivos(path_)
        
        for texto in textos:
            caminho_completo = os.path.join(path_, texto)
            dict_txt[texto] = self.ler_arquivo(caminho_completo)
        return dict_txt




# p1 = FileHandler()
# print(p1.ler_todos_arquivos("/home/breno/search-engine/data"))

# print(p1.ler_arquivo("/home/breno/search-engine/data/notas_python.txt"))

# print(p1.ler_todos_arquivos())
