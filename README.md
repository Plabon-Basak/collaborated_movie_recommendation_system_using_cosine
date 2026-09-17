# Movie Recommendation System (Using Cosine Similarity)

A user-based collaborative filtering movie recommender built with Pandas and scikit-learn. It compares users by cosine similarity of their rating histories and suggests movies you have not rated yet.

## How It Works

1. Loads the rating data from `movie_ratings.csv` (format: `user, movie, rating`).
2. Builds a user x movie matrix and fills missing ratings with 0.
3. Computes the cosine similarity between every pair of users.
4. For the selected user, scores unrated movies based on the ratings of their most similar users.

## Usage

```bash
pip install pandas scikit-learn
python app.py
```

Enter the user ID when prompted. The script prints the recommended movies sorted by score.

## Requirements

- Python 3.x
- `pandas`
- `scikit-learn`

## Note

The CSV loader uses a relative path (`movie_recommendation_app/movie_ratings.csv`), so run the script from the parent directory, or update the path in `app.py`.

## License

This project is provided for educational purposes.