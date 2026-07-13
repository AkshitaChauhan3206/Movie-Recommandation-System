import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Page title
st.title("🎬 Movie Recommendation System")

st.write("Select a movie and get similar movie recommendations.")


# Load movie dataset
df = pd.read_pickle("movies_data.pkl")


# Check which text column is available
if "clean_text" in df.columns:
    text_column = "clean_text"

elif "tags" in df.columns:
    text_column = "tags"

elif "overview" in df.columns:
    text_column = "overview"

else:
    st.error("Text column not found in dataset.")
    st.stop()


# Fill missing values
df[text_column] = df[text_column].fillna("")


# Convert text into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(df[text_column])


# Calculate cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix)


# Recommendation function
def recommend(movie_name):

    # Get selected movie index
    movie_index = df[df["title"] == movie_name].index[0]

    # Similarity score
    similarity_score = list(enumerate(similarity_matrix[movie_index]))

    # Sort according to similarity
    similarity_score = sorted(
        similarity_score,
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movies = []

    # Top 5 recommendations
    for movie in similarity_score[1:6]:

        movie_title = df.iloc[movie[0]]["title"]

        recommended_movies.append(movie_title)

    return recommended_movies


# Dropdown list
movie_list = df["title"].tolist()

selected_movie = st.selectbox(
    "Choose Movie",
    movie_list
)


# Button
if st.button("Recommend Movies"):

    movies = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in movies:

        st.write(movie)