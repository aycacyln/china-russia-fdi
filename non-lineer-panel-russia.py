import pandas as pd
import numpy as np
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

# 🔹 Veriyi yükle
df = pd.read_excel(r"C:\Users\Ayca\Desktop\Rusya makalesi\ÖZgürlük Endeksi.xlsx", sheet_name="Sayfa1")

# 🔹 Panel indeksi oluştur
df = df.set_index(["Country/Territory", "Yıl"])

# 🔹 NaN’leri düşür, ilgili değişkenleri al
df = df[["Rusya ile oy uyumu", "DYY_Rusya"]].dropna()

# 🔹 Kuadratik (karesel) terimi ekle
df["DYY_Rusya_kare"] = df["DYY_Rusya"] ** 2

# 🔹 Bağımlı ve bağımsız değişkenleri tanımla
y = df["Rusya ile oy uyumu"]
X = df[["DYY_Rusya", "DYY_Rusya_kare"]]
X = sm.add_constant(X)

# 🔹 Sabit etkili panel regresyonu
model = PanelOLS(y, X, entity_effects=True)
results = model.fit()

# 🔹 Sonuçları göster
print(results.summary)
