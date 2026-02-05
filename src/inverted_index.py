from .file_handler import FileHandler
from .text_processor import TextProcessor



class InvertedIndex:
    def __init__(self):
        self.file_handler = FileHandler()
        self.text_processor = TextProcessor()
    
    def clean_text(self, path_):

        ''' 
        Limpa os conteúdos textos e os coloca em um dicionário

        Args:
            caminho_arquivo (str): caminho absoluto dos arquivos

        Returns:
            dict: arquivos e seus respectivos conteúdos
        '''

        text_dict = self.file_handler.ler_todos_arquivos(path_)
        index = {}
        for nome, texto_completo in text_dict.items():
            tokens = self.text_processor.preprocess(texto_completo)
            index[nome] = tokens 

        return index

    def iv_index(self, dict_):
        ''' 
        Inverte os índices do dicionário

        Args:
            dict_ (dict): dicionário "limpo" dos textos e seus conteúdos

        Returns:
            dict: índices invertidos
        '''


        inverted_index = {}
        for documento, palavras in dict_.items():
            lista_palavras = palavras
            for palavra in lista_palavras:
                if palavra not in inverted_index:
                    inverted_index[palavra] = []
                
                if documento not in inverted_index[palavra]:
                    inverted_index[palavra].append(documento)
        return inverted_index

