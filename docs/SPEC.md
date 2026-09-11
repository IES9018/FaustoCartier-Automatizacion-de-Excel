# SPEC — Automatización de Excel para Gestión Financiera de PyMEs

**Versión:** 0.1 (borrador)
**Autor:** Fausto Cartier
**Fecha:** 2026-09-10
**Estado:** En definición

---

## 1. Resumen

Sistema de automatización que ayuda a pequeñas y medianas empresas (PyMEs) a generar
reportes diarios, semanales y mensuales de ingresos y egresos de capital, evitando la
pérdida o inconsistencia de datos que ocurre habitualmente al llevar estos registros
de forma manual en planillas de Excel.

## 2. Problema

Actualmente el registro de ingresos y egresos en las PyMEs se hace de forma manual en
Excel. Esto genera:

- Pérdida de datos por errores humanos (sobrescritura de celdas, fórmulas rotas, etc.)
- Falta de consistencia entre reportes diarios, semanales y mensuales.
- Tiempo perdido consolidando información dispersa en varias planillas.
- Dificultad para que el gerente/dueño tenga una visión clara y rápida del flujo de caja.

## 3. Objetivo

Automatizar la carga, consolidación y generación de reportes de ingresos y egresos,
de forma que el usuario (gerente o jefe de la empresa) pueda confiar en los datos y
ahorrar tiempo en tareas repetitivas.

### 3.1 Objetivos específicos (in scope)

- Registrar movimientos de ingreso y egreso de capital.
- Consolidar datos provenientes de una o varias planillas de Excel.
- Generar automáticamente reportes diarios, semanales y mensuales.
- Evitar pérdida o corrupción de datos durante el procesamiento.
- Dejar un histórico auditable de movimientos.

### 3.2 Fuera de alcance (out of scope) — por ahora

- Integración con sistemas bancarios o de facturación electrónica.
- Múltiples usuarios concurrentes / permisos por rol.
- Interfaz web o aplicación móvil (v0 es un script/herramienta local).
- Predicciones o análisis financiero avanzado (forecasting).

## 4. Usuarios

- **Usuario principal:** Gerente o jefe de la PyME. Uso personal, no colaborativo
  (al menos en esta primera versión).
- **Nivel técnico esperado:** Bajo. El usuario no necesariamente sabe programar,
  por lo que la herramienta debe ser simple de ejecutar (idealmente un solo comando
  o un archivo ejecutable).

## 5. Requisitos funcionales

| ID | Requisito |
|----|-----------|
| RF-01 | El sistema debe poder leer datos de ingresos y egresos desde uno o más archivos Excel de entrada. |
| RF-02 | El sistema debe validar los datos leídos (tipos de dato, columnas obligatorias, fechas válidas) antes de procesarlos. |
| RF-03 | El sistema debe consolidar los movimientos en un registro único sin duplicar ni perder filas. |
| RF-04 | El sistema debe generar un reporte diario con el detalle de movimientos del día. |
| RF-05 | El sistema debe generar un reporte semanal con totales de ingresos, egresos y balance. |
| RF-06 | El sistema debe generar un reporte mensual con totales y comparación respecto al mes anterior. |
| RF-07 | El sistema debe guardar los reportes generados en archivos Excel nuevos, sin sobrescribir los datos originales. |
| RF-08 | El sistema debe registrar un log de cada ejecución (qué se procesó, cuándo, si hubo errores). |

## 6. Requisitos no funcionales

| ID | Requisito |
|----|-----------|
| RNF-01 | **Integridad de datos:** ninguna ejecución debe modificar o borrar el archivo de origen. |
| RNF-02 | **Simplicidad de uso:** ejecutar el proceso debe requerir un solo comando o acción. |
| RNF-03 | **Portabilidad:** debe poder ejecutarse en Windows (SO más común en PyMEs) sin instalaciones complejas. |
| RNF-04 | **Trazabilidad:** todo error debe quedar registrado en un log legible. |
| RNF-05 | **Rendimiento:** debe procesar archivos de hasta ~10.000 filas en menos de 30 segundos. |

## 7. Flujo general de datos

1. El usuario coloca/actualiza el archivo Excel con movimientos del período.
2. El script lee y valida los datos con pandas.
3. Se consolidan los movimientos en un dataset interno.
4. Se calculan totales (ingresos, egresos, balance) según el período (diario/semanal/mensual).
5. Se genera un archivo Excel de salida con el reporte correspondiente.
6. Se registra la ejecución en un log.

## 8. Criterios de aceptación

- [ ] Dado un archivo Excel con movimientos válidos, el sistema genera el reporte diario correcto.
- [ ] Dado un archivo con filas inválidas (fecha vacía, monto no numérico), el sistema las reporta como error y no detiene todo el proceso.
- [ ] El archivo original nunca se modifica.
- [ ] Los reportes semanales y mensuales reflejan sumas correctas de ingresos, egresos y balance.
- [ ] Cada ejecución queda registrada en el log con fecha, hora y resultado.

## 9. Riesgos y supuestos

- **Supuesto:** el usuario mantiene un formato mínimamente consistente en su Excel de origen (columnas de fecha, monto, tipo de movimiento).
- **Riesgo:** si el usuario cambia el formato del Excel de origen sin avisar, la validación debe detectarlo y avisar, no fallar en silencio.
- **Riesgo:** manejo de archivos Excel abiertos simultáneamente por el usuario (bloqueo de archivo).

## 10. Glosario

- **Ingreso:** entrada de capital a la empresa.
- **Egreso:** salida de capital de la empresa.
- **Balance:** diferencia entre ingresos y egresos en un período.
- **Consolidación:** proceso de unificar movimientos de distintas fuentes en un único registro.
