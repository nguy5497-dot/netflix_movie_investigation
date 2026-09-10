import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')

# Part 1: Most frequent movie duration in the 1990's

# Filter dataframe to only select movies during the 1990's
movies_1990s = netflix_df[netflix_df['release_year'].between(1990, 1999)]

#Select duration only
freq_dur = movies_1990s['duration']

plt.figure()
plt.hist(freq_dur, bins=50)
plt.xticks(range(0, 200, 15))
plt.title('Most frequent movie duration in the 1990s')
plt.xlabel('Duration in minutes')
plt.ylabel('Number of occurences')
plt.show()

# Part 2: The most common movie genre in the 1990's

movie_genres = movies_1990s['genre']

plt.figure()
plt.hist(movie_genres, bins=11)
plt.xticks(rotation=45, ha='right', fontsize=5)
plt.title('Most common movie genre in the 1990s')
plt.xlabel('Movie genre')
plt.ylabel('Number of occurences')
plt.show()

# Part 3: The country that produced the most Action movies in the 1990's

action_movies_country = (movies_1990s[movies_1990s['genre'] == 'Action'])['country']

print(action_movies_country.value_counts())

plt.figure()
plt.hist(action_movies_country, bins=7)
plt.xticks(rotation=45, ha='right', fontsize=5)
plt.title('Countries that produced the most 1990s Action movies')
plt.xlabel('Country')
plt.ylabel('Number of occurences')
plt.show()


