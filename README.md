# App-Estadística-Inferencial-Versión 1.0

## Descripción

Está aplicación web fue creada con el propósito de ayudar en la resolución de problemas relacionados con la estadística inferencial.
La aplicación presenta un menú interactivo que le guiará a través de las diferentes opciones, siendo las siguientes:

- **Valores De Tendencia Central Y Dispersión**
  - Con valores muéstrales
  - Con valores poblacionales
  - Con carga desde archivos .CSV o .XLSX

- **Valor Z**
  - Calcular valor Z desde datos
  - Calcular valor Z desde probabilidad con el valor p

- **Cálculo de Tamaño de Muestra**
  - Determinar el tamaño de muestra para poblaciones finitas
  - Determinar el tamaño de muestra para poblaciones infinitas

- **Intervalo de Confianza Para Una Población**
  - Calculo del intervalo de confianza para la media de una población
  - Calculo del intervalo de confianza para la proporción de una población

- **Comparación entre Dos Poblaciones**
  - Comparación entre dos medias poblacionales
  - Comparación entre dos proporciones poblacionales

- **Error Estándar**
  - Calcular el error estándar de la media
  - Calcular el error estándar de la proporción

- **Cálculo t**
  - Cálculo para encontrar el valor T student

- **Prueba de Hipótesis**
  - Analisis de pruebas de hipótesis para diferentes escenarios estadísticos
  - Tipos de pruebas = Bilateral, Cola derecha, Cola izquierda
  - Pruebas para la media
  - Pruebas para la proporción
  - Pruebas para dos medias

## Requisitos

- Python 3.7 o superior
- SciPy
- NumPy
- Pandas
- OpenPyXL
- Streamlit 1.52

## Instalación

1. Clone el repositorio:

```bash
git clone https://github.com/Celest90/App-Estad-stica-Inferencial-V1.git
cd App-Estad-stica-Inferencial-V1
```

1. Instale las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecute la aplicación con:

```bash

python estadistica_inferencial.py
```

## Conceptos Estadísticos

### Medidas de Tendencia Central

Valores que describen el centro de un conjunto de datos:

- **Media (x̄ / μ):** El promedio aritmético.
- **Mediana:** El valor central cuando los datos están ordenados.
- **Moda:** El valor que aparece con mayor frecuencia.

### Medidas de Dispersión

Valores que describen qué tan separados están los datos:

- **Varianza (s² / σ²):** Promedio de las desviaciones al cuadrado respecto a la media.
- **Desviación Estándar (s / σ):** La raíz cuadrada de la varianza; indica la dispersión en las mismas unidades que los datos.

### Valor Z (Puntaje Z)

Medida que indica a cuántas desviaciones estándar se encuentra un valor específico de la media de su grupo. Útil para comparar datos de diferentes distribuciones normales.

### Distribución t de Student

Distribución de probabilidad utilizada para estimar medias poblacionales cuando el tamaño de la muestra es pequeño o se desconoce la desviación estándar poblacional.

### Error Estándar

Estimación de la desviación estándar de una estadística muestral (como la media). Mide la precisión con la que la muestra representa a la población.

### Nivel de Confianza

Probabilidad de que el intervalo de confianza contenga el verdadero parámetro poblacional. Niveles comunes: 90% (0.90), 95% (0.95), 99% (0.99).

### Margen de Error

Rango de valores por encima y por debajo de la estadística muestral en un intervalo de confianza.

### Hipótesis Nula (H0)

Afirmación sobre un parámetro poblacional que se asume verdadera hasta que la evidencia sugiera lo contrario.

### Valor p

Probabilidad de obtener resultados al menos tan extremos como los observados, asumiendo que la hipótesis nula es verdadera.

### Nivel de Significancia (α)

Probabilidad de rechazar la hipótesis nula cuando es verdadera (error tipo I). Común: α = 0.05.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de crear un pull request.

## Licencia

Este proyecto está disponible bajo la licencia MIT.

## Autor

Celest90
