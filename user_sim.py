import csv
import pickle
import math
import operator


movies={}
with open("movies.pickle","rb") as file:
    movies=pickle.load(file)

user_rating={}

with open("users_final.pickle","rb") as file:
    user_rating=pickle.load(file)

item_rating={}

with open("sim_new.pickle","rb") as file:
    item_rating=pickle.load(file)

##for i in item_rating:
##    for j in item_rating[i]:
##        print(j,item_rating[i][j],i)

def item_recom(rating_list):
    score={}
    for movie in item_rating:
        if movie in rating_list:
            continue
        sim=0
        total=0

        for mov in rating_list:
            sim = sim+item_rating[movie][mov]
            total = total+(item_rating[movie][mov]*rating_list[mov])

        if sim == 0:
            continue

        score[movie] = total/sim
    return score

def user_sim(user_sim_mat,rating_list):

    for user in user_rating:
        sum1=sum([rating_list[i] for i in rating_list])
        sum1=sum1/len(rating_list)

        sum2=sum([user_rating[user][i] for i in rating_list])
        sum2=sum2/len(rating_list)

        num=sum([(rating_list[i]-sum1)*(user_rating[user][i]-sum2)
                for i in rating_list])

        den1 =math.sqrt(sum([math.pow(rating_list[i]-sum1,2)
                            for i in rating_list]))
        den2 =math.sqrt(sum([math.pow(user_rating[user][i]-sum2,2)
                            for i in rating_list]))

        if den1!=float(0):
            den=den1*den2
        elif den1==float(0):
            den=den2



        if den==0:
            user_sim_mat[user]=0
            continue

        pearsons=num/den
        user_sim_mat[user]=pearsons



def user_recom(rating_list):
    user_sim_mat={}
    user_sim(user_sim_mat,rating_list)

    movie_score={}
    for movie in movies:

        if movie in rating_list:
            continue

        sim=0
        total=0

        for user in user_rating:

            if user_sim_mat[user] <= 0:
                continue

            sim=sim+user_sim_mat[user]
            total=total+(user_sim_mat[user]*user_rating[user][movie])

        if sim==0:
            continue

        movie_score[movie]=total/sim

    return movie_score




def recommender(rating_list):
    l=user_recom(rating_list)
    print(l)
    l=list(reversed(sorted(l.items(), key=operator.itemgetter(1))))
    print(l[:10])
    return(l[:10])

def recommender1(rating_list):
    l1=item_recom(rating_list)
    l1=list(reversed(sorted(l1.items(), key=operator.itemgetter(1))))
    print(l1[:10])
    return(l1[:10])

rating_list={}

i=0
with open('afile.csv',mode='r',encoding="utf-8") as movi:
    read=csv.reader(movi)
    for row in read:
        i=i+1
        rating_list[row[0]]=float(row[3])
        if i==1:
            break

recommender(rating_list)
recommender1(rating_list)
