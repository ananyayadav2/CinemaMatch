🎬 CinemaMatch
CinemaMatch is a content-based movie recommendation system built with Python. It suggests movies to users based on their interests by analyzing movie metadata such as genres, keywords, cast, and crew.

🚀 Live Demo
You can check out the live application here: https://cinemamatch-iai.streamlit.app/

✨ Features
Search Functionality: Quickly find a movie from a database of thousands.

Similarity Scoring: Uses advanced vectorization to find movies with similar themes.

Poster Integration: Fetches real-time movie posters using the TMDB API.

Interactive UI: Clean and responsive interface powered by Streamlit.

🛠️ Technical Stack
Language: Python

Web Framework: Streamlit

Data Manipulation: Pandas, NumPy

Machine Learning: Scikit-learn (CountVectorizer & Cosine Similarity)

API: TMDB (The Movie Database)

⚙️ How it Works
Data Preprocessing: The dataset is cleaned by merging tags (genres, keywords, cast, and director) into a single column.

Vectorization: Text data is converted into numerical vectors using Bag of Words (CountVectorizer).

Similarity Calculation: We calculate the Cosine Similarity between movie vectors to determine how "close" two movies are in terms of content.

Recommendation: When a user selects a movie, the system identifies the top 5 movies with the highest similarity scores.
