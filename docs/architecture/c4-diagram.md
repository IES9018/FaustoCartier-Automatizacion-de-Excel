# Diagrama C4 — Automatización de Excel para pymes

Arquitectura propuesta: app de escritorio local en Python (empaquetada como
`.exe` con PyInstaller), sin servidor ni conexión a internet, que lee y
escribe directamente sobre el archivo Excel del cliente.

## Nivel 1 — Contexto

```mermaid
C4Context
    title Diagrama de contexto - Automatización de Excel

    Person(gerente, "Gerente / dueño de pyme", "Usa la herramienta para gestionar sus cuentas")

    System(sistema, "Automatización de Excel", "Permite limpiar, calcular y organizar las cuentas de la pyme sin conocimientos técnicos")

    System_Ext(excel, "Archivo Excel", "Archivo .xlsx local donde el cliente ya lleva sus cuentas")

    Rel(gerente, sistema, "Abre y usa")
    Rel(sistema, excel, "Lee y escribe", "Pandas / openpyxl")
```

## Nivel 2 — Contenedores

```mermaid
C4Container
    title Diagrama de contenedores - Automatización de Excel

    Person(gerente, "Gerente / dueño de pyme", "Usa la herramienta para gestionar sus cuentas")

    System_Boundary(sistema, "Automatización de Excel") {
        Container(interfaz, "Interfaz de escritorio", "Python (Tkinter / PySimpleGUI)", "Pantallas simples: cargar archivo, ver resultados, exportar")
        Container(motor, "Motor de procesamiento", "Python + Pandas", "Limpia datos, hace cálculos y genera reportes")
    }

    ContainerDb(excel, "Archivo Excel", ".xlsx local", "Datos de cuentas del cliente")

    Rel(gerente, interfaz, "Usa", "Doble clic, sin instalación de servidor")
    Rel(interfaz, motor, "Envía datos y pide procesamiento")
    Rel(motor, excel, "Lee y escribe", "openpyxl / pandas")
```

## Notas

- Sin servidor ni base de datos: todo corre en la máquina del cliente, sobre
  su propio archivo Excel. Esto simplifica mucho la puesta en marcha.
- Si más adelante agregas reportes en la nube, backups automáticos, o
  múltiples usuarios, ahí aparecería un nuevo contenedor (API/backend) y
  probablemente una base de datos — momento en el que conviene ampliar este
  diagrama.
- Si preferís PlantUML en vez de Mermaid (por ejemplo si tu editor no
  renderiza Mermaid), decime y te paso la versión equivalente con
  C4-PlantUML.
