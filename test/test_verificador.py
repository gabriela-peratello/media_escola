
import pytest
from escola import verificar_media

def test_aprovado():
    assert verificar_media(8) == "Aprovado"

def test_reprovado():
    assert verificar_media(4) == "Reprovado"

def test_recuperacao():
    assert verificar_media(6) == "Recuperação"