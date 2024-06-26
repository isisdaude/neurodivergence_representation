from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
import json

OUTPUT = ['schizophrenia', 'bipolar', 'autism', 'intellectual_disability', 'ptsd']

for o in OUTPUT:
    # 1. Filter out the lines to remove
    file_path = "articles_new/html_articles/html_articles_"+ o +".txt"

    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter out the lines to remove
    filtered_lines = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('<div class="dedupHeadlines">') and i+1 < len(lines):
            i += 2  # Skip the line and the following line
        else:
            filtered_lines.append(lines[i])
            i += 1

    # Write the filtered lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

    print("Duplicates removed successfully.")

    # 2. Extract the data from the file
    file = open(file_path, "r")

    file_data = file.read()
    # html_templates = file_data.split("---")
    data = []

    for i in range(1990, 2025):
        index = file_data.find('---'+str(i))
        next_index = file_data.find('---'+str(i+1))

        year = file_data[index+3:index+3+4]
        articles = file_data[index+5:next_index]

        soup = BeautifulSoup(articles, 'html.parser')

        table = soup.find('table')
        if table is None:
            continue
        # Extract the headline
        headline = [th.find('a', class_='enHeadline').get_text().strip() for th in table.find_all("td") if th.find('a') is not None]

        # Extract the publishing journal
        journal = [th.find('a').get_text().strip() for th in table.find_all("div", class_='leadFields') if th.find('a') is not None]

        # Extract the article content (opening)
        opening = [th.find("div", class_='snippet ensnippet').get_text().strip().replace('\n', ' ') for th in table.find_all("td") if th.find("div", class_='snippet ensnippet') is not None]

        # Extract the year of publication
        year = [year] * len(headline)

        # new_dict = dict(zip(data_columns, [headline, opening, journal, year]))
        print(len(headline), len(journal), len(year), len(opening))
        for d in range(len(headline)):
            # print(d)
            new_dict = {'title': headline[d], 'journal': journal[d], 'year': year[d], 'opening': opening[d]}
            data.append(new_dict)

    with open('articles_new/json_articles_' + o + '.json', 'w') as outfile:
        json.dump(data, outfile)    