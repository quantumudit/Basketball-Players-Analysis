import numpy as np
import pandas as pd
from raw_basketball_players_data import *

# -- Creating Individual DataFrames by Measures -- #

salary_df = pd.DataFrame(data=salary, columns=years, index=players)
salary_df["Measure"] = "Salary"

games_df = pd.DataFrame(data=games, columns=years, index=players)
games_df["Measure"] = "Games Played"

minutes_played_df = pd.DataFrame(data=minutes_played, columns=years, index=players)
minutes_played_df["Measure"] = "Minutes Played"

field_goals_df = pd.DataFrame(data=field_goals, columns=years, index=players)
field_goals_df["Measure"] = "Field Goals"

field_goal_attempts_df = pd.DataFrame(data=field_goal_attempts, columns=years, index=players)
field_goal_attempts_df["Measure"] = "Field Goal Attempts"

points_df = pd.DataFrame(data=points, columns=years, index=players)
points_df["Measure"] = "Points"

# -- Combining Individual DataFrames -- #

combined_df = pd.concat([salary_df, games_df, minutes_played_df, field_goals_df, field_goal_attempts_df, points_df])
combined_df.index.name = "Player"

# -- Resetting Index -- #

combined_df.reset_index(level=0, inplace=True)

# -- Rearranging Columns --#

reordered_cols = ["Player","Measure", "2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]

pivoted_df = combined_df.reindex(columns=reordered_cols)

# -- Unpivoting Dataset --#

id_cols = ["Player","Measure"]

unpivoted_df = pivoted_df.melt(id_vars=id_cols, var_name="Year", value_name="Values")

# -- Naming Index Column --#

unpivoted_df.index.name = "RowID"

# -- Exporting DataFrame into a CSV File --#

unpivoted_df.to_csv('../02_DATA/basketball_players_data.csv')