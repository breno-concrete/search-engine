import pytest
from unittest.mock import patch
from src.inverted_index import InvertedIndex


def test_clean_text_retorna_dicionario():
    inverted_index = InvertedIndex()
    
    resultado = inverted_index.clean_text("/home/breno/search-engine/data")
    
    assert isinstance(resultado, dict)


def test_clean_text_arquivos_processados():
    inverted_index = InvertedIndex()
    
    resultado = inverted_index.clean_text("/home/breno/search-engine/data")
    
    assert len(resultado) == 3
    assert "notas_python.txt" in resultado
    assert "anotanoes_oop.txt" in resultado
    assert "resumo_banco_dados.txt" in resultado


def test_clean_text_retorna_listas():
    inverted_index = InvertedIndex()
    
    resultado = inverted_index.clean_text("/home/breno/search-engine/data")
    
    for arquivo, palavras in resultado.items():
        assert isinstance(palavras, list)
        assert len(palavras) > 0


def test_iv_index_retorna_dicionario():
    inverted_index = InvertedIndex()
    
    dict_teste = {
        "arquivo1.txt": ["python", "linguagem", "python"],
        "arquivo2.txt": ["banco", "dados", "sql"]
    }
    
    resultado = inverted_index.iv_index(dict_teste)
    
    assert isinstance(resultado, dict)


def test_iv_index_mapeia_palavras_corretamente():
    inverted_index = InvertedIndex()
    
    dict_teste = {
        "arquivo1.txt": ["python", "linguagem"],
        "arquivo2.txt": ["python", "dados"]
    }
    
    resultado = inverted_index.iv_index(dict_teste)
    
    assert resultado["python"] == ["arquivo1.txt", "arquivo2.txt"]
    assert resultado["linguagem"] == ["arquivo1.txt"]
    assert resultado["dados"] == ["arquivo2.txt"]


def test_iv_index_nao_duplica_documentos():
    inverted_index = InvertedIndex()
    
    dict_teste = {
        "arquivo1.txt": ["python", "python", "python"]
    }
    
    resultado = inverted_index.iv_index(dict_teste)
    
    assert len(resultado["python"]) == 1
    assert resultado["python"] == ["arquivo1.txt"]


def test_iv_index_com_mock():
    inverted_index = InvertedIndex()
    
    with patch.object(inverted_index, "clean_text") as mock_clean:
        mock_clean.return_value = {
            "doc1.txt": ["palavra1", "palavra2"],
            "doc2.txt": ["palavra1", "palavra3"]
        }
        
        dict_limpo = mock_clean("/fake/path")
        resultado = inverted_index.iv_index(dict_limpo)
        
        assert "palavra1" in resultado
        assert len(resultado["palavra1"]) == 2


def test_pipeline_completo_inverted_index():
    inverted_index = InvertedIndex()
    
    caminho = "/home/breno/search-engine/data"
    textos_limpos = inverted_index.clean_text(caminho)
    indice = inverted_index.iv_index(textos_limpos)
    
    assert isinstance(indice, dict)
    assert len(indice) > 0
    assert all(isinstance(docs, list) for docs in indice.values())

