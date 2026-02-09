import pytest
from unittest.mock import patch
from src.searcher import Searcher


def test_search_retorna_lista():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt", "arquivo2.txt"],
        "dados": ["arquivo3.txt"]
    }
    
    resultado = searcher.search(indice_teste, "python")
    
    assert isinstance(resultado, list)


def test_search_encontra_palavra():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt", "arquivo2.txt"],
        "dados": ["arquivo3.txt"]
    }
    
    resultado = searcher.search(indice_teste, "python")
    
    assert resultado == ["arquivo1.txt", "arquivo2.txt"]


def test_search_palavra_nao_encontrada():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt"],
        "dados": ["arquivo3.txt"]
    }
    
    resultado = searcher.search(indice_teste, "inexistente")
    
    assert resultado == []


def test_counter_retorna_dicionario():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {"python": ["notas_python.txt"]}
    
    resultado = searcher.counter(indice_teste, "python")
    
    assert isinstance(resultado, dict)


def test_counter_conta_frequencia_corretamente():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["notas_python.txt", "anotanoes_oop.txt"]
    }
    
    resultado = searcher.counter(indice_teste, "python")
    
    assert "notas_python.txt" in resultado
    assert "anotanoes_oop.txt" in resultado
    assert isinstance(resultado["notas_python.txt"], int)


def test_order_retorna_dicionario_ordenado():
    searcher = Searcher("/home/breno/search-engine/data")
    
    freq_teste = {
        "arquivo1.txt": 2,
        "arquivo2.txt": 5,
        "arquivo3.txt": 1
    }
    
    resultado = searcher.order(freq_teste)
    
    assert isinstance(resultado, dict)
    assert list(resultado.values()) == [5, 2, 1]


def test_order_ordena_por_frequencia_decrescente():
    searcher = Searcher("/home/breno/search-engine/data")
    
    freq_teste = {
        "arquivo1.txt": 1,
        "arquivo2.txt": 10,
        "arquivo3.txt": 5
    }
    
    resultado = searcher.order(freq_teste)
    
    lista_ordenada = list(resultado.items())
    assert lista_ordenada[0] == ("arquivo2.txt", 10)
    assert lista_ordenada[1] == ("arquivo3.txt", 5)
    assert lista_ordenada[2] == ("arquivo1.txt", 1)


def test_or_search_retorna_lista():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt"],
        "banco": ["arquivo2.txt"]
    }
    
    resultado = searcher.or_search(indice_teste, "python banco")
    
    assert isinstance(resultado, list)


def test_or_search_encontra_uma_ou_outra_palavra():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt"],
        "banco": ["arquivo2.txt"],
        "dados": ["arquivo3.txt"]
    }
    
    resultado = searcher.or_search(indice_teste, "python banco")
    
    assert "arquivo1.txt" in resultado
    assert "arquivo2.txt" in resultado
    assert len(resultado) == 2


def test_or_search_sem_duplicatas():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt"],
        "banco": ["arquivo1.txt"]
    }
    
    resultado = searcher.or_search(indice_teste, "python banco")
    
    assert resultado.count("arquivo1.txt") == 1


def test_and_search_retorna_lista():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt", "arquivo2.txt"],
        "banco": ["arquivo2.txt", "arquivo3.txt"]
    }
    
    resultado = searcher.and_search(indice_teste, "python banco")
    
    assert isinstance(resultado, list)


def test_and_search_encontra_documentos_com_todas_palavras():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt", "arquivo2.txt"],
        "banco": ["arquivo2.txt", "arquivo3.txt"]
    }
    
    resultado = searcher.and_search(indice_teste, "python banco")
    
    assert resultado == ["arquivo2.txt"]


def test_and_search_nenhum_resultado():
    searcher = Searcher("/home/breno/search-engine/data")
    
    indice_teste = {
        "python": ["arquivo1.txt"],
        "banco": ["arquivo2.txt"]
    }
    
    resultado = searcher.and_search(indice_teste, "python banco")
    
    assert resultado == []


def test_pipeline_completo_busca():
    searcher = Searcher("/home/breno/search-engine/data")
    
    from src.inverted_index import InvertedIndex
    
    ii = InvertedIndex()
    textos_limpos = ii.clean_text("/home/breno/search-engine/data")
    indice = ii.iv_index(textos_limpos)
    
    resultado = searcher.search(indice, "python")
    
    assert isinstance(resultado, list)
    assert len(resultado) > 0

