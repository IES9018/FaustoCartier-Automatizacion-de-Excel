# Proyecto Automatización de Excel — Notas y solución de errores

## Resumen rápido
Este README recoge la explicación de un error que apareció al intentar instalar dependencias y los pasos realizados para arreglarlo. También incluye instrucciones claras para reproducir, ejecutar y extender el proyecto en Windows/PowerShell.

## ¿Qué ocurrió? (causa del error)
- Mensaje original observado al intentar instalar: "Defaulting to user installation because normal site-packages is not writeable". Esto indica que pip no pudo escribir en los paquetes globales (falta de permisos), por lo que optó por instalar en el espacio de usuario. Esto es habitual cuando no se ejecuta como administrador.
- Error crítico: "Could not find a version that satisfies the requirement openpyx1" y "No matching distribution found for openpyx1". Esto ocurrió porque se escribió mal el nombre del paquete: `openpyx1` (con un '1') no existe. El paquete correcto para leer/escribir archivos .xlsx desde pandas es `openpyxl`.

## Qué hice aquí (pasos realizados, comentados)
1. Verifiqué y usé el entorno Python del proyecto (virtualenv) para instalar dependencias en el entorno correcto.
2. Instalé el paquete correcto `openpyxl` en el entorno del proyecto.
3. Verifiqué la versión de `openpyxl` importándolo (por ejemplo, se detectó la versión `3.1.5`).
4. Edité `main.py` para añadir:
   - Un intento de exportar el DataFrame a `ventas.xlsx` con manejo de excepciones y un mensaje claro si `openpyxl` falta.
   - Lectura posterior de `ventas.xlsx` y mostrar su contenido (el archivo se crea y se vuelve a leer en el script actual).
5. Al ejecutar el script con el Python del virtualenv faltaba `pandas` en el entorno, así que también instalé `pandas` en el virtualenv.
6. Ejecuté el script y confirmé que imprime el DataFrame y crea `ventas.xlsx`.

## Resultado comprobado
Salida de la ejecución (ejemplo):

```
    Nombre  Ventas
0      Juan     100
1     Pedro     500
2      Jose     200
3  Santiago      50
Archivo 'ventas.xlsx' creado correctamente en el directorio de trabajo.
```

El archivo `ventas.xlsx` se crea en el directorio del proyecto.

## Comandos recomendados (PowerShell / Windows)
Si no usas virtualenv y prefieres instalar localmente para tu usuario:

```powershell
python -m pip install --user openpyxl
```

Recomendado (crear y usar virtualenv dentro del proyecto):

```powershell
# crear virtualenv en la carpeta del proyecto (si no existe)
python -m venv .venv

# activar el virtualenv (PowerShell)
& .\.venv\Scripts\Activate.ps1

# instalar dependencias dentro del virtualenv
python -m pip install pandas openpyxl

# ejecutar el script
python .\main.py
```

Si no quieres activar el virtualenv, puedes llamar directamente al ejecutable del entorno (útil si hay espacios en la ruta); en PowerShell usa `&` antes de la ruta:

```powershell
& "c:/Users/faust/OneDrive/Desktop/Proyecto Automatización de Excel/.venv/Scripts/python.exe" "c:/Users/faust/OneDrive/Desktop/Proyecto Automatización de Excel/main.py"
```

Nota: en PowerShell se recomienda usar el operador `&` para ejecutar rutas que contengan espacios.

## Qué cambié en `main.py`
- Añadí un bloque que intenta guardar el DataFrame a `ventas.xlsx` y captura `ImportError` para mostrar un mensaje claro si falta `openpyxl`.
- Añadí manejo genérico de excepciones al guardar para mostrar el error exacto en caso de fallo.
- El archivo ahora también intenta leer `ventas.xlsx` y mostrar su contenido (útil para comprobar que la exportación fue correcta).

Contenido relevante aproximado (resumen):

```python
import pandas as pd

# ... crear DataFrame ...
print(df)

try:
    df.to_excel('ventas.xlsx', index=False)
    print("Archivo 'ventas.xlsx' creado correctamente en el directorio de trabajo.")
except ImportError:
    print("No se pudo guardar a Excel: falta el paquete 'openpyxl'. Instálalo con:\npython -m pip install --user openpyxl")
except Exception as e:
    print('Error al guardar el archivo Excel:', e)

# leer ventas.xlsx y mostrar
df = pd.read_excel('ventas.xlsx')
print(df)
```

## Recomendaciones / siguientes pasos
- Crear un `requirements.txt` con las dependencias del proyecto para que sea más sencillo instalar todo (ejemplo abajo). Si quieres, lo creo ahora.

Ejemplo `requirements.txt` mínimo:
```
pandas
openpyxl
```

- Si prefieres que el script pida por consola el nombre del archivo de salida o una ruta, puedo modificar `main.py` para añadir una opción interactiva o parámetros de línea de comandos.
- Puedo añadir un pequeño `README` más técnico con instrucciones para producción (por ejemplo, cómo crear un instalador, usar Task Scheduler, etc.).

## Cómo comprobar que todo funciona
1. Asegúrate de ejecutar el Python del virtualenv o instalar las dependencias en tu usuario.
2. Ejecuta `main.py` con el Python correcto (ver sección comandos).
3. Revisa que exista `ventas.xlsx` en el directorio del proyecto y ábrelo con Excel o con pandas (`pd.read_excel('ventas.xlsx')`).

---

Si quieres que cree ahora mismo `requirements.txt` y/o un README más corto con solo los comandos rápidos, dime cuál prefieres (creo ambos sin problema). También puedo revertir cambios en `main.py` o refactorizar para entrada/argumentos si lo deseas.