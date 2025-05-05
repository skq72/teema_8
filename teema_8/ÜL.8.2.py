from re import I
import numpy as np
import matplotlib.pyplot as plt

mäed=[]
kõrgus=[]


with open("maed.txt", encoding="utf-8") as f:
    for rida in f:
         osad = rida.strip().split()
         linn = " ".join(osad[:-1])
         arv = int(osad[-1])
         mäed.append(linn)
         kõrgus.append(arv)

arvud_np = np.array(kõrgus)


keskmine = arvud_np.mean()
kõrgeim = arvud_np.max()
madalam = arvud_np.min()
suurima_mäe = mäed[np.argmax(arvud_np)]
väikseima_mäe = mäed[np.argmin(arvud_np)]



for n in range(0,len(mäed)):
        for m in range(n,len(mäed)):
            if kõrgus[n]<kõrgus[m]:
                kõrgus[n],kõrgus[m]=kõrgus[m],kõrgus[n]
                mäed[n],mäed[m]=mäed[m],mäed[n]


print(f"Keskmine: {keskmine:.1f}")
print(f"Suurim: {suurima_mäe} ({kõrgeim})")
print(f"Väikseim: {väikseima_mäe} ({madalam})")



plt.figure(figsize=(10, 6))
plt.bar(mäed, kõrgus, color="yellow")
plt.title("Kõrgeimad mäed maailmas")
plt.xlabel("mägede nimed")
plt.ylabel("kõrgused meetrites")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("mäed_graafik.png")
plt.show()