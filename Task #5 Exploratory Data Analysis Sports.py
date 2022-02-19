#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Exploratory Data Analysis : Sports (Indian Premier League)


# In[6]:


#Importing Modules
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import linear_model


# In[8]:


#Importing First Dataset
ipl_matches = pd.read_csv("C:\\Users\\user\\Downloads\\Indian Premier League\\matches.csv")
ipl_matches


# In[11]:


ipl_delveries = pd.read_csv("C:\\Users\\user\\Downloads\\Indian Premier League\\deliveries.csv")
ipl_delveries


# In[12]:


#Data Preparation and Cleaning
ipl_matches.info()


# In[13]:


ipl_matches.describe()


# In[14]:


ipl_matches.columns


# In[15]:


#Let’s view the unique values of each column to help us understand the dataset better.
for col in ipl_matches:
    print(ipl_matches[col].unique())


# In[16]:


#the first index that doesn't contain a NaN value 
ipl_matches.umpire3.first_valid_index()


# In[17]:


#Confirming the first valid index
ipl_matches.loc[633:640]


# In[18]:


ipl_matches.isnull().sum()


# In[19]:


ipl_matches = ipl_matches.drop(columns=['umpire3'], axis=1)


# In[21]:


ipl_delveries.info()


# In[ ]:


#For Better Data Analysis Replacing all the IPL Team Names By Shorter Names


# In[22]:


#Replacing the Full names of IPL TEAMS by short names
ipl_matches.replace(['Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings',
                 'Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab',
                 'Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors','Rising Pune Supergiant']
                ,['MI','KKR','RCB','DC','CSK','RR','DD','GL','KXIP','SRH','RPS','KTK','PW','RPS'],inplace=True)


# In[24]:


#Replacing the Full names of IPL TEAMS by short names
ipl_delveries.replace(['Mumbai Indians','Kolkata Knight Riders','Royal Challengers Bangalore','Deccan Chargers','Chennai Super Kings',
                 'Rajasthan Royals','Delhi Daredevils','Gujarat Lions','Kings XI Punjab',
                 'Sunrisers Hyderabad','Rising Pune Supergiants','Kochi Tuskers Kerala','Pune Warriors','Rising Pune Supergiant']
                ,['MI','KKR','RCB','DC','CSK','RR','DD','GL','KXIP','SRH','RPS','KTK','PW','RPS'],inplace=True)


# In[26]:


# merging seasons column in deliveries dataset which will be helpful in further analysis for each season
ipl_delveries = ipl_delveries.merge(ipl_matches["season"], left_on=ipl_delveries.index, right_on=ipl_matches.index)


# In[ ]:


#Exploratory Data Analysis(EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods.


# In[27]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.color_palette("Paired")
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (12, 8)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[ ]:


#ANALYSIS-1


# In[28]:


teams_per_season = ipl_matches.groupby('season')['winner'].value_counts()
teams_per_season


# In[29]:


"""
for i, v in win_per_season.iteritems():
    print(i, v)
    
for items in win_per_season.iteritems():
    print(items)    
"""
year = 2008
win_per_season_df = pd.DataFrame(columns=['year', 'team', 'wins'])
for items in teams_per_season.iteritems():    
    if items[0][0]==year:
        print(items)
        win_series = pd.DataFrame({
            'year': [items[0][0]],
            'team': [items[0][1]],
            'wins': [items[1]]
        })
        win_per_season_df = win_per_season_df.append(win_series)
        year += 1   


# In[ ]:


#The number of wins is a discrete value. Hence, we will plot a bar chart(barplot in Seaborn).


# In[30]:


plt.title("Team Wise Win Per Season")
sns.barplot('wins', 'team', hue='year', data=win_per_season_df, palette='Paired');


# In[ ]:


#Observations:
#Mumbai Indians has secured the most wins in four seasons(2010, 2013, 2017, and 2019).


# In[ ]:


#ANALYSIS-2


# In[31]:


venue_ser = ipl_matches['venue'].value_counts()
venue_df = pd.DataFrame(columns=['venue', 'matches'])
for items in venue_ser.iteritems():
    temp_df = pd.DataFrame({
        'venue':[items[0]],
        'matches':[items[1]]
    })
    venue_df = venue_df.append(temp_df, ignore_index=True)


# In[32]:


plt.title("IPL Venues")
sns.barplot(x='matches',y='venue', data=venue_df);


# In[ ]:


#Observations:
# Eden Gardens has hosted the maximum number of IPL matches followed by Wankhede Stadium and M Chinnaswamy Stadium.
#Till 2019, IPL matches were hosted by 40 venues.


# In[33]:


venue_df


# In[ ]:


#ANALYSIS-3
#In a game of sports, every team competes for victory. Hence, the team that has registered the most number of victories is the most successful.


# In[34]:


team_wins_ser = ipl_matches['winner'].value_counts()

team_wins_df = pd.DataFrame(columns=["team", "wins"])
for items in team_wins_ser.iteritems():
    temp_df1 = pd.DataFrame({
        'team':[items[0]],
        'wins':[items[1]]
    })
    team_wins_df = team_wins_df.append(temp_df1, ignore_index=True)


# In[35]:


team_wins_df


# In[36]:


plt.title("Total Victories of IPL Teams")
sns.barplot(x='wins', y='team', data=team_wins_df, palette='Paired');


# In[ ]:


#Observations:
#Mumbai Indians has won the most toss(till 2019) in IPL history.
#All the top teams in IPL are successful in winning the toss as well.

