import streamlit as st

st.set_page_config(page_title="Intervalo De Confianza Para Una Población",
                     layout="wide")

st.title(":green[Intervalo De Confianza Para Una Población]",
         text_alignment="center")

valores_z = {
    "90%": 1.645,
    "95%": 1.96,
    "97.5%": 2.241,
    "99%": 2.576
}

def mostrar_resultados(limite_inferior, limite_superior, nivel_confianza):
    st.divider()
    st.subheader("Resultados Del Cálculo")
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="Límite Inferior", value=f"{limite_inferior:.3f}")
    with c2:
        st.metric(label="Límite Superior", value=f"{limite_superior:.3f}")
    st.divider()
    st.info(f"""
    **Interpretación**
    - Con un nivel de confianza del {nivel_confianza}, el intervalo de confianza es
    de <{limite_inferior:.3f}, {limite_superior:.3f}>.""")

tab1, tab2 = st.tabs(["INTERVALO DE LA MEDIA", "INTERVALO DE LA PROPORCIÓN"])
with tab1:
    st.subheader("Calcular El Intervalo De Confianza Para La Media De Una Población",
              text_alignment="justify",)
    st.info("Ingresa los datos necesarios para calcular el intervalo de confianza para la media de una población "
            "Grande y Con Una Desviación Estándar Desconocida.")
    col1, col2 = st.columns(2)
    with col1:
        tamano_muestra_media = st.number_input(
            "Tamaño Muestral (n):",
            value = 30,
            step=1,
            key="n_tamano_muestra_media"
        )
        media_muestral_media = st.number_input(
            "Media Muestral (x̄):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="media_muestral_media"
        )

    with col2:
        desviacion_estandar_media = st.number_input(
            "Desviación Estándar (s):",
            value=1.0,
            step=0.01,
            format="%.2f",
            key="desviacion_estandar_media"
        )
        nivel_confianza_media = st.selectbox(
            "Nivel de Confianza:",
            options = list (valores_z.keys()),
            index = 1,
            key="confianza_media"
        )

    if st.button("CALCULAR INTERVALO DE CONFIANZA", key="calcular_intervalo_media"):
        try:
            z = valores_z[nivel_confianza_media]

            margen_error_media = z * (desviacion_estandar_media / (tamano_muestra_media ** 0.5))

            limite_inferior_media = media_muestral_media - margen_error_media
            limite_superior_media = media_muestral_media + margen_error_media

            mostrar_resultados(limite_inferior_media, limite_superior_media, nivel_confianza_media)

            st.success("EL CÁLCULO SE HA REALIZADO CON ÉXITO.")

        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")
pass




with tab2:
    st.subheader("Calcular El Intervalo De Confianza Para La Proporción De Una Población",
                text_alignment="justify",)

    st.info("Ingresa los datos necesarios para calcular el intervalo de confianza para la proporción de una población.")

    col1, col2 = st.columns(2)
    with col1:
        tamano_muestra_proporcion = st.number_input(
            "Tamaño Muestral (n):",
            value=30,
            step=1,
            key="n_tamano_muestra_proporcion"
        )
        proporcion_muestra_proporcion = st.number_input(
            "Propoción Con Respecto A La Muestra (X):",
            value=1,
            step=1,
            key="proporcion_muestra_proporcion"
        )

    with col2:
        nivel_confianza_proporcion = st.selectbox(
            "Nivel De Confianza:",
            options=list(valores_z.keys()),
            index=1,
            key="confianza_proporcion"
        )

    if st.button("CALCULAR INTERVALO DE CONFIANZA", key="calcular_intervalo_proporcion"):
        try:
            z = valores_z[nivel_confianza_proporcion]

            p_hat = proporcion_muestra_proporcion / tamano_muestra_proporcion

            q_hat = 1 - p_hat

            margen_error_proporcion = z * (((p_hat * q_hat) / tamano_muestra_proporcion) ** 0.5)

            limite_inferior_proporcion = p_hat - margen_error_proporcion
            limite_superior_proporcion = p_hat + margen_error_proporcion

            mostrar_resultados(limite_inferior_proporcion, limite_superior_proporcion, nivel_confianza_proporcion)

            st.success("EL CÁLCULO SE HA REALIZADO CON ÉXITO.")

        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")

pass




