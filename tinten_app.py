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

        st.markdown("### 📊 Aktuelle Marktpreise")
        st.markdown(f"**Einkaufspreis insgesamt:** {result['Einkaufspreis insgesamt']} G")
        st.markdown(f"**Zugewiesen an Traumtinte:** {result['Zugewiesen an Traumtinte']} G")
        st.markdown(f"**Zugewiesen an Sternentinte:** {result['Zugewiesen an Sternentinte']} G")
        st.markdown(f"**Traumtinte Umsatz:** {result['Traumtinte Umsatz']} G")
        st.markdown("**Gewinn mit direktem Verkauf von Traumtinte:** " + (f"<span style='color:green;font-weight:bold;'>{result['Gewinn mit direktem Verkauf von Traumtinte']} G</span>" if result['Gewinn mit direktem Verkauf von Traumtinte'] >= 0 else f"<span style='color:red;font-weight:bold;'>{result['Gewinn mit direktem Verkauf von Traumtinte']} G</span>"), unsafe_allow_html=True)
        st.markdown(f"**Sternentinte Umsatz:** {result['Sternentinte Umsatz']} G")
        st.markdown("**Gewinn bei Herstellung und Verkauf von Sternentinte:** " + (f"<span style='color:green;font-weight:bold;'>{result['Gewinn bei Herstellung und Verkauf von Sternentinte']} G</span>" if result['Gewinn bei Herstellung und Verkauf von Sternentinte'] >= 0 else f"<span style='color:red;font-weight:bold;'>{result['Gewinn bei Herstellung und Verkauf von Sternentinte']} G</span>"), unsafe_allow_html=True)

        st.markdown("**Gesamtgewinn (aktuelle Preise):** " + (f"<span style='color:green;font-weight:bold;'>{result['Gesamtgewinn (aktuelle Preise)']} G</span>" if result['Gesamtgewinn (aktuelle Preise)'] >= 0 else f"<span style='color:red;font-weight:bold;'>{result['Gesamtgewinn (aktuelle Preise)']} G</span>"), unsafe_allow_html=True)

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
        st.markdown(f"Aktueller Preis ({traumtinte_preis} G): {'✅ Ja' if result['Tausch lohnt sich aktuell'] else '❌ Nein'}")
        st.markdown(f"Wunschpreis ({traumtinte_preis_wunsch} G): {'✅ Ja' if result['Tausch lohnt sich bei Wunschpreis'] else '❌ Nein'}")


with tab2:
    st.title("Geistereisenbolzen Rechner")

    with st.form("bolzen_form"):
        erz_preis = st.number_input("💎 Aktueller Preis pro Geistererz", value=0.0, format="%.2f")
        barren_kaufpreis = st.number_input("🪙 Kaufpreis pro Geistereisenbarren", value=0.0, format="%.2f")
        # Hinweis: effektiver_barrenpreis wird nicht mehr verwendet, beide Varianten werden separat ausgewertet
        bolzen_marktpreis = st.number_input("💰 Aktueller Verkaufspreis pro Bolzen", value=0.0, format="%.2f")
        bolzen_wunschpreis = st.number_input("⭐ Wunschpreis pro Bolzen", value=0.0, format="%.2f")
        bolzen_menge = st.number_input("🔧 Geplante Anzahl Bolzen, die du herstellen willst", value=0, step=1)
        submit_bolzen = st.form_submit_button("Bolzen-Kalkulation starten")

    if submit_bolzen:
        barren_pro_bolzen = 1.5
        menge_erforderlich = bolzen_menge * barren_pro_bolzen

        # Variante 1: Barren
        kosten_barren = menge_erforderlich * barren_kaufpreis
        umsatz_aktuell_barren = bolzen_menge * bolzen_marktpreis
        umsatz_wunsch_barren = bolzen_menge * bolzen_wunschpreis
        gewinn_aktuell_barren = round(umsatz_aktuell_barren - kosten_barren, 2)
        gewinn_wunsch_barren = round(umsatz_wunsch_barren - kosten_barren, 2)

        # Variante 2: Erz
        barren_aus_erz = menge_erforderlich
        benoetigte_erz = barren_aus_erz * 2
        kosten_erz = benoetigte_erz * erz_preis
        umsatz_aktuell_erz = bolzen_menge * bolzen_marktpreis
        umsatz_wunsch_erz = bolzen_menge * bolzen_wunschpreis
        gewinn_aktuell_erz = round(umsatz_aktuell_erz - kosten_erz, 2)
        gewinn_wunsch_erz = round(umsatz_wunsch_erz - kosten_erz, 2)

        st.subheader("📦 Geistereisenbolzen Auswertung")
        st.markdown("Hier siehst du beide Varianten im Vergleich. Keine automatische Auswahl – du entscheidest!")
        # Variante 1: Barren
        df_barren = pd.DataFrame({
            'Art': ['🪙 Barren'],
            'Gesamtkosten (G)': [kosten_barren],
            'Umsatz (Marktpreis)': [umsatz_aktuell_barren],
            'Gewinn (Marktpreis)': [gewinn_aktuell_barren],
            'Umsatz (Wunschpreis)': [umsatz_wunsch_barren],
            'Gewinn (Wunschpreis)': [gewinn_wunsch_barren]
        }).round(2)

        # Variante 2: Erz
        df_erz = pd.DataFrame({
            'Art': ['💎 Erz'],
            'Gesamtkosten (G)': [kosten_erz],
            'Umsatz (Marktpreis)': [umsatz_aktuell_erz],
            'Gewinn (Marktpreis)': [gewinn_aktuell_erz],
            'Umsatz (Wunschpreis)': [umsatz_wunsch_erz],
            'Gewinn (Wunschpreis)': [gewinn_wunsch_erz]
        }).round(2)

        st.markdown("### 🪙 Barren")
        st.dataframe(df_barren, use_container_width=True)
        st.markdown("### 💎 Erz")
        st.dataframe(df_erz, use_container_width=True)
