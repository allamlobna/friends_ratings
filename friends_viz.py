import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

friends_df = pd.read_csv('TheFriendsIMDBPerEpisode.csv')
print(friends_df.info())

# average rating per season: rating, episode, season, and number of votes
# sort by season then episode ascending
friends_df_avg = friends_df.sort_values(['season_num', 'episode_num'])
# episode_id are episode numbers irrespective of the season
friends_df_avg['episode_id'] = np.arange(len(friends_df_avg))+1
friends_df_avg = friends_df_avg.assign(
    avg=friends_df_avg.groupby('season_num')['rating'].transform('mean')
)
print(friends_df_avg.to_string())
plt.barh(friends_df_avg['season_num'], friends_df_avg['avg'])
plt.xlabel('Average Rating')
plt.ylabel('Season')
plt.title('Average Ratings per Season')
plt.show()
