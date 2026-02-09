import pytest
from unittest.mock import patch
from src.file_handler import FileHandler

def test_listar_arquivos_retorna_lista(tmp_path):
    handler = FileHandler()

    resultado = handler.listar_arquivos(tmp_path)

    assert isinstance(resultado, list)

def test_listar_arquivos_so_txt(tmp_path):
    (tmp_path / "a.txt").write_text("1")
    (tmp_path / "b.txt").write_text("2")
    (tmp_path / "c.pdf").write_text("3")

    handler = FileHandler()
    resultado = handler.listar_arquivos(tmp_path)

    assert set(resultado) == {"a.txt", "b.txt"}

def test_ler_arquivos_retorna_string(tmp_path):
    handler = FileHandler()
    arquivo = tmp_path / "teste.txt"
    arquivo.write_text("Olá", encoding="UTF-8")
    resultado = handler.ler_arquivo(arquivo)

    assert isinstance(resultado, str)

def test_ler_arquivo_arquivo_inexistente(tmp_path):
    handler = FileHandler()

    caminho_inexistente = tmp_path / "nao_existe.txt"

    with pytest.raises(ValueError):
        handler.ler_arquivo(caminho_inexistente)

def test_ler_todos_arquivos_com_mock():
    handler = FileHandler()

    with patch.object(handler, "listar_arquivos") as mock_listar, \
         patch.object(handler, "ler_arquivo") as mock_ler:

        mock_listar.return_value = ["a.txt", "b.txt"]

        mock_ler.side_effect = lambda caminho: {
            "pasta/a.txt": "conteudo A",
            "pasta/b.txt": "conteudo B"
        }[caminho]

        resultado = handler.ler_todos_arquivos("pasta")

        assert resultado == {
            "a.txt": "conteudo A",
            "b.txt": "conteudo B"
        }


