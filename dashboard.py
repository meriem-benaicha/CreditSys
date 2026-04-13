import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt

with open("model.pkl", "rb") as f:
    model, scaler = pickle.load(f)

st.set_page_config(page_title="CreditSys — Scoring Crédit", page_icon="🏦")
st.title("🏦 CreditSys — Scoring de Crédit")
st.markdown("Module DS1 · Système bancaire de gestion du risque crédit")

st.sidebar.header("📋 Profil du client")
age                = st.sidebar.slider("Âge", 18, 70, 35)
revenu_mensuel     = st.sidebar.slider("Revenu mensuel (€)", 1000, 8000, 3000)
anciennete_emploi  = st.sidebar.slider("Ancienneté emploi (ans)", 0, 30, 5)
nb_credits_actifs  = st.sidebar.slider("Nb crédits actifs", 0, 5, 1)
taux_endettement   = st.sidebar.slider("Taux d'endettement", 0.05, 0.80, 0.30)
incidents_passes   = st.sidebar.slider("Incidents passés", 0, 3, 0)
montant_demande    = st.sidebar.slider("Montant demandé (€)", 1000, 50000, 10000)

client = pd.DataFrame([{
    "age": age,
    "revenu_mensuel": revenu_mensuel,
    "anciennete_emploi": anciennete_emploi,
    "nb_credits_actifs": nb_credits_actifs,
    "taux_endettement": taux_endettement,
    "incidents_passes": incidents_passes,
    "montant_demande": montant_demande,
}])

client_sc = scaler.transform(client)
proba_defaut = model.predict_proba(client_sc)[0][1]
decision = "🔴 REFUSÉ" if proba_defaut > 0.5 else "🟢 ACCORDÉ"

st.subheader("📊 Résultat du scoring")
col1, col2 = st.columns(2)
col1.metric("Probabilité de défaut", f"{proba_defaut:.1%}")
col2.metric("Décision", decision)

fig, ax = plt.subplots(figsize=(6, 1.5))
ax.barh(["Risque"], [proba_defaut], color="crimson" if proba_defaut > 0.5 else "seagreen")
ax.barh(["Risque"], [1 - proba_defaut], left=[proba_defaut], color="#e0e0e0")
ax.axvline(0.5, color="orange", linestyle="--", label="Seuil 50%")
ax.set_xlim(0, 1)
ax.legend()
st.pyplot(fig)

st.subheader("📁 Base clients")
df = pd.read_csv("clients.csv")
st.dataframe(df.head(20))