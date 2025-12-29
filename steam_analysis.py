import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PEAK PLAYERS EACH YEARS

df = pd.read_csv('Valve_Player_Data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

peak_players_each_years = (
    df.groupby(df['Date'].dt.to_period('Y'))['Peak_Players']
    .max()
    .sort_values(ascending=False)
)

sns.barplot(x=peak_players_each_years.values, y=peak_players_each_years.index, palette='pastel')
plt.title('Peak Players in each years')
plt.xlabel('Total Peak Players')
plt.ylabel('Years')
plt.tight_layout()
plt.grid(axis='x')
plt.show()

# AVERAGE PLAYERS EACH YEARS

avg_players_each_years = (
    df.groupby(df['Date'].dt.to_period('Y'))['Avg_players']
    .mean()
    .sort_values(ascending=False)
)

sns.barplot(x=avg_players_each_years.values, y=avg_players_each_years.index, palette='pastel')
plt.title('Average Players in each years')
plt.xlabel('Total Average Players')
plt.ylabel('Years')
plt.tight_layout()
plt.grid(axis='x')
plt.show()

df_sorted = df.sort_values(['Game_Name', 'Date'])

players_change = (
    df_sorted
    .groupby('Game_Name')['Avg_players']
    .diff()
)


top_game_year = (
    df.groupby([df['Date'].dt.year, 'Game_Name'])['Avg_players']
    .mean()
    .reset_index()
    .sort_values('Avg_players', ascending=False) ## ---
    .head(10)
)

#print(top_game_year)

top_game_alltime = (
    df.groupby(['Game_Name'])['Avg_players']
    .max()
    .sort_values(ascending=False)
    .head(10)
)

print(top_game_alltime)

print()
# cезон

def get_season(months):
    if months in [12, 1, 2]:
        return 'Winter'
    elif months in [3, 4, 5]:
        return 'Spring'
    elif months in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'
    
df['Season'] = df['Date'].dt.month.apply(get_season)
df['Year'] = df['Date'].dt.year


top_game_season = (
    df.groupby(['Year','Season'])['Avg_players']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

top_season_each_year = (
    top_game_season
    .loc[top_game_season.groupby('Year')['Avg_players'].idxmax()]
)
print(top_game_season)