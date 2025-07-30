import streamlit as st
import pandas as pd
import math


def gewinnrechner(
    einkaufspreis: float,
    traumtinte_menge: int,
    sternentinte_menge: int,
    traumtinte_preis_wunsch: float,
    sternentinte_preis_wunsch: float
):
    gesamte_tinten = traumtinte_menge + sternentinte_menge if (traumtinte_menge + sternentinte_menge) > 0 else 1
    anteil_traum = traumtinte_menge / gesamte_tinten
    anteil_stern = sternentinte_menge / gesamte_tinten
    kosten_traumtinte = einkaufspreis * anteil_traum
    kosten_sternentinte = einkaufspreis * anteil_stern

    traumtinte_umsatz_wunsch = traumtinte_menge * traumtinte_preis_wunsch
    gewinn_traumtinte_wunsch = traumtinte_umsatz_wunsch - kosten_traumtinte

    sternentinte_umsatz_wunsch = sternentinte_menge * sternentinte_preis_wunsch
    gewinn_sternentinte_wunsch = sternentinte_umsatz_wunsch - kosten_sternentinte

    gesamt_gewinn_wunsch = round(gewinn_traumtinte_wunsch + gewinn_sternentinte_wunsch, 2)
    break_even_traumtinte_preis_wunsch = sternentinte_preis_wunsch / 10
    tausch_lohnt_wunsch = traumtinte_preis_wunsch < break_even_traumtinte_preis_wunsch

    return {
        "Gesamtgewinn (Wunschpreise)": gesamt_gewinn_wunsch,
        "Tausch lohnt sich bei Wunschpreis": tausch_lohnt_wunsch,
        "Tauschgrenze Wunschpreis": round(break_even_traumtinte_preis_wunsch, 2),
        "Einkaufspreis insgesamt": einkaufspreis,
        "Zugewiesen an Traumtinte": round(kosten_traumtinte, 2),
        "Zugewiesen an Sternentinte": round(kosten_sternentinte, 2),
        "Traumtinte Umsatz (Wunschpreis)": traumtinte_umsatz_wunsch,
        "Gewinn Traumtinte (Wunschpreis)": round(gewinn_traumtinte_wunsch, 2),
        "Sternentinte Umsatz (Wunschpreis)": sternentinte_umsatz_wunsch,
        "Gewinn Sternentinte (Wunschpreis)": round(gewinn_sternentinte_wunsch, 2)
    }


st.set_page_config(layout="wide")
tab1, tab2 = st.tabs(["🧪 Tinten Gewinnrechner", "🔩 Geistereisenbolzen"])

with tab1:
    st.header("🧪 Tinten Gewinnrechner")

    with st.form("input_form"):
        einkaufspreis = st.number_input("Gesamtkosten für Blumen", value=0.0, format="%.2f")
        traumtinte_menge = st.number_input("Herstellbare Traumtinten", min_value=0, value=0)
        sternentinte_menge = st.number_input("Herstellbare Sternentinten", min_value=0, value=0)
        traumtinte_preis_wunsch = st.number_input("Wunschpreis pro Traumtinte", value=0.0, format="%.2f")
        sternentinte_preis_wunsch = st.number_input("Wunschpreis pro Sternentinte", value=0.0, format="%.2f")
        submitted = st.form_submit_button("Berechne Gewinn")

    if submitted:
        result = gewinnrechner(
            einkaufspreis,
            traumtinte_menge,
            sternentinte_menge,
            traumtinte_preis_wunsch,
            sternentinte_preis_wunsch
        )

        st.subheader("📊 Auswertung")

        st.markdown(f"**💰 Gesamtgewinn (Wunschpreise):** ")
        if result['Gesamtgewinn (Wunschpreise)'] >= 0:
            st.markdown(f"<span style='color:green;font-weight:bold;'>{result['Gesamtgewinn (Wunschpreise)']} G</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:red;font-weight:bold;'>{result['Gesamtgewinn (Wunschpreise)']} G</span>", unsafe_allow_html=True)

        st.markdown(f"**🔁 Tauschgrenze Wunschpreis:** {result['Tauschgrenze Wunschpreis']} G")
        tausch_text = "✅ **Tausch lohnt sich**" if result['Tausch lohnt sich bei Wunschpreis'] else "❌ **Tausch lohnt sich nicht**"
        st.markdown(tausch_text)

        st.markdown("---")
        st.markdown(f"**📦 Einkaufspreis insgesamt:** {result['Einkaufspreis insgesamt']} G")
        st.markdown(f"**🔹 Zugewiesen an Traumtinte:** {result['Zugewiesen an Traumtinte']} G")
        st.markdown(f"**🔸 Zugewiesen an Sternentinte:** {result['Zugewiesen an Sternentinte']} G")

        st.markdown("---")
        st.markdown(f"**🔹 Traumtinte Umsatz (Wunschpreis):** {result['Traumtinte Umsatz (Wunschpreis)']} G")
        st.markdown(f"**🔹 Gewinn Traumtinte (Wunschpreis):** {result['Gewinn Traumtinte (Wunschpreis)']} G")

        st.markdown(f"**🔸 Sternentinte Umsatz (Wunschpreis):** {result['Sternentinte Umsatz (Wunschpreis)']} G")
        st.markdown(f"**🔸 Gewinn Sternentinte (Wunschpreis):** {result['Gewinn Sternentinte (Wunschpreis)']} G")


with tab2:
    st.header("🔩 Geistereisenbolzen-Auswertung")
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
