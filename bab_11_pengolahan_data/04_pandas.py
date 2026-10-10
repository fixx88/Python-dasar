# BAB 11 - Langkah Berikutnya: pandas
# Install dulu di terminal:  pip install pandas
import os

try:
    import pandas as pd
except ImportError:
    print("pandas belum terpasang. Jalankan di terminal: pip install pandas")
    raise SystemExit

FOLDER = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(FOLDER, "nilai.csv"))

print(df.groupby("kelas")["nilai"].mean())
print(df[df["nilai"] >= 75]["nama"].tolist())
print(df.sort_values("nilai").tail(1))
