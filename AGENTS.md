# Reglas del agente

## Qué puede tocar
- Archivos Python (.py): scripts del módulo principal y tests
- requirements.txt, opencode.json, .gitignore, ci.yml
- Archivos bajo tests/
- Docs: solo bajo pedido explícito del usuario
- Nunca archivos Excel de datos de usuario (.xlsx, .xlsm)

## Estándares que debe seguir
- Python 3.12, pandas 3.0.2, openpyxl 3.1.5, target Windows
- Sin comentarios en código salvo que se pidan
- Estilo flake8 (select=E9,F63,F7,F82) como el CI
- Correr flake8 + pytest después de cada cambio antes de dar por terminado
- Respetar docs/SPEC.md como fuente de verdad funcional

## Prácticas prohibidas
- Modificar o sobrescribir archivos Excel de origen del usuario (RF-07 / RNF-01)
- Versionar archivos .xlsx en el repo (gitignored)
- Implementar features out-of-scope: integraciones bancarias, multi-usuario, interfaz web/móvil, forecasting
- Hacer commits, push o PR sin que el usuario lo pida
- Introducir secretos o claves en el código
- Modificar docs/SPEC.md o docs/adr/ sin pedido explícito
