import os
from .file_handler import FileHandler
from .text_processor import TextProcessor

class Searcher:
    def __init__(self, path_):
        self.file_handler = FileHandler()
        self.text_processor = TextProcessor()
        self.path_ = path_

    def search(self,  dict_, word):
        ''' 
        Busca palavras nos conteúdos dos arquivos

        Args:
            dict_ (dict): dicionário com índice invertido dos textos e seus conteúdos
            word (string): palavra a ser buscada

        Returns:
            list : lista de documentos onde aparece a palavra
        '''


        if word in dict_:
            return dict_[word]
        return []
        
    def counter(self, dict_, word):
        ''' 
        Conta quantas vezes uma palavra aparece no texto

        Args:
            dict_ (dict): dicionário com índice invertido dos textos e seus conteúdos
            word (string): palavra a ser buscada

        Returns:
            freq (dict): documentos e qunatas vezes "tal" palavra aparece neles
        '''

        docs = self.search(dict_, word)
        freq = {}
        
        for doc in docs:
            caminho =  os.path.join(self.path_, doc)
            texto = self.file_handler.ler_arquivo(caminho)


            tokens = self.text_processor.preprocess(texto)

            freq[doc] = tokens.count(word)

        return freq

    def order(self, freq):
        ''' 
        Ordena os documentos que mais aparecem a palavra

        Args:
            freq (dict): dicionário com os dcouemntos e o número de vezes que as palavras aparecem nele

        Returns:
            ordered (dict): dicionário com os documentos ordenados
        '''
        ordered = dict(sorted(freq.items(), key=lambda x: x[1], reverse = True))
        return ordered
        
    def or_search(self, dict_, word):
        ''' 
        Busca de palavras usando o parâmetro "OR"

        Args:
            dict_ (dict): dicionário com índice invertido dos textos e seus conteúdos
            word (string): palavra(s) a ser buscada (com " or " ou espaço como separador)

        Returns:
            list : lista de documentos onde aparece a(s) palavra(s)
        '''
        # Aceitar tanto " or " com espaços quanto sem
        if ' or ' in word:
            palavras_brutas = word.split(' or ')
        else:
            palavras_brutas = word.split()
        
        palavras = []
        for p in palavras_brutas:
            processado = self.text_processor.preprocess(p)
            if processado:
                palavras.append(processado[0])
        
        resultado = []
        if not palavras:
            return []
      
        for palavra in palavras:
            docs = self.search(dict_, palavra)
            for doc in docs:
                if not doc in resultado:
                    resultado.append(doc)

        return resultado
    
    def and_search(self, dict_, word):
        ''' 
        Busca de palavras usando o parâmetro "AND"

        Args:
            dict_ (dict): dicionário com índice invertido dos textos e seus conteúdos
            word (string): palavra(s) a ser buscada (com " and " ou espaço como separador)

        Returns:
            list : lista de documentos onde aparece a(s) palavra(s)
        '''

        # Aceitar tanto " and " com espaços quanto sem
        if ' and ' in word:
            palavras_brutas = word.split(' and ')
        else:
            palavras_brutas = word.split()
        
        palavras = []
        for p in palavras_brutas:
            processado = self.text_processor.preprocess(p)
            if processado:
                palavras.append(processado[0])

        if not palavras:
            return []
        
        resultado = self.search(dict_, palavras[0])
        
        for palavra in palavras[1:]:
            docs = self.search(dict_, palavra)
            resultado = [doc for doc in resultado if doc in docs]
        
        return resultado

