import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

# Veriyi oku
df = pd.read_excel(r"C:\Users\Ayca\Desktop\Rusya makalesi\Data-c-r-fdi.xlsx", sheet_name="Sayfa1")

# Panel veri indekslemesi
df = df.set_index(["Country/Territory", "Yıl"])

# Gerekli değişkenleri sayısal olarak tanımla
df = df[["Çin ile oy uyumu", "DYY_Çin"]].dropna()

# Bağımlı ve bağımsız değişkenler
y = df["Çin ile oy uyumu"]
X = df[["DYY_Çin"]]
X = sm.add_constant(X)

# Sabit etkili model
model = PanelOLS(y, X, entity_effects=True)
results = model.fit()
print(results.summary)
