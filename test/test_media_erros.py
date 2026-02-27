import pytest
from escola import verificar_media


def test_string():
     with pytest.raises(TypeError, match="Tipo iválido, a entrada deve sernumérica."):
          verificar_media("OITO")