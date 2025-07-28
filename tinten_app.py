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
    # Aufteilung Einkaufspreis
    gesamte_tinten = traumtinte_menge + sternentinte_menge if (traumtinte_menge + sternentinte_menge) > 0 else 1
    anteil_traum = traumtinte_menge / gesamte_tinten
    anteil_stern = sternentinte_menge / gesamte_tinten
    kosten_traumtinte = einkaufspreis * anteil_traum
    kosten_sternentinte = einkaufspreis * anteil_stern

    # Rechenweg Traumtinte
    traumtinte_umsatz = traumtinte_menge * traumtinte_preis
    gewinn_traumtinte = traumtinte_umsatz - kosten_traumtinte

    # Rechenweg Sternentinte
    sternentinte_umsatz = sternentinte_menge * sternentinte_preis
    gewinn_sternentinte = sternentinte_umsatz - kosten_sternentinte

    # Rechenweg mit Wunschpreisen
    traumtinte_umsatz_wunsch = traumtinte_menge * traumtinte_preis_wunsch
    gewinn_traumtinte_wunsch = traumtinte_umsatz_wunsch - kosten_traumtinte

    sternentinte_umsatz_wunsch = sternentinte_menge * sternentinte_preis_wunsch
    gewinn_sternentinte_wunsch = sternentinte_umsatz_wunsch - kosten_sternentinte

    # Ab welchem Traumtinte-Preis lohnt sich der Tausch nicht mehr
    break_even_traumtinte_preis = sternentinte_preis / 10

        tausch_lohnt_aktuell = traumtinte_preis < break_even_traumtinte_preis
    tausch_lohnt_wunsch = traumtinte_preis_wunsch < break_even_traumtinte_preis

    return {
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

    st.markdown("### 📊 Aktuelle Marktpreise")
    st.markdown(f"**Einkaufspreis insgesamt:** {result['Einkaufspreis insgesamt']} G")
    st.markdown(f"**Zugewiesen an Traumtinte:** {result['Zugewiesen an Traumtinte']} G")
    st.markdown(f"**Zugewiesen an Sternentinte:** {result['Zugewiesen an Sternentinte']} G")
    st.markdown(f"**Traumtinte Umsatz:** {result['Traumtinte Umsatz']} G")
    st.markdown(f"**Gewinn mit direktem Verkauf von Traumtinte:** {result['Gewinn mit direktem Verkauf von Traumtinte']} G")
    st.markdown(f"**Sternentinte Umsatz:** {result['Sternentinte Umsatz']} G")
    st.markdown(f"**Gewinn bei Herstellung und Verkauf von Sternentinte:** {result['Gewinn bei Herstellung und Verkauf von Sternentinte']} G")

    st.markdown("---")
    st.markdown("### 🌟 Wunschpreise (zukünftiger Marktwert)")
    st.markdown(f"**Traumtinte Umsatz (Wunschpreis):** {result['Traumtinte Umsatz (Wunschpreis)']} G")
    st.markdown(f"**Gewinn Traumtinte (Wunschpreis):** {result['Gewinn Traumtinte (Wunschpreis)']} G")
    st.markdown(f"**Sternentinte Umsatz (Wunschpreis):** {result['Sternentinte Umsatz (Wunschpreis)']} G")
    st.markdown(f"**Gewinn Sternentinte (Wunschpreis):** {result['Gewinn Sternentinte (Wunschpreis)']} G")

    st.markdown("---")
        st.markdown(f"**🔁 Tausch lohnt sich, wenn Traumtinte unter:** {result['Tausch lohnt sich, wenn Traumtinte unter']} G")

    if result['Tausch lohnt sich, wenn Traumtinte unter'] > 0:
        st.markdown("**📉 Aktueller Preisvergleich:**")
        st.markdown(f"Aktueller Preis: {traumtinte_preis} G – {'✅ Tausch lohnt sich' if traumtinte_preis < result['Tausch lohnt sich, wenn Traumtinte unter'] else '❌ Kein Tausch nötig'}")
        st.markdown(f"Wunschpreis: {traumtinte_preis_wunsch} G – {'✅ Tausch lohnt sich' if traumtinte_preis_wunsch < result['Tausch lohnt sich, wenn Traumtinte unter'] else '❌ Kein Tausch nötig'}")
