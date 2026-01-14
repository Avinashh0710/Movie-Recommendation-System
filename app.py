import streamlit as st
import pickle
import numpy as np
import pandas as pd

def recommend(movie):
  movie_index = movies[movies['title']==movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)),reverse=True, key= lambda x:x[1])[1:6]
  recommended_movies = []
  for i in movies_list:
    recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies

movies_dict = pickle.load(open('moviedict_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = np.load('similarity.npy')

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
    'which movie you would be like to contacted',
    movies['title'].values
)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
       st.write(i)