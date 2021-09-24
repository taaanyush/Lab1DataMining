import pandas as pd
from matplotlib import pyplot as plt

hamdic = pd.read_csv("ham-dic.csv")
words_ham = {}

ham_max=sorted(hamdic.w2)

#frequently used words
for i in range(20):
    for j in range(len(hamdic.w1)):
        if(ham_max[len(ham_max)-i-1]==hamdic.w2[j]):
            words_ham.update({hamdic.w1[j]:hamdic.w2[j]})

plt.figure(figsize=(11,4))
plt.title("Frequency in ham")
plt.plot(words_ham.keys(),words_ham.values())
plt.xlabel("Words")
plt.ylabel("Amount")

plt.show()

