import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 🔷 Veriyi yükle
dosya_yolu = r"C:\Users\Ayca\Desktop\Rusya makalesi\Data-c-r-fdi.xlsx"
df = pd.read_excel(dosya_yolu, sheet_name="Sayfa1")

# 🔷 Ülke listesi
countries = ["Kazakhstan", "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Uzbekistan"]

# 🔷 Tüm ülkelerin verisini birleştir
df_all = df[df["Country/Territory"].isin(countries)][["Country/Territory", "DYY_Rusya", "Rusya ile oy uyumu"]].dropna()

x_all = df_all["DYY_Rusya"]
y_all = df_all["Rusya ile oy uyumu"]

# 🔷 Kuadratik regresyon modeli
coeffs_all = np.polyfit(x_all, y_all, 2)  # a*x² + b*x + c
x_pred = np.linspace(x_all.min(), x_all.max(), 100)
y_pred = np.polyval(coeffs_all, x_pred)

# 🔷 Grafik
plt.figure(figsize=(10, 6))

# Her ülkeyi farklı renkle işaretleyerek çiz
for country in countries:
    subset = df_all[df_all["Country/Territory"] == country]
    plt.scatter(
        subset["DYY_Rusya"],
        subset["Rusya ile oy uyumu"],
        label=country,
        alpha=0.7
    )

# Kuadratik eğri
plt.plot(x_pred, y_pred, color="black", linewidth=2, label="Quadratic Fit Curve")

#plt.title("Rusya'dan Gelen DYY ile Rusya ile BM Oy Uyumu (Birleşik Kuadratik Model)")
print(f"Kuadratik regresyon katsayıları (birleşik): {coeffs_all}")

plt.xlabel("FDI from Russia")
plt.ylabel("Alignment with Russia")
plt.ylim(0.5, 1.0)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


