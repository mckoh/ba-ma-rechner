import streamlit as st

st.set_page_config(
    page_title="WEBTA Lehre-Werkzeuge",
    page_icon="🧰",
    initial_sidebar_state="auto"
)

st.title("Willkommen")

st.markdown("Von dieser Startseite aus können die einzelnen Werkzeuge erreicht werden. Verwende die **Navigation links**, um zwischen den einzelnen Seiten zu wechseln. Achtung: Beim Verlassen der Seite wird deren Inhalt verworfen.")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.image("static/ba_rechner.png", caption="BA Rechner")

with col2:
    st.image("static/ma_rechner.png", caption="MA Rechner")

st.header("Rechtliche Rahmenbedingungen")

st.subheader("Bachelor-/Masterprüfung im FHG")

text = """§ 16. (1) Die einen Fachhochschul-Bachelorstudiengang abschließende Gesamtprüfung gemäß § 3 Abs. 2 Z 6 ist als kommissionelle Prüfung vor einem facheinschlägigen Prüfungssenat abzulegen. Die Prüfung setzt sich aus den Prüfungsteilen: (a) Prüfungsgespräch über die durchgeführten Bachelorarbeiten sowie, (b) deren Querverbindungen zu relevanten Fächern des Studienplans zusammen.

§ 16. (2) Die einen Fachhochschul-Masterstudiengang abschließende Gesamtprüfung gemäß § 3 Abs. 2 Z 6 ist als kommissionelle Prüfung vor einem facheinschlägigen Prüfungssenat abzulegen. Die Prüfung setzt sich aus den Prüfungsteilen (a) Präsentation der Masterarbeit, (b) einem Prüfungsgespräch, das auf die Querverbindungen des Themas der Diplom- oder Masterarbeit zu den relevanten Fächern des Studienplans eingeht, sowie (c) einem Prüfungsgespräch über sonstige studienplanrelevante Inhalte zusammen.

§ 16. (3) Die Studierenden sind in geeigneter Weise über die Zulassung zu den kommissionellen Prüfungen zu verständigen.

§ 16. (4) Die Beurteilungskriterien und Ergebnisse der Leistungsbeurteilung der kommissionellen Prüfungen sind den Studierenden mitzuteilen.

§ 16. (5) Die Prüfungskommission besteht aus dem Kreis aller für die kommissionellen Prüfungen in Frage kommenden Personen. Der Prüfungssenat setzt sich aus den Prüferinnen und Prüfern je Kandidatin oder Kandidat zusammen."""

st.markdown(text)

st.subheader("Bachelorprüfung in der ASPO")

text = """Die einen Fachhochschul-Bachelorstudiengang abschließende Gesamtprüfung gemäß § 3 Abs. 2 Z 6 FHG ist als kommissionelle Prüfung vor einem facheinschlägigen Prüfungssenat abzulegen.

(1) Die Prüfungskommission setzt sich aus allen für die Durchführung der kommissionellen Prüfung in Frage kommenden Personen aus dem Kreis der haupt- und nebenberuflich Lehrenden des Lehrpersonals des Studiengangs zusammen. Aus dieser Kommission wird der Prüfungssenat gebildet.

(2) Die abschließende Prüfung des Bachelorstudiengangs besteht aus einer mündlichen Prüfung vor einem facheinschlägigen Prüfungssenat. Der Prüfungssenat setzt sich aus drei Personen aus dem Kreis der Prüfungskommission zusammen, einer davon ist in der Regel die Betreuungsperson. Die Mitglieder des Prüfungssenats werden von der Studiengangsleitung ausgewählt. Über die Prüfung wird Protokoll geführt.

(3) Zur abschließenden Gesamtprüfung werden nur diejenigen Studierenden zugelassen, die alle Prüfungen sowie die Bachelorarbeit des Studiums positiv absolviert haben. Die Kandidaten werden in jedem Fall rechtzeitig schriftlich über die Zulassung zur kommissionellen Prüfung in Kenntnis gesetzt.

(4) Die kommissionelle Prüfung setzt sich aus einem Prüfungsgespräch über die durchgeführte Bachelorarbeit sowie deren Querverbindungen zu relevanten Fächern des Curriculums zusammen.

- Prüfungsgespräch über die durchgeführte Bachelorarbeit (Anteil an der Gesamtbeurteilung: 30 %)
- Querverbindungen der Bachelorarbeit zu relevanten Fächern des Curriculums (Anteil an der Gesamtbeurteilung: 70 %)

Insgesamt dauert die Prüfung mindestens 20 Minuten.

(5) Für die Benotung wird folgendes Schema herangezogen, wobei auf ganze Prozentsätze kaufmännisch auf- bzw. abzurunden ist.
- Ab 90 %: „Mit ausgezeichnetem Erfolg bestanden“
- Ab 80 %, unter 90 %: „Mit gutem Erfolg bestanden“
- Ab 60 %, unter 80 %: „Bestanden“
- Unter 60 %: „Nicht bestanden“

(6) Bei Nichtbestehen kann die kommissionelle Bachelorprüfung zwei Mal wiederholt werden (siehe Kapitel 1.6)."""

st.markdown(text)

st.subheader("Masterprüfung in der ASPO")

text = """4.3 Abschließende Gesamtprüfung für Masterstudiengänge Die einen Fachhochschul-Masterstudiengang abschließende Gesamtprüfung gemäß § 3 Abs. 2 Z 6 FHG ist als kommissionelle Prüfung vor einem facheinschlägigen Prüfungssenat abzulegen.

(1) Zum kommissionellen Teil der Masterprüfung sind nur diejenigen Kandidat:innen zuzulassen, die alle relevanten Prüfungen des Studiums positiv absolviert haben und deren Masterarbeit von beiden Gutachter:innen positiv bewertet wurde. Die Kandidat:innen sind rechtzeitig, in der Regel mindestens 2 Wochen vor der kommissionellen Masterprüfung, schriftlich über die Zulassung zum kommissionellen Teil der Masterprüfung zu informieren.

(2) Der kommissionelle Teil der Masterprüfung ist eine mündliche, fächerübergreifende Prüfung. Sie ist
öffentlich zugänglich. Die kommissionelle Prüfung wird von einem facheinschlägigen kompetenten Prüfungssenat aus dem Kreis der Prüfungskommission abgehalten.

(3) Die Prüfungskommission setzt sich aus allen für die Durchführung der kommissionellen Prüfung in
Frage kommenden Personen aus dem Kreis der haupt- und nebenberuflich Lehrenden des Lehrkörpers
des jeweiligen Fachhochschul-Masterstudiengangs zusammen. Aus dieser Kommission wird der Prüfungssenat gebildet.

(4) Der Prüfungssenat setzt sich aus mindestens drei Personen zusammen. Die Mitglieder des Prüfungssenats sind von der Studiengangsleitung auszuwählen.

(5) Die kommissionelle Prüfung umfasst

- die Präsentation und Defensio der Masterarbeit (gewichtet mit 20 %),
- ein Prüfungsgespräch, das auf Querverbindungen des Themas und des Inhalts der Masterarbeit

zu den relevanten Fächern des Studienplans eingeht, sowie ein Prüfungsgespräch über sonstige studienplanrelevante Inhalte (gewichtet mit insgesamt 40 %), und dauert mindestens 45 Minuten. Die Masterarbeit und der kommissionelle Teil der Masterprüfung werden zunächst nach dem für Prüfungsleistungen vorgesehenen Punktesystem beurteilt, wobei die Masterarbeit mit 40 % und die kommissionelle Prüfung mit insgesamt 60 % gewichtet werden. Die sich daraus ergebenden Gesamtpunkte werden in einem zweiten Schritt in das für die Beurteilung der Masterprüfung vorgesehene Notensystem überführt.

(6) Die Beratung und Abstimmung über das Ergebnis des kommissionellen Teils der Masterprüfung haben in nicht öffentlicher Sitzung des Prüfungssenats zu erfolgen.

(7) Falls die Prüfung nicht bestanden wurde, sind dem:der Prüfungskandidat:in die Gründe hierfür bekannt zu geben.

(8) Für die Benotung wird dabei folgendes Schema herangezogen, wobei auf ganze Prozentsätze kaufmännisch auf- bzw. abzurunden ist.
- Ab 90 %: „Mit ausgezeichnetem Erfolg bestanden“
- Ab 80 %, unter 90 %: „Mit gutem Erfolg bestanden“
- Ab 60 %, unter 80 %: „Bestanden“
- Unter 60 %: „Nicht bestanden“

(9) Die Masterprüfung gilt nur dann als bestanden, wenn beide Prüfungsteile (Masterarbeit und kommissionelle Masterprüfung) jeweils bestanden wurden.

(10) Nicht bestandene kommissionelle Masterprüfungen können zwei Mal wiederholt werden (siehe Kapitel 1.6)"""

st.markdown(text)