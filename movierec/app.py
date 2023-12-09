import streamlit as st 
import pickle 
import requests

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=070d32c2abd31dbfa4fbf5ebd4c6da56&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies = pickle.load(open("movies_lst.pkl", 'rb'))

similarity = pickle.load(open("similarity.pkl", 'rb'))

movies_list = movies['title'].values

st.header("Movie Recommender System")

# Create a dropdown to select a movie

selected_movie = st.selectbox("Select a movie:", movies_list)

import streamlit.components.v1 as components

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    
    # Print columns for debugging
    print("Columns in movies DataFrame:", movies.columns)

    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])

    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        # Access the first column if 'id' doesn't exist
        movie_id = movies.iloc[i[0]].iloc[0]
        recommend_movie.append(movies.iloc[i[0]]['title'])
        recommend_poster.append(fetch_poster(movie_id))
    return recommend_movie, recommend_poster



if st.button("Show Recommend"):
    movie_name, movie_poster = recommend (selected_movie)
    coll, col2, col3, col4, col5 = st.columns(5)
    with coll:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])