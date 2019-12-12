from imdb import IMDb
import pandas as pd
import numpy as np
import csv
import pickle
import string
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 



movies={}
with open("movies_words.pickle",'rb') as dic:
     movies=pickle.load(dic)

movies1={}
with open("movies_genre.pickle",'rb') as dic:
     movies1=pickle.load(dic)

movies2={}
with open("movies_cast.pickle",'rb') as dic:
     movies2=pickle.load(dic)

c={}
c1={}
c2={}
c3={}
d={}
d1={}
d2={}
d3={}
new={}
l=0
for i in movies:
    new[i] = list(set(movies[i]))
    
for i in movies:
    for j in movies:
        if str(i) == str(j):
            continue
        count=0
        count1=0
        count2=0
        for word in new[i]:
            if word in new[j]:
                count=count+1
        for word in movies1[i]:
            if word in movies1[j]:
                count1=count1+1
        for word in movies2[i]:
            if word in movies2[j]:
                count2=count2+1           
        c[str(j)]=(count/len(new[i]))+(count1/len(movies1[i]))
        +(count2/len(movies2[i]))
        
        c1[str(j)]=(count1/len(movies1[i]))
        +(count2/len(movies2[i]))
        
        c2[str(j)]=(count2/len(movies2[i]))
        
        c3[str(j)]=(count/len(new[i]))
        
    d[str(i)]=c
    d1[str(i)]=c1
    d2[str(i)]=c2
    d3[str(i)]=c3
    c={}
    c1={}
    c2={}
    c3={}
    l=l+1
    print(l)

with open("sim.pickle",'wb') as dic:
     pickle.dump(d,dic,protocol=pickle.HIGHEST_PROTOCOL)
print("DONE")

with open("sim_gc.pickle",'wb') as dic:
     pickle.dump(d1,dic,protocol=pickle.HIGHEST_PROTOCOL)
print("DONE")


with open("sim_c.pickle",'wb') as dic:
     pickle.dump(d2,dic,protocol=pickle.HIGHEST_PROTOCOL)
print("DONE")

with open("sim_w.pickle",'wb') as dic:
     pickle.dump(d3,dic,protocol=pickle.HIGHEST_PROTOCOL)
print("DONE")


