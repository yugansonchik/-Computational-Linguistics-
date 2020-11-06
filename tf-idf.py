import collections
import math



def tf(words):
    counter = collections.Counter(words)
    d = {}
    for i in counter:
        d[i] = counter[i] / float(len(words))
    return d



def idf(word, corpus):
    return math.log(len(corpus) / sum(word in i for i in corpus))



text1 = ["book", "fan", "car", "book"]
text2 = ["baby", "book", "axe", "baby"]

corpus = [text1, text2]

print(tf(text1))
print(tf(text2))
print(idf("book", corpus))
print(idf("baby", corpus))
print(idf("fan", corpus))



