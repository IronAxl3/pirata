import streamlit as st
from models.sir_model import solve_sir
from utils.plotter import plot_sir

st.title("Modelo SIR: Simulación de Propagación de Rumores")
st.sidebar.header("Parámetros del modelo")

N = st.sidebar.number_input("Población total", value=266+8+1)
I0 = st.sidebar.number_input("Infectados iniciales", value=1)
R0 = st.sidebar.number_input("Racionales iniciales", value=8)
b = st.sidebar.slider("Tasa de infección (b)", 0.0, 1.0, 0.004)
k = st.sidebar.slider("Tasa de racionalización (k)", 0.0, 0.1, 0.01)
t_max = st.sidebar.number_input("Días de simulación", value=15)

S, I, R, t = solve_sir(N, I0, R0, b, k, t_max)
plot_sir(S, I, R, t)