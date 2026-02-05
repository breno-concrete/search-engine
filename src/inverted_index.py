from file_handler import FileHandler
from text_processor import TextProcessor



class Inverted_index:
    def __init__(self):
        self.file_handler = FileHandler()
        self.text_processor = TextProcessor()
    
    def clean_text(self, path_):
        text_dict = self.file_handler.ler_todos_arquivos(path_)
        index = {}
        for nome, texto_completo in text_dict.items():
            texto = self.text_processor.remove_ponctuations(texto_completo)
            texto = self.text_processor.lowercase(texto)
            texto = self.text_processor.remove_spaces(texto)
            tokens = self.text_processor.remove_stopwords(texto)

            index[nome] = tokens 

        return index

    def iv_index(self, dict_):
        inverted_index = {}
        for documento, palavras in dict_.items():
            lista_palavras = palavras
            for palavra in lista_palavras:
                if palavra not in inverted_index:
                    inverted_index[palavra] = []
                
                if documento not in inverted_index[palavra]:
                    inverted_index[palavra].append(documento)
        return inverted_index

#================= teste =====================================

if __name__ == "__main__":
    path = "../data"

    indexer = Inverted_index()

    # 1. Limpa os textos
    clean_docs = indexer.clean_text(path)

    print("\n=== TEXTOS PROCESSADOS ===")
    for doc, tokens in clean_docs.items():
        print(doc, "->", tokens)

    # 2. Cria o índice invertido
    inverted = indexer.iv_index(clean_docs)

    print("\n=== ÍNDICE INVERTIDO ===")
    for palavra, docs in inverted.items():
        print(palavra, "->", docs)



        
        

