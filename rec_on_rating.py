import os
import pandas as pd
from datetime import datetime


# os.chdir("E:\\Python_Project_Ayush\\Final Login and sign up page\\Python Tkinter Modern GUI login and sign up form")
def rec_on_top():
    movies_df = pd.read_csv("refinedmovies.csv",index_col=0)

    movies_df["release_date"] = pd.to_datetime(movies_df["release_date"])

    start_date = datetime.strptime("1/1/2023", "%d/%m/%Y")
    movies_2023_df = movies_df[(movies_df["release_date"] >= start_date) ]

    sorted_movies_df = movies_2023_df.sort_values(by="vote_average", ascending=False)
    ls=[]
    for s,i in enumerate(sorted_movies_df.index):
        if s<10:
            ls.append(i)
    return ls


##or we can use this 
#top_movie = sorted_movies_df.head(15)
#print("Based on the top-rated movies of 2014:\n",
#      top_movie["title"])