import streamlit as st
import matplotlib.pyplot as plt


def gewinnrechner(
    einkaufspreis: float,
    schattenpigment_menge: int,
    mystisches_pigment_menge: int,
    schattenpigment_preis: float,
    mystisches_pigment_preis: float,
    traumtinte_preis: float,
    sternentinte_preis: float,
    traumtinte_preis_vortag: float,
    sternentinte_preis_vortag: float
):
    # Direktverkauf Pigmente
    wert_pigmente = schattenpigment_menge * schattenpigment_preis + mystisches_pigment_menge * mystisches_pigment_preis
    gewinn_pigmente = wert_pigmente - einkaufspreis

    # Herstellung Tinten
    traumtinte_menge = schattenpigment_menge // 2
    sternentinte_menge = mystisches_pigment_menge // 2

    wert_traumtinte = traumtinte_menge * traumtinte_preis
    wert_sternentinte = sternentinte_menge * sternentinte_preis
    gesamtwert_tinten = wert_traumtinte + wert_sternentinte
    gewinn_tinten = gesamtwert_tinten - einkaufspreis

    # Tausch Traumtinte -> Sternentinte
    tauschbare_tinten = traumtinte_menge // 10
    rest_traumtinte_nach_tausch = traumtinte_menge % 10
    neue_sternentinte_anzahl = sternentinte_menge + tauschbare_tinten
    wert_neue_sternentinten = neue_sternentinte_anzahl * sternentinte_preis
    wert_rest_traumtinte = rest_traumtinte_nach_tausch * traumtinte_preis
    gesamtwert_tausch = wert_neue_sternentinten + wert_rest_traumtinte
    gewinn_tausch = gesamtwert_tausch - einkaufspreis

    # Szenario: Markt normalisiert sich
    wert_traumtinte_vortag = traumtinte_menge * traumtinte_preis_vortag
    wert_sternentinte_vortag = sternentinte_menge * sternentinte_preis_vortag
    gesamtwert_vortag = wert_traumtinte_vortag + wert_sternentinte_vortag
    gewinn_vortag = gesamtwert_vortag - einkaufspreis

    # Break-even Mengen berechnen
    schattenpigment_break_even = einkaufspreis / schattenpigment_preis if schattenpigment_preis else float('inf')
    mystisches_pigment_break_even = einkaufspreis / mystisches_pigment_preis if mystisches_pigment_preis else float('inf')
    traumtinte_break_even = einkaufspreis / traumtinte_preis if traumtinte_preis else float('inf')
    sternentinte_break_even = einkaufspreis / sternentinte_preis if sternentinte_preis else float('inf')

    return {
        "Direktverkauf Pigmente": round(gewinn_pigmente, 2),
        "Tintenherstellung (heute)": round(gewinn_tinten, 2),
        "Tausch zu Sternentinte": round(gewinn_tausch, 2),
        "Marktpreis normalisiert": round(gewinn_vortag, 2),
        "Break-even Schattenpigmente": round(schattenpigment_break_even, 2),
        "Break-even Mystische Pigmente": round(mystisches_pigment_break_even, 2),
        "Break-even Traumtinte": round(traumtinte_break_even, 2),
        "Break-even Sternentinte": round(sternentinte_break_even, 2)
    }


st.title("Tinten & Pigment Gewinnrechner")

# Eingabefelder
with st.form("input_form"):
    einkaufspreis = st.number_input("Einkaufspreis der Blumen", value=12536.0)
    schattenpigment_menge = st.number_input("Anzahl Schattenpigmente", value=1192, step=1)
    mystisches_pigment_menge = st.number_input("Anzahl Mystische Pigmente", value=122, step=1)
    schattenpigment_preis = st.number_input("Preis pro Schattenpigment", value=7.0)
    mystisches_pigment_preis = st.number_input("Preis pro Mystisches Pigment", value=93.0)
    traumtinte_preis = st.number_input("Aktueller Preis Traumtinte", value=13.88)
    sternentinte_preis = st.number_input("Aktueller Preis Sternentinte", value=120.0)
    traumtinte_preis_vortag = st.number_input("Preis Traumtinte (Vortag)", value=18.5)
    sternentinte_preis_vortag = st.number_input("Preis Sternentinte (Vortag)", value=185.0)
    submitted = st.form_submit_button("Berechnen")

if submitted:
    result = gewinnrechner(
        einkaufspreis,
        schattenpigment_menge,
        mystisches_pigment_menge,
        schattenpigment_preis,
        mystisches_pigment_preis,
        traumtinte_preis,
        sternentinte_preis,
        traumtinte_preis_vortag,
        sternentinte_preis_vortag
    )

    st.subheader("Ergebnisse")
    for szenario, gewinn in result.items():
        if "Break-even" in szenario:
            st.info(f"{szenario}: {gewinn} Stück nötig für 0 G Gewinn")
        else:
            color = "green" if gewinn > 0 else ("orange" if gewinn == 0 else "red")
            st.markdown(f"<span style='color:{color}'>{szenario}: {gewinn} G Gewinn</span>", unsafe_allow_html=True)

    # Diagramm
    st.subheader("Gewinnvergleich")
    fig, ax = plt.subplots()
    labels = [k for k in result if "Break-even" not in k]
    values = [result[k] for k in labels]
    ax.bar(labels, values)
    ax.set_ylabel("Gewinn in Gold")
    ax.set_title("Vergleich der Verkaufsmöglichkeiten")
    plt.xticks(rotation=15)
    st.pyplot(fig)
