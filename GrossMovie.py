import os
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')

os.chdir("/Users/ming/PycharmProjects/Numpy")
os.getcwd()
data = pd.read_csv("MovieData.csv",encoding ='latin1')

data.describe()
data.head()
data.info()

data.Genre = data.Genre.astype('object')
data.Studio = data.Studio.astype('object')
data.info()

data.columns = ['DayOfWeek', 'Director', 'Genre', 'MovieTitle', 'ReleaseDate',\
                'Studio', 'AdjustedGross($mill)', 'Budget($mill)', 'Gross($mill)',\
                'IMDb Rating', 'MovieLensRating', 'Overseas($mill)', 'Overseas%',\
                'Profit ($mill)', 'Profit%', 'Runtime(min)', 'US($mill)',\
                'Gross%US']


data.columns

#Filtering Dataset
#dataGenre = data[(data.Genre == 'action') | (data.Genre == 'adventure') | (data.Genre == 'animation') | (data.Genre == 'comedy') | (data.Genre == 'drama')]
#dataStudio = data[(data.Studio == 'Buena Vista Studios') | (data.Studio == 'Fox') | (data.Studio == 'Paramount Pictures') | (data.Studio == 'Sony') | (data.Studio == 'Universal') | (data.Studio == 'WB')]

#quicker way of Filtering:
DataGen = ['action','adventure','animation','comedy','drama']
filter1 = data[data.Genre.isin(dataGenre)]

filter1.Genre.unique()

DataStu = ['Buena Vista Studios','Fox','Paramount Pictures','Sony','Universal','WB'] #Filtering studio based on genre filter1
filter2 = filter1[data.Studio.isin(DataStu)]

filter2.Studio.unique()

dataGenre['Genre'].unique()
dataStudio['Studio'].unique()
len(filter2) #check length to see if filtering applied
filter2
print("Hello World")
_
#Create style
sns.set(style="darkgrid", palette='muted', color_codes=True)
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
ax = sns.boxplot(data=filter2,x='Genre',y='Gross%US',color='lightgray',linewidth=3, orient='v', showfliers=False)
plt.setp(vis1.artists, alpha=0.5)
#vis1.set_xticklabels(vis1.get_xticklabels(),rotation=30) #Rotates xtick labels
sns.stripplot(data = filter2, x='Genre',y='Gross%US', jitter=True, hue='Studio', linewidth=0)

ax.axes.set_title('Domestic Gross % By Genre',fontsize=30)
ax.set_xlabel('Gross % US',fontsize=20)
ax.set_ylabel('Genre',fontsize=20)

# Define where to place the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
