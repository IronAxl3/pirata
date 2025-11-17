import streamlit as st
import numpy as np
from models.sir_model import solve_sir
from utils.plotter import plot_sir

def show():
    st.header("Asignación 1 – Modelo SIR Clásico: Gripe Porcina en San Marcos")
    st.markdown("""
    **Universidad Nacional Mayor de San Marcos**  
    Facultad de Ciencias Matemáticas  
    Curso: Técnicas de Modelamiento Matemático  
    """)

    st.subheader("Modelo Matemático")
    st.latex(r"""
    \frac{dS}{dt} = -\beta S I \\
    \frac{dI}{dt} = \beta S I - k I \\
    \frac{dR}{dt} = k I
    """)

    st.markdown("""
    - **S(t)**: Estudiantes susceptibles  
    - **I(t)**: Estudiantes infectados  
    - **R(t)**: Estudiantes recuperados (inmunes)  
    - **β**: Tasa de infección por contacto  
    - **k**: Tasa de recuperación por día  
    """)

    st.subheader("Parámetros del Modelo")
    col1, col2 = st.columns(2)
    with col1:
        N = st.number_input("Población total (N)", min_value=100, max_value=20000, value=7138)
        I0 = st.number_input("Infectados iniciales (I₀)", min_value=1, max_value=100, value=1)
    with col2:
        beta = st.slider("Tasa de infección (β)", 0.0, 0.001, 1/7138, step=1e-6, format="%.6f")
        k = st.slider("Tasa de recuperación (k)", 0.1, 1.0, 0.40, step=0.01)

    S0 = N - I0
    R0 = 0
    t_max = 40

    S, I, R, t = solve_sir(N, I0, R0, beta, k, t_max)

    st.subheader("Simulación Numérica")
    fig = plot_sir(S, I, R, t)
    st.pyplot(fig)

    st.subheader("Análisis del Comportamiento")
    pico_dia = t[np.argmax(I)]
    pico_infectados = int(max(I))
    final_susceptibles = int(S[-1])
    total_infectados = N - final_susceptibles
    R0_valor = beta * N / k

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pico de Infectados", f"{pico_infectados}", f"Día {pico_dia:.1f}")
    with col2:
        st.metric("Total Infectados", f"{total_infectados}")
    with col3:
        st.metric("R₀ (Número Básico)", f"{R0_valor:.2f}")

    st.markdown(f"""
    - **¿Se infectará toda la población?** No.  
    - **¿Por qué?** Porque cuando **S(t)** cae por debajo de **γ/β ≈ {k/beta:.0f}**, el número reproductivo efectivo cae por debajo de 1 y la epidemia decae.
    - **Susceptibles finales:** ≈ {final_susceptibles} personas nunca se infectan.
    """)

    st.subheader("Conclusión")
    st.markdown("""
    El modelo SIR clásico predice que la gripe porcina se propaga rápidamente al inicio, alcanza un pico intermedio y luego decae conforme la población se agota de susceptibles.  
    Aunque **R₀ > 1**, la infección **no alcanza al 100%** de la población, lo cual es consistente con brotes reales.
    """)