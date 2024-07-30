import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv(r'P:\mini_project_main\Mini_project_dataset.csv')

def movie_recommender(mood, genre):
    # Filter the dataset based on mood and genre
    filtered_movies = dataset[(dataset['mood'] == mood) & (dataset['genre'] == genre)]

    # Get the list of recommended movies
    recommended_movies = filtered_movies['title'].tolist()

    return recommended_movies

@app.route('/')
def index():
    moods = ['cheerful', 'reflective', 'energetic', 'romantic', 'mysterious', 'gloomy', 'dreamy', 'spooky', 'wild']
    genres = ['drama', 'fantasy', 'romance', 'comedy', 'horror', 'thriller', 'action', 'mystery', 'western']
    return render_template('index.html', moods=moods, genres=genres)

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_mood = request.form['mood']
    selected_genre = request.form['genre']

    recommended_movies = movie_recommender(selected_mood, selected_genre)

    return render_template('recommend.html', recommended_movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
