import pandas as pd
from scipy.stats import spearmanr

# Veriyi yükle
df = pd.read_excel(r"C:\Users\Ayca\Desktop\Rusya makalesi\Data-c-r-fdi.xlsx", sheet_name="Sayfa1")

# Ülke isimleri
countries = df["Country/Territory"].unique()

# Sonuçları tutmak için liste
results = []

# Her ülke için
for country in countries:
    df_country = df[df["Country/Territory"] == country]
    
    # DYY Çin ↔ Çin ile oy uyumu
    x1 = df_country["DYY_Çin"]
    y1 = df_country["Çin ile oy uyumu"]
    r1, p1 = spearmanr(x1, y1, nan_policy='omit')
    signif1 = "Yes" if p1 < 0.05 else "No"
    
    results.append({
        "Ülke": country,
        "Variable Pair(s)": "FDI China ↔ Alignment with China",
        "Spearman R": r1,
        "P-Değeri": p1,
        "Anlamlı mı?": signif1
    })
    
    # DYY Rusya ↔ Rusya ile oy uyumu
    x2 = df_country["DYY_Rusya"]
    y2 = df_country["Rusya ile oy uyumu"]
    r2, p2 = spearmanr(x2, y2, nan_policy='omit')
    signif2 = "Yes" if p2 < 0.05 else "No"
    
    results.append({
        "Ülke": country,
        "Variable Pair(s)": "FDI Russia ↔ Alignment with Russia",
        "Spearman R": r2,
        "P-Değeri": p2,
        "Anlamlı mı?": signif2
    })

# Sonuçları tabloya çevir
results_df = pd.DataFrame(results)

# Sonuçları görüntüle
print(results_df)

# Excel’e kaydetmek istersen
results_df.to_excel(r"C:\Users\Ayca\Desktop\spearman_sonuclari.xlsx", index=False)
