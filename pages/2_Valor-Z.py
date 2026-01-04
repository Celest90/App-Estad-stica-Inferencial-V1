import streamlit as st
import numpy as np
from scipy import stats

st.set_page_config(page_title="Valor Z",
                   layout= "wide")
st.title(":green[Valor Z]",
            text_alignment ="center",)

tab1, tab2 = st.tabs(["CALCULAR VALOR Z", "CALCULAR DESDE PROBABILIDAD"])

with tab1:
    st.header("Calcular Valor Z Desde Datos")
    st.text("Calcula el valor Z estandarizado para un valor dado en una distribución normal.")
    st.info("Ingresa los datos necesarios para calcular el valor Z.")

    col1, col2, col3 = st.columns(3)
    with col1:
        puntaje_bruto_x = st.number_input(
            "Puntaje Bruto (X):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="puntaje_bruto_x"
        )

    with col2:
        media_poblacional = st.number_input(
            "Media Poblacional (μ):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="media_poblacional"
        )

    with col3:
        desviacion_estandar = st.number_input(
            "Desviación Estándar (σ):",
            value=1.0,
            step=0.01,
            format="%.2f",
            key="desviacion_estandar"
        )

    if st.button("CALCULAR VALOR Z", key="btn_calcular_valor_z"):
        try:
            if desviacion_estandar == 0:
                st.error("La Desviación Estándar no puede ser cero.")

            else:
                valor_z = (puntaje_bruto_x - media_poblacional) / desviacion_estandar

                st.divider()
                st.subheader("Resultados Del Cálculo")

                c1, c2 = st.columns(2)
                with c1:
                    st.metric(label="Valor Z", value=f"{valor_z:.4f}")

                with c2:
                    probabilidad = stats.norm.cdf(valor_z)
                    st.metric(label="Probabilidad Acumulada P(Z <= z)", value=f"{probabilidad:.4f}")

                st.divider()

                st.info(f"""
                **Interpretación**
                - El puntaje {puntaje_bruto_x:.4f} está a {abs(valor_z):.4f} desviaciones estándar {'por encima' if valor_z > 0 else 'por debajo'} de la media poblacional {media_poblacional:.4f}.
                - Aproximadamente el {probabilidad*100:.2f}% de los datos estan por debajo de este valor.
                """)

                st.success("EL CÁLCULO SE HA REALIZADO CON ÉXITO.")

        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")

with tab2:
    st.header("Calcular Valor Z Desde Probabilidad")
    st.text('Encuentra el valor Z Correspondiente a una probabilidad dada en una distribución normal.')
    st.info("Ingresa el valor de probabilidad (p) para calcular el valor Z.")

    col1, col2 = st.columns(2)

    with col1:
        probabilidad_input = st.number_input(
            "Probabilidad (p):",
            value = 0.5,
            min_value=0.0001,
            max_value=0.9999,
            step=0.01,
            format="%.4f",
            key="probabilidad_input",
            help="Ingrese valores entre 0 y 1"
        )

    with col2:
        st.write("")

    if st.button("CALCULAR VALOR Z DESDE PROBABILIDAD", key="btn_calcular_valor_z_probabilidad"):
        try:
            valor_z_inverso = stats.norm.ppf(probabilidad_input)

            st.divider()
            st.subheader("Resultado Del Cálculo")

            c1, c2 = st.columns(2)
            with c1:
                st.metric(label="Valor Z", value=f"{valor_z_inverso:.4f}")

            with c2:
                st.metric(label="Probabilidad (p)", value=f"{probabilidad_input:.4f}")

            st.divider()

            st.info(f""" 
            **Interpretación**
            - Un valor Z de {valor_z_inverso:.4f} corresponde a una probabilidad acumulada de {probabilidad_input:.4f}.
            - Siendo un aproximado del {probabilidad_input*100:.2f}% de los datos por debajo de este valor Z.
            - Este valor está a {abs(valor_z_inverso):.4f} desviaciones estándar {'por encima' if valor_z_inverso > 0 else 'por debajo'} de la media poblacional.
            """)

            st.success("EL CÁLCULO SE HA REALIZADO CON ÉXITO.")

        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")










