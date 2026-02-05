import string
import nltk
from nltk.corpus import stopwords


class TextProcessor:
    def __init__(self):
        pass

    def remove_punctuations(self, texto):
        ''' 
        Remove pontuação

        Args:
            texto (string): conteúdo do arquivo

        Returns:
            empty_text (string) : Conteúdo sem pontuações
        '''
        punc = '''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¹º»¼½¾¿'''
        empty_text = ''
        for i in texto:
            if i not in punc:
                empty_text += i
        return empty_text
    
    def lowercase(self, texto):
        ''' 
        Coloca todas as letras em padrão minúsculo

        Args:
            texto (string): conteúdo do arquivo

        Returns:
            texto (string) : Conteúdo em minúsculo
        '''
        return texto.lower()
    
    def remove_spaces(self, texto):
        ''' 
        Remove expaços extras

        Args:
            texto (string): conteúdo do arquivo

        Returns:
            ' '.join(texto.split()) (string) : Conteúdo sem espaços extras
        '''
        
        return ' '.join(texto.split())
    
    def separe_words(self, texto):
        ''' 
        Separa cada palavra

        Args:
            texto (string): conteúdo do arquivo

        Returns:
            texto.split() (array) : Lista com todas as palvras
        '''
        
        
        return texto.split()

    def remove_stopwords(self, texto):
        ''' 
        Remove "stopwords" do texto

        Args:
            texto (string): conteúdo do arquivo

        Returns:
            empty_text (array) : Lista com todas as palavras com exceção das "stopwords"
        '''
        
        empty_text = []
        texto_separado = self.separe_words(texto)
        stop_words_pt = set(stopwords.words('portuguese'))
        for i in texto_separado:
            if i not in stop_words_pt:
                empty_text.append(i)
        return empty_text

    def preprocess(self, texto):
        ''' 
        Realiza toda limpa de textos 

        Args:
            texto (string): conteúdo do arquivo

        Returns:
            tokens (array) : Lista com todas as palavras "limpas"
        '''
        texto = self.remove_punctuations(texto)
        texto = self.lowercase(texto)
        texto = self.remove_spaces(texto)
        tokens = self.remove_stopwords(texto)
        return tokens



# p1 = text_processor("Meu nome,        (oi) é um breno!!!")

# # print(p1.remove_ponctuations())
# # print(p1.lowercase())
# print(p1.remove_stopwords())
