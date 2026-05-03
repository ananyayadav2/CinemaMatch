import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="CinemaMatch", page_icon="🎬", layout="wide")

# Custom CSS for Butter Yellow & Pastel Pink Aesthetic
st.markdown("""
    <style>
    /* Main background - Pastel Pink */
    .stApp {
        background-color: #FFF0F5; /* Lavender Blush / Pastel Pink */
        color: #5D4037;
    }
    
    /* Sidebar - Butter Yellow */
    section[data-testid="stSidebar"] {
        background-color: #FFF9C4;
    }

    /* Titles and Text */
    h1, h2, h3, p {
        color: #8D6E63 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Genre Card styling - Butter Yellow */
    .movie-card {
        background-color: #FFFDE7;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #FBC02D;
        margin-bottom: 20px;
        min-height: 160px;
        text-align: center;
        box-shadow: 3px 3px 12px rgba(0,0,0,0.05);
    }
    
    .movie-card:hover {
        transform: translateY(-5px);
        background-color: #FFFFFF;
        border-color: #F06292;
    }

    /* Styling the IMDb link */
    .imdb-link {
        text-decoration: none;
        color: #F06292;
        font-weight: bold;
        font-size: 1.2em;
    }
    .imdb-link:hover {
        color: #D81B60;
        text-decoration: underline;
    }

    /* Search Input styling */
    .stTextInput>div>div>input {
        background-color: #FFFDE7;
        border: 2px solid #FBC02D;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP HEADER ---
st.title("🎬 CinemaMatch")
st.write("Browse by category or search for a specific title. Click a movie to view it on IMDb!")

# 1. Load the data
@st.cache_data
def load_data():
    movies = pd.read_csv('movies.csv')
    return movies

try:
    movies = load_data()

    # --- TOP SEARCH BAR ---
    search_query = st.text_input("🔍 Search for a movie title:", "")

    # --- SIDEBAR CATEGORY SELECTION ---
    categories = ["Children", "Horror", "Comedy", "Romance", "Action", "Sci-Fi", "Drama", "Animation"]
    st.sidebar.header("Explore Categories")
    selected_genre = st.sidebar.radio("Pick a genre:", categories)

    # --- LOGIC ---
    def get_filtered_movies(genre, query):
        results = movies[movies['genres'].str.contains(genre, case=False)]
        if query:
            results = results[results['title'].str.contains(query, case=False)]
        return results.head(12)

    # --- DISPLAY AREA ---
    display_title = f"✨ Top {selected_genre} Results" if not search_query else f"🔍 Results for '{search_query}'"
    st.subheader(display_title)
    
    recs = get_filtered_movies(selected_genre, search_query)
    
    if recs.empty:
        st.warning("No movies found matching that search in this category.")
    else:
        # Displaying in a 3-column grid
        cols = st.columns(3)
        for i, (index, row) in enumerate(recs.iterrows()):
            # Create a Google/IMDb search link for the movie
            imdb_url = f"https://www.imdb.com/find?q={row['title'].replace(' ', '+')}"
            
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="movie-card">
                        <a href="{imdb_url}" target="_blank" class="imdb-link">{row['title']}</a>
                        <p style="color: #795548; font-size: 0.9em; margin-top: 10px;">
                            {row['genres'].replace('|', ' • ')}
                        </p>
                    </div>
                """, unsafe_allow_html=True)

except Exception as e:
    st.error("Please check if 'movies.csv' is in your project folder!")