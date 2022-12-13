from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

friends_df = pd.read_csv('TheFriendsIMDBPerEpisode.csv')
print(friends_df.info())

# change airdate format from object to date
friends_df['airdate'] =pd.to_datetime(friends_df['airdate'], dayfirst=True)



# average rating per season: rating, episode, season, and number of votes
# sort by season then episode ascending
friends_df_avg = friends_df.sort_values(['season_num', 'episode_num'])
# episode_id are episode numbers irrespective of the season
friends_df_avg['episode_id'] = np.arange(len(friends_df_avg)) + 1
friends_df_avg = friends_df_avg.assign(
    rating_avg=friends_df_avg.groupby('season_num')['rating'].transform('mean'),
    rating_med=friends_df_avg.groupby('season_num')['rating'].transform('median')
)
# normalized the avg rating column for better interpretation
friends_df_avg['rating_avg_norm'] = (friends_df_avg['rating_avg'] - friends_df_avg['rating_avg'].min()) / \
                                    (friends_df_avg['rating_avg'].max() - friends_df_avg['rating_avg'].min())

plt.bar(friends_df_avg['season_num'], friends_df_avg['rating_avg_norm'])
plt.ylabel('Average Rating (Normalized)')
plt.xlabel('Season')
plt.title('Average Ratings per Season')
plt.show()

# normalized the avg rating column for better interpretation
friends_df_avg['rating_norm'] = (friends_df_avg['rating'] - friends_df_avg['rating'].min()) / \
                                    (friends_df_avg['rating'].max() - friends_df_avg['rating'].min())
# normalized the avg rating column for better interpretation
plt.plot(friends_df_avg['airdate'], friends_df_avg['rating_norm'])
plt.ylabel('Average Rating (Normalised)')
plt.xlabel('Season')
plt.title('Average Ratings per Season')
date_form = DateFormatter("%m-%d")
plt.show()

