import streamlit as st
from streamlit_shortcuts import button
from pyperclip import copy
from datetime import datetime as dt

time_now = dt.strftime(dt.now(), "%Y-%m-%d")

def safe_results():
    with open(f"{time_now}___MA-Prüfungsprotokoll__{lname}_{fname}.backup", "w", encoding="utf-8") as f:
        f.write("Punkte Verteidigung: "+str(df)+"\n\n\n"+memo_a+"\n\n\n"+"Punkte Präsentation+Inhalt: "+str(iv+pt)+"\n\n\n"+memo_b+"\n\n\n"+str(gesamt_punkte))


st.set_page_config(
    page_title="MA Prüfungsprotokoll",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="auto"
)

pruefer = [
    "Mario DÖLLER",
    "Michael KOHLEGGER",
    "Karsten BÖHM",
    "Johannes LÜTHI",
    "Lukas HUBER",
    "Lukas DEMETZ",
    "Robert KATHREIN",
    "Michael HECHT",
    "Julian BIALAS",
    "Dietmar MILLINGER",
    "Johannes LARCHER",
    "Johannes SPIESS"
]

with st.sidebar:

    st.header("Masterprüfung Dokumentation")

    st.subheader("Prüfungskandidat:in")

    fname = st.text_input("Vorname")
    lname = st.text_input("Nachname")
    ma = st.number_input("Punkte Masterarbeit",  step=1, max_value=100, min_value=60)

    st.subheader("Kommission")

    frag1_pruef = st.selectbox("Erstes Kommissionsmitglied", pruefer)
    frag2_pruef = st.selectbox("Zweites Kommissionsmitglied", pruefer)
    frag3_pruef = st.selectbox("Drittes Kommissionsmitglied", pruefer)

    button("Daten zwischenspeichern", on_click=safe_results, shortcut='Ctrl+Shift+S')
    st.link_button("MA-Formular im Intranet aufrufen", "https://intranet.fh-kufstein.ac.at/ba/ma-prufung")


tab1, tab2 = st.tabs(["Dokumentation", "Ergebnisse"])

with tab1:

    st.header(f"Dokumentation der Fragen")

    st.subheader("Präsentation der Masterarbeit")

    pt = st.slider('Präsentationstechnik', 0, 5, 5, 1)
    iv = st.slider('Inhaltsvermerk', 0, 5, 5, 1)

    frag1_ma = st.text_area(f"Fragen zur Masterarbeit P1: {frag1_pruef}")
    frag2_ma = st.text_area(f"Fragen zur Masterarbeit P2: {frag2_pruef}")
    frag3_ma = st.text_area(f"Fragen zur Masterarbeit P3: {frag3_pruef}")

    df = st.slider('Defensio', 0, 10, 10, 1)

    st.subheader(f"Dokumentation der allgemeinen Fragen")

    frag1_allg = st.text_area(f"Allgemeiner Fragenteil P1: {frag1_pruef}")
    frag1 = st.slider(f'Bewertung P1 ({frag1_pruef})', 0, 100, 50, 5) / 100

    frag2_allg = st.text_area(f"Allgemeiner Fragenteil P2: {frag2_pruef}")
    frag2 = st.slider(f'Bewertung P2 ({frag2_pruef})', 0, 100, 50, 5) / 100

    frag3_allg = st.text_area(f"Allgemeiner Fragenteil P3: {frag3_pruef}")
    frag3 = st.slider(f'Bewertung P3 ({frag3_pruef})', 0, 100, 50, 5) / 100

with tab2:

    st.header("Ergebnis")

    ma_anteil = ma * 0.4
    fragen_punkte = frag1*40/3+frag2*40/3+frag3*40/3
    memo_a = f"{frag1_pruef}: {frag1_ma}\n\n{frag2_pruef}: {frag2_ma}\n\n{frag3_pruef}: {frag3_ma}"
    memo_b = f"{frag1_pruef} ({frag1*100}%): {frag1_allg}\n\n{frag2_pruef} ({frag2*100}%): {frag2_allg}\n\n{frag3_pruef} ({frag3*100}%): {frag3_allg}"
    gesamt_punkte = ma_anteil + pt + iv + df + fragen_punkte

    st.text_input(
        label="Präsentationstechnik (wie – max. 5 Punkte)",
        value=f"{pt}",
        disabled=True
    )

    st.text_input(
        label="Inhaltsvermerk (was – max. 5 Punkte)",
        value=f"{iv}",
        disabled=True
    )

    st.text_input(
        label="Prüfungsgespräch, das auf die Querverbindungen des Themas der Masterarbeit zu den relevanten Fächern des Studienplans eingeht (max. 10 Punkte)",
        value=f"{df}",
        disabled=True
    )

    st.text_area(
        label="Bemerkung zur Defensio",
        value=memo_a,
        disabled=True
    )

    if st.button("Bemerkung zur Verteidigung kopieren"):
        copy(memo_a)


    st.text_input(
        label="Prüfungsgespräch über sonstige studienplanrelevante Inhalte (max. 40 Punkte)",
        value=f"{fragen_punkte}",
        disabled=True
    )

    st.text_area(
        label="Bemerkungen zum allgemeinen Fragenteil",
        value=memo_b,
        disabled=True
    )
    if st.button("Bemerkung zum allgemeinen Fragenteil kopieren"):
        copy(memo_b)

    st.text_input("Gesamtpunkte", f"{gesamt_punkte}", disabled=True)
