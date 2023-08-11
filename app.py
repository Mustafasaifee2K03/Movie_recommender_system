import streamlit as st
import pickle
import pandas as pd
import requests
import helper
# load the dataset object that we preprocessed in the file preprocessing.ipynb
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
# print(type(movies_dict))
#Convert it to a pandas dataframe 
movies=pd.DataFrame(movies_dict)
st.title('Movie Recommender System')
selected_movie_name=st.selectbox(
'Select a movie',
movies['title'].values
)
similarity=pickle.load(open('similarity.pkl','rb'))
if st.button('Recommend Similar Movies'):
   names,posters=helper.recommend_movies(selected_movie_name,lower_limit=1,upper_limit=7)
   col1,col2,col3,col4,col5,col6=st.columns(6)
   with col1:
      st.text(names[0])
      st.image(posters[0])
   with col2:
      st.text(names[1])
      st.image(posters[1])
   with col3:
      st.text(names[2])
      st.image(posters[2])
   with col4:
      st.text(names[3])
      st.image(posters[3])
   with col5:
      st.text(names[4])
      st.image(posters[4])
   with col6:
      st.text(names[5])
      st.image(posters[5])
