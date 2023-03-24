import pytest
from example_new_code import diptongos


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("peine", True),
        ("caer", False),
        ("ruido", True),
        ("cambiar", True),
    ],
)
def test_diptongos(texto, esperado):
    resultado = diptongos(texto)
    assert resultado == esperado
