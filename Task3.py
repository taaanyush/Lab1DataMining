import pandas as pd
from matplotlib import pyplot as plt

hamdic = pd.read_csv("ham-dic.csv")
spamdic = pd.read_csv("spam-dic.csv")

length_ham = {1:0}
length_spam = {1:0}

#count amount of words by length
for s1 in hamdic.w1:
    if(type(s1)==float): continue
    if (length_ham.get(len(s1))):
        length_ham.update({len(s1): length_ham.get(len(s1)) + 1})
    else:
        length_ham.setdefault(len(s1), 1)
#sort
ham_keys=sorted(length_ham)
ham_values = []
ham_middle = 0
sumH_values = 0
#calc average length
for i in ham_keys:
    ham_middle+=i*length_ham[i]
    ham_values.append(length_ham[i])
    sumH_values+=length_ham[i]
ham_middle=ham_middle/len(hamdic.w1)
for i in range(len(ham_values)) : ham_values[i]=ham_values[i]/sumH_values

#count amount of words by length
for s1 in spamdic.w1:
    if(type(s1)==float): continue
    if (length_spam.get(len(s1))):
        length_spam.update({len(s1): length_spam.get(len(s1)) + 1})
    else:
        length_spam.setdefault(len(s1), 1)

#sort
spam_keys=sorted(length_spam)
spam_values = []
spam_middle = 0
sumS_values = 0
#calc average length
for i in spam_keys:
    spam_middle+=i*length_spam[i]
    spam_values.append(length_spam[i])
    sumS_values+=length_spam[i]
spam_middle=spam_middle/len(spamdic.w1)
for i in range(len(spam_values)) : spam_values[i]=spam_values[i]/sumS_values

plt.title("Length of words")
plt.plot(ham_keys,ham_values)
plt.plot(spam_keys,spam_values)
plt.xlabel("Length")
plt.ylabel("Amount")

plt.legend(["ham "+str(round(ham_middle,2)), "spam "+str(round(spam_middle,2))])
plt.show()