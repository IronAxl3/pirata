import matplotlib.pyplot as plt
import streamlit as st

def plot_sir(S, I, R, t):
    fig, ax = plt.subplots()
    ax.plot(t, S, label="Susceptibles")
    ax.plot(t, I, label="Infectados")
    ax.plot(t, R, label="Racionales")
    ax.set_xlabel("Tiempo (días)")
    ax.set_ylabel("Población")
    ax.legend()
    st.pyplot(fig)