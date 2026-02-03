import os

class file_handler:
    def __init__(self, path_):
        self.path_ = path_

    def listar_arquivos(self):
        texts = []
        for arquivo in os.listdir(self.path_):
            file_path = os.path.join(self.path_, arquivo)
            if os.path.isfile(file_path) and file_path.endswith(".txt"):
                texts.append(arquivo)
        return texts
        
    def ler_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, "r", encoding = 'utf-8') as f:
            return f.read()

    def ler_todos_arquivos(self):
        dict_txt = {}
        textos = self.listar_arquivos()
        
        for texto in textos:
            caminho_completo = os.path.join(self.path_, texto)
            dict_txt[texto] = self.ler_arquivo(caminho_completo)
        return dict_txt




p1 = file_handler("/home/breno/search-engine/data")
# # print(p1.listar_arquivos())
# print(p1.ler_arquivo("/home/breno/search-engine/data/notas_python.txt"))

print(p1.ler_todos_arquivos())
