#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:21:11 2024

@author: hiiko
"""
#----------------------------------------------------------------------------------------

# Question 1

import pandas as pd

# Load the dataset
movies = pd.read_csv("movie_dataset.csv")

# Find the highest rating
highest_rating = movies['Rating'].max()

# Find the movie(s) with the highest rating
highest_rated = movies[movies['Rating'] == highest_rating]

print("***************************************")
print("Question 1:")
print("Highest rated movie is:\n")
print(highest_rated[['Title', 'Rating']])
print("***************************************")

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

# Question 2

# Remove none-values
cleaned_data = movies.dropna()

average_revenue = cleaned_data['Revenue (Millions)'].mean()

print("\n Question 2")
print(f"Average Revenue: {average_revenue}")
print("***************************************")

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

# Question 3

# Filter movies from 2015 to 2017
filtered_data = cleaned_data[(cleaned_data['Year'] >= 2015) & (cleaned_data['Year'] <= 2017)]

# Calculate the average revenue
average_revenue = filtered_data['Revenue (Millions)'].mean()

print("\n Question 3")
print(f"\nAverage Revenue (2015-2017): {average_revenue}")
print("***************************************")

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

# Question 4

# Filter for movies released in 2016
movies_2016 = movies[movies['Year'] == 2016]

# Get the count of movies
count_2016_movies = len(movies_2016)

print("\n Question 4")
print(f"Number of movies released in 2016: {count_2016_movies}")
print("***************************************")

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

# Question 5

# Filter for movies directed by Christopher Nolan
nolan_movies = movies[movies['Director'] == 'Christopher Nolan']

# Get the count of movies
count_nolan_movies = len(nolan_movies)

print("\n Question 5")
print(f"Number of movies directed by Christopher Nolan: {count_nolan_movies}")
print("***************************************")

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

# Question 6

# Filter for movies with a rating of at least 8.0
high_rated_movies = movies[movies['Rating'] >= 8.0]

# Get the count of movies
count_high_rated_movies = len(high_rated_movies)

print("\n Question 6")
print(f"Number of movies with a rating of at least 8.0: {count_high_rated_movies}")
print("***************************************")

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# Question 7

# Filter for movies directed by Christopher Nolan
nolan_movies = movies[movies['Director'] == 'Christopher Nolan']

# Calculate the median rating
median_rating_nolan = nolan_movies['Rating'].median()

print("\n Question 7")
print(f"Median rating of Christopher Nolan's movies: {median_rating_nolan}")
print("***************************************")

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# Question 8

# Group by year and calculate the average rating
average_rating_per_year = movies.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year = average_rating_per_year.idxmax()

print("\n Question 8")
print(f"Year with the highest average rating: {year}")
print("***************************************")

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

# Question 9

# Count the number of movies made in 2006 and 2016
movies_2006 = len(movies[movies['Year'] == 2006])
movies_2016 = len(movies[movies['Year'] == 2016])

# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print("\n Question 9")
print(f"Percentage increase in number of movies from 2006 to 2016: {percentage_increase}%")
print("***************************************")

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

# Question 10

# Initialize an empty list for all actors
all_actors = []

# Go through each row in the 'Actors' column and add the actors to the list
for actors in movies['Actors']:
    all_actors += actors.split(', ')  # Split actor names and add them to the list

# Find the most common actor
most_common_actor = max(all_actors, key=all_actors.count)

print("\n Question 10")
print(f"The most common actor is: {most_common_actor}")
print("***************************************")

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

# Question 11

# Initialize an empty list for unique genres
unique_genres = []

# Go through each row in the 'Genre' column
for genres in movies['Genre']:
    # Split genres and check if each genre is already in the list before adding
    for genre in genres.split(', '):
        if genre not in unique_genres:  # Only add the genre if it's not already in the list
            unique_genres.append(genre)

# Find the number of unique genres
num_unique_genres = len(unique_genres)

print("\n Question 11")
print(f"Number of unique genres: {num_unique_genres}")
print("***************************************")

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

# Question 12

"""

1. Budget vs Revenue:
Correlation between budget and revenue could help show whether higher-budget movies tend to generate higher revenues or not.

2. Runtime vs Rating:
This correlation would help us observe how runtime affects audience enjoyment (rating). Are shorter movies mostly well received or not?

3. Year vs Revenue:
This correlation would help indicate the progression of the movie industry. Have newer movies been making more money or not?

4. Votes vs Rating: 
This correlation can help understand whether movies with more audience votes tend to have higher ratings. 

5. Genre vs Revenue: 
This correlation would help us explore whether certain genres tend to generate more revenue than others.


I would advice the directors to use data analytics and statistics to understand what genres and which actors are currently trending and resonate well with viewers.

"""