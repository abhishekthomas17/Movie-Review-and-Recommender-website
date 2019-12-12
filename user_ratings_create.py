from imdb import IMDb
import pandas as pd
import csv
import time
import random
import numpy as np
import pickle
user_ratings={}

print(round(random.uniform(6,9),1))

m1={}
new={}

with open("movies.pickle",'rb') as dic:
     m1=pickle.load(dic)


user_rating={}
user_rating2={}
k=1
for i in range(1,401):
    new={}
    for j in m1:
        a=round(random.uniform(4,10),1)
        new[str(j)]=a
    user_rating2[i]=new
    print(k)
    k=k+1


##ra=round(random.random()*random.random()*random.random()
##         *random.random()*random.random()*100000)
##ra1=random.randint(ra,ra+1000000)
##
##random.seed(ra1)

for i in range(1,5):
    print(user_rating2[i])




print("DONE")


with open("users_final.pickle",'wb') as dic:
     pickle.dump(user_rating2,dic,protocol=pickle.HIGHEST_PROTOCOL)



print("done")
