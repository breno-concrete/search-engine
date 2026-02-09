import pytest
from unittest.mock import patch
from src.text_processor import TextProcessor



def test_remove_punctuations_retorna_string():
    
    processor = TextProcessor()
    texto = "Olá, meu amigo!!!"

    resultado = processor.remove_punctuations(texto)

    assert resultado == "Olá meu amigo"

def test_remove_punctuation_texto_limpo():
    
    processor = TextProcessor()
    texto = "Texto sem pontuacao"
    resultado = processor.remove_punctuations(texto)

    assert resultado == texto

def test_lowercase_converte_para_minusculo():
    processor = TextProcessor()

    texto = "Olá Mundo"
    resultado = processor.lowercase(texto)

    assert resultado == "olá mundo"

def test_remove_spaces_remove_espacos_inicio_fim():
    processor = TextProcessor()

    texto = "   Olá  mundo   "
    resultado = processor.remove_spaces(texto)

    assert resultado == "Olá mundo"

def test_separe_words():
    processor = TextProcessor()

    texto = "ab cd ef"
    resultado = processor.separe_words(texto)

    assert resultado == ["ab", "cd", "ef"]

def test_separe_words_return_list():
    processor = TextProcessor()

    texto = "ab cd ef"
    resultado = processor.separe_words(texto)

    assert isinstance(resultado, list)

def test_remove_stopwords():
    processor = TextProcessor()
        # Mock do método separe_words
    processor.separe_words = lambda texto: ["eu", "gosto", "de", "python"]

    # Mock das stopwords do NLTK
    with patch("nltk.corpus.stopwords.words") as mock_stopwords:
        mock_stopwords.return_value = ["eu", "de"]

        resultado = processor.remove_stopwords("qualquer texto")

        assert resultado == ["gosto", "python"]

def test_preprocess_integracao():
    processor = TextProcessor()
    
    texto = "Eu,  AMO   Python!!!"
    resultado = processor.preprocess(texto)

    assert resultado == ["amo", "python"]
