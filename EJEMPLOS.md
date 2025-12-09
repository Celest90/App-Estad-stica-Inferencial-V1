# Ejemplos de Uso - Estadística Inferencial

Este documento proporciona ejemplos prácticos de cómo usar la aplicación de estadística inferencial.

## Ejemplo 1: Control de Calidad en Manufactura

**Situación:** Una fábrica produce tornillos que deben tener una longitud de 25 mm. La desviación estándar histórica es de 0.5 mm. Se toma una muestra de 50 tornillos con una longitud media de 25.2 mm.

**Pregunta:** ¿Cuál es el intervalo de confianza del 95% para la longitud media de todos los tornillos?

**Solución usando la aplicación:**
1. Seleccione opción 1: "Intervalo de Confianza para la Media"
2. Seleccione opción 1: "Sí (usar distribución normal)" - porque conocemos la varianza poblacional
3. Ingrese los datos:
   - Media muestral: 25.2
   - Tamaño de muestra: 50
   - Nivel de confianza: 0.95
   - Desviación estándar poblacional: 0.5

**Resultado:**
- Intervalo de confianza: (25.06, 25.34)
- Interpretación: Con 95% de confianza, la longitud media real de los tornillos está entre 25.06 y 25.34 mm.

---

## Ejemplo 2: Encuesta de Satisfacción

**Situación:** Una empresa realiza una encuesta de satisfacción. De 400 clientes encuestados, 280 expresaron satisfacción con el servicio.

**Pregunta:** ¿Cuál es el intervalo de confianza del 95% para la proporción de clientes satisfechos?

**Solución usando la aplicación:**
1. Seleccione opción 2: "Intervalo de Confianza para una Proporción"
2. Ingrese los datos:
   - Número de éxitos: 280
   - Tamaño de muestra: 400
   - Nivel de confianza: 0.95

**Resultado:**
- Proporción muestral: 0.70 (70%)
- Intervalo de confianza: (0.655, 0.745)
- Interpretación: Con 95% de confianza, entre el 65.5% y el 74.5% de todos los clientes están satisfechos.

---

## Ejemplo 3: Planificación de Encuesta

**Situación:** Una organización quiere estimar la proporción de votantes a favor de una propuesta con un margen de error del 3% y un nivel de confianza del 95%.

**Pregunta:** ¿Cuántas personas deben encuestar?

**Solución usando la aplicación:**
1. Seleccione opción 3: "Cálculo de Tamaño de Muestra para Proporción"
2. Ingrese los datos:
   - Proporción estimada: 0.5 (caso más conservador, sin información previa)
   - Margen de error: 0.03
   - Nivel de confianza: 0.95

**Resultado:**
- Tamaño de muestra necesario: 1068
- Interpretación: Se necesita encuestar al menos 1068 personas para lograr el margen de error deseado.

---

## Ejemplo 4: Prueba de Calidad de Bombillas

**Situación:** Un fabricante afirma que sus bombillas duran en promedio 1000 horas. Un inspector toma una muestra de 36 bombillas y encuentra una duración media de 980 horas con una desviación estándar de 80 horas.

**Pregunta:** ¿Hay evidencia suficiente para afirmar que las bombillas duran menos de 1000 horas? (usar α = 0.05)

**Solución usando la aplicación:**
1. Seleccione opción 4: "Prueba de Hipótesis para la Media"
2. Ingrese los datos:
   - Media muestral: 980
   - Media bajo H0: 1000
   - Tamaño de muestra: 36
   - ¿Conoce la varianza poblacional? No
   - Desviación estándar muestral: 80
   - Tipo de prueba: Cola izquierda (opción 3)
   - Nivel de significancia: 0.05

**Resultado:**
- Estadístico t: -1.5
- Valor p: 0.0713
- Decisión: No rechazar H0
- Interpretación: No hay evidencia estadística suficiente para afirmar que las bombillas duran menos de 1000 horas.

---

## Ejemplo 5: Proporción de Clientes Recurrentes

**Situación:** Una empresa afirma que el 30% de sus clientes son recurrentes. En una auditoría, se analizan 200 clientes y se encuentra que 75 son recurrentes.

**Pregunta:** ¿Hay evidencia de que la proporción real difiere del 30%? (usar α = 0.05)

**Solución usando la aplicación:**
1. Seleccione opción 5: "Prueba de Hipótesis para una Proporción"
2. Ingrese los datos:
   - Número de éxitos: 75
   - Tamaño de muestra: 200
   - Proporción bajo H0: 0.30
   - Tipo de prueba: Bilateral (opción 1)
   - Nivel de significancia: 0.05

**Resultado:**
- Proporción muestral: 0.375 (37.5%)
- Estadístico Z: 2.31
- Valor p: 0.0206
- Decisión: Rechazar H0
- Interpretación: Hay evidencia estadística significativa de que la proporción real de clientes recurrentes difiere del 30%.

---

## Consejos para Usar la Aplicación

1. **Nivel de Confianza:** Los valores más comunes son 0.90 (90%), 0.95 (95%), y 0.99 (99%).

2. **Tamaño de Muestra:** Un tamaño de muestra mayor generalmente produce intervalos de confianza más estrechos y pruebas más potentes.

3. **Proporción Desconocida:** Si no tiene información previa sobre una proporción, use 0.5 como estimación conservadora para calcular el tamaño de muestra.

4. **Tipo de Prueba de Hipótesis:**
   - Bilateral: cuando busca diferencia en cualquier dirección
   - Cola derecha: cuando busca evidencia de que el parámetro es mayor
   - Cola izquierda: cuando busca evidencia de que el parámetro es menor

5. **Interpretación del Valor p:**
   - Si valor p < α: Rechazar H0
   - Si valor p ≥ α: No rechazar H0

6. **Varianza Conocida vs Desconocida:**
   - Use varianza conocida solo si tiene datos históricos confiables
   - En la mayoría de casos prácticos, use varianza desconocida (distribución t)
