import pandas as pd

sample = pd.read_csv("sms-spam-corpus.csv")
hamstr1 = sample[sample.v1=="ham"]
spamstr1 = sample[sample.v1=="spam"]
hamstr = []
spamstr = []

#remove numbers and special characters
for s1 in hamstr1.v2:
    hamstr.append("".join(c for c in s1 if c.isalpha() or c == " ").lower())
for s1 in spamstr1.v2:
    spamstr.append("".join(c for c in s1 if c.isalpha() or c == " ").lower())

stopwords1 = ["a","the","to","in","an","of","on"]

flag = True
ham = []
spam = []
#remove stop words
for s1 in spamstr:
    for s2 in s1.split():
        for s3 in stopwords1:
            if s2==s3: flag = False
        if flag: spam.append(s2)
        flag = True

for s1 in hamstr:
    for s2 in s1.split():
        for s3 in stopwords1:
            if s2==s3: flag = False
        if flag: ham.append(s2)
        flag = True

hamdic ={'w1':'w2'}
spamdic = {'w1':'w2'}

#count amount of every word
for s1 in ham:
    if(hamdic.get(s1)):
        hamdic.update({s1: hamdic.get(s1) + 1})
    else: hamdic.setdefault(s1, 1)

for s1 in spam:
    if(spamdic.get(s1)):
        spamdic.update({s1: spamdic.get(s1) + 1})
    else: spamdic.setdefault(s1, 1)
hamdic1= []
for s in hamdic.keys():
    hamdic1.append([s,hamdic.get(s)])
spamdic1= []
for s in spamdic.keys():
    spamdic1.append([s,spamdic.get(s)])
ham_filename = "ham-dic.csv"
spam_filename = "spam-dic.csv"

#write dictionaries to files

dfh = pd.DataFrame(hamdic1)
dfh.to_csv(ham_filename, index=False, header=None)

dfs = pd.DataFrame(spamdic1)
dfs.to_csv(spam_filename, index=False, header=None)



