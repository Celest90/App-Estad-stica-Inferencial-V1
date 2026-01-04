import streamlit as st
import numpy as np
from scipy.stats import norm


st.set_page_config(page_title="Prueba de Hipótesis",
                   layout="wide")

st.title("Prueba de Hipótesis",
         text_alignment="center",)

st.markdown("""
Esta herramienta te permite realizar pruebas de hipótesis para diferentes escenarios estadísticos.""")
st.info("Selecciona el tipo de prueba que deseas realizar y completa los parámetros requeridos.")



# Crear pestañas
tab1, tab2, tab3 = st.tabs([
    "PRUEBA PARA LA MEDIA",
    "PRUEBA PARA LA PROPORCIÓN",
    "PRUEBA PARA DOS MEDIAS"
])

# --- PESTAÑA 1: Prueba para Media ---
with tab1:
    st.header("Prueba de Hipótesis para la Media")

    st.markdown("""
    **Hipótesis:**
    - H₀: μ = μ₀
    - H₁: μ ≠ μ₀ (bilateral) o μ > μ₀ (derecha) o μ < μ₀ (izquierda)
    """)

    tipo_prueba_media = st.selectbox(
        "Tipo de prueba:",
        ["Bilateral (≠)", "Cola derecha (>)", "Cola izquierda (<)"],
        key="tipo_media"
    )

    st.subheader("Parámetros De Entrada")

    col1, col2 = st.columns(2)

    with col1:
        media_poblacional = st.number_input(
            "Media Poblacional Bajo H₀ (μ₀):",
            value=0.0,
            format="%.2f",
            key="media_pob"
        )

        media_muestral = st.number_input(
            "Media Muestral (x̄):",
            value=0.0,
            format="%.2f",
            key="media_muest"
        )

        desv_std = st.number_input(
            "Desviación Estándar Poblacional (σ):",
            min_value=0.001,
            value=1.0,
            format="%.2f",
            key="desv_std"
        )

    with col2:
        tamano_muestra = st.number_input(
            "Tamaño de Muestra (n):",
            min_value=2,
            value=30,
            step=1,
            key="n_media"
        )

        nivel_significancia = st.number_input(
            "Nivel de Significancia (α):",
            min_value=0.001,
            max_value=0.5,
            value=0.05,
            format="%.3f",
            key="alpha_media"
        )

    if st.button("CALCULAR PRUEBA PARA MEDIA", type="secondary", key="btn_media"):
        # Calcular estadístico Z
        error_estandar = desv_std / np.sqrt(tamano_muestra)
        z_calc = (media_muestral - media_poblacional) / error_estandar

        # Calcular p-valor según tipo de prueba
        if tipo_prueba_media == "Bilateral (≠)":
            p_valor = 2 * (1 - norm.cdf(abs(z_calc)))
            z_critico = norm.ppf(1 - nivel_significancia/2)
            region = f"Z < -{z_critico:.4f} o Z > {z_critico:.4f}"
        elif tipo_prueba_media == "Cola derecha (>)":
            p_valor = 1 - norm.cdf(z_calc)
            z_critico = norm.ppf(1 - nivel_significancia)
            region = f"Z > {z_critico:.4f}"
        else:  # Cola izquierda
            p_valor = norm.cdf(z_calc)
            z_critico = norm.ppf(nivel_significancia)
            region = f"Z < {z_critico:.4f}"

        # Mostrar resultados
        st.markdown("---")
        st.subheader("Resultados")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label="Estadístico Z Calculado",
                value=f"{z_calc:.4f}"
            )

        with col2:
            st.metric(
                label="P-Valor",
                value=f"{p_valor:.4f}"
            )

        with col3:
            st.metric(
                label="α (significancia)",
                value=f"{nivel_significancia:.3f}"
            )

        st.info(f"**Región Crítica:** {region}")

        # Decisión y conclusión
        st.subheader("INTERPRETACIÓN Y DECISIÓN")

        if p_valor < nivel_significancia:
            st.error(f"""
            **Se rechaza H₀**
            
            El p-valor ({p_valor:.4f}) es menor que α ({nivel_significancia:.3f}).
            
            **Conclusión:** Hay evidencia estadística suficiente para rechazar la hipótesis nula 
            al nivel de significancia de {nivel_significancia*100}%.
            """)
        else:
            st.success(f"""
            **No se rechaza H₀**
            
            El p-valor ({p_valor:.4f}) es mayor o igual que α ({nivel_significancia:.3f}).
            
            **Conclusión:** No hay evidencia estadística suficiente para rechazar la hipótesis nula 
            al nivel de significancia de {nivel_significancia*100}%.
            """)

# --- PESTAÑA 2: Prueba para Proporción ---
with tab2:
    st.header("Prueba de Hipótesis para Proporción")

    st.markdown("""
    **Hipótesis:**
    - H₀: p = p₀
    - H₁: p ≠ p₀ (bilateral) o p > p₀ (derecha) o p < p₀ (izquierda)
    """)

    tipo_prueba_prop = st.selectbox(
        "Tipo de prueba:",
        ["Bilateral (≠)", "Cola derecha (>)", "Cola izquierda (<)"],
        key="tipo_prop"
    )

    st.subheader("Parámetros de entrada")

    col1, col2 = st.columns(2)

    with col1:
        prop_poblacional = st.number_input(
            "Proporción Poblacional Bajo H₀ (p₀):",
            min_value=0.0001,
            max_value=0.9999,
            value=0.5,
            format="%.2f",
            key="prop_pob"
        )

        exitos = st.number_input(
            "Número de Éxitos en la Muestra (x):",
            min_value=0,
            value=50,
            step=1,
            key="exitos"
        )

    with col2:
        tamano_muestra_prop = st.number_input(
            "Tamaño de Muestra (n):",
            min_value=30,
            value=100,
            step=1,
            key="n_prop",
            help="Se recomienda n ≥ 30 para la aproximación normal"
        )

        nivel_significancia_prop = st.number_input(
            "Nivel de Significancia (α):",
            min_value=0.001,
            max_value=0.5,
            value=0.05,
            format="%.3f",
            key="alpha_prop"
        )

    if st.button("CALCULAR PRUEBA PARA PROPORCIÓN", type="secondary", key="btn_prop"):
        prop_muestral = exitos / tamano_muestra_prop

        # Verificar condiciones para aproximación normal
        np_val = tamano_muestra_prop * prop_poblacional
        nq_val = tamano_muestra_prop * (1 - prop_poblacional)

        if np_val < 5 or nq_val < 5:
            st.warning(f"""
            **Advertencia:** Las condiciones para la aproximación normal pueden no cumplirse.
            - np₀ = {np_val:.2f}
            - n(1-p₀) = {nq_val:.2f}
            
            Se recomienda que ambos valores sean ≥ 5.
            """)

        # Calcular estadístico Z
        error_estandar = np.sqrt((prop_poblacional * (1 - prop_poblacional)) / tamano_muestra_prop)
        z_calc = (prop_muestral - prop_poblacional) / error_estandar

        # Calcular p-valor
        if tipo_prueba_prop == "Bilateral (≠)":
            p_valor = 2 * (1 - norm.cdf(abs(z_calc)))
            z_critico = norm.ppf(1 - nivel_significancia_prop/2)
            region = f"Z < -{z_critico:.4f} o Z > {z_critico:.4f}"
        elif tipo_prueba_prop == "Cola derecha (>)":
            p_valor = 1 - norm.cdf(z_calc)
            z_critico = norm.ppf(1 - nivel_significancia_prop)
            region = f"Z > {z_critico:.4f}"
        else:
            p_valor = norm.cdf(z_calc)
            z_critico = norm.ppf(nivel_significancia_prop)
            region = f"Z < {z_critico:.4f}"

        # Mostrar resultados
        st.markdown("---")
        st.subheader("Resultados")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="Proporción Muestral (p̂)",
                value=f"{prop_muestral:.4f}"
            )

        with col2:
            st.metric(
                label="Estadístico Z",
                value=f"{z_calc:.4f}"
            )

        with col3:
            st.metric(
                label="P-Valor",
                value=f"{p_valor:.4f}"
            )

        with col4:
            st.metric(
                label="α",
                value=f"{nivel_significancia_prop:.3f}"
            )

        st.info(f"**Región Crítica:** {region}")

        # Decisión
        st.subheader("INTERPRETACIÓN Y DECISIÓN")

        if p_valor < nivel_significancia_prop:
            st.error(f"""
            **Se rechaza H₀**
            
            El p-valor ({p_valor:.4f}) es menor que α ({nivel_significancia_prop:.3f}).
            
            **Conclusión:** Hay evidencia estadística suficiente para rechazar que la proporción 
            poblacional es {prop_poblacional:.4f} al nivel de significancia de {nivel_significancia_prop*100}%.
            """)
        else:
            st.success(f"""
            **No se rechaza H₀**
            
            El p-valor ({p_valor:.4f}) es mayor o igual que α ({nivel_significancia_prop:.3f}).
            
            **Conclusión:** No hay evidencia estadística suficiente para rechazar que la proporción 
            poblacional es {prop_poblacional:.4f} al nivel de significancia de {nivel_significancia_prop*100}%.
            """)

# --- PESTAÑA 3: Prueba para Dos Medias ---
with tab3:
    st.header("Prueba de Hipótesis para Diferencia de Medias")

    st.markdown("""
    **Hipótesis:**
    - H₀: μ₁ = μ₂  (o μ₁ - μ₂ = 0)
    - H₁: μ₁ ≠ μ₂ (bilateral) o μ₁ > μ₂ (derecha) o μ₁ < μ₂ (izquierda)
    """)

    tipo_prueba_dos = st.selectbox(
        "Tipo de prueba:",
        ["Bilateral (μ₁ ≠ μ₂)", "Cola derecha (μ₁ > μ₂)", "Cola izquierda (μ₁ < μ₂)"],
        key="tipo_dos"
    )

    st.subheader("Parámetros de entrada")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Muestra 1**")
        media1 = st.number_input(
            "Media Muestral 1 (x̄₁):",
            value=0.0,
            format="%.2f",
            key="media1"
        )
        desv1 = st.number_input(
            "Desviación Estándar 1 (σ₁):",
            min_value=0.0001,
            value=1.0,
            format="%.2f",
            key="desv1"
        )
        n1 = st.number_input(
            "Tamaño de Muestra 1 (n₁):",
            min_value=2,
            value=30,
            step=1,
            key="n1"
        )

    with col2:
        st.markdown("**Muestra 2**")
        media2 = st.number_input(
            "Media Muestral 2 (x̄₂):",
            value=0.0,
            format="%.2f",
            key="media2"
        )
        desv2 = st.number_input(
            "Desviación Estándar 2 (σ₂):",
            min_value=0.0001,
            value=1.0,
            format="%.2f",
            key="desv2"
        )
        n2 = st.number_input(
            "Tamaño de Muestra 2 (n₂):",
            min_value=2,
            value=30,
            step=1,
            key="n2"
        )

    nivel_significancia_dos = st.number_input(
        "Nivel de significancia (α):",
        min_value=0.001,
        max_value=0.5,
        value=0.05,
        format="%.3f",
        key="alpha_dos"
    )

    if st.button("CÁLCULAR PRUEBA PARA DOS MEDIAS", type="secondary", key="btn_dos"):
        # Calcular estadístico Z
        diferencia_medias = media1 - media2
        error_std = np.sqrt((desv1**2 / n1) + (desv2**2 / n2))
        z_calc = diferencia_medias / error_std

        # Calcular p-valor
        if tipo_prueba_dos == "Bilateral (μ₁ ≠ μ₂)":
            p_valor = 2 * (1 - norm.cdf(abs(z_calc)))
            z_critico = norm.ppf(1 - nivel_significancia_dos/2)
            region = f"Z < -{z_critico:.4f} o Z > {z_critico:.4f}"
        elif tipo_prueba_dos == "Cola derecha (μ₁ > μ₂)":
            p_valor = 1 - norm.cdf(z_calc)
            z_critico = norm.ppf(1 - nivel_significancia_dos)
            region = f"Z > {z_critico:.4f}"
        else:
            p_valor = norm.cdf(z_calc)
            z_critico = norm.ppf(nivel_significancia_dos)
            region = f"Z < {z_critico:.4f}"

        # Mostrar resultados
        st.markdown("---")
        st.subheader("Resultados")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="Diferencia (x̄₁ - x̄₂)",
                value=f"{diferencia_medias:.4f}"
            )

        with col2:
            st.metric(
                label="Error Estándar",
                value=f"{error_std:.4f}"
            )

        with col3:
            st.metric(
                label="Estadístico Z",
                value=f"{z_calc:.4f}"
            )

        with col4:
            st.metric(
                label="P-Valor",
                value=f"{p_valor:.4f}"
            )

        st.info(f"**Región crítica:** {region}")

        # Decisión
        st.subheader("**INTERPRETACIÓN Y DECISIÓN**")

        if p_valor < nivel_significancia_dos:
            st.error(f"""
            **Se rechaza H₀**
            
            El p-valor ({p_valor:.4f}) es menor que α ({nivel_significancia_dos:.3f}).
            
            **Conclusión:** Hay evidencia estadística suficiente para rechazar que las medias 
            poblacionales son iguales al nivel de significancia de {nivel_significancia_dos*100}%.
            """)
        else:
            st.success(f"""
            **No se rechaza H₀**
            
            El p-valor ({p_valor:.4f}) es mayor o igual que α ({nivel_significancia_dos:.3f}).
            
            **Conclusión:** No hay evidencia estadística suficiente para rechazar que las medias 
            poblacionales son iguales al nivel de significancia de {nivel_significancia_dos*100}%.
            """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>Tip: El p-valor representa la probabilidad de obtener resultados al menos tan extremos 
    como los observados, asumiendo que H₀ es verdadera.</small>
</div>
""", unsafe_allow_html=True)