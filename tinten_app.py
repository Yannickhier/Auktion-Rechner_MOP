import streamlit as st


def gewinnrechner(
    einkaufspreis: float,
    traumtinte_menge: int,
    sternentinte_menge: int,
    traumtinte_preis: float,
    sternentinte_preis: float,
    traumtinte_preis_wunsch: float,
    sternentinte_preis_wunsch: float
):
    # Rechenweg Traumtinte
    traumtinte_umsatz = traumtinte_menge * traumtinte_preis
    gewinn_traumtinte = traumtinte_umsatz - einkaufspreis

    # Rechenweg Sternentinte
    sternentinte_umsatz = sternentinte_menge * sternentinte_preis
    gewinn_sternentinte = sternentinte_umsatz - einkaufspreis

    # Rechenweg mit Wunschpreisen
    traumtinte_umsatz_wunsch = traumtinte_menge * traumtinte_preis_wunsch
    gewinn_traumtinte_wunsch = traumtinte_umsatz_wunsch - einkaufspreis

    sternentinte_umsatz_wunsch = sternentinte_menge * sternentinte_preis_wunsch
    gewinn_sternentinte_wunsch = sternentinte_umsatz_wunsch - einkaufspreis

    # Ab welchem Traumtinte-Preis lohnt sich der Tausch nicht mehr
    break_even_traumtinte_preis = sternentinte_preis / 10

    return {
        "Einkaufspreis": einkaufspreis,
        "Traumtinte Umsatz": traumtinte_umsatz,
        "Gewinn mit direktem Verkauf von Traumtinte": round(gewinn_traumtinte, 2),
        "Sternentinte Umsatz": sternentinte_umsatz,
        "Gewinn bei Herstellung und Verkauf von Sternentinte": round(gewinn_sternentinte, 2),
        "Traumtinte Umsatz (Wunschpreis)": traumtinte_umsatz_wunsch,
        "Gewinn Traumtinte (Wunschpreis)": round(gewinn_traumtinte_wunsch, 2),
        "Sternentinte Umsatz (Wunschpreis)": sternentinte_umsatz_wunsch,
        "Gewinn Sternentinte (Wunschpreis)": round(gewinn_sternentinte_wunsch, 2),
        "Tausch lohnt sich, wenn Traumtinte unter": round(break_even_traumtinte_preis, 2)
    }


st.title("Tinten-Gewinnrechner – Fokus auf Traum- & Sternentinte")

with st.form("input_form"):
    einkaufspreis = st.number_input("Gesamtkosten für Blumen", value=0.0)
    traumtinte_menge = st.number_input("Herstellbare Traumtinten", value=0, step=1)
    sternentinte_menge = st.number_input("Herstellbare Sternentinten", value=0, step=1)
    traumtinte_preis = st.number_input("Aktueller Preis Traumtinte", value=0.0, format="%.2f")
    sternentinte_preis = st.number_input("Aktueller Preis Sternentinte", value=0.0, format="%.2f")
    traumtinte_preis_wunsch = st.number_input("Wunschpreis Traumtinte", value=0.0, format="%.2f")
    sternentinte_preis_wunsch = st.number_input("Wunschpreis Sternentinte", value=0.0, format="%.2f")
    submitted = st.form_submit_button("Berechnen")

if submitted:
    result = gewinnrechner(
        einkaufspreis,
        traumtinte_menge,
        sternentinte_menge,
        traumtinte_preis,
        sternentinte_preis,
        traumtinte_preis_wunsch,
        sternentinte_preis_wunsch
    )

    st.subheader("Rechenweg & Ergebnisse")
    for key, val in result.items():
        st.markdown(f"**{key}:** {val} G")
