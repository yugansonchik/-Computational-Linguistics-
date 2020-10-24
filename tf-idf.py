import docx
import os
os.getcwd()
"C:\Users\Õ‡Ú‡Î¸ˇ\Desktop\ÍÓÏ ÎËÌ„\tf-idf.py"
doc = docx.Document(' “Œ »Ÿ≈“, “Œ“ ¬—≈√ƒ¿ Õ¿…ƒ®“..docx')
text = docx.Document('222.docx')

import collections
def compute1_tf(doc):
    tf_doc = collections.Counter(doc)
for i in tf_doc:
    tf_doc[i] = tf_doc[i]/float(len(doc))
return tf_doc

def compute2_tf(text):
    tf_text = collections.Counter(text)
for i in tf_text:
    tf_text[i] = tf_text[i]/float(len(text))
return tf_text


import math
word = 'Û‰Ó˜ÍÛ'
corpus = [' “Œ »Ÿ≈“, “Œ“ ¬—≈√ƒ¿ Õ¿…ƒ®“..docx', '222.docx']
def compute_idf(word, corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))



from collections import Counter
import math
def compute1_tfidf(corpus):
    def compute1_tf(text):
        tf_text = Counter(text)

def compute1_tf(doc):
    tf_text = Counter(doc)

for i in tf_text:
    tf_text[i] = tf_text[i]/float(len(text))
return tf_text
def compute1_idf(word, corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))


for i in tf_doc:
    tf_doc[i] = tf_doc[i]/float(len(doc))
return tf_doc
def compute2_idf(word, corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

documents1_list = []
for text in corpus:
tf_idf_dictionary = {}
computed1_tf = compute_tf(text)

for word in computed1_tf:
    tf_idf_dictionary[word] = computed1_tf[word] * compute1_idf(word, corpus)
documents_list.append(tf_idf_dictionary)
return documents1_list


documents2_list = []
for text in corpus:
tf_idf_dictionary = {}
computed2_tf = compute_tf(text)

for word in computed2_tf:
    tf_idf_dictionary[word] = computed2_tf[word] * compute2_idf(word, corpus)
documents_list.append(tf_idf_dictionary)
return documents2_list



print(compute1_tfidf(corpus))
print(compute2_tfidf(corpus))



