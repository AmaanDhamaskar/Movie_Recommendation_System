import pandas as pd  
from numpy import*
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_index_from(df,title):
    return df[df['title']==title].index.values[0]

def combined_features(row):
    return row['production_companies']+" "+row['genres']+" "+row['credits']

def get_title_from_index(df,index):
        return df.loc[index][1]
    
def recommend(movie_user_like):
    ls={}
    df=pd.read_csv("refinedMovies.csv")
    features =['production_companies','genres','credits']

    df['combined_features']=df.apply(combined_features,axis=1)
    cv=CountVectorizer()
    count_matrix=cv.fit_transform(df['combined_features'])
    cosine_sim=cosine_similarity(count_matrix)

    movie_index=get_index_from(df,movie_user_like)
    similar_movies=list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies,key= lambda x:x[1],reverse=True)
    
    i=0
    for movies in sorted_similar_movies:
        if df.loc[movies[0]]['genres'].__contains__('Animation'):
            ls[df.loc[movies[0]][0]]=(get_title_from_index(df,movies[0]))
            i=i+1
            if i>15:
                return ls
    
