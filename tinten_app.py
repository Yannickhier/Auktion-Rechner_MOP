import streamlit as st


def gewinnrechner(
    einkaufspreis: float,
    traumtinte_menge: int,
    sternentinte_menge: int,
    traumtinte_preis: float,
    sternentinte_preis: float,
    traumtinte_preis_vortag: float,
    sternentinte_preis_vortag: float
):
    # Gewinne berechnen
    gewinn_traumtinte = traumtinte_menge * traumtinte_preis - einkaufspreis
    gewinn_sternentinte = sternentinte_menge * sternentinte_preis - einkaufspreis

    # Gewinne mit Vortagespreisen
    gewinn_traumtinte_vortag = traumtinte_menge * traumtinte_preis_vortag - einkaufspreis
    gewinn_sternentinte_vortag = sternentinte_menge * sternentinte_preis_vortag - einkaufspreis

    # Ab welchem Traumtinte-Preis lohnt sich der Tausch nicht mehr
    break_even_traumtinte_preis = sternentinte_preis / 10

    return {
        "Gewinn mit direktem Verkauf von Traumtinte": round(gewinn_traumtinte, 2),
        "Gewinn bei Herstellung und Verkauf von Sternentinte": round(gewinn_sternentinte, 2),
        "Gewinn Traumtinte (Vortagspreis)": round(gewinn_traumtinte_vortag, 2),
        "Gewinn Sternentinte (Vortagspreis)": round(gewinn_sternentinte_vortag, 2),
        "Tausch lohnt sich, wenn Traumtinte unter": round(break_even_traumtinte_preis, 2)
    }


st.title("Tinten-Gewinnrechner – Fokus auf Traum- & Sternentinte")

with st.form("input_form"):
    einkaufspreis = st.number_input("Gesamtkosten für Blumen", value=12536.0)
    traumtinte_menge = st.number_input("Herstellbare Traumtinten", value=596, step=1)
    sternentinte_menge = st.number_input("Herstellbare Sternentinten", value=61, step=1)
    traumtinte_preis = st.number_input("Aktueller Preis Traumtinte", value=13.88)
    sternentinte_preis = st.number_input("Aktueller Preis Sternentinte", value=120.0)
    traumtinte_preis_vortag = st.number_input("Vortagespreis Traumtinte", value=18.5)
    sternentinte_preis_vortag = st.number_input("Vortagespreis Sternentinte", value=185.0)
    submitted = st.form_submit_button("Berechnen")

if submitted:
    result = gewinnrechner(
        einkaufspreis,
        traumtinte_menge,
        sternentinte_menge,
        traumtinte_preis,
        sternentinte_preis,
        traumtinte_preis_vortag,
        sternentinte_preis_vortag
    )

    for key, val in result.items():
        st.markdown(f"**{key}:** {val}{' G' if isinstance(val, (int, float)) and 'Tinte' not in key else ''}")
