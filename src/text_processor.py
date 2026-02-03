import string
import nltk
from nltk.corpus import stopwords


class text_processor:
    def __init__(self, texto):
        self.texto = texto

    def remove_ponctuations(self):
        punc = '''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¹º»¼½¾¿'''
        empty_text = ''
        for i in self.texto:
            if i not in punc:
                empty_text += i
        return empty_text
    
    def lowercase(self):
        return self.texto.lower()
    
    def remove_spaces(self):
        return ' '.join(self.texto.split())
    
    def separe_words(self):
        return self.texto.split()

    def remove_stopwords(self):
        empty_text = []
        texto_separado = self.separe_words()
        nltk.download('stopwords')
        stop_words_pt = set(stopwords.words('portuguese'))
        for i in texto_separado:
            if i not in stop_words_pt:
                empty_text.append(i)
        return empty_text



p1 = text_processor("Meu nome,        (oi) é um breno!!!")

# print(p1.remove_ponctuations())
# print(p1.lowercase())
print(p1.remove_stopwords())
