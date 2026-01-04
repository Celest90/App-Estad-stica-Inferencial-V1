import streamlit as st

st.set_page_config(page_title="Error Estandar",
                        layout="wide")

st.title(":green[Error Estándar]",
            text_alignment="center")

tab1, tab2 = st.tabs(["ERROR ESTÁNDAR DE LA MEDIA", "ERROR ESTÁNDAR DE LA PROPORCIÓN"])

with tab1:
    st.subheader("Calcular El Error Estándar De La Media",)
    st.info("Ingresa los datos necesarios para calcular el error estándar de la media.")

    col1, col2 = st.columns(2)

    with col1:
        desviacion_estandar_media = st.number_input(
            "Desviación Estándar (s):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="desviacion_estandar_error_media"
        )

    with col2:
        tamano_muestra_media = st.number_input(
            "Tamaño Muestral (n):",
            value = 0,
            step=1,
            key="n_tamano_muestra_media"
        )

    if st.button("CÁLCULAR ERROR ESTÁNDAR", key = "calcular_error_media"):
        try:
            if tamano_muestra_media <= 0:
                st.error("El tamaño muestral debe ser mayor que cero.")
            else:
                error_estandar_media = desviacion_estandar_media / (tamano_muestra_media ** 0.5)
                st.divider()
                st.subheader("Resultados Del Cálculo")
                st.metric(label="Error Estándar De La Media (SE)", value=f"{error_estandar_media:.3f}")
                st.success("EL CÁLCULO SE HA REALIZADO CON ÉXITO.")
        except Exception as e:
            st.error(f"Ocurrio Un Error Inesperado: {e}")

pass

with tab2:
    st.subheader("Calcular El Error Estándar De La Proporción",)
    st.info("Ingresa los datos necesarios para calcular el error estándar de la proporción.")

    col1, col2 = st.columns(2)

    with col1:
        proporcion_muestral = st.number_input(
            "Proporción Muestral (p̂):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="proporcion_muestral_error_proporcion"
        )

    with col2:
        tamano_muestra_proporcion = st.number_input(
            "Tamaño Muestral (n):",
            value = 0,
            step=1,
            key="n_tamano_muestra_proporcion"
        )

    if st.button("CÁLCULAR ERROR ESTÁNDAR", key = "calcular_error_proporcion"):
        try:
            if tamano_muestra_proporcion <= 0:
                st.error("El tamaño muestral debe ser mayor que cero.")
            else:
                error_estandar_proporcion = ((proporcion_muestral * (1 - proporcion_muestral)) / tamano_muestra_proporcion) ** 0.5
                st.divider()
                st.subheader("Resultados Del Cálculo")
                st.metric(label="Error Estándar De La Proporción (SE)", value=f"{error_estandar_proporcion:.3f}")
                st.success("EL CÁLCULO SE HA REALIZADO CON ÉXITO.")

        except Exception as e:
            st.error(f"Ocurrio Un Error Inesperado: {e}")



