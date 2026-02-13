
import pytest
from escola import verificar_media

def aprovado_test():
    # verificar resultado
    assert verificar_media(8) == "Aprovado"
