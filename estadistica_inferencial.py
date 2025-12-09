#!/usr/bin/env python3
"""
Aplicación de Estadística Inferencial
Programa útil para resolver problemas sencillos en el ámbito de la estadística inferencial,
con el manejo de poblaciones y proporciones.
"""

import math
from scipy import stats
import numpy as np


class EstadisticaInferencial:
    """Clase principal para cálculos de estadística inferencial"""
    
    @staticmethod
    def intervalo_confianza_media_varianza_conocida(media_muestral, desviacion_poblacional, 
                                                      n, nivel_confianza=0.95):
        """
        Calcula el intervalo de confianza para la media poblacional con varianza conocida.
        
        Args:
            media_muestral: Media de la muestra
            desviacion_poblacional: Desviación estándar poblacional (conocida)
            n: Tamaño de la muestra
            nivel_confianza: Nivel de confianza (por defecto 0.95)
            
        Returns:
            tuple: (límite_inferior, límite_superior, margen_error)
        """
        alpha = 1 - nivel_confianza
        z_critico = stats.norm.ppf(1 - alpha/2)
        error_estandar = desviacion_poblacional / math.sqrt(n)
        margen_error = z_critico * error_estandar
        
        limite_inferior = media_muestral - margen_error
        limite_superior = media_muestral + margen_error
        
        return limite_inferior, limite_superior, margen_error
    
    @staticmethod
    def intervalo_confianza_media_varianza_desconocida(media_muestral, desviacion_muestral,
                                                         n, nivel_confianza=0.95):
        """
        Calcula el intervalo de confianza para la media poblacional con varianza desconocida.
        Utiliza la distribución t de Student.
        
        Args:
            media_muestral: Media de la muestra
            desviacion_muestral: Desviación estándar de la muestra
            n: Tamaño de la muestra
            nivel_confianza: Nivel de confianza (por defecto 0.95)
            
        Returns:
            tuple: (límite_inferior, límite_superior, margen_error)
        """
        alpha = 1 - nivel_confianza
        grados_libertad = n - 1
        t_critico = stats.t.ppf(1 - alpha/2, grados_libertad)
        error_estandar = desviacion_muestral / math.sqrt(n)
        margen_error = t_critico * error_estandar
        
        limite_inferior = media_muestral - margen_error
        limite_superior = media_muestral + margen_error
        
        return limite_inferior, limite_superior, margen_error
    
    @staticmethod
    def intervalo_confianza_proporcion(p_muestral, n, nivel_confianza=0.95):
        """
        Calcula el intervalo de confianza para una proporción poblacional.
        
        Args:
            p_muestral: Proporción muestral (número de éxitos / tamaño de muestra)
            n: Tamaño de la muestra
            nivel_confianza: Nivel de confianza (por defecto 0.95)
            
        Returns:
            tuple: (límite_inferior, límite_superior, margen_error)
        """
        if p_muestral <= 0 or p_muestral >= 1:
            if p_muestral == 0:
                p_muestral = 0.5 / n
            elif p_muestral == 1:
                p_muestral = 1 - 0.5 / n
        
        alpha = 1 - nivel_confianza
        z_critico = stats.norm.ppf(1 - alpha/2)
        error_estandar = math.sqrt((p_muestral * (1 - p_muestral)) / n)
        margen_error = z_critico * error_estandar
        
        limite_inferior = max(0, p_muestral - margen_error)
        limite_superior = min(1, p_muestral + margen_error)
        
        return limite_inferior, limite_superior, margen_error
    
    @staticmethod
    def tamano_muestra_proporcion(p_estimada, margen_error, nivel_confianza=0.95):
        """
        Calcula el tamaño de muestra necesario para estimar una proporción.
        
        Args:
            p_estimada: Proporción estimada (usar 0.5 si no se conoce)
            margen_error: Margen de error deseado
            nivel_confianza: Nivel de confianza (por defecto 0.95)
            
        Returns:
            int: Tamaño de muestra necesario
        """
        alpha = 1 - nivel_confianza
        z_critico = stats.norm.ppf(1 - alpha/2)
        n = (z_critico**2 * p_estimada * (1 - p_estimada)) / (margen_error**2)
        
        return math.ceil(n)
    
    @staticmethod
    def prueba_hipotesis_media(media_muestral, media_hipotetica, desviacion, n, 
                                tipo_prueba='bilateral', varianza_conocida=True):
        """
        Realiza una prueba de hipótesis para la media poblacional.
        
        Args:
            media_muestral: Media de la muestra
            media_hipotetica: Media bajo la hipótesis nula
            desviacion: Desviación estándar (poblacional o muestral según varianza_conocida)
            n: Tamaño de la muestra
            tipo_prueba: 'bilateral', 'izquierda', 'derecha'
            varianza_conocida: True si se conoce la varianza poblacional
            
        Returns:
            tuple: (estadístico, valor_p, decisión)
        """
        error_estandar = desviacion / math.sqrt(n)
        
        if varianza_conocida:
            # Usar distribución normal
            estadistico = (media_muestral - media_hipotetica) / error_estandar
            
            if tipo_prueba == 'bilateral':
                valor_p = 2 * (1 - stats.norm.cdf(abs(estadistico)))
            elif tipo_prueba == 'derecha':
                valor_p = 1 - stats.norm.cdf(estadistico)
            else:  # izquierda
                valor_p = stats.norm.cdf(estadistico)
        else:
            # Usar distribución t
            grados_libertad = n - 1
            estadistico = (media_muestral - media_hipotetica) / error_estandar
            
            if tipo_prueba == 'bilateral':
                valor_p = 2 * (1 - stats.t.cdf(abs(estadistico), grados_libertad))
            elif tipo_prueba == 'derecha':
                valor_p = 1 - stats.t.cdf(estadistico, grados_libertad)
            else:  # izquierda
                valor_p = stats.t.cdf(estadistico, grados_libertad)
        
        return estadistico, valor_p
    
    @staticmethod
    def prueba_hipotesis_proporcion(p_muestral, p_hipotetica, n, tipo_prueba='bilateral'):
        """
        Realiza una prueba de hipótesis para una proporción poblacional.
        
        Args:
            p_muestral: Proporción muestral
            p_hipotetica: Proporción bajo la hipótesis nula
            n: Tamaño de la muestra
            tipo_prueba: 'bilateral', 'izquierda', 'derecha'
            
        Returns:
            tuple: (estadístico, valor_p)
        """
        error_estandar = math.sqrt((p_hipotetica * (1 - p_hipotetica)) / n)
        estadistico = (p_muestral - p_hipotetica) / error_estandar
        
        if tipo_prueba == 'bilateral':
            valor_p = 2 * (1 - stats.norm.cdf(abs(estadistico)))
        elif tipo_prueba == 'derecha':
            valor_p = 1 - stats.norm.cdf(estadistico)
        else:  # izquierda
            valor_p = stats.norm.cdf(estadistico)
        
        return estadistico, valor_p


def mostrar_menu_principal():
    """Muestra el menú principal de la aplicación"""
    print("\n" + "="*60)
    print("  APLICACIÓN DE ESTADÍSTICA INFERENCIAL")
    print("="*60)
    print("\n1. Intervalo de Confianza para la Media")
    print("2. Intervalo de Confianza para una Proporción")
    print("3. Cálculo de Tamaño de Muestra para Proporción")
    print("4. Prueba de Hipótesis para la Media")
    print("5. Prueba de Hipótesis para una Proporción")
    print("0. Salir")
    print("="*60)


def intervalo_confianza_media_menu():
    """Menú para calcular intervalos de confianza para la media"""
    print("\n--- INTERVALO DE CONFIANZA PARA LA MEDIA ---")
    print("¿Conoce la varianza poblacional?")
    print("1. Sí (usar distribución normal)")
    print("2. No (usar distribución t de Student)")
    
    opcion = input("\nSeleccione una opción: ")
    
    try:
        media_muestral = float(input("Ingrese la media muestral: "))
        n = int(input("Ingrese el tamaño de la muestra: "))
        nivel_confianza = float(input("Ingrese el nivel de confianza (ejemplo: 0.95): "))
        
        if opcion == '1':
            desviacion_poblacional = float(input("Ingrese la desviación estándar poblacional: "))
            li, ls, me = EstadisticaInferencial.intervalo_confianza_media_varianza_conocida(
                media_muestral, desviacion_poblacional, n, nivel_confianza
            )
            print("\n--- RESULTADOS ---")
            print(f"Intervalo de confianza al {nivel_confianza*100}%:")
            print(f"  Límite inferior: {li:.4f}")
            print(f"  Límite superior: {ls:.4f}")
            print(f"  Margen de error: {me:.4f}")
        elif opcion == '2':
            desviacion_muestral = float(input("Ingrese la desviación estándar muestral: "))
            li, ls, me = EstadisticaInferencial.intervalo_confianza_media_varianza_desconocida(
                media_muestral, desviacion_muestral, n, nivel_confianza
            )
            print("\n--- RESULTADOS ---")
            print(f"Intervalo de confianza al {nivel_confianza*100}%:")
            print(f"  Límite inferior: {li:.4f}")
            print(f"  Límite superior: {ls:.4f}")
            print(f"  Margen de error: {me:.4f}")
        else:
            print("Opción no válida.")
    except ValueError as e:
        print(f"Error en la entrada de datos: {e}")
    except Exception as e:
        print(f"Error: {e}")


def intervalo_confianza_proporcion_menu():
    """Menú para calcular intervalos de confianza para proporciones"""
    print("\n--- INTERVALO DE CONFIANZA PARA UNA PROPORCIÓN ---")
    
    try:
        exitos = int(input("Ingrese el número de éxitos: "))
        n = int(input("Ingrese el tamaño de la muestra: "))
        nivel_confianza = float(input("Ingrese el nivel de confianza (ejemplo: 0.95): "))
        
        p_muestral = exitos / n
        li, ls, me = EstadisticaInferencial.intervalo_confianza_proporcion(
            p_muestral, n, nivel_confianza
        )
        
        print("\n--- RESULTADOS ---")
        print(f"Proporción muestral: {p_muestral:.4f}")
        print(f"Intervalo de confianza al {nivel_confianza*100}%:")
        print(f"  Límite inferior: {li:.4f}")
        print(f"  Límite superior: {ls:.4f}")
        print(f"  Margen de error: {me:.4f}")
    except ValueError as e:
        print(f"Error en la entrada de datos: {e}")
    except Exception as e:
        print(f"Error: {e}")


def tamano_muestra_menu():
    """Menú para calcular el tamaño de muestra necesario"""
    print("\n--- CÁLCULO DE TAMAÑO DE MUESTRA PARA PROPORCIÓN ---")
    
    try:
        print("Si no tiene una estimación de la proporción, use 0.5 (caso más conservador)")
        p_estimada = float(input("Ingrese la proporción estimada: "))
        margen_error = float(input("Ingrese el margen de error deseado: "))
        nivel_confianza = float(input("Ingrese el nivel de confianza (ejemplo: 0.95): "))
        
        n = EstadisticaInferencial.tamano_muestra_proporcion(
            p_estimada, margen_error, nivel_confianza
        )
        
        print("\n--- RESULTADOS ---")
        print(f"Tamaño de muestra necesario: {n}")
    except ValueError as e:
        print(f"Error en la entrada de datos: {e}")
    except Exception as e:
        print(f"Error: {e}")


def prueba_hipotesis_media_menu():
    """Menú para realizar pruebas de hipótesis para la media"""
    print("\n--- PRUEBA DE HIPÓTESIS PARA LA MEDIA ---")
    
    try:
        media_muestral = float(input("Ingrese la media muestral: "))
        media_hipotetica = float(input("Ingrese la media bajo H0 (hipótesis nula): "))
        n = int(input("Ingrese el tamaño de la muestra: "))
        
        print("\n¿Conoce la varianza poblacional?")
        print("1. Sí")
        print("2. No")
        opcion_var = input("Seleccione una opción: ")
        
        varianza_conocida = opcion_var == '1'
        if varianza_conocida:
            desviacion = float(input("Ingrese la desviación estándar poblacional: "))
        else:
            desviacion = float(input("Ingrese la desviación estándar muestral: "))
        
        print("\nTipo de prueba:")
        print("1. Bilateral (H1: μ ≠ μ0)")
        print("2. Cola derecha (H1: μ > μ0)")
        print("3. Cola izquierda (H1: μ < μ0)")
        opcion_tipo = input("Seleccione una opción: ")
        
        tipo_prueba = 'bilateral'
        if opcion_tipo == '2':
            tipo_prueba = 'derecha'
        elif opcion_tipo == '3':
            tipo_prueba = 'izquierda'
        
        alpha = float(input("Ingrese el nivel de significancia (ejemplo: 0.05): "))
        
        estadistico, valor_p = EstadisticaInferencial.prueba_hipotesis_media(
            media_muestral, media_hipotetica, desviacion, n, tipo_prueba, varianza_conocida
        )
        
        print("\n--- RESULTADOS ---")
        if varianza_conocida:
            print(f"Estadístico Z: {estadistico:.4f}")
        else:
            print(f"Estadístico t: {estadistico:.4f}")
        print(f"Valor p: {valor_p:.4f}")
        print(f"Nivel de significancia: {alpha}")
        
        if valor_p < alpha:
            print("\nDecisión: Rechazar H0")
            print("Hay evidencia estadística significativa para rechazar la hipótesis nula.")
        else:
            print("\nDecisión: No rechazar H0")
            print("No hay evidencia estadística suficiente para rechazar la hipótesis nula.")
    except ValueError as e:
        print(f"Error en la entrada de datos: {e}")
    except Exception as e:
        print(f"Error: {e}")


def prueba_hipotesis_proporcion_menu():
    """Menú para realizar pruebas de hipótesis para proporciones"""
    print("\n--- PRUEBA DE HIPÓTESIS PARA UNA PROPORCIÓN ---")
    
    try:
        exitos = int(input("Ingrese el número de éxitos: "))
        n = int(input("Ingrese el tamaño de la muestra: "))
        p_hipotetica = float(input("Ingrese la proporción bajo H0 (hipótesis nula): "))
        
        print("\nTipo de prueba:")
        print("1. Bilateral (H1: p ≠ p0)")
        print("2. Cola derecha (H1: p > p0)")
        print("3. Cola izquierda (H1: p < p0)")
        opcion_tipo = input("Seleccione una opción: ")
        
        tipo_prueba = 'bilateral'
        if opcion_tipo == '2':
            tipo_prueba = 'derecha'
        elif opcion_tipo == '3':
            tipo_prueba = 'izquierda'
        
        alpha = float(input("Ingrese el nivel de significancia (ejemplo: 0.05): "))
        
        p_muestral = exitos / n
        estadistico, valor_p = EstadisticaInferencial.prueba_hipotesis_proporcion(
            p_muestral, p_hipotetica, n, tipo_prueba
        )
        
        print("\n--- RESULTADOS ---")
        print(f"Proporción muestral: {p_muestral:.4f}")
        print(f"Estadístico Z: {estadistico:.4f}")
        print(f"Valor p: {valor_p:.4f}")
        print(f"Nivel de significancia: {alpha}")
        
        if valor_p < alpha:
            print("\nDecisión: Rechazar H0")
            print("Hay evidencia estadística significativa para rechazar la hipótesis nula.")
        else:
            print("\nDecisión: No rechazar H0")
            print("No hay evidencia estadística suficiente para rechazar la hipótesis nula.")
    except ValueError as e:
        print(f"Error en la entrada de datos: {e}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Función principal de la aplicación"""
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            intervalo_confianza_media_menu()
        elif opcion == '2':
            intervalo_confianza_proporcion_menu()
        elif opcion == '3':
            tamano_muestra_menu()
        elif opcion == '4':
            prueba_hipotesis_media_menu()
        elif opcion == '5':
            prueba_hipotesis_proporcion_menu()
        elif opcion == '0':
            print("\n¡Gracias por usar la aplicación de Estadística Inferencial!")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
