import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats

st.set_page_config(layout="wide")
st.title(":green[Valores de Tendencia Central y Dispersión]",
         text_alignment ="center",
         )


def mostrar_metrica(data, tipo):
    """
    Calcula y muestra las métricas estadísticas.
    Toda la lógica de cálculo y visualización se mueve aquí.
    """
    if not data:
        st.warning("No hay datos para calcular.")
        return

    # Convertir a numpy array para asegurar consistencia
    data_array = np.array(data)

    n = len(data_array)
    media = np.mean(data_array)
    mediana = np.median(data_array)

    # Uso corregido de scipy.stats.mode
    mode_result = stats.mode(data_array)
    # Asegurar que el resultado de la moda sea siempre un array
    moda_array = np.atleast_1d(mode_result.mode)
    moda = moda_array[0] if moda_array.size > 0 else "N/A"

    # ddof=1 para muestra, ddof=0 para población
    ddof_val = 1 if tipo == "MUESTRAL" else 0
    varianza = np.var(data_array, ddof=ddof_val)
    desviacion_estandar = np.std(data_array, ddof=ddof_val)

    st.divider()
    st.subheader(f"Resultados para el cálculo {tipo}")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        label_n = f"Número De Datos ({'n' if tipo == 'MUESTRAL' else 'N'})"
        st.metric(label=label_n, value=f"{n}")

    with c2:
        st.metric(label="Mediana", value=f"{mediana:.4f}")

    with c3:
        # Maneja el caso donde la moda no es numérica
        moda_display = f"{moda:.4f}" if isinstance(moda, (int, float)) else moda
        st.metric(label="Moda", value=moda_display)

    with c4:
        label_media = "Media Muestral (x̄)" if tipo == "MUESTRAL" else "Media Poblacional (μ)"
        st.metric(label=label_media, value=f"{media:.4f}")

    st.divider()

    c5, c6 = st.columns(2)

    with c5:
        label_var = "Varianza Muestral (s²)" if tipo == "MUESTRAL" else "Varianza Poblacional (σ²)"
        st.metric(label=label_var, value=f"{varianza:.4f}")

    with c6:
        label_dev = "Desviación Estándar Muestral (s)" if tipo == "MUESTRAL" else "Desviación Estándar Poblacional (σ)"
        st.metric(label=label_dev, value=f"{desviacion_estandar:.4f}")


tab1, tab2, tab3 = st.tabs(["MUESTRAL", "POBLACIONAL", "ARCHIVOS"])

with tab1:
    st.header("Estadísticos Muestrales")
    st.text('Calcula las medidas estadísticas de una muestra de datos.')
    st.info("Ingresa los datos para calcular las Medidas Muestrales. Por favor, Separe los números con comas.")

    data_input_m = st.text_area("Datos (Muestrales):", height=100, key="input_muestral")

    # Se añade una clave única al botón
    if st.button("CALCULAR DATOS", key="btn_muestral"):
        try:
            data_list = [float(x.strip()) for x in data_input_m.split(",") if x.strip()]
            st.success("LOS DATOS SE CARGARON CORRECTAMENTE")
            mostrar_metrica(data_list, "MUESTRAL")
        except ValueError:
            st.error("ERROR: REVISAR EL FORMATO DE LOS DATOS. SOLO SE ADMITEN NÚMEROS SEPARADOS POR COMAS.")
        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")

with tab2:
    st.header("Estadísticos Poblacionales")
    st.text("Calcula las medidas estadísticas de una población de datos.")
    st.info("Ingresa los datos para calcular las Medidas Poblacionales. Por favor, Separe los números con comas.")

    data_input_p = st.text_area("Datos (Poblacionales):", height=100, key="input_poblacional")

    # Se añade una clave única al botón
    if st.button("CALCULAR DATOS", key="btn_poblacional"):
        try:
            data_list = [float(x.strip()) for x in data_input_p.split(",") if x.strip()]
            st.success("LOS DATOS SE CARGARON CORRECTAMENTE")
            mostrar_metrica(data_list, "POBLACIONAL")
        except ValueError:
            st.error("ERROR: REVISAR EL FORMATO DE LOS DATOS. SOLO SE ADMITEN NÚMEROS SEPARADOS POR COMAS.")
        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")

with tab3:
    st.header("Cargar Datos desde Archivo")
    st.text("Carga un archivo CSV o Excel para calcular las medidas estadísticas.")

    uploaded_file = st.file_uploader("Sube tu archivo", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file, engine='openpyxl')

            st.write("Vista previa de los datos cargados:", df.head())

            columna = st.selectbox("Selecciona la columna para análisis estadístico:", df.columns)

            tipo_calculo = st.radio("Selecciona el tipo de cálculo:", ["MUESTRAL", "POBLACIONAL"], key="radio_archivo")

            if st.button("CALCULAR DATOS DEL ARCHIVO", key="btn_archivo"):
                # Asegurarse de que la columna exista
                if columna in df.columns:
                    # Convertir a numérico, los errores se convierten en NaN
                    datos_numericos = pd.to_numeric(df[columna], errors='coerce')
                    # Eliminar los valores NaN
                    datos_limpios = datos_numericos.dropna().tolist()

                    if datos_limpios:
                        mostrar_metrica(datos_limpios, tipo=tipo_calculo)
                    else:
                        st.error("ERROR: LA COLUMNA SELECCIONADA NO CONTIENE DATOS NUMÉRICOS VÁLIDOS.")
                else:
                    st.error("La columna seleccionada no existe en el archivo.")

        except Exception as e:
            st.error(f"ERROR AL PROCESAR EL ARCHIVO: {e}")









