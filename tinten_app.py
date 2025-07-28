import streamlit as st


def gewinnrechner(
    einkaufspreis: float,
    traumtinte_menge: int,
    traumtinte_preis: float,
    sternentinte_preis: float
):
    # Gewinne berechnen
    gewinn_traumtinte = traumtinte_menge * traumtinte_preis - einkaufspreis
    getauschte_sternentinte = traumtinte_menge // 10
    rest_traumtinte = traumtinte_menge % 10
    wert_getauscht = getauschte_sternentinte * sternentinte_preis + rest_traumtinte * traumtinte_preis
    gewinn_durch_tausch = wert_getauscht - einkaufspreis

    # Ab welchem Traumtinte-Preis lohnt sich der Tausch nicht mehr
    break_even_traumtinte_preis = sternentinte_preis / 10

    return {
        "Gewinn mit direktem Verkauf von Traumtinte": round(gewinn_traumtinte, 2),
        "Herstellbare Sternentinten (durch Tausch)": getauschte_sternentinte,
        "Gewinn bei Tausch in Sternentinte": round(gewinn_durch_tausch, 2),
        "Tausch lohnt sich, wenn Traumtinte unter": round(break_even_traumtinte_preis, 2)
    }


st.title("Tinten-Gewinnrechner – Fokus auf Traum- & Sternentinte")

with st.form("input_form"):
    einkaufspreis = st.number_input("Gesamtkosten für Blumen", value=12536.0)
    traumtinte_menge = st.number_input("Herstellbare Traumtinten", value=596, step=1)
    traumtinte_preis = st.number_input("Aktueller Preis Traumtinte", value=13.88)
    sternentinte_preis = st.number_input("Aktueller Preis Sternentinte", value=120.0)
    submitted = st.form_submit_button("Berechnen")

if submitted:
    result = gewinnrechner(
        einkaufspreis,
        traumtinte_menge,
        traumtinte_preis,
        sternentinte_preis
    )

    for key, val in result.items():
        st.markdown(f"**{key}:** {val}{' G' if isinstance(val, (int, float)) and 'Tinte' not in key else ''}")
