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

ia = IMDb()

lem=WordNetLemmatizer()

bad_words=[',','.','(',')','+','-','_','/','|','[',']','*',
           '&','^','%','$','#','@','!',':',';','','"','" "',' ']

stop_words=set(stopwords.words("english"))

numbers=[]
decimal=[]
for i in range(0,10000):
    numbers.append(str(i))
    
for i in np.arange(0,10,0.1):
    decimal.append(str(i))
    

top=ia.get_top250_movies()

##movie = ia.get_movie('0133093')
##ia.update(movie,info=['critic reviews','photo sites','review'])
##print(movie.infoset2keys)
##if 'arithmetic mean' in movie:
##    print(movie['reviews'][0]['content'])

l=[]
movies={}
inc=0
not1=[]
for i in range(0,250):
    movie=top[i]
    a=ia.search_movie(str(movie))
    b=a[0].movieID
    mov=ia.get_movie(str(b))
    ia.update(mov,info=['plot'])
    try:
        sent=sent_tokenize(mov['synopsis'][0])
        for i in mov['cast']:
            l.append(str(i))
        movies[str(mov)]=l
        inc=inc+1
        l=[]
        print(inc)
    except:
        l=[]
        not1.append(mov)
        print("no cast")


    

##with open("movie_words2.pickle",'wb') as dic:
##     pickle.dump(movies,dic,protocol=pickle.HIGHEST_PROTOCOL)

with open("movies_cast.pickle",'wb') as dic1:
     pickle.dump(movies,dic1,protocol=pickle.HIGHEST_PROTOCOL)
print("done")
    

