import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import shapiro, normaltest, anderson
from linearmodels.panel import PanelOLS

# Veriyi yükle
df = pd.read_excel(r"C:\Users\Ayca\Desktop\Rusya makalesi\Data-c-r-fdi.xlsx", sheet_name="Sayfa1")

# Test yapmak istediğiniz değişken isimleri
variables = [
    "DYY_Çin",
    "DYY_Rusya",
    "Çin ile oy uyumu",
    "Rusya ile oy uyumu"
]

# Sonuçları saklayacağımız liste
results = []

for var in variables:
    data = df[var].dropna()  # eksik değerleri at
    
    # Shapiro-Wilk
    shapiro_p = shapiro(data)[1]
    
    # D'Agostino and Pearson's K²
    dagostino_p = normaltest(data)[1]
    
    # Anderson-Darling
    anderson_stat = anderson(data).statistic
    
    results.append({
        "Değişken": var,
        "Shapiro Wilk p": shapiro_p,
        "D’agostino p": dagostino_p,
        "Anderson stat": anderson_stat
    })

# Sonuçları tabloya çevir
results_df = pd.DataFrame(results)
print(results_df)
