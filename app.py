import streamlit as st
import os

# 1. Grundkonfiguration
st.set_page_config(page_title="Lennart Voss | Autor & Schreibcoach", page_icon="📖", layout="centered")

# 2. CSS (Entfernt Menüs für einen sauberen Look)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# 3. TITEL & WILLKOMMEN
st.write(f"<h1 style='text-align: center; color: #2E4053;'>Willkommen in der Roman-Fabrik! ✍️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Handwerk trifft Inspiration.</h3>", unsafe_allow_html=True)
st.write("""
<p style='text-align: center; font-size: 1.2em;'>
Ich bin <strong>Lennart Voss</strong>. Ich helfe Autoren dabei, ihre Visionen in fesselnde Geschichten zu verwandeln – 
mit Struktur, System und Leidenschaft.
</p>
""", unsafe_allow_html=True)

st.divider()

# 4. Buch-Präsentation: Die Roman-Fabrik
st.header("Das aktuelle Werk")
col1, col2 = st.columns([1, 2])
with col1:
    # Hier das Cover-Bild der Roman-Fabrik (z.B. cover_rf.png) hochladen
    if os.path.exists("cover_rf.png"):
        try:
            st.image("cover_rf.png", use_container_width=True)
        except Exception:
            st.error("Bilddatei 'cover_rf.png' fehlerhaft.")
    else:
        st.info("📖 Cover-Bild folgt...")

with col2:
    st.write("""
    **Die Roman-Fabrik: Vom Plot zum Bestseller**
    Dieser Ratgeber ist dein Werkzeugkasten für die moderne Romanerstellung. Erfahre, wie du 
    deine Charaktere tiefgründig gestaltest, Spannungsbögen meisterhaft planst und 
    den Weg durch den Veröffentlichungsdschungel findest.
    """)

st.divider()

# 5. BESTELL-ÜBERSICHT & FORMULAR
st.header("📦 Buch direkt bei mir bestellen")
st.write("Wähle hier deine gewünschte Ausgabe aus (Preise inkl. Versand innerhalb Deutschland):")

# Liste der Bestelloptionen
st.markdown("""
* **14,99 €** – Die Roman-Fabrik (Standard Taschenbuch, inkl. Versand innerhalb Deutschland)
""")

# Falls du ein eigenes Google Formular für Lennart Voss hast, hier die URL austauschen:
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf60i048_9KbQ_yMcM0kJQpBGA6s3xOuASdLO6hPfhr6z2zbQ/viewform?embedded=true"

st.markdown(f"""
    <iframe src="{form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
        Wird geladen...
    </iframe>
    """, unsafe_allow_html=True)

# 6. BUSINESS-MODUL (Optional, für deine potenziellen Kunden)
st.divider()
st.success("### Du bist Autor und möchtest auch so eine Homepage?")
st.write("""
Präsentiere deine Bücher professionell und verkaufe sie direkt an deine Leser. 
Ich erstelle für dich eine moderne Autoren-Homepage – schnell, unkompliziert und individuell. 
Schreib mir einfach eine Nachricht über das Formular oben oder direkt per E-Mail!
""")

# 7. FOOTER
st.divider()
st.write("<p style='text-align: center;'>© 2026 Lennart Voss</p>", unsafe_allow_html=True)

footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    with st.expander("Impressum"):
        st.write("""
        **Angaben gemäß § 5 TMG:** Stefan Röser (Lennart Voss),  
        c/o Online Impressum.de #6281, Europaring 90, 
        53757 Sankt Augustin
        
        **Kontakt:** E-Mail: stefan@booksart.de  
        """)
with footer_col2:
    with st.expander("Datenschutz"):
        st.write("""
        **Datenschutzerklärung** Diese Seite nutzt ein eingebettetes Google Formular zur Bestellabwicklung. 
        Die Daten werden auf Google-Servern gespeichert, damit der Autor die Bestellung bearbeiten kann. 
        """)
