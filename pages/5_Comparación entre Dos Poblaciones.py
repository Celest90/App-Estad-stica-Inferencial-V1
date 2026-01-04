import streamlit as st

st.set_page_config(page_title="Comparación entre Dos Poblaciones",
                   layout="wide")

st.title(":green[Comparación entre Dos Poblaciones]",
            text_alignment="center")

valores_z = {
    "90%": 1.645,
    "95%": 1.96,
    "97.5%": 2.241,
    "99%": 2.576
}

tab1, tab2 = st.tabs(["COMPARACIÓN DE MEDIAS", "COMPARACIÓN DE PROPORCIONES"])
with tab1:
    st.subheader("Comparar Dos Medias Poblacionales",)
    st.info("ingresa los datos necesarios para comparar dos medias poblacionales.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("POBLACIÓN 1",
                     text_alignment="center")

        tamano_muestra_1 = st.number_input(
            "Tamaño Muestral (n):",
            value=0,
            step=1,
            key="n_tamano_muestra_comparacion_1"
        )
        media_muestral_1 = st.number_input(
            "Media Muestral (x̄):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="media_muestral_comparacion_1"
        )
        varianza_1 = st.number_input(
            "Varianza (s²):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="varianza_comparacion_1"
        )

    with col2:
        st.subheader("POBLACIÓN 2",
                     text_alignment="center")

        tamano_muestra_2 = st.number_input(
            "Tamaño Muestral (n):",
            value=0,
            step=1,
            key="n_tamano_muestra_comparacion_2"
        )
        media_muestral_2 = st.number_input(
            "Media Muestral (x̄):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="media_muestral_comparacion_2"
        )
        varianza_2 = st.number_input(
            "Varianza (s²):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="varianza_comparacion_2"
        )
        nivel_confianza_medias = st.selectbox(
            "Nivel de Confianza:",
            options=list(valores_z.keys()),
            index=1,
            key="confianza_comparacion_medias"
        )

    if st.button("COMPARAR MEDIAS", key="comparar_medias"):
        try:
            z = valores_z[nivel_confianza_medias]

            diferencia_medias = media_muestral_1 - media_muestral_2

            error_estandar_medias = ((varianza_1 / tamano_muestra_1) + (varianza_2 / tamano_muestra_2)) ** 0.5

            intervalo_confianza_superior = diferencia_medias + (z * error_estandar_medias)
            intervalo_confianza_inferior = diferencia_medias - (z * error_estandar_medias)

            st.divider()

            st.subheader("Resultados Del Cálculo")

            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric(label = "Diferencia de Medias", value = f"{diferencia_medias:.3f}")
            with c2:
                st.metric(label = "Error Estándar Entre Medias", value = f"{error_estandar_medias:.3f}")
            with c3:
                st.metric(label = "IC Limiter Superior", value = f"{intervalo_confianza_superior:.3f}")
                st.metric(label = "IC Limiter Inferior", value = f"{intervalo_confianza_inferior:.3f}")

            st.divider()

            if intervalo_confianza_inferior > 0 or intervalo_confianza_superior < 0:
                conclusion = "Hay evidencia suficiente para afirmar que las medias poblacionales son diferentes."
            else:
                conclusion = "No hay evidencia suficiente para afirmar que las medias poblacionales son diferentes."

            st.info(f"""
            **Interpretación**
            - Con un nivel de confianza del {nivel_confianza_medias}, el intervalo de confianza para la diferencia de medias es
            de <{intervalo_confianza_inferior:.3f}, {intervalo_confianza_superior:.3f}>.
            - {conclusion}
            """)

        except Exception as e:
            st.error(f"Ocurrió Un Error Inesperado: {e}")
pass

with tab2:
    st.subheader("Comparar Dos Proporciones Poblacionales")
    st.info("Ingresa los datos necesarios para comparar dos proporciones poblacionales.")

    col1, col2 = st.columns(2)
    with col1:

        st.subheader("POBLACIÓN 1",
                     text_alignment="center")

        tamano_muestra_proporcion_1 = st.number_input(
            "Tamaño Muestral (n):",
            value=0,
            step=1,
            key="n_tamano_muestra_proporcion_1"
        )
        proporcion_1 = st.number_input(
            "Proporción (p):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="proporcion_comparacion_1"
        )

    with col2:
        st.subheader("POBLACIÓN 2",
                     text_alignment="center")

        tamano_muestra_proporcion_2 = st.number_input(
            "Tamaño Muestral (n):",
            value=0,
            step=1,
            key="n_tamano_muestra_proporcion_2"
        )
        proporcion_2 = st.number_input(
            "Proporción (p):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="proporcion_comparacion_2"
        )
        nivel_confianza_proporciones = st.selectbox(
            "Nivel de Confianza:",
            options=list(valores_z.keys()),
            index=1,
            key="confianza_comparacion_proporciones"
        )

    if st.button("COMPARAR PROPORCIONES", key="comparar_proporciones"):
        try:
            z = valores_z[nivel_confianza_proporciones]

            diferencia_proporciones = proporcion_1 - proporcion_2

            q1 = 1 - proporcion_1
            q2 = 1 - proporcion_2

            error_estandar_proporciones =(((proporcion_1 * q1) / tamano_muestra_proporcion_1) + ((proporcion_2 * q2) / tamano_muestra_proporcion_2)) ** 0.5

            intervalo_confianza_superior_prop = diferencia_proporciones + (z * error_estandar_proporciones)
            intervalo_confianza_inferior_prop = diferencia_proporciones - (z * error_estandar_proporciones)

            st.divider()

            st.subheader("Resultados Del Cálculo")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric(label = "Diferencia de Proporciones", value = f"{diferencia_proporciones:.3f}")
            with c2:
                st.metric(label = "Error Estándar Entre Proporciones", value = f"{error_estandar_proporciones:.3f}")
            with c3:
                st.metric(label = "IC Limiter Superior", value = f"{intervalo_confianza_superior_prop:.3f}")
                st.metric(label = "IC Limiter Inferior", value = f"{intervalo_confianza_inferior_prop:.3f}")

            st.divider()

            if intervalo_confianza_inferior_prop > 0 or intervalo_confianza_superior_prop < 0:
                conclusion_prop = "Hay evidencia suficiente para afirmar que las proporciones poblacionales son diferentes."
            else:
                conclusion_prop = "No hay evidencia suficiente para afirmar que las proporciones poblacionales son diferentes."

            st.info(f"""
            **Interpretación**
            - Con un nivel de confianza del {nivel_confianza_proporciones}, el intervalo de confianza para la diferencia de proporciones es
            de <{intervalo_confianza_inferior_prop:.3f}, {intervalo_confianza_superior_prop:.3f}>.
            - {conclusion_prop}
            """)

        except Exception as e:
            st.error(f"Ocurrió Un Error Inesperado: {e}")

pass














