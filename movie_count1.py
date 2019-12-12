from imdb import IMDb
import pandas as pd
import numpy as np
import csv
import math
import pickle
import string
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 



movies={}
with open("movie_words_vector.pickle",'rb') as dic:
     movies=pickle.load(dic)

movies1={}
with open("movie_genre_vector.pickle",'rb') as dic:
     movies1=pickle.load(dic)

movies2={}
with open("movie_cast_vector.pickle",'rb') as dic:
     movies2=pickle.load(dic)

sim={}
sim1={}
k=0  
for i in movies:
    for j in movies:
        if str(i) == str(j):
            continue
        a=movies[i]+movies1[i]+movies2[i]
        b=movies[j]+movies1[j]+movies2[j]
        num=0
        den1=0
        den2=0
        den=0
        for p in range(0,len(a)):
            num=num+a[p]*b[p]
            den1=den1+a[p]*a[p]
            den2=den2+b[p]*b[p]
            den=(math.sqrt(den1))*(math.sqrt(den2))

        if den==0:
            sim[j]=0
            continue
        cosine=num/den
        sim[j]=cosine
    sim1[i]=sim
    sim={}
    k=k+1
    print(k)
    
    
        
        

with open("sim_new.pickle",'wb') as dic:
     pickle.dump(sim1,dic,protocol=pickle.HIGHEST_PROTOCOL)
print("DONE")

##with open("sim_gc.pickle",'wb') as dic:
##     pickle.dump(d1,dic,protocol=pickle.HIGHEST_PROTOCOL)
##print("DONE")
##
##
##with open("sim_c.pickle",'wb') as dic:
##     pickle.dump(d2,dic,protocol=pickle.HIGHEST_PROTOCOL)
##print("DONE")
##
##with open("sim_w.pickle",'wb') as dic:
##     pickle.dump(d3,dic,protocol=pickle.HIGHEST_PROTOCOL)
##print("DONE")


