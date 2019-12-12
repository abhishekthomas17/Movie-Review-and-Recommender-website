import csv
import pickle
import math
import operator
from imdb import IMDb
import pandas as pd
import numpy as np
import csv
import pickle
import string
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 


with open("movies_words.pickle",'rb') as dic:
     m1=pickle.load(dic)


all_cast=[]

for i in m1:
    for j in m1[i]:
        all_cast.append(j)

all_cast=list(set(all_cast))
all_cast.sort()
##for j in range(0,len(all_cast)):
##    print(j,all_cast[j])
##print(all_cast)
##
##for i in all_cast:
##    print(i)

m={}
l=[]
k=0
for i in m1:
    for j in range(0,len(all_cast)):
        if all_cast[j] in m1[i]:
            l.insert(j,1)
        else:
            l.insert(j,0)
    m[i]=l
    k=k+1
    print(k)
    l=[]


            

with open("movie_words_vector.pickle",'wb') as dic:
     pickle.dump(m,dic,protocol=pickle.HIGHEST_PROTOCOL)
