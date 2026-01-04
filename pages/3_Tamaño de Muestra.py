import streamlit as st

st.set_page_config(page_title="Tamaño de Muestra",
                   layout="wide")
st.title(":green[Calculo De Tamaño De Muestra]",
            text_alignment="center",)
valores_z = {
    "90%": 1.645,
    "95%": 1.96,
    "97.5%": 2.241,
    "99%": 2.576
}

tab1, tab2 = st.tabs(["POBLACION FINITA", "POBLACION INFINITA"])
with tab1:
    st.header("Calcular Tamaño de Muestra para Población Finita")
    st.text("Calcula el tamaño de muestra necesario para una población finita.")
    st.info("Ingresa los datos necesarios para calcular el tamaño de muestra.")

    col1, col2= st.columns(2)
    with col1:
        tamano_poblacional = st.number_input(
            "Tamaño de Población (N):",
            value=0.0,
            step=1.0,
            format="%.0f",
            key="N_poblacion_finita"
        )
        nvl_confianza = st.selectbox(
            "Nivel de Confianza:",
            options=list(valores_z.keys()),
            index=1,
            key="confianza_poblacion_finita"
        )
        z = valores_z[nvl_confianza]

    with col2:
        probabilidad = st.number_input(
            "Probabilidad Estimada (p):",
            value=0.5,
            min_value=0.0001,
            max_value=0.9999,
            step=0.01,
            format="%.2f",
            key="probabilidad_poblacion_finita"
        )

        margen_error = st.number_input(
            "Margen de Error (E) (%):",
            value=5.0,
            min_value=0.1,
            max_value=100.0,
            step=0.1,
            key="margen_error_poblacion_finita"
        )
        e = margen_error / 100

    if st.button("CALCULAR TAMAÑO DE MUESTRA", key="btn_calcular_tamano_muestra_finita"):
        if tamano_poblacional > 0:
            q = 1 - probabilidad

            numerador = tamano_poblacional * (z ** 2) * probabilidad * q
            denominador = ((e ** 2) * (tamano_poblacional - 1) + ((z ** 2) * probabilidad * q))

            resultado = numerador / denominador if denominador != 0 else 0

            st.success(f"El tamaño de muestra necesario es: {round(resultado)}")
            st.write(f"**Resultado Exacto:** {resultado:.4f}")

        else:
            st.error("ERROR: INGRESAR UNA POBLACIÓN VÁLIDA (N > 0).")

with tab2:
    st.header("Calcular Tamaño de Muestra para Población Infinita")
    st.text("Calcula el tamaño de muestra necesario para una población infinita.")
    st.info("Ingresa los datos necesarios para calcular el tamaño de muestra.")

    col1, col2 = st.columns(2)
    with col1:
        nvl_confianza_inf = st.selectbox(
            "Nivel de Confianza:",
            options=list(valores_z.keys()),
            index=1,
            key="confianza_poblacion_infinita"
        )
        z_inf = valores_z[nvl_confianza_inf]

    with col2:
        probabilidad_inf = st.number_input(
            "Probabilidad Estimada (p):",
            value=0.5,
            min_value=0.0001,
            max_value=0.9999,
            step=0.01,
            format="%.2f",
            key="probabilidad_poblacion_infinita"
        )

        margen_error_inf = st.number_input(
            "Margen de Error (E) (%):",
            value=5.0,
            min_value=0.1,
            max_value=100.0,
            step=0.1,
            key="margen_error_poblacion_infinita"
        )
        e_inf = margen_error_inf / 100

    if st.button("CALCULAR TAMAÑO DE MUESTRA", key="btn_calcular_tamano_muestra_infinita"):

        q_inf = 1 - probabilidad_inf

        numerador_inf = (z_inf ** 2) * probabilidad_inf * q_inf
        denominador_inf = e_inf ** 2

        resultado_inf = numerador_inf / denominador_inf if denominador_inf != 0 else 0

        st.success(f"El tamaño de muestra necesario es: {round(resultado_inf)}")
        st.write(f"**Resultado Exacto:** {resultado_inf:.4f}")



