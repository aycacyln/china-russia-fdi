import pandas as pd
import matplotlib.pyplot as plt

# Veri setini oku
df = pd.read_excel(r"C:\Users\Ayca\Desktop\Rusya makalesi\Data-c-r-fdi.xlsx", sheet_name="Sayfa1")

# Ülkeleri listele
countries = df['Country/Territory'].unique()

# Her ülke için grafik
for country in countries:
    df_country = df[df['Country/Territory'] == country]
    
    plt.figure(figsize=(8,4))
    plt.plot(df_country['Yıl'], df_country['DYY_Çin'], marker='o', label='FDI China')
    plt.plot(df_country['Yıl'], df_country['DYY_Rusya'], marker='o', label='FDI Russia')
    plt.title(f"{country}")
    plt.xlabel("Year")
    plt.ylabel("FDI")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
