import pytest
from escola import verificar_media

# Teste parametrizado - Única função com vários valores
@pytest.mark.parametrize(
    ("media", "resultado_esperado"),
    [
        (7,"Aprovado"),
        (5, "Recuperação"),
        (5.5, "Recuperação"),
        (0, "Reprovado"),
        (10, "Aprovado"),
    ]
)
def test_testando_bordas(media, resultado_esperado):
    assert verificar_media(media == resultado_esperado)