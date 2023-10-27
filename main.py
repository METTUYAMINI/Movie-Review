import requests
import re
from bs4 import BeautifulSoup
from tabulate import tabulate

movie_name = str(input("Enter Movie Name : "))

url = f"https://www.google.com/search?q={movie_name}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

rating = {}

def imdb_rating(url):
    url = url + " movie review IMDB"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        response_text = str(soup)
        rating = re.search(r"(\d+\.\d+)/10", response_text)
        
        if rating:
            extracted_rating = rating.group(1)
            return extracted_rating + "/10"
        else:
            return "Rating not found"
        
    else:
        return "Response Error"
    
def rotten_tomatoes_rating(url):
    url = url + " movie review rotten tomatoes"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        response_text = str(soup)
        rating = re.search(r"(\d+\.\d+)/5", response_text)
        
        if rating:
            extracted_rating = rating.group(1)
            return extracted_rating + "/5"
        else:
            return "Rating not found"
        
    else:
        return "Response Error"
    
def times_of_india_rating(url):
    url = url + " movie rating times of india"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        response_text = str(soup)
        rating = re.search(r"(\d+\.\d+)/5", response_text)
        
        if rating:
            extracted_rating = rating.group(1)
            return extracted_rating + "/5"
        else:
            return "Rating not found"
        
    else:
        return "Response Error"
    
rating["IMDB"] = imdb_rating(url)
rating["Rotten Tomatoes"] = rotten_tomatoes_rating(url)
rating["Times of India"] = times_of_india_rating(url)

table_data = [[website, rating] for website, rating in rating.items()]

table = tabulate(table_data, headers=['Website', 'Rating'], tablefmt='grid')

print(f"Movie Name: {movie_name}")
print(table)
