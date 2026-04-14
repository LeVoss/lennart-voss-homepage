import streamlit as st
import os

st.set_page_config(page_title="Lennart Voss | Die Roman-Fabrik", page_icon="📖", layout="centered")

# CSS für den Look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Header
st.write(f"<h1 style='text-align: center; color: #2E4053;'>Lennart Voss ✍️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Die Roman-Fabrik: Vom Plot zum Bestseller</h3>", unsafe_allow_html=True)

st.divider()

# Vorstellung der Roman-Fabrik
st.write("""
Hier entsteht die Zentrale für alle, die das Handwerk des Schreibens meistern wollen. 
In der **Roman-Fabrik** zeige ich dir, wie du Struktur in dein Chaos bringst.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Teil 1: Das Fundament")
    if os.path.exists("cover_rf1.png"):
        st.image("cover_rf1.png", use_container_width=True)
    st.write("Der Leitfaden für Struktur, Plotting und Charakterentwicklung.")
    st.markdown("**14,99 €** (Inkl. Versand)")

with col2:
    st.subheader("Teil 2: Die Veröffentlichung")
    if os.path.exists("cover_rf2.png"):
        st.image("cover_rf2.png", use_container_width=True)
    else:
        st.info("Coming Soon: Erscheint Kürze!")
    st.write("Marketing, KDP-Geheimnisse und der Weg in den Buchhandel.")
    st.markdown("**14,99 €** (Inkl. Versand)")

st.divider()

# Call to Action für dein neues Business
st.success("### Du bist Autor und willst auch so eine Seite?")
st.write("""
Ich helfe dir, deine eigene Autoren-Homepage wie diese hier zu erstellen. 
Schnell, professionell und ohne Technik-Frust.
""")
if st.button("Jetzt unverbindlich anfragen"):
    st.info("Schreib mir eine E-Mail an: lennart@voss-books.de") # Deine E-Mail anpassen

# Footer
st.divider()
st.write("<p style='text-align: center;'>© 2026 Lennart Voss</p>", unsafe_allow_html=True)
