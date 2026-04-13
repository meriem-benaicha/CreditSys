# 🏦 CreditSys — Système Bancaire de Gestion du Risque Crédit

Projet personnel intégré simulant un système bancaire complet de scoring et contrôle du risque crédit.

##  Modules

| Module | Description | Stack |
|--------|-------------|-------|
| DS1 | Scoring crédit — modèle ML de prédiction de défaut | Python, sklearn, Streamlit |
| F1  | Stress test du portefeuille de prêts | Python, pandas, openpyxl |
| F2  | Contrôle permanent et reporting automatique | Python, SQL, SQLite |
| DS2 | Détection d'anomalies et alertes | Python, scipy |

##  Pipeline
##  Lancer le dashboard DS1

```bash
pip install -r requirements.txt
python data_simulation.py
python model.py
python -m streamlit run dashboard.py
```

##  Contexte

Étudiante en MAM3 à Polytech Nice Sophia, j'ai construit ce projet pour approfondir 
mes compétences en data science appliquée à la finance bancaire.

L'idée est de montrer qu'un système de gestion du risque crédit peut être construit 
de A à Z : de la simulation des données jusqu'au dashboard interactif, en passant 
par le modèle ML et le reporting automatique.