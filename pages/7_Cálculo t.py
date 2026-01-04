import streamlit as st

st.set_page_config(page_title="Error Estándar",
                        layout="wide")

st.title(":green[Cálculo t student]",
         text_alignment="center")

tab1, = st.tabs(["CÁLCULO PARA ENCONTRAR VALOR T STUDENT"])

with tab1:
    st.subheader("Calcular El Valor T Student",)
    st.info("Ingresa los datos necesarios para calcular el valor t student.")

    col1, col2 = st.columns(2)
    with col1:
        media_muestral = st.number_input(
            "Media Muestral (x̄):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="media_muestral_t_student"
        )
        media_poblacional = st.number_input(
            "Media Poblacional (μ):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="media_poblacional_t_student"
        )

    with col2:
        desviacion_estandar = st.number_input(
            "Desviación Estándar (s):",
            value=0.0,
            step=0.01,
            format="%.2f",
            key="desviacion_estandar_t_student"
        )
        tamano_muestra = st.number_input(
            "Tamaño Muestral (n):",
            value = 0,
            step=1,
            key="n_tamano_muestra_t_student"
        )

    if st.button("CÁLCULAR VALOR T STUDENT", key = "calcular_t_student"):
        try:
            if tamano_muestra <= 1:
                st.error("El tamaño de la muestra debe ser mayor que uno.")
            else:
                error_estandar = desviacion_estandar / (tamano_muestra ** 0.5)
                t_student = (media_muestral - media_poblacional) / error_estandar

                st.divider()

                st.subheader("Resultados Del Cálculo")
                st.metric(label = "Valor T Student (t)" , value = f"{t_student:.3f}")

                st.success("EL CÁLCULO SE HA REALIZADO CON ÉXITO.")

        except Exception as e:
            st.error(f"Ocurrio Un Error Inesperado: {e}")

