import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

# Veriyi oku
df = pd.read_excel(r"C:\Users\Ayca\Desktop\Rusya makalesi\ÖZgürlük Endeksi.xlsx", sheet_name="Sayfa1")

# Panel veri indekslemesi
df = df.set_index(["Country/Territory", "Yıl"])

# Gerekli değişkenleri sayısal olarak tanımla
df = df[["Rusya ile oy uyumu", "DYY_Rusya"]].dropna()

# Bağımlı ve bağımsız değişkenler
y = df["Rusya ile oy uyumu"]
X = df[["DYY_Rusya"]]
X = sm.add_constant(X)

# Sabit etkili model
model = PanelOLS(y, X, entity_effects=True)
results = model.fit()
print(results.summary)
