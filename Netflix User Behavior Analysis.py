# Netflix User Behavior Analysis (Console Version)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic Netflix viewing dataset
np.random.seed(42)
users = [f'User{i}' for i in range(1, 101)]
titles = ['Stranger Things', 'Breaking Bad', 'The Crown', 'Black Mirror', 'The Witcher', 'Money Heist']
genres = ['Drama', 'Thriller', 'Sci-Fi', 'Action', 'Fantasy']
dates = pd.date_range(start='2024-01-01', periods=60)
data = []

for _ in range(1000):
    user = np.random.choice(users)
    title = np.random.choice(titles)
    genre = np.random.choice(genres)
    hours_watched = np.random.exponential(scale=2.0)
    rating = np.random.randint(1, 6)
    date = np.random.choice(dates)
    data.append([user, title, genre, hours_watched, rating, date])

df = pd.DataFrame(data, columns=['User', 'Title', 'Genre', 'HoursWatched', 'Rating', 'Date'])
df.to_csv("netflix_data.csv", index=False)
print("Saved dataset as netflix_data.csv")

# Top genres by total watch hours
top_genres = df.groupby('Genre')['HoursWatched'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
top_genres.plot(kind='bar', color='purple')
plt.title("Top Genres by Total Watch Hours")
plt.ylabel("Total Hours Watched")
plt.tight_layout()
plt.show()

# Watch hours per user
user_hours = df.groupby('User')['HoursWatched'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 5))
user_hours.plot(kind='bar', color='orange')
plt.title("Top 10 Users by Watch Hours")
plt.ylabel("Total Hours Watched")
plt.tight_layout()
plt.show()

# Binge behavior: number of sessions per user
sessions = df.groupby('User').size().sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 5))
sessions.plot(kind='bar', color='teal')
plt.title("Top 10 Users by Viewing Sessions")
plt.ylabel("Number of Sessions")
plt.tight_layout()
plt.show()

# Ratings vs genres
plt.figure(figsize=(10, 6))
df.boxplot(column='Rating', by='Genre', grid=False)
plt.title("Ratings by Genre")
plt.suptitle("")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

# Show data sample
print("\nSample Data:")
print(df.head())
