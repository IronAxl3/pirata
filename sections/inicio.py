import streamlit as st
from PIL import Image

def show():
    left, center, right = st.columns([2.5, 1, 2.5])
    with center:
        logo = Image.open("assets/LOGO_UNMSM.png")
        st.image(logo, width=180, use_container_width=False)

    st.markdown(
        """
        <div style="text-align:center;">
            <h1 style="font-size:2.4rem; margin-bottom:0;">Proyecto Pirata – Modelos SIR</h1>
            <p style="color:#555; margin:0;">Universidad Nacional Mayor de San Marcos</p>
            <p style="color:#777; margin:0;">Facultad de Ciencias Matemáticas | Computación Científica</p>
            <p style="color:#999; margin:0;">Técnicas de Modelamiento Matemático – Profesor: Yefri Ander Vidal Vega</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### ¿Qué podrás explorar?")
    st.write(
        """
        En esta aplicación interactiva podrás:
        - 🔬 **Simular** brotes epidémicos, rumores o reclutamiento ideológico
        - 📊 **Visualizar** curvas S-I-R en tiempo real
        - 🎚️ **Ajustar parámetros** y observar cambios inmediatos
        - 📈 **Analizar picos, umbrales críticos y R₀**
        - 🧠 **Comprender** la matemática detrás de fenómenos sociales
        """
    )

    st.divider()

    st.markdown("### Integrantes del Proyecto")

    integrantes = [
        {"nombre": "Iron Axl Ortega Yucra", "foto": "assets/yo.jpeg"},
        {"nombre": "Juan Chipana Bellido", "foto": "assets/juanCook.jpeg"},
        {"nombre": "Dylan Lucar Jaimes", "foto": "assets/licuar.jpeg"},
        {"nombre": "Marcela Ventura Castillo", "foto": "assets/peligrosa.jpeg"},
        {"nombre": "Jan Mancinelli Vite", "foto": "assets/osito.jpeg"},
    ]

    cols = st.columns([1, 1, 1, 1, 1])  
    for col, integrante in zip(cols, integrantes):
        with col:
            try:
                img = Image.open(integrante["foto"]).convert("RGB")
                w, h = img.size
                side = min(w, h)
                img = img.crop(((w - side) // 2, (h - side) // 2,
                                (w + side) // 2, (h + side) // 2)).resize((180, 180))
                st.image(img, width=180)
                st.caption(f"**{integrante['nombre']}**")
            except FileNotFoundError:
                st.error(f"No se encontró: {integrante['foto']}")

    
    st.divider()
    st.markdown("### Resumen por sección")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Asignación 1 – Gripe Porcina**")
        st.write(
            "Simula el brote clásico SIR en 7 138 estudiantes. "
            "Ajusta β y k para ver el pico de infectados y el % que nunca se enferma."
        )

    with col2:
        st.markdown("**Asignación 2 – Rumor Académico**")
        st.write(
            "Modela la cancelación de un examen. "
            "Compara cómo la “persuasión racional” reduce el número de creyentes."
        )

    with col3:
        st.markdown("**Asignación 3 – Reclutamiento de Sectas**")
        st.write(
            "Incluye inmunización preventiva α. "
            "Descubre por qué la secta desaparece al año aunque R₀ > 1."
        )
        st.divider()

    st.info("Tip: Ajusta los sliders y observa cómo cambian las curvas en tiempo real.", icon="ℹ️")

    st.markdown(
        "<p style='text-align:center; color:#888; font-size:14px; margin-top:40px;'>"
        "© 2025 – Universidad Nacional Mayor de San Marcos | Equipo Pirata</p>",
        unsafe_allow_html=True,
    )
