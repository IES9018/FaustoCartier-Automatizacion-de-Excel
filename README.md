# Automatización de Excel para la gestión financiera de PyMEs

Herramienta local para automatizar la lectura, validación, consolidación y generación de reportes financieros a partir de archivos Excel.

El proyecto está pensado para pequeñas y medianas empresas que necesitan registrar ingresos y egresos sin depender de consolidaciones manuales, fórmulas frágiles o varias planillas desconectadas.

## Estado del proyecto

**Fase actual:** definición y diseño (versión 0.1).

Actualmente el repositorio contiene la especificación funcional, la decisión tecnológica, un pipeline de CI básico y un test de humo. La implementación del script de la automatización (lectura, validación, consolidación, reportes y logs) todavía está pendiente.

## Objetivos

- Registrar movimientos de ingreso y egreso de capital.
- Leer información desde uno o más archivos Excel.
- Validar fechas, montos y columnas obligatorias antes de procesar los datos.
- Consolidar los movimientos en un registro único sin duplicar ni perder filas.
- Generar reportes diarios, semanales y mensuales.
- Mantener intactos los archivos originales.
- Dejar un histórico auditable de cada ejecución.

## Alcance inicial

La primera versión será una herramienta local para Windows, orientada principalmente al gerente o jefe de una PyME y pensada para ejecutarse con una acción o comando sencillo.

Quedan fuera del alcance inicial:

- Integraciones bancarias o con sistemas de facturación electrónica.
- Usuarios concurrentes y permisos por rol.
- Interfaz web o aplicación móvil.
- Predicciones y análisis financiero avanzado.

## Flujo previsto

1. El usuario coloca o actualiza el archivo Excel con los movimientos.
2. El programa lee y valida los datos.
3. Los movimientos válidos se consolidan en un dataset interno.
4. Se calculan ingresos, egresos y balance para el período solicitado.
5. Se genera un nuevo archivo Excel con el reporte.
6. Se registra la ejecución, incluidos los errores detectados.

Las filas inválidas deberán informarse sin detener innecesariamente el procesamiento de las filas correctas.

## Tecnología

- **Lenguaje:** Python.
- **Procesamiento de datos:** pandas.
- **Lectura y escritura de Excel:** se prevé utilizar openpyxl y/o xlsxwriter según las necesidades de implementación.
- **Plataforma objetivo:** Windows.

La elección de Python y pandas está documentada en [ADR-0001](docs/adr/0001-eleccion-python-pandas.md).

## Estructura actual

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── SPEC.md
│   └── adr/
│       └── 0001-eleccion-python-pandas.md
├── tests/
│   └── test_basico.py
├── README.md
└── requirements.txt
```

### Documentación

- [Especificación del proyecto](docs/SPEC.md): problema, objetivos, requisitos, flujo de datos, criterios de aceptación, riesgos y glosario.
- [ADR-0001: elección de Python y pandas](docs/adr/0001-eleccion-python-pandas.md): alternativas consideradas, decisión y consecuencias.

## Requisitos funcionales previstos

- Leer datos desde uno o más archivos Excel.
- Validar tipos de datos, columnas obligatorias y fechas válidas.
- Consolidar movimientos sin duplicaciones ni pérdida de filas.
- Generar reportes diarios con el detalle de movimientos.
- Generar reportes semanales con ingresos, egresos y balance.
- Generar reportes mensuales con totales y comparación con el mes anterior.
- Guardar los reportes en archivos nuevos, sin sobrescribir los originales.
- Registrar cada ejecución en un log legible.

## Requisitos de calidad

- **Integridad:** los archivos de origen no deben modificarse ni eliminarse.
- **Simplicidad:** la ejecución debe requerir una sola acción o comando.
- **Portabilidad:** debe poder utilizarse en Windows sin una instalación compleja.
- **Trazabilidad:** los errores deben quedar registrados.
- **Rendimiento:** el objetivo es procesar aproximadamente 10.000 filas en menos de 30 segundos.

## Instalación y uso

La implementación todavía no está disponible, por lo que aún no hay un comando de instalación o ejecución que pueda utilizarse.

Cuando se incorpore el código, esta sección deberá documentar como mínimo:

1. La versión de Python compatible.
2. La creación y activación del entorno virtual.
3. La instalación de dependencias.
4. El formato esperado para las columnas del Excel de entrada.
5. El comando de ejecución.
6. La ubicación y el formato de los reportes y logs generados.

## Próximos pasos

1. Definir el esquema exacto del Excel de entrada: columnas, tipos y valores permitidos.
2. Crear la estructura del código y la configuración de dependencias.
3. Implementar la lectura y validación de archivos.
4. Implementar la consolidación y las reglas de cálculo.
5. Generar reportes diarios, semanales y mensuales sin alterar los originales.
6. Incorporar logging y manejo de errores.
7. Añadir pruebas con datos válidos, inválidos y casos límite.
8. Documentar la instalación y evaluar la distribución como ejecutable para usuarios sin Python.

## Criterios de aceptación

La versión inicial se considerará lista cuando:

- Genere correctamente un reporte diario a partir de un Excel válido.
- Informe filas inválidas, como fechas vacías o montos no numéricos, sin fallar silenciosamente.
- Mantenga sin cambios el archivo original.
- Calcule correctamente los totales semanales y mensuales.
- Registre fecha, hora y resultado de cada ejecución.

## Documentación relacionada

- [SPEC.md](docs/SPEC.md)
- [ADR-0001](docs/adr/0001-eleccion-python-pandas.md)