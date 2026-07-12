import streamlit as st
import pandas as pd
import pickle

# Movie Recommendation System
st.title("🎬 Movie Recommendation System")

st.write("Select a movie and get similar movie recommendations.")

# Load movie dataset
df = pd.read_pickle("movies_data.pkl")

# Load similarity matrix
with open("similarity.pkl", "rb") as file:
    similarity_matrix = pickle.load(file)


# Function to recommend movies
def recommend(movie_name):

    # Find movie index
    movie_index = df[df["title"] == movie_name].index[0]

    # Get similarity scores
    distance = similarity_matrix[movie_index]

    movie_list = list(enumerate(distance))

    # Sort movies according to similarity
    movie_list = sorted(movie_list, key=lambda x: x[1], reverse=True)

    recommended_movies = []

    # Get top 5 similar movies
    for movie in movie_list[1:6]:

        index = movie[0]

        title = df.iloc[index]["title"]

        recommended_movies.append(title)

    return recommended_movies


# Movie names for dropdown
movie_names = df["title"].tolist()

selected_movie = st.selectbox(
    "Choose a Movie",
    movie_names
)


# Show recommendations
if st.button("Recommend Movies"):

    movies = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in movies:
        st.write("•", movie)