import numpy as np
import matplotlib.pyplot as plt

# 1. Failist lugemine
linnad = []
rahvaarvud = []

with open("rahvaarv.txt", encoding="utf-8") as f:
    for rida in f:
        osad = rida.strip().split()
        linn = " ".join(osad[:-1])
        arv = int(osad[-1])
        linnad.append(linn)
        rahvaarvud.append(arv)

# 2. NumPy array töötluseks
arvud_np = np.array(rahvaarvud)

# 3. Statistika
koguarv = arvud_np.sum()
keskmine = arvud_np.mean()
suurim = arvud_np.max()
väikseim = arvud_np.min()
suurima_linn = linnad[np.argmax(arvud_np)]
väikseima_linn = linnad[np.argmin(arvud_np)]

# 4. Tulemuste printimine
print(f"Koguarv: {koguarv}")
print(f"Keskmine: {keskmine:.1f}")
print(f"Suurim: {suurima_linn} ({suurim})")
print(f"Väikseim: {väikseima_linn} ({väikseim})")

# 5. Tulpdiagramm
plt.figure(figsize=(10, 6))
plt.bar(linnad, rahvaarvud, color="skyblue")
plt.title("Eesti linnade rahvaarv")
plt.xlabel("Linn")
plt.ylabel("Elanike arv")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()