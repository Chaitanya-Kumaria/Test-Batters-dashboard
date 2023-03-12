# Importing the libraries required
import os
import requests
import json
from urllib.parse import urlencode
import re
import numpy as np
import pandas as pd
from dash import Dash, html, dcc,Input,Output
from bs4 import BeautifulSoup
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Intializing the Dash app
app = Dash(__name__)
# Using Beautiful Soup library to collect the data
# starting by taking year on year data of the player

def get_id(player,type):
    player = player.split()
    url = 'http://www.cricmetric.com/jscripts/search2.py?term='+player[0]+'+'+player[1]+'&'+'category=player'
    request = requests.get(url).json()
    return 'http://www.cricmetric.com/playerstats.py?player='+request['results'][0]['id'].replace(' ','+')+'&role=batsman&format=Test&groupby='+type

#intially starting  with the batting statistics of the players year on year
def year_on_year(player):
    res = requests.get(get_id(player,'year'))
    soup = BeautifulSoup(res.content,'html.parser')
    data_heads = soup.find_all('th')
    data_heads = data_heads[:13]
    data_heads = [data_heads[i].text.strip().split() for i in range(len(data_heads))]
    data_heads_val =[' '.join(i) for i in data_heads]
    data = soup.find_all('div',attrs={'id':'Test-Batting'})
    val  = data[0].find_all('td')
    years = [val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==0]
    innings = [val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==1]
    innings = list(map(int,innings))
    runs= map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==2])
    balls = map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==3])
    outs = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==4])
    avg = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==5])
    sr = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==6])
    hs = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==7])
    fifty = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==8])
    hundered = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==9])
    fours = map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==10])
    sixes = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==11])
    dot_percent = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==12])
    zipped = zip(years,innings,runs,balls,outs,avg,sr,hs,fifty,hundered,fours,sixes,dot_percent)
    df2 = pd.DataFrame(list(zipped),columns=data_heads_val)
    df2.drop(df2.tail(1).index,inplace=True)
    return df2

# player stats versus oppositions
def opp_team(player):
    opp = requests.get(get_id(player,'opp_team'))
    soup = BeautifulSoup(opp.content,'html.parser')
    data_heads = soup.find_all('th')
    data_heads = data_heads[:13]
    data_heads = [data_heads[i].text.strip().split() for i in range(len(data_heads))]
    data_heads_val =[' '.join(i) for i in data_heads]
    data = soup.find_all('div',attrs={'id':'Test-Batting'})
    val  = data[0].find_all('td')
    versus = [' '.join(val[i].text.strip().split()) for i in range(len(val)) if i%13 ==0]
    innings = [val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==1]
    innings = list(map(int,innings))
    runs= map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==2])
    balls = map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==3])
    outs = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==4])
    avg = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==5])
    sr = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==6])
    hs = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==7])
    fifty = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==8])
    hundered = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==9])
    fours = map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==10])
    sixes = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==11])
    dot_percent = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==12])
    zipped = zip(versus,innings,runs,balls,outs,avg,sr,hs,fifty,hundered,fours,sixes,dot_percent)
    df = pd.DataFrame(list(zipped),columns=data_heads_val)
    df.drop(df.tail(1).index,inplace=True)
    return df

# Plyers statistics at different batting positions
def bat_pos(player):
    batting_position = requests.get(get_id(player, 'batpos'))
    soup = BeautifulSoup(batting_position.content,'html.parser')
    data_heads = soup.find_all('th')
    data_heads = data_heads[:13]
    data_heads = [data_heads[i].text.strip().split() for i in range(len(data_heads))]
    data_heads_val =[' '.join(i) for i in data_heads]
    data = soup.find_all('div',attrs={'id':'Test-Batting'})
    val  = data[0].find_all('td')
    batting_pos = [' '.join(val[i].text.strip().split()) for i in range(len(val)) if i%13 ==0]
    innings = [val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==1]
    innings = list(map(int,innings))
    runs= map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==2])
    balls = map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==3])
    outs = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==4])
    avg = [val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==5]
    sr = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==6])
    hs = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==7])
    fifty = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==8])
    hundered = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==9])
    fours = map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==10])
    sixes = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==11])
    dot_percent = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==12])
    zipped = zip(batting_pos,innings,runs,balls,outs,avg,sr,hs,fifty,hundered,fours,sixes,dot_percent)
    df = pd.DataFrame(list(zipped),columns=data_heads_val)
    df['Avg'] = df['Avg'].replace('-',0)
    df['Avg'] = df['Avg'].astype(str).astype(float)
    return df

def vs_bowler_type(player):
    bowler = requests.get(get_id(player,'opp_player_type'))
    soup = BeautifulSoup(bowler.content,'html.parser')
    data_heads = soup.find_all('th')
    data_heads = data_heads[:13]
    data_heads = [data_heads[i].text.strip().split() for i in range(len(data_heads))]
    data_heads_val =[' '.join(i) for i in data_heads]
    data = soup.find_all('div',attrs={'id':'Test-Batting'})
    val  = data[0].find_all('td')
    bowlers = [' '.join(val[i].text.strip().split()) for i in range(len(val)) if i%13 ==0]
    innings = [val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==1]
    innings = list(map(int,innings))
    runs= map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==2])
    balls = map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==3])
    outs = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==4])
    avg = [val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==5]
    sr = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==6])
    hs = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==7])
    fifty = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==8])
    hundered = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==9])
    fours = map(int,[''.join(val[i].text.strip().split()[0].split(',')) for i in range(len(val)) if i%13 ==10])
    sixes = map(int,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==11])
    dot_percent = map(float,[val[i].text.strip().split()[0] for i in range(len(val)) if i%13 ==12])
    zipped = zip(bowlers,innings,runs,balls,outs,avg,sr,hs,fifty,hundered,fours,sixes,dot_percent)
    df = pd.DataFrame(list(zipped),columns=data_heads_val)
    df['Avg'] = df['Avg'].replace('-',0)
    df['Avg'] = df['Avg'].astype(str).astype(float)
    return df
# App layout
app.layout = html.Div([
    html.H1("Welcome to the Test Cricketers Batting dashboard"),
    html.H2("Here you can player name and an interactive dashboard will appear"),
    html.H2([
        "Player Name: ",
        dcc.Input(id='my-input', value='virat kohli', type='text')
    ]),
    html.Br(),
    
  
    html.H2('Player year on year average'),
   
    dcc.Graph(
        id='player_year_on_year_average',
        figure={}
    ),
    html.Br(),
    html.H2('Player Average vs oppositions'),
    dcc.Graph(
        id = 'player_statistics_vs_oppositions',
        figure = {}
    ),
    html.Br(),
    html.H2('Player Average at different batting positions'),
    dcc.Graph(
        id = 'player_statistics_at_different_batting_position',
        figure = {}
    ),
    html.Br(),
    html.H2('Performance vs different bowler types '),
    dcc.Graph(
        id = 'player_vs_diff_bowler_type',
        figure = {}
    )

])
@app.callback(Output(component_id = 'player_year_on_year_average',component_property='figure'),
    Input(component_id='my-input', component_property='value'))

def update_graph(input_value):
    df2 = year_on_year(input_value)
    fig = px.line(df2,x='Year',y='Avg',template = 'plotly_dark', markers=True,title=input_value+" Year on year average")
    fig.update_traces(line=dict(color="orange", width=3.5))

    return fig

@app.callback(Output(component_id = 'player_statistics_vs_oppositions',component_property='figure'),
    Input(component_id='my-input', component_property='value'))
def update_graph(input_value):
    df2 = opp_team(input_value)
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(values = df2['Innings'],labels =df2['Versus Team'],title = input_value+' innings vs team'),1,1)
    fig.add_trace(go.Pie(values=df2['Runs'],labels =df2['Versus Team'],title=input_value+' runs vs team'),1,2)

    fig.update_traces(title_font_size = 30,sort=False,marker=dict(colors=['yellow','green','#8690FF','black','#607D3B','#00ff00','dark blue','maroon','red']))
    return fig
@app.callback(Output(component_id ='player_statistics_at_different_batting_position',component_property='figure'),
    Input(component_id='my-input', component_property='value'))
def update_graph(input_value):
    df2 = bat_pos(input_value)
    fig = px.bar(df2,x = 'Batting Position',y = 'Avg',template = 'plotly_dark',title=input_value+'  batting average at different batting positions',color = 'Batting Position')
    
    return fig

@app.callback(Output(component_id='player_vs_diff_bowler_type',component_property='figure'),Input(component_id = 'my-input', component_property='value'))
def update_graph(input_value):
    df2= vs_bowler_type(input_value)
    df2.drop(df2.tail(1).index,inplace=True)
    fig = px.scatter(df2, x="Innings", y="Avg",
	         size="Runs", color="Versus Player Type",
                 hover_name="Versus Player Type", log_x=True, size_max=60,template='plotly_dark',
                 title= input_value+' performance versus different bowler types')
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
