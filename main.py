import pandas as pd

data = {
    "Nombre": ["Juan", "Pedro", "Jose", "Santiago"],
    "Ventas": [100, 500, 200, 50]
}

df = pd.DataFrame(data)

print(df)

# Intentar exportar a Excel (.xlsx). Requiere el paquete `openpyxl`.
try:
    df.to_excel('ventas.xlsx', index=False)
    print("Archivo 'ventas.xlsx' creado correctamente en el directorio de trabajo.")
except ImportError:
    # Esto ocurriría si falta el motor para escribir .xlsx
    print("No se pudo guardar a Excel: falta el paquete 'openpyxl'. Instálalo con:\npython -m pip install --user openpyxl")
except Exception as e:
    print('Error al guardar el archivo Excel:', e)
    

import pandas as pd 
df = pd.read_excel("ventas.xlsx")
print(df)