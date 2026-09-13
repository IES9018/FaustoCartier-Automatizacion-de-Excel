# ADR-002: Estilo arquitectónico de la automatización de Excel

**Estado:** Aceptada
**Fecha:** 2026-09-13
**Decisores:** Fausto Cartier

## Contexto

El SPEC define una herramienta local para generar reportes (diarios, semanales y
mensuales) de ingresos y egresos de capital para PyMEs, a partir de archivos Excel.

El usuario final es el gerente o dueño de la empresa, con bajo nivel técnico. El
proyecto está en fase de definición y diseño (versión 0.1), por lo que antes de
implementar era necesario fijar el estilo arquitectónico general del sistema: dónde
corre el software, cómo se distribuye, y cuáles son sus límites y componentes.

ADR-0001 ya resolvió la elección del stack (Python + pandas). Esta ADR define la
arquitectura de alto nivel y su representación visual.

## Opciones consideradas

### 1. App de escritorio local (script empaquetado)
- Todo corre en la máquina del usuario, sin servidor ni conexión a internet.
- Lee y escribe directamente sobre un archivo Excel local del cliente.
- No requiere base de datos ni infraestructura adicional.
- Se distribuye como un ejecutable (`.exe`) de Windows, sin exigir Python instalado.

### 2. Aplicación web
- Se accede desde un navegador; los datos se procesan en un servidor.
- Requiere hosting, mantenimiento del servidor y conexión a internet.
- Sobresimplifica el despliegue local, pero agrega infraestructura y costos de
  administración que el proyecto no necesita en esta etapa.

### 3. Cliente-servidor multiusuario
- Un backend central procesa los reportes y una base de datos guarda los datos.
- Admite varios usuarios concurrentes y reportes en la nube.
- Mucho más complejo de construir y mantener; hoy hay un solo usuario, que trabaja
  sobre su propio archivo local.

## Decisión

Se adopta el estilo de **aplicación de escritorio local de un solo usuario**: sin
servidor, sin base de datos, sin conexión a internet, ejecutada como script o
ejecutable en la máquina del cliente y operando directamente sobre su archivo Excel.

La arquitectura queda documentada con el modelo **C4** en
`docs/architecture/c4-diagram.md`:

- **Nivel 1 (Contexto):** el gerente usa la herramienta; la herramienta lee y
  escribe el archivo Excel local del cliente.
- **Nivel 2 (Contenedores):**
  - *Interfaz de escritorio* (Python, Tkinter o PySimpleGUI): pantallas simples para
    cargar el archivo, ver resultados y exportar.
  - *Motor de procesamiento* (Python + pandas): limpia datos, hace cálculos y genera
    reportes.
  - *Archivo Excel* como fuente de datos y destino de los reportes.

Esta decisión complementa ADR-0001, que fija el stack tecnológico.

## Consecuencias

**Positivas:**
- Simplicidad total de puesta en marcha: sin servidores, sin base de datos, sin
  conexión externa.
- Mantiene intacta la privacidad de los datos, que nunca salen de la máquina del
  cliente.
- Facilita el cumplimiento de RNF-01 (no modificar el archivo de origen), ya que el
  alcance se limita a un archivo local conocido.
- El modelo C4 (niveles 1 y 2) da una visión clara de límites y componentes antes de
  implementar.

**Negativas / trade-offs:**
- El usuario final no tiene Python instalado por defecto, por lo que la distribución
  requerirá empaquetar la herramienta como ejecutable (ej: PyInstaller) o acompañar
  con instrucciones claras de instalación.
- Los datos solo existen en la máquina del cliente: no hay backups automáticos ni
  acceso remoto.
- Si el proyecto creciera a reportes en la nube, múltiples usuarios o una base de
  datos central, este estilo quedaría limitado y se abriría un nuevo contenedor
  (API/backend) — momento en el que esta ADR debería revisarse.

## Notas

- El diagrama C4 con los niveles 1 y 2 está en `docs/architecture/c4-diagram.md`.
- La elección de Python y pandas está documentada en `docs/adr/0001-eleccion-python-pandas.md`.
- Esta decisión podría revisarse en una futura ADR si el proyecto incorporara
  integraciones bancarias, usuarios concurrentes o una interfaz web (actualmente
  fuera de alcance según el SPEC).