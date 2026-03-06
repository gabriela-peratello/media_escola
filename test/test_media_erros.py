import pytest
from escola import verificar_media


def test_string():
     with pytest.raises(TypeError, match="Tipo inválido, a entrada deve ser numérica."):
          verificar_media("OITO")


def test_numero_negativo():
     with pytest.raises(ValueError, match="O valor deve ser maior ou igual a 0 e menor ou igual a 10."):
          verificar_media(-5)


def test_maior_10():
     with pytest.raises(ValueError, match="O valor deve ser menor ou igual a 0 e menor ou igual a 10."):
          verificar_media