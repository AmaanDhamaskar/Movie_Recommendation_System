from AnimeRec import recommend,get_index_from
import sqlite3
from collections import Counter
import pandas as pd
def recTop1(username):
    df=pd.read_csv("refinedMovies.csv",index_col=0)
    ls=[]
    con=sqlite3.connect("userRating.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE if not exists userMovieRating (username	TEXT,	movieID	INTEGER,	rating	INTEGER,	PRIMARY KEY(username,movieID))")
    cur.execute(f"select * from userMovieRating where username='{username}' and rating>=4 order by rating")
    res=cur.fetchall()
    for row in res:
        if row[1] in df.index:
            ls.append(df.loc[row[1]]['title'])
    list=[]
    ls2=[]
    if len(ls)>0:
        for movie in ls:
            ls2.append(get_index_from(df,title=movie))
            a=recommend(movie)
            for i in a:
                list.append(i)
                
        f=Counter(list)
        s=[word for word, count in f.most_common(15 if len(f.keys())>15 else len(f.keys()))]
        
        a=[]
        top=[m for m in s if m not in ls2]
        return top
    
    else:
        con=sqlite3.connect('AccountSystem1.db')
        cur=con.cursor()
        cur.execute(f"select Genre1,Genre2,Genre3 from AccountDB where EMAIL='{username}'")
        res=cur.fetchall()
        res.sort()
        gen_on_3 = str(res[0][0])+'-'+str(res[0][1])+'-'+str(res[0][2])
        gen_on_2 = res[0][0]+'-'+res[0][1]
        gen_on_1 = res[0][0]
        
        li1 = []
        li2 = []
        li3 = []
        
        li1 = df[df['genres'].str.contains(gen_on_1)].index.tolist()
        li2 = df[df['genres'].str.contains(gen_on_2)].index.tolist()
        li3 = df[df['genres'].str.contains(gen_on_3)].index.tolist()
        
        movie_genre3 = []
        movie_genre2 = []
        movie_genre1 = []
        
        movie_genre32 = []
        movie_genre321 = []
        dem1 = []
        dem2 = []
        
        for i in li3:
            if df.loc[int(i)]['genres'].__contains__('Animation'):
                movie_genre3.append(i)
        
        if len(movie_genre3)<15:
            for i in li2:
                if df.loc[int(i)]['genres'].__contains__('Animation'): 
                    movie_genre2.append(i)
                
        else:
            return(movie_genre3[:15])
        
        
        
        
        if (len(movie_genre3) + len(movie_genre2)) < 15:
            for i in li1:
                if df.loc[int(i)]['genres'].__contains__('Animation'):
                    movie_genre1.append(i)
                
        else:
            dem1 = movie_genre3 + movie_genre2
            
            for i in dem1:
                if i in movie_genre32:
                    continue
                else:
                    movie_genre32.append(i)
            return(movie_genre32[:15])
        
        dem2 = movie_genre3 + movie_genre2 + movie_genre1
        for i in dem2:
            if (i in movie_genre321):
                continue
            else:
                movie_genre321.append(i)
        return (movie_genre321[:15])

