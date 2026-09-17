import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_dataset(file_path):
	return pd.read_csv(file_path)

def calculate_similarity(matrix):
	similarity = cosine_similarity(matrix)
	return pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)

def recommend_movies(user_id, ratings_matrix, user_similarity):
    similar_users = user_similarity[user_id].sort_values(ascending=False).index[1:]
    recommended_movies = {}

    for similar_user in similar_users:
        watched_movies = ratings_matrix.loc[similar_user][ratings_matrix.loc[similar_user] > 0]
        for movie, rating in watched_movies.items():
            if ratings_matrix.loc[user_id, movie] == 0:
                if movie not in recommended_movies:
                    recommended_movies[movie] = rating
                else:
                    recommended_movies[movie] += rating

    return sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)


def main():
    print("Welcome to the Movie Recommendation System!")
    ratings = load_dataset("movie_recommendation_app/movie_ratings.csv")
    ratings_matrix = ratings.pivot_table(index="user", columns="movie", values="rating").fillna(0)
    user_similarity = calculate_similarity(ratings_matrix)
    
    user_id = int(input("Enter the user ID for recommendations: "))
    recommendations = recommend_movies(user_id, ratings_matrix, user_similarity)
    print(f"\nRecommendations for User {user_id}:")
    for movie, score in recommendations:
        print(f"{movie}: {score}")

if __name__ == "__main__":
    main()

# ratings = load_dataset("movie_ratings.csv")
# # print(ratings.head())

# ratings_matrix = ratings.pivot_table(index="user", columns="movie", values="rating").fillna(0)
# # print(ratings_matrix)

# user_similarity = calculate_similarity(ratings_matrix)
# # print(user_similarity)

# recommendations = recommend_movies(2, ratings_matrix, user_similarity)
# print("Recommendations for User 1:", recommendations)





