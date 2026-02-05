import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


class TextProcessor:
    def __init__(self):
        pass

    def remove_ponctuations(self, texto):
        punc = '''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¹º»¼½¾¿'''
        empty_text = ''
        for i in texto:
            if i not in punc:
                empty_text += i
        return empty_text
    
    def lowercase(self, texto):
        return texto.lower()
    
    def remove_spaces(self, texto):
        return ' '.join(texto.split())
    
    def separe_words(self, texto):
        return texto.split()

    def remove_stopwords(self, texto):
        empty_text = []
        texto_separado = self.separe_words(texto)
        stop_words_pt = set(stopwords.words('portuguese'))
        for i in texto_separado:
            if i not in stop_words_pt:
                empty_text.append(i)
        return empty_text



# p1 = text_processor("Meu nome,        (oi) é um breno!!!")

# # print(p1.remove_ponctuations())
# # print(p1.lowercase())
# print(p1.remove_stopwords())
