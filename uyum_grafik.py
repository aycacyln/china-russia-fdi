import pandas as pd
import matplotlib.pyplot as plt

# Veriyi oku
df = pd.read_excel(r"C:\Users\Ayca\Desktop\Rusya makalesi\rusya_oy_uyumu.xlsx")

# Grafik boyutu
plt.figure(figsize=(12, 6))

# Ülkeler listesi
countries = ["KAZAKHSTAN", "KYRGYZSTAN", "TAJIKISTAN", "TURKMENISTAN", "UZBEKISTAN"]

# Her ülke için çizgi grafiği
for country in countries:
    plt.plot(df["Vote Year"], df[f"{country}_alignment"], label=country)

# Başlık ve eksenler
#plt.title("Orta Asya Ülkelerinin Rusya ile BM Oy Uyumu (Yıllar Bazında)")
plt.xlabel("Year")
plt.ylabel("Alignment Rate")
plt.ylim(0.4, 1.0)  # Y-eksenini 0.4'ten başlat
plt.grid(True)
plt.legend()
plt.tight_layout()

# Göster
plt.show() 

plt.savefig(r"C:\Users\Ayca\Desktop\Rusya makalesi\rusya_oy_uyumu_grafik.png", dpi=300)
