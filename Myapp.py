import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


from sqlalchemy import create_engine
from sqlalchemy import inspect
import sqlite3

st.write("""
# NBA Statistics App
Data Engineering Module at Metis
""")

engine = create_engine("sqlite:///nba_data.db")
inspect(engine).get_table_names()

df = pd.read_csv("merged_df.csv")

st.title("NBA Player Comparrison Dashboard")

st.markdown( "The dashboard will allow for player statistics to be compared across many different statistics and window of time." )

st.sidebar.title('Select Desired Statistics and Time Frame')

# st.sidebar.markdown('Select the Charts/Plots accordingly:')

# chart_visual = st.sidebar.selectbox('Select Charts/Plot type', ('Line Chart', 'Bar Chart', 'Bubble Chart'))

# st.sidebar.checkbox("Choose different options for analysis", True, key=1)
stat_types = selected_status = st.sidebar.selectbox('Select Statistical Categories', options=['Traditional', 'Shooting', 'Rebounds', 'Steals'])

time_types = selected_status = st.sidebar.selectbox('Select Window of Time', options=['Beginning of Career', 'Game', 'Season', 'Real Time'])

player_choice1 = st.text_input('First Player Name')    
player_choice2 = st.text_input('Second Player Name')

query1 = f'''SELECT  SEASON_ID, AVG(PTS) as AVG_PTS, AVG(STL) as AVG_STL, AVG(REB) as AVG_REB, AVG(AST) as AVG_AST, AVG(FG_PCT) as AVG_FG_PCT, AVG(FGM) as AVG_FGM, AVG(FG3_PCT) as AVG_FG3_PCT, AVG(FTM) as AVG_FTM, AVG(FT_PCT) as AVG_FT_PCT, AVG(FG3M) as AVG_FG3M, full_name FROM nba_all_games WHERE full_name = '{player_choice1}' GROUP BY SEASON_ID '''

query2 = f'''SELECT  SEASON_ID, AVG(PTS) as AVG_PTS, AVG(STL) as AVG_STL, AVG(REB) as AVG_REB, AVG(AST) as AVG_AST, AVG(FG_PCT) as AVG_FG_PCT, AVG(FGM) as AVG_FGM, AVG(FG3_PCT) as AVG_FG3_PCT, AVG(FTM) as AVG_FTM, AVG(FT_PCT) as AVG_FT_PCT, AVG(FG3M) as AVG_FG3M, full_name FROM nba_all_games WHERE full_name = "{player_choice2}"  GROUP BY SEASON_ID '''

player1_all_stats_avg = pd.read_sql(query1, engine)
player2_all_stats_avg = pd.read_sql(query2, engine)

if player1_all_stats_avg['full_name'].count() > player2_all_stats_avg['full_name'].count():
    x_tick_length = player1_all_stats_avg['full_name'].count()
else:
    x_tick_length = player2_all_stats_avg['full_name'].count()

# player1_assist_avg = pd.read_sql(query1, engine)
# player2_assist_avg = pd.read_sql(query2, engine)

# player1_rebound_avg = pd.read_sql(query1, engine)
# player2_rebound_avg = pd.read_sql(query2, engine)

# player1_steal_avg = pd.read_sql(query1, engine)
# player2_steal_avg = pd.read_sql(query2, engine)


# fig, ax = plt.subplots()

# ax.hist(data['PRICE'])
# ax.set_title('Distribution of House Prices in $100,000s')

# show_graph = st.checkbox('Show Graph', value=True)

# if show_graph:
#     st.pyplot(fig)





if stat_types == 'Traditional' and time_types == 'Beginning of Career':

    fig = plt.figure(figsize=[20,14])

    plt.suptitle('Career Averages',fontsize = 34)

    plt.subplot(2,2,1)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_PTS'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_PTS'], linewidth=4)
    plt.title('Points per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.legend([player_choice1, player_choice2], fontsize=20)
    # plt.xticks(np.linspace(1, x_tick_length, x_tick_length)

    plt.subplot(2,2,2)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_AST'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_AST'], linewidth=4)
    plt.title('Assists per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(2,2,3)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_REB'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_REB'], linewidth=4)
    plt.title('Rebounds per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(2,2,4)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_STL'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_STL'], linewidth=4)
    plt.title('Steals per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.show()
    st.pyplot(fig)


if stat_types == 'Shooting' and time_types == 'Beginning of Career':

    fig = plt.figure(figsize=[20,21])

    plt.suptitle('Shooting Statistics',fontsize = 34)

    plt.subplot(3,2,1)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FGM'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FGM'], linewidth=4)
    plt.title('Average Field Goals Made', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.legend([player_choice1, player_choice2], fontsize=20)
    # plt.xticks(np.linspace(1, x_tick_length, x_tick_length)

    plt.subplot(3,2,2)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FG_PCT'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FG_PCT'], linewidth=4)
    plt.title('Average Field Goal Percentage', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,3)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FTM'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FTM'], linewidth=4)
    plt.title('Average Free Throws Made', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,4)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FT_PCT'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FT_PCT'], linewidth=4)
    plt.title('Average Free Throw Percentage', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,5)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FG3M'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FG3M'], linewidth=4)
    plt.title('Made Threes per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,6)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FG3_PCT'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FG3_PCT'], linewidth=4)
    plt.title('Average Three Point Percentage', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.show()
    st.pyplot(fig)


# test_fig = plt.figure(figsize=(10, 4))
# test_fig, axs = plt.subplots(nrows=1, ncols=2)
# st.pyplot(test_fig)




# if stat_types == 'Points':
    # query = f'''SELECT full_name, PTS FROM nba_all_games WHERE full_name = "{player_choice}" ORDER BY PTS DESC'''

    # player_point_avg = np.mean(pd.read_sql(query, engine)['PTS'])

#     st.write(
#         f"{player_choice} averages {round(player_point_avg, 1)} points per game.")

# if stat_types == 'Assists':
#     query = f'''SELECT full_name, AST FROM nba_all_games WHERE full_name = "{player_choice}" ORDER BY PTS DESC'''
    
#     player_assist_avg = np.mean(pd.read_sql(query, engine)['AST'])

#     st.write(
#         f"{player_choice} averages {round(player_assist_avg, 1)} assists per game.")

# if stat_types == 'Rebounds':
#     query = f'''SELECT full_name, REB FROM nba_all_games WHERE full_name = "{player_choice}" ORDER BY PTS DESC'''
    
#     player_rebound_avg = np.mean(pd.read_sql(query, engine)['REB'])

#     st.write(
#         f"{player_choice} averages {round(player_rebound_avg, 1)} rebounds per game.")

# if stat_types == 'Steals':
#     query = f'''SELECT full_name, STL FROM nba_all_games WHERE full_name = "{player_choice}" ORDER BY PTS DESC'''
    
#     player_steal_avg = np.mean(pd.read_sql(query, engine)['STL'])

#     st.write(
#         f"{player_choice} averages {round(player_steal_avg, 1)} steals per game.")


