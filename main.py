from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt

# connect to website
url = 'https://www.imdb.com/title/tt0108778/episodes?season='
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/108.0.0.0 Safari/537.36'}
friends_data = []
friends_data_season = {}

for s in range(1, 11):
    season_set = []
    page = requests.get(url + str(s), headers=header)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    episodes = soup2.findAll('div', {'class': 'list_item'})
    for episode in episodes:
        title = episode.findAll('a', {'itemprop': 'name'})
        airdate = episode.findAll('div', {'class': 'airdate'})
        rating = episode.findAll('span', {'class': 'ipl-rating-star__rating'})
        num_votes = episode.findAll('span', {'class': 'ipl-rating-star__total-votes'})
        description = episode.findAll('div', {'class': 'item_description'})
        row_data = [title[0].text, airdate[0].text, rating[0].text, num_votes[0].text.replace('(', '').replace(')', '')
        .replace(',', ''), description[0].text]
        for i in range(len(row_data)):
            row_data[i] = row_data[i].replace('\n', '').strip()
        friends_data.append(row_data)
        season_set.append(row_data)
    friends_data_season['Season'+str(s)] = season_set

df = pd.DataFrame(friends_data, columns=['Title','AirDate','Rating','Num_Votes','Description'])
print(df.head())
for s in range(1,11):
    df = pd.DataFrame(friends_data_season['Season'+str(s)],columns=['Title','AirDate','Rating','Num_Votes',
                                                                    'Description'])

print(df.head())
