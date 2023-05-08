import pandas as pd 
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
def get_index_from(df,movie_title):
    return df[df['title']==movie_title].index.values[0]

def combined_features(row):
    return row['production_companies']+" "+row['genres']+" "+row['credits']

def get_title_from_index(df,index):
        return df.loc[index][1]
    
df=pd.read_csv("C:\\Users\\sanket\\coding\\python\\pythonVS\\PyQt5\\refinedMovies.csv")
features =['production_companies','genres','credits']
df['combined_features']=df.apply(combined_features,axis=1)
cv=CountVectorizer()
movie_matrix=cv.fit_transform(df['combined_features'])

# train_data, test_data = train_test_split(movie_matrix, test_size=0.2,random_state=42)

knn_model = NearestNeighbors(metric='cosine',algorithm='brute',n_neighbors=5)
knn_model.fit(movie_matrix)

def get_similar_movies(movie_title):
    movie_index=get_index_from(df,movie_title)
    distances,indices=knn_model.kneighbors(movie_matrix[movie_index].reshape(1,-1),n_neighbors=15)
    similar_movies =[]
    for i in range(len(indices.flatten())):
        if i==0:
            print("Recoomendationsfor",df['title'][movie_index])
        else:
            similar_movies.append(df['title'][indices.flatten()[i]])
            print(i,":",df['title'][indices.flatten()[i]])
            
    # return similar_movies
      
