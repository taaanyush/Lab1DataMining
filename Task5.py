import pandas as pd
from matplotlib import pyplot as plt

spamdic = pd.read_csv("spam-dic.csv")

words_spam = {}

spam_max = sorted(spamdic.w2)
#frequently used words
for i in range(20):
    for j in range(len(spamdic.w1)):
        if(spam_max[len(spam_max)-i-1]==spamdic.w2[j]):
            words_spam.update({spamdic.w1[j]:spamdic.w2[j]})
plt.figure(figsize=(11,4))
plt.title("Frequency in spam")
plt.plot(words_spam.keys(),words_spam.values())
plt.xlabel("Words")
plt.ylabel("Amount")

plt.show()

