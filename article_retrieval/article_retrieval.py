from bs4 import BeautifulSoup
from pprint import pprint
import json

# file = open("article_retrieval/html_articles_schizophrenia.txt", "r")
file = open("article_retrieval/html_articles_bipolar.txt", "r")
# file = open("article_retrieval/html_articles_autism.txt", "r")
# file = open("article_retrieval/html_articles_intellectual_disability.txt", "r")
# file = open("article_retrieval/html_articles_ptsd.txt", "r")


file_data = file.read()
html_templates = file_data.split("\n")

articles = []

for html_template in html_templates:
    if not html_template.startswith('<br></td></tr><tr class="headline"'):
        continue
    # Parse the HTML template using BeautifulSoup
    soup = BeautifulSoup(html_template, 'html.parser')

    # Extract the headline
    headline = soup.find('td', class_='count').find_next('a').text.strip()

    # Extract the publishing journal
    journal = soup.find('div', class_='leadFields').find('a').text.strip()

    # Extract the year of publication
    year = soup.find('div', class_='leadFields').text.strip()
    year = year.split(',')[1].split(' ')[-1]

    # Extract the article content (opening)
    opening = soup.find('div', class_='snippet').text.strip()

    # Create a dictionary to store the extracted information
    output = {
        'title': headline,
        'journal': journal,
        'year': year,
        'opening': opening
    }

    articles.append(output)

# with open('article_retrieval/json_articles_schizophrenia.json', 'w') as outfile:
#     json.dump(articles, outfile)

with open('article_retrieval/json_articles_bipolar.json', 'w') as outfile:
    json.dump(articles, outfile)

# with open('article_retrieval/json_articles_autism.json', 'w') as outfile:
#     json.dump(articles, outfile)

# with open('article_retrieval/json_articles_intellectual_disability.json', 'w') as outfile:
#     json.dump(articles, outfile)

# with open('article_retrieval/json_articles_ptsd.json', 'w') as outfile:
#     json.dump(articles, outfile)    
    
# # Opening JSON file
# with open('article_retrieval/json_articles_schizophrenia.json', 'r') as openfile:
#     # Reading from json file
#     json_object = json.load(openfile)
 
# pprint(json_object[0:5])