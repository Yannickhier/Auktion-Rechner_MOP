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
