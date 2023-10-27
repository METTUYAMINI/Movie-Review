# Movie Rating Web Scraper

This Python script allows users to input a movie name and retrieves its ratings from various movie review websites, including IMDB, Rotten Tomatoes, and Times of India. The script uses web scraping techniques to extract the ratings from the search results of Google.

## Prerequisites:

-Python 3.x
-Required libraries:
-requests
-re
-bs4 (Beautiful Soup)
-tabulate
Make sure to install the required libraries using pip install requests beautifulsoup4 tabulate.

## How to Use:

Run the script in a Python environment.
Input the movie name when prompted.
The script will fetch ratings from IMDB, Rotten Tomatoes, and Times of India for the specified movie.
It will then display the ratings in a tabulated format.

## Code Explanation:

The script starts by importing the necessary libraries, setting up user-agent information, and defining a dictionary to store the ratings.
It defines three functions, imdb_rating, rotten_tomatoes_rating, and times_of_india_rating, to extract ratings from the respective websites.
The script then prompts the user to enter a movie name and constructs a Google search URL with the input.
It calls the rating functions for each website and stores the results in the rating dictionary.
The ratings are displayed in a table format using the tabulate library.

## Note:

Web scraping may be subject to legal and ethical considerations. Ensure that you have the right to access and use the data from the websites.
The script may require adjustments if the structure of the websites being scraped changes.
Disclaimer:
This script is for educational purposes and should be used responsibly and in compliance with the terms and conditions of the websites being scraped.
