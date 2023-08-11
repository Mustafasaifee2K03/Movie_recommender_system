# import all the necessary libraries
import pandas as pd
import pickle
import requests
# laod the similarity matrix that contains the matrix of cosine similarities of each tuple with all the tuples
similarity=pickle.load(open('similarity.pkl','rb'))
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
# print(type(movies_dict))
movies=pd.DataFrame(movies_dict)
#fetch the poster of the movie
def fetch_poster(movie_id):
   response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
   data=response.json()
   return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
# def fetch_index(obj,movies):
#     mydf=movies[movies['title']==obj]
#     ans=mydf.index[0]
#     return ans
def recommend_movies(selected_movie_name,lower_limit,upper_limit):
   mydf = movies[movies['title'] == selected_movie_name]
   index_of_movie = mydf.index[0]
   distances = similarity[index_of_movie]
   movie_list = sorted(list(enumerate(similarity[index_of_movie])), reverse=True, key=lambda x: x[1])[lower_limit:upper_limit]
   recommend_movies=[]
   recommend_movies_poster=[]
   for i in movie_list:
      movie_id=movies.iloc[i[0]].movie_id
      recommend_movies.append(movies.iloc[i[0]].title)
      # now we need to fetch the poster of that movie through API
      recommend_movies_poster.append(fetch_poster(movie_id))
   return recommend_movies,recommend_movies_poster
