import streamlit as st
import pandas as pd
import math


def gewinnrechner(
    einkaufspreis: float,
    traumtinte_menge: int,
    sternentinte_menge: int,
    traumtinte_preis: float,
    sternentinte_preis: float,
    traumtinte_preis_wunsch: float,
    sternentinte_preis_wunsch: float
):
    gesamte_tinten = traumtinte_menge + sternentinte_menge if (traumtinte_menge + sternentinte_menge) > 0 else 1
    anteil_traum = traumtinte_menge / gesamte_tinten
    anteil_stern = sternentinte_menge / gesamte_tinten
    kosten_traumtinte = einkaufspreis * anteil_traum
    kosten_sternentinte = einkaufspreis * anteil_stern

    traumtinte_umsatz = traumtinte_menge * traumtinte_preis
    gewinn_traumtinte = traumtinte_umsatz - kosten_traumtinte

    sternentinte_umsatz = sternentinte_menge * sternentinte_preis
    gewinn_sternentinte = sternentinte_umsatz - kosten_sternentinte

    traumtinte_umsatz_wunsch = traumtinte_menge * traumtinte_preis_wunsch
    gewinn_traumtinte_wunsch = traumtinte_umsatz_wunsch - kosten_traumtinte

    sternentinte_umsatz_wunsch = sternentinte_menge * sternentinte_preis_wunsch
    gewinn_sternentinte_wunsch = sternentinte_umsatz_wunsch - kosten_sternentinte

    gesamt_gewinn_aktuell = round(gewinn_traumtinte + gewinn_sternentinte, 2)
    gesamt_gewinn_wunsch = round(gewinn_traumtinte_wunsch + gewinn_sternentinte_wunsch, 2)
    break_even_traumtinte_preis_aktuell = sternentinte_preis / 10
    break_even_traumtinte_preis_wunsch = sternentinte_preis_wunsch / 10
    tausch_lohnt_aktuell = traumtinte_preis < break_even_traumtinte_preis_aktuell
    tausch_lohnt_wunsch = traumtinte_preis_wunsch < break_even_traumtinte_preis_wunsch

    return {
        "Gesamtgewinn (aktuelle Preise)": gesamt_gewinn_aktuell,
        "Gesamtgewinn (Wunschpreise)": gesamt_gewinn_wunsch,
        "Tausch lohnt sich aktuell": tausch_lohnt_aktuell,
        "Tausch lohnt sich bei Wunschpreis": tausch_lohnt_wunsch,
        "Tauschgrenze aktuell": round(break_even_traumtinte_preis_aktuell, 2),
        "Tauschgrenze Wunschpreis": round(break_even_traumtinte_preis_wunsch, 2),
        "Einkaufspreis insgesamt": einkaufspreis,
        "Zugewiesen an Traumtinte": round(kosten_traumtinte, 2),
        "Zugewiesen an Sternentinte": round(kosten_sternentinte, 2),
        "Traumtinte Umsatz": traumtinte_umsatz,
        "Gewinn mit direktem Verkauf von Traumtinte": round(gewinn_traumtinte, 2),
        "Sternentinte Umsatz": sternentinte_umsatz,
        "Gewinn bei Herstellung und Verkauf von Sternentinte": round(gewinn_sternentinte, 2),
        "Traumtinte Umsatz (Wunschpreis)": traumtinte_umsatz_wunsch,
        "Gewinn Traumtinte (Wunschpreis)": round(gewinn_traumtinte_wunsch, 2),
        "Sternentinte Umsatz (Wunschpreis)": sternentinte_umsatz_wunsch,
        "Gewinn Sternentinte (Wunschpreis)": round(gewinn_sternentinte_wunsch, 2)
    }


tab1, tab2 = st.tabs(["Tinten", "Geistereisenbolzen"])

with tab1:
    st.title("Tinten-Gewinnrechner – Fokus auf Traum- & Sternentinte")

    with st.form("input_form"):
        einkaufspreis = st.number_input("Gesamtkosten für Blumen", value=0.0)
        traumtinte_menge = st.number_input("Herstellbare Traumtinten", value=0, step=1)
        sternentinte_menge = st.number_input("Herstellbare Sternentinten", value=0, step=1)
        traumtinte_preis_wunsch = st.number_input("Wunschpreis Traumtinte", value=0.0, format="%.2f")
        sternentinte_preis_wunsch = st.number_input("Wunschpreis Sternentinte", value=0.0, format="%.2f")
        submitted = st.form_submit_button("Berechnen")

    if submitted:
        result = gewinnrechner(
            einkaufspreis,
            traumtinte_menge,
            sternentinte_menge,
                        traumtinte_preis_wunsch,
            sternentinte_preis_wunsch
        )

        st.subheader("Rechenweg & Ergebnisse")

        st.markdown("---")
        st.markdown("### 🌟 Wunschpreise (zukünftiger Marktwert)")
        st.markdown(f"**Traumtinte Umsatz (Wunschpreis):** {result['Traumtinte Umsatz (Wunschpreis)']} G")
        st.markdown("**Gewinn Traumtinte (Wunschpreis):** " + (f"<span style='color:green;font-weight:bold;'>{result['Gewinn Traumtinte (Wunschpreis)']} G</span>" if result['Gewinn Traumtinte (Wunschpreis)'] >= 0 else f"<span style='color:red;font-weight:bold;'>{result['Gewinn Traumtinte (Wunschpreis)']} G</span>"), unsafe_allow_html=True)
        st.markdown(f"**Sternentinte Umsatz (Wunschpreis):** {result['Sternentinte Umsatz (Wunschpreis)']} G")
        st.markdown("**Gesamtgewinn (Wunschpreise):** " + (f"<span style='color:green;font-weight:bold;'>{result['Gesamtgewinn (Wunschpreise)']} G</span>" if result['Gesamtgewinn (Wunschpreise)'] >= 0 else f"<span style='color:red;font-weight:bold;'>{result['Gesamtgewinn (Wunschpreise)']} G</span>"), unsafe_allow_html=True)
        st.markdown("**Gewinn Sternentinte (Wunschpreis):** " + (f"<span style='color:green;font-weight:bold;'>{result['Gewinn Sternentinte (Wunschpreis)']} G</span>" if result['Gewinn Sternentinte (Wunschpreis)'] >= 0 else f"<span style='color:red;font-weight:bold;'>{result['Gewinn Sternentinte (Wunschpreis)']} G</span>"), unsafe_allow_html=True)

        st.markdown("---")
        st.markdown(f"**🔁 Tauschgrenze aktuell:** {result['Tauschgrenze aktuell']} G")
        st.markdown(f"**🔁 Tauschgrenze bei Wunschpreis:** {result['Tauschgrenze Wunschpreis']} G")

        st.markdown("**📉 Tauschbewertung:**")

with tab2:
    st.markdown("""
        <style>
            [data-testid="stDataFrame"] div[role="grid"] {
                min-width: 100% !important;
                overflow-x: auto;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("Geistereisenbolzen-Rechner")

    with st.form("bolzen_form"):
        bolzen_menge = st.number_input("🔩 Anzahl herstellbarer Bolzen", min_value=0, step=1)
        barren_preis = st.number_input("🪙 Preis pro Geistereisenbarren", value=0.0, format="%.2f")
        erz_preis = st.number_input("💎 Preis pro Geistererz", value=0.0, format="%.2f")
        bolzen_preis_aktuell = st.number_input("📈 Marktpreis je Bolzen", value=0.0, format="%.2f")
        bolzen_preis_wunsch = st.number_input("🌟 Wunschpreis je Bolzen", value=0.0, format="%.2f")
        submitted_bolzen = st.form_submit_button("Berechnen")

    if submitted_bolzen and bolzen_menge > 0:
        # Erz-Variante
        benötigte_erz = math.ceil(((bolzen_menge / 2) * 3 * 2) / 2) * 2  # 3 Barren pro 2 Bolzen, 1 Barren = 2 Erz
        kosten_erz = benötigte_erz * erz_preis
        umsatz_erz_aktuell = bolzen_menge * bolzen_preis_aktuell
        umsatz_erz_wunsch = bolzen_menge * bolzen_preis_wunsch
        gewinn_erz_aktuell = umsatz_erz_aktuell - kosten_erz
        gewinn_erz_wunsch = umsatz_erz_wunsch - kosten_erz

        # Barren-Variante
        benötigte_barren = math.ceil(((bolzen_menge / 2) * 3) / 3) * 3
        kosten_barren = benötigte_barren * barren_preis
        umsatz_barren_aktuell = bolzen_menge * bolzen_preis_aktuell
        umsatz_barren_wunsch = bolzen_menge * bolzen_preis_wunsch
        gewinn_barren_aktuell = umsatz_barren_aktuell - kosten_barren
        gewinn_barren_wunsch = umsatz_barren_wunsch - kosten_barren

        df = pd.DataFrame({
            'Variante': ['🪙 Barren', '💎 Erz'],
            'Gesamtkosten (G)': [kosten_barren, kosten_erz],
            'Umsatz (Marktpreis)': [umsatz_barren_aktuell, umsatz_erz_aktuell],
            'Gewinn (Marktpreis)': [gewinn_barren_aktuell, gewinn_erz_aktuell],
            'Umsatz (Wunschpreis)': [umsatz_barren_wunsch, umsatz_erz_wunsch],
            'Gewinn (Wunschpreis)': [gewinn_barren_wunsch, gewinn_erz_wunsch]
        })

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🪙 Barren-Variante")
            st.markdown(f"**Benötigte Barren:** {benötigte_barren}")
            st.markdown(f"**Gesamtkosten:** {kosten_barren:.2f} G")
            st.markdown(f"**Umsatz (Marktpreis):** {umsatz_barren_aktuell:.2f} G")
            st.markdown("**Gewinn (Marktpreis):** " + (f"<span style='color:green;font-weight:bold;'>{gewinn_barren_aktuell:.2f} G</span>" if gewinn_barren_aktuell >= 0 else f"<span style='color:red;font-weight:bold;'>{gewinn_barren_aktuell:.2f} G</span>"), unsafe_allow_html=True)
            st.markdown(f"**Umsatz (Wunschpreis):** {umsatz_barren_wunsch:.2f} G")
            st.markdown("**Gewinn (Wunschpreis):** " + (f"<span style='color:green;font-weight:bold;'>{gewinn_barren_wunsch:.2f} G</span>" if gewinn_barren_wunsch >= 0 else f"<span style='color:red;font-weight:bold;'>{gewinn_barren_wunsch:.2f} G</span>"), unsafe_allow_html=True)

        with col2:
            st.markdown("### 💎 Erz-Variante")
            st.markdown(f"**Benötigte Erze:** {benötigte_erz}")
            st.markdown(f"**Gesamtkosten:** {kosten_erz:.2f} G")
            st.markdown(f"**Umsatz (Marktpreis):** {umsatz_erz_aktuell:.2f} G")
            st.markdown("**Gewinn (Marktpreis):** " + (f"<span style='color:green;font-weight:bold;'>{gewinn_erz_aktuell:.2f} G</span>" if gewinn_erz_aktuell >= 0 else f"<span style='color:red;font-weight:bold;'>{gewinn_erz_aktuell:.2f} G</span>"), unsafe_allow_html=True)
            st.markdown(f"**Umsatz (Wunschpreis):** {umsatz_erz_wunsch:.2f} G")
            st.markdown("**Gewinn (Wunschpreis):** " + (f"<span style='color:green;font-weight:bold;'>{gewinn_erz_wunsch:.2f} G</span>" if gewinn_erz_wunsch >= 0 else f"<span style='color:red;font-weight:bold;'>{gewinn_erz_wunsch:.2f} G</span>"), unsafe_allow_html=True)
