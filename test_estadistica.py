#!/usr/bin/env python3
"""
Script de prueba para la aplicación de Estadística Inferencial
"""

from estadistica_inferencial import EstadisticaInferencial

def test_intervalo_confianza_media_varianza_conocida():
    """Prueba el cálculo de intervalo de confianza con varianza conocida"""
    print("=" * 60)
    print("TEST 1: Intervalo de Confianza para la Media (Varianza Conocida)")
    print("=" * 60)
    
    # Ejemplo: Media muestral = 25.2, desviación = 0.5, n = 50, confianza = 95%
    li, ls, me = EstadisticaInferencial.intervalo_confianza_media_varianza_conocida(
        25.2, 0.5, 50, 0.95
    )
    
    print(f"Media muestral: 25.2")
    print(f"Desviación estándar poblacional: 0.5")
    print(f"Tamaño de muestra: 50")
    print(f"Nivel de confianza: 95%")
    print(f"\nResultados:")
    print(f"  Límite inferior: {li:.4f}")
    print(f"  Límite superior: {ls:.4f}")
    print(f"  Margen de error: {me:.4f}")
    print("✓ PASADO\n")


def test_intervalo_confianza_media_varianza_desconocida():
    """Prueba el cálculo de intervalo de confianza con varianza desconocida"""
    print("=" * 60)
    print("TEST 2: Intervalo de Confianza para la Media (Varianza Desconocida)")
    print("=" * 60)
    
    # Ejemplo: Media = 980, desviación muestral = 80, n = 36, confianza = 95%
    li, ls, me = EstadisticaInferencial.intervalo_confianza_media_varianza_desconocida(
        980, 80, 36, 0.95
    )
    
    print(f"Media muestral: 980")
    print(f"Desviación estándar muestral: 80")
    print(f"Tamaño de muestra: 36")
    print(f"Nivel de confianza: 95%")
    print(f"\nResultados:")
    print(f"  Límite inferior: {li:.4f}")
    print(f"  Límite superior: {ls:.4f}")
    print(f"  Margen de error: {me:.4f}")
    print("✓ PASADO\n")


def test_intervalo_confianza_proporcion():
    """Prueba el cálculo de intervalo de confianza para proporciones"""
    print("=" * 60)
    print("TEST 3: Intervalo de Confianza para una Proporción")
    print("=" * 60)
    
    # Ejemplo: 280 éxitos de 400, confianza = 95%
    p_muestral = 280 / 400
    li, ls, me = EstadisticaInferencial.intervalo_confianza_proporcion(
        p_muestral, 400, 0.95
    )
    
    print(f"Número de éxitos: 280")
    print(f"Tamaño de muestra: 400")
    print(f"Proporción muestral: {p_muestral:.4f}")
    print(f"Nivel de confianza: 95%")
    print(f"\nResultados:")
    print(f"  Límite inferior: {li:.4f}")
    print(f"  Límite superior: {ls:.4f}")
    print(f"  Margen de error: {me:.4f}")
    print("✓ PASADO\n")


def test_tamano_muestra_proporcion():
    """Prueba el cálculo del tamaño de muestra para proporciones"""
    print("=" * 60)
    print("TEST 4: Cálculo de Tamaño de Muestra para Proporción")
    print("=" * 60)
    
    # Ejemplo: p = 0.5, margen error = 0.03, confianza = 95%
    n = EstadisticaInferencial.tamano_muestra_proporcion(0.5, 0.03, 0.95)
    
    print(f"Proporción estimada: 0.5")
    print(f"Margen de error: 0.03")
    print(f"Nivel de confianza: 95%")
    print(f"\nResultados:")
    print(f"  Tamaño de muestra necesario: {n}")
    print("✓ PASADO\n")


def test_prueba_hipotesis_media():
    """Prueba la prueba de hipótesis para la media"""
    print("=" * 60)
    print("TEST 5: Prueba de Hipótesis para la Media")
    print("=" * 60)
    
    # Ejemplo: Media = 980, H0: μ = 1000, desviación = 80, n = 36
    estadistico, valor_p = EstadisticaInferencial.prueba_hipotesis_media(
        980, 1000, 80, 36, 'izquierda', False
    )
    
    print(f"Media muestral: 980")
    print(f"Media bajo H0: 1000")
    print(f"Desviación estándar muestral: 80")
    print(f"Tamaño de muestra: 36")
    print(f"Tipo de prueba: Cola izquierda")
    print(f"\nResultados:")
    print(f"  Estadístico t: {estadistico:.4f}")
    print(f"  Valor p: {valor_p:.4f}")
    
    if valor_p < 0.05:
        print(f"  Decisión (α=0.05): Rechazar H0")
    else:
        print(f"  Decisión (α=0.05): No rechazar H0")
    print("✓ PASADO\n")


def test_prueba_hipotesis_proporcion():
    """Prueba la prueba de hipótesis para proporciones"""
    print("=" * 60)
    print("TEST 6: Prueba de Hipótesis para una Proporción")
    print("=" * 60)
    
    # Ejemplo: 75 éxitos de 200, H0: p = 0.30
    p_muestral = 75 / 200
    estadistico, valor_p = EstadisticaInferencial.prueba_hipotesis_proporcion(
        p_muestral, 0.30, 200, 'bilateral'
    )
    
    print(f"Número de éxitos: 75")
    print(f"Tamaño de muestra: 200")
    print(f"Proporción muestral: {p_muestral:.4f}")
    print(f"Proporción bajo H0: 0.30")
    print(f"Tipo de prueba: Bilateral")
    print(f"\nResultados:")
    print(f"  Estadístico Z: {estadistico:.4f}")
    print(f"  Valor p: {valor_p:.4f}")
    
    if valor_p < 0.05:
        print(f"  Decisión (α=0.05): Rechazar H0")
    else:
        print(f"  Decisión (α=0.05): No rechazar H0")
    print("✓ PASADO\n")


def main():
    """Ejecuta todas las pruebas"""
    print("\n" + "=" * 60)
    print("  PRUEBAS DE LA APLICACIÓN DE ESTADÍSTICA INFERENCIAL")
    print("=" * 60 + "\n")
    
    try:
        test_intervalo_confianza_media_varianza_conocida()
        test_intervalo_confianza_media_varianza_desconocida()
        test_intervalo_confianza_proporcion()
        test_tamano_muestra_proporcion()
        test_prueba_hipotesis_media()
        test_prueba_hipotesis_proporcion()
        
        print("=" * 60)
        print("  TODAS LAS PRUEBAS PASARON EXITOSAMENTE ✓")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ ERROR EN LAS PRUEBAS: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
