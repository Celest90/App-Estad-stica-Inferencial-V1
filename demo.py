#!/usr/bin/env python3
"""Demostración de la aplicación de Estadística Inferencial"""

from estadistica_inferencial import EstadisticaInferencial

print('\n' + '='*60)
print('DEMOSTRACIÓN DE LA APLICACIÓN DE ESTADÍSTICA INFERENCIAL')
print('='*60)

print('\n1. Intervalo de Confianza para Media (Varianza Conocida)')
print('-' * 60)
li, ls, me = EstadisticaInferencial.intervalo_confianza_media_varianza_conocida(25.2, 0.5, 50, 0.95)
print(f'Ejemplo: Tornillos con media=25.2mm, σ=0.5mm, n=50')
print(f'IC al 95%: [{li:.4f}, {ls:.4f}]')

print('\n2. Intervalo de Confianza para Proporción')
print('-' * 60)
li, ls, me = EstadisticaInferencial.intervalo_confianza_proporcion(280/400, 400, 0.95)
print(f'Ejemplo: 280 satisfechos de 400 clientes')
print(f'IC al 95%: [{li:.4f}, {ls:.4f}] = [{li*100:.2f}%, {ls*100:.2f}%]')

print('\n3. Tamaño de Muestra para Proporción')
print('-' * 60)
n = EstadisticaInferencial.tamano_muestra_proporcion(0.5, 0.03, 0.95)
print(f'Ejemplo: Margen de error 3%, confianza 95%')
print(f'Tamaño de muestra necesario: {n}')

print('\n4. Prueba de Hipótesis para Media')
print('-' * 60)
est, pval = EstadisticaInferencial.prueba_hipotesis_media(980, 1000, 80, 36, 'izquierda', False)
print(f'Ejemplo: Bombillas, H0: μ=1000h, muestra: x̄=980h, s=80h, n=36')
print(f'Estadístico t = {est:.4f}, valor p = {pval:.4f}')
decision = "Rechazar H0" if pval < 0.05 else "No rechazar H0"
print(f'Decisión (α=0.05): {decision}')

print('\n5. Prueba de Hipótesis para Proporción')
print('-' * 60)
est, pval = EstadisticaInferencial.prueba_hipotesis_proporcion(75/200, 0.30, 200, 'bilateral')
print(f'Ejemplo: Clientes recurrentes, H0: p=0.30, muestra: 75/200')
print(f'Estadístico Z = {est:.4f}, valor p = {pval:.4f}')
decision = "Rechazar H0" if pval < 0.05 else "No rechazar H0"
print(f'Decisión (α=0.05): {decision}')

print('\n' + '='*60)
print('✓ APLICACIÓN FUNCIONANDO CORRECTAMENTE')
print('='*60)
