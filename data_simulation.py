import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(42)
N = 1000

data = {
    "age": np.random.randint(18, 70, N),
    "revenu_mensuel": np.random.randint(1000, 8000, N),
    "anciennete_emploi": np.random.randint(0, 30, N),
    "nb_credits_actifs": np.random.randint(0, 5, N),
    "taux_endettement": np.round(np.random.uniform(0.05, 0.80, N), 2),
    "incidents_passes": np.random.randint(0, 4, N),
    "montant_demande": np.random.randint(1000, 50000, N),
}

df = pd.DataFrame(data)

# Score de risque → label défaut (1 = défaut, 0 = bon payeur)
score = (
    -0.01 * df["revenu_mensuel"]
    + 0.5  * df["taux_endettement"] * 100
    + 2.0  * df["incidents_passes"]
    - 0.5  * df["anciennete_emploi"]
    + 0.3  * df["nb_credits_actifs"]
)
threshold = np.percentile(score, 80)
df["defaut"] = (score > threshold).astype(int)

df.to_csv("clients.csv", index=False)
print(f"✅ Dataset généré : {len(df)} clients")
print(f"   Taux de défaut : {df['defaut'].mean():.1%}")
print(df.head())