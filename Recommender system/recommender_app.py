
import streamlit as st
import pandas as pd

# Load datasets
ratings = pd.read_csv('u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])
movie_titles = pd.read_csv('Movie_Id_Titles')

# Merge movie titles into ratings
df = pd.merge(ratings, movie_titles, on='item_id')

# Compute mean ratings and number of ratings
movie_stats = df.groupby('title')['rating'].agg(['mean', 'count']).rename(columns={'mean': 'mean_rating', 'count': 'num_ratings'})

# Create user-movie matrix
user_movie_matrix = df.pivot_table(index='user_id', columns='title', values='rating')

# Function to get recommendations
def get_recommendations(movie_name):
    if movie_name not in user_movie_matrix.columns:
        return pd.DataFrame(columns=['Correlation', 'num_ratings'])

    movie_ratings = user_movie_matrix[movie_name]
    similar_movies = user_movie_matrix.corrwith(movie_ratings)
    corr_df = pd.DataFrame(similar_movies, columns=['Correlation'])
    corr_df.dropna(inplace=True)
    corr_df = corr_df.join(movie_stats['num_ratings'])
    recommendations = corr_df[corr_df['num_ratings'] > 50].sort_values('Correlation', ascending=False).head(10)
    return recommendations

# Streamlit App UI
st.title("🎬 Movie Recommender System")
st.write("Select a movie and get similar movie recommendations.")

movie_list = sorted(user_movie_matrix.columns.dropna().tolist())

selected_movie = st.selectbox("Choose a Movie", movie_list)

if st.button("Recommend"):
    results = get_recommendations(selected_movie)
    if not results.empty:
        st.write("📽️ **Top Recommendations:**")
        st.dataframe(results)
    else:
        st.warning("No recommendations found for this movie.")
