"""
Tests básicos del proyecto de Automatización de Excel.

Este archivo empieza como un test mínimo para que el pipeline de CI
tenga algo que ejecutar. A medida que se desarrollen las funciones
reales de lectura, validación y consolidación de datos, este archivo
(o nuevos archivos test_*.py dentro de tests/) deben ir sumando casos
reales, por ejemplo:

- test_lectura_excel_valido()
- test_deteccion_fila_invalida()
- test_calculo_balance_diario()
"""


def test_suma_basica():
    """Test de humo: confirma que el entorno de tests funciona correctamente."""
    assert 1 + 1 == 2