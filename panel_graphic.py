import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi yükle
df = pd.read_excel(r"C:\Users\Ayca\Desktop\Rusya makalesi\Data-c-r-fdi.xlsx", sheet_name="Sayfa1")

# Temizle
df = df[["Country/Territory", "Yıl", "DYY_Çin", "Çin ile oy uyumu", "DYY_Rusya", "Rusya ile oy uyumu"]].dropna()

# Grafik
plt.figure(figsize=(10, 6))
sns.regplot(x="DYY_Çin", y="Çin ile oy uyumu", data=df, scatter_kws={"alpha":0.6}, line_kws={"color":"red"})
plt.title("The Relationship Between Chinese FDI and UN Voting Alignment")
plt.xlabel("FDI from China")
plt.ylabel("Alignment with China")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.regplot(x="DYY_Rusya", y="Rusya ile oy uyumu", data=df, scatter_kws={"alpha":0.6}, line_kws={"color":"blue"})
plt.title("The Relationship Between Russian FDI and UN Voting Alignment")
plt.xlabel("FDI from Russia")
plt.ylabel("Alignment with Russia")
plt.grid(True)
plt.tight_layout()
plt.show()