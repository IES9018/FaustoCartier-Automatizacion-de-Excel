# ADR-0001: Uso de Python y Pandas para la automatización de reportes de Excel

**Estado:** Aceptada
**Fecha:** 2026-09-10
**Decisores:** Fausto Cartier

## Contexto

Se necesita construir una herramienta que automatice la lectura, consolidación y
generación de reportes (diarios, semanales, mensuales) de ingresos y egresos de
capital para PyMEs, a partir de archivos Excel.

El usuario final es el gerente o jefe de la empresa, con bajo nivel técnico, por lo
que la solución debe ser simple de ejecutar y mantener. Quien desarrolla el proyecto
tiene conocimientos iniciales de Python y está aprendiendo la librería pandas, la
cual además es ampliamente recomendada para este tipo de tareas.

Era necesario elegir una tecnología base antes de empezar a construir el sistema
descrito en el SPEC.

## Opciones consideradas

### 1. Python + pandas
- Lenguaje de propósito general, sintaxis simple.
- pandas está diseñado específicamente para manipulación y análisis de datos
  tabulares (como los que se manejan en Excel).
- Gran cantidad de documentación y comunidad activa.
- Se integra bien con librerías para leer/escribir Excel (openpyxl, xlsxwriter).

### 2. VBA / Macros nativas de Excel
- Ya integrado dentro de Excel, no requiere instalar nada adicional.
- Sintaxis más antigua y menos intuitiva para quien recién empieza a programar.
- Mantenimiento más difícil a largo plazo; menos portable fuera del ecosistema Excel.

### 3. Power Query / Power Automate
- Buena opción para transformaciones dentro del ecosistema Microsoft.
- Menos flexible para lógica de negocio compleja (validaciones, reglas de negocio,
  generación de logs, cálculos personalizados por período).
- Curva de aprendizaje distinta a la que ya se está desarrollando (Python).

## Decisión

Se elige **Python con la librería pandas** como stack principal para la automatización.

Razones principales:

1. **Curva de aprendizaje:** Python es un lenguaje sencillo de manejar, lo que facilita
   tanto el desarrollo inicial como el mantenimiento futuro del proyecto.
2. **Alineación con el aprendizaje actual:** quien desarrolla el proyecto ya está
   aprendiendo pandas, y fue la librería recomendada específicamente para este tipo
   de automatización.
3. **Adecuación técnica:** pandas está pensado para exactamente este tipo de problema
   (lectura, limpieza, validación y consolidación de datos tabulares), lo que reduce
   la cantidad de código necesario comparado con VBA.
4. **Escalabilidad futura:** si más adelante se necesita agregar validaciones más
   complejas, generación de gráficos, o incluso una interfaz simple, el ecosistema
   Python lo permite sin cambiar de tecnología base.

## Consecuencias

**Positivas:**
- Desarrollo más rápido gracias a la simplicidad de pandas para manipular datos.
- Código más mantenible y testeable que una solución en VBA.
- Posibilidad de reutilizar el conocimiento adquirido en futuros proyectos.

**Negativas / trade-offs:**
- El usuario final no tiene Python instalado por defecto (a diferencia de VBA, que
  ya viene con Excel), por lo que habrá que resolver cómo distribuir la herramienta
  (ej: ejecutable empaquetado, instalador simple, o instrucciones claras de instalación).
- Se depende de librerías externas (pandas, openpyxl) que deben mantenerse actualizadas.
- Al ser quien desarrolla todavía está aprendiendo pandas, es posible que la primera
  versión requiera refactorización a medida que se profundice en la librería.

## Notas

Esta decisión podría revisarse en una futura ADR si, por ejemplo, se necesitara
empaquetar la herramienta como un complemento nativo de Excel o si el proyecto
creciera a un uso multiusuario que requiera otro tipo de arquitectura (por ejemplo,
una base de datos en vez de archivos Excel como fuente de verdad).
