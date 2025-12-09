# App-Estadística-Inferencial-V1

Programa útil para resolver problemas sencillos en el ámbito de la estadística inferencial, con el manejo de poblaciones y proporciones utilizando Python.

## Descripción

Esta aplicación proporciona herramientas para realizar cálculos comunes en estadística inferencial, incluyendo:

- **Intervalos de Confianza para la Media**
  - Con varianza conocida (distribución normal)
  - Con varianza desconocida (distribución t de Student)

- **Intervalos de Confianza para Proporciones**
  - Estimación de intervalos de confianza para proporciones poblacionales

- **Cálculo de Tamaño de Muestra**
  - Determinación del tamaño de muestra necesario para estimar proporciones

- **Pruebas de Hipótesis para la Media**
  - Pruebas bilaterales, cola derecha y cola izquierda
  - Con varianza conocida o desconocida

- **Pruebas de Hipótesis para Proporciones**
  - Pruebas bilaterales, cola derecha y cola izquierda

## Requisitos

- Python 3.7 o superior
- SciPy
- NumPy

## Instalación

1. Clone el repositorio:
```bash
git clone https://github.com/Celest90/App-Estad-stica-Inferencial-V1.git
cd App-Estad-stica-Inferencial-V1
```

2. Instale las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecute la aplicación con:
```bash
python estadistica_inferencial.py
```

La aplicación presenta un menú interactivo que le guiará a través de las diferentes opciones.

## Ejemplos de Uso

### Ejemplo 1: Intervalo de Confianza para la Media (Varianza Conocida)

**Problema:** Una fábrica produce tornillos con una desviación estándar de 0.5 mm. Una muestra de 50 tornillos tiene una longitud media de 25.2 mm. Calcule un intervalo de confianza del 95%.

**Datos de entrada:**
- Media muestral: 25.2
- Tamaño de muestra: 50
- Desviación estándar poblacional: 0.5
- Nivel de confianza: 0.95

**Salida esperada:**
- Límite inferior: ≈ 25.06
- Límite superior: ≈ 25.34

### Ejemplo 2: Intervalo de Confianza para una Proporción

**Problema:** En una encuesta de 400 personas, 280 dijeron que prefieren el producto A. Calcule un intervalo de confianza del 95% para la proporción poblacional.

**Datos de entrada:**
- Número de éxitos: 280
- Tamaño de muestra: 400
- Nivel de confianza: 0.95

**Salida esperada:**
- Proporción muestral: 0.70
- Intervalo de confianza aproximado: (0.655, 0.745)

### Ejemplo 3: Tamaño de Muestra para Proporción

**Problema:** ¿Cuántas personas debemos encuestar para estimar una proporción con un margen de error del 3% y un nivel de confianza del 95%?

**Datos de entrada:**
- Proporción estimada: 0.5 (caso más conservador)
- Margen de error: 0.03
- Nivel de confianza: 0.95

**Salida esperada:**
- Tamaño de muestra: ≈ 1068

### Ejemplo 4: Prueba de Hipótesis para la Media

**Problema:** Un fabricante afirma que sus bombillas duran en promedio 1000 horas. Una muestra de 36 bombillas tiene una media de 980 horas con una desviación estándar de 80 horas. ¿Hay evidencia de que la duración real es menor a 1000 horas? (α = 0.05)

**Datos de entrada:**
- Media muestral: 980
- Media bajo H0: 1000
- Desviación estándar muestral: 80
- Tamaño de muestra: 36
- Tipo de prueba: Cola izquierda
- Nivel de significancia: 0.05

**Interpretación:**
Si el valor p < 0.05, rechazamos la hipótesis nula y concluimos que hay evidencia de que las bombillas duran menos de 1000 horas.

### Ejemplo 5: Prueba de Hipótesis para una Proporción

**Problema:** Una empresa afirma que el 30% de sus clientes son recurrentes. En una muestra de 200 clientes, 75 son recurrentes. ¿Hay evidencia de que la proporción real es diferente del 30%? (α = 0.05)

**Datos de entrada:**
- Número de éxitos: 75
- Tamaño de muestra: 200
- Proporción bajo H0: 0.30
- Tipo de prueba: Bilateral
- Nivel de significancia: 0.05

**Interpretación:**
Si el valor p < 0.05, rechazamos la hipótesis nula y concluimos que la proporción real difiere del 30%.

## Conceptos Estadísticos

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
