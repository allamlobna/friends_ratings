from bs4 import BeautifulSoup
import pandas as pd
import requests

# connect to website
url = 'https://www.imdb.com/title/tt0108778/episodes?season='
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/108.0.0.0 Safari/537.36'}
# episode data
friends_data = []
# s = season
for s in range(1, 11):
    page = requests.get(url + str(s), headers=header)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    episodes = soup2.findAll('div', {'class': 'list_item'})
    episode_num = 0
    for episode in episodes:
        # parsing html page for info
        title = episode.findAll('a', {'itemprop': 'name'})
        airdate = episode.findAll('div', {'class': 'airdate'})
        rating = episode.findAll('span', {'class': 'ipl-rating-star__rating'})
        num_votes = episode.findAll('span', {'class': 'ipl-rating-star__total-votes'})
        episode_num = episode_num + 1
        episode_num2 = str(episode_num)
        season_num = str(s)
        description = episode.findAll('div', {'class': 'item_description'})
        # creates a row per episode with parsed data
        row_data = [title[0].text, airdate[0].text, rating[0].text, num_votes[0].text.replace('(', '').replace(')', '')
        .replace(',', ''), season_num, episode_num2, description[0].text]
        # cycles through row_data and removes \n and extra space
        for i in range(len(row_data)):
            row_data[i] = row_data[i].replace('\n', '').strip()
        #adds info for each episode to friends_data
        friends_data.append(row_data)
# creates data frame of friends_data
df = pd.DataFrame(friends_data, columns=['title','airdate','rating','num_votes', 'season_num', 'episode_num', 'description'])
print(df.head())
#exports data to csv
df.to_csv('TheFriendsIMDBPerEpisode.csv', index=False)
