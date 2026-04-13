import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score
import pickle

df = pd.read_csv("clients.csv")

X = df.drop("defaut", axis=1)
y = df["defaut"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_sc, y_train)

y_pred = model.predict(X_test_sc)
y_proba = model.predict_proba(X_test_sc)[:, 1]

print("=== Résultats du modèle ===")
print(classification_report(y_test, y_pred))
print(f"ROC-AUC : {roc_auc_score(y_test, y_proba):.3f}")

# Sauvegarde du modèle
with open("model.pkl", "wb") as f:
    pickle.dump((model, scaler), f)
print("✅ Modèle sauvegardé dans model.pkl")