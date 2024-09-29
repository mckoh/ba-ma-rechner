import streamlit as st
from streamlit_shortcuts import button
from pyperclip import copy
from datetime import datetime as dt

time_now = dt.strftime(dt.now(), "%Y-%m-%d_%H-%M")

def safe_results():
    with open(f"{time_now}___BA-Prüfungsprotokoll__{lname}_{fname}.backup", "w", encoding="utf-8") as f:
        f.write("Punkte Verteidigung: "+str(ba_punkte)+"\n\n\n"+memo_a+"\n\n\n"+"Punkte Querverbindungen: "+str(fragen_punkte)+"\n\n\n"+memo_b+"\n\n\n"+str(gesamt_punkte))

st.set_page_config(
    page_title="BA Prüfungsprotokoll",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="auto"
)

pruefer = [
    "Mario DÖLLER",
    "Michael KOHLEGGER",
    "Karsten BÖHM",
    "Johannes LÜTHI",
    "Lukas DEMETZ",
    "Robert KATHREIN",
    "Julian BIALAS",
    "Johannes LARCHER",
    "Carmen SOMMER",
    "Thomas STRÖHLE",
    "Johannes RIEDER"
]

with st.sidebar:

    st.header("Masterprüfung Dokumentation")

    st.subheader("Prüfungskandidat:in")

    fname = st.text_input("Vorname")
    lname = st.text_input("Nachname")

    st.subheader("Kommission")

    frag1_pruef = st.selectbox("Erstes Kommissionsmitglied", pruefer)
    frag2_pruef = st.selectbox("Zweites Kommissionsmitglied", pruefer)
    frag3_pruef = st.selectbox("Drittes Kommissionsmitglied", pruefer)

    button("Daten zwischenspeichern", on_click=safe_results, shortcut='Ctrl+Shift+S')
    st.link_button("MA-Formular im Intranet aufrufen", "https://intranet.fh-kufstein.ac.at/ba/ma-prufung")


tab1, tab2 = st.tabs(["Dokumentation", "Ergebnisse"])

with tab1:

    st.header("Vorstellung der Bachelorarbeit")

    frag1_ba = st.text_area(f"Prüfer(in) DEF-1: {frag1_pruef}")
    frag2_ba = st.text_area(f"Prüfer(in) DEF-2: {frag2_pruef}")
    frag3_ba = st.text_area(f"Prüfer(in) DEF-3: {frag3_pruef}")

    ba_punkte = st.slider('Vorstellung + Verteidigung BA', 0, 30, 20, 1)

    st.header(f"Dokumentation der Fragen im Querverbindungsteil")

    frag1_quer = st.text_area(f"Prüfer(in) QUER-1: {frag1_pruef}")
    frag1 = st.slider(f'Bewertung 1 ({frag1_pruef})', 0, 100, 50, 5) / 100

    frag2_quer = st.text_area(f"Prüfer(in) QUER-2: {frag2_pruef}")
    frag2 = st.slider(f'Bewertung 2 ({frag2_pruef})', 0, 100, 50, 5) / 100

    frag3_quer = st.text_area(f"Prüfer(in) QUER-3: {frag3_pruef}")
    frag3 = st.slider(f'Bewertung 3 ({frag3_pruef})', 0, 100, 50, 5) / 100

with tab2:

    st.header("Ergebnis")

    fragen_punkte = frag1*70/3+frag2*70/3+frag3*70/3
    memo_a = f"{frag1_pruef}: {frag1_ba}\n\n{frag2_pruef}: {frag2_ba}\n\n{frag3_pruef}: {frag3_ba}"
    memo_b = f"{frag1_pruef} ({frag1*100}%): {frag1_quer}\n\n{frag2_pruef} ({frag2*100}%): {frag2_quer}\n\n{frag3_pruef} ({frag3*100}%): {frag3_quer}"
    gesamt_punkte = ba_punkte + fragen_punkte

    st.text_input(
        label="Punkte Vorstellung und Verteidigung",
        value=f"{ba_punkte}",
        disabled=True
    )

    st.text_area(
        label="Dokumentation zur Verteidigung",
        value=memo_a,
        disabled=True
    )

    if st.button("Dokumentation zur Verteidigung kopieren"):
        copy(memo_a)

    st.text_input(
        label="Punkte Fragenteil",
        value=f"{fragen_punkte}",
        disabled=True
    )

    st.text_area(
        label="Dokumentation Fragenteil",
        value=memo_b,
        disabled=True
    )
    if st.button("Copy Fragenteil Memo"):
        copy(memo_b)

    st.text_input(
        "Gesamtpunkte",
        f"{gesamt_punkte}",
        disabled=True
    )
