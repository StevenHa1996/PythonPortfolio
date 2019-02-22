import pandas as pd
import os

os.getcwd()

movies = pd.read_csv('Movie-Ratings.csv')

len(movies)
movies.head()

#rotten tomatoes ratings = critics ratings
movies.columns

#Renaming column
movies.columns = ['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']
#Exploring the dataset:

#movies.info should be used to manually specify variables and changing them to whats most suitable
movies.info() #Year should be changed to category as it will not be used for calculations
movies.describe()


#Changing variable and overiding
movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')

movies.info()

#unique in category
movies.Genre.cat.categories

movies.describe() #We can now see here that the year has been taken off and will only calculate info tht is useful to {us for value in variable}


from matplotlib import pyplot as plt
import seaborn as  sns
import warnings
warnings.filterwarnings('ignore')

#Jointplot
j = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating')
#As we can see on this scatterplot, if we were to draw  a line of fit, we could see
#audiencereviews are higher than critics in most films. however, further down the line
#we can see there are slightly higher critics than audience reviews in some movies.



j = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating', kind='hex')



#Histograms

h1 = sns.distplot(movies.AudienceRating, bins = 15)
#Insights: from this histogram we can see that there is a normal distribution of data throughout.

h2 = sns.distplot(movies.CriticRating, bins = 15)
#Insights: compared to audienceRating, this histogram is uniformed.
#There are some reviews that are just above and below the average.
#This is because Critics, unlike AudienceReviews, behave in a certain way
#They have certain criteria how they mark their movie which is why it isnt normally distributed.
#Its interesting how when people use their natural intuition, we get a normal distributution.
#When critics come into play, there are more rules involved when making a review as theyre going to be based
#on certain criterias. e.g. sound effect, film plot, actors/actresses etc.


#using PLT
m1 = plt.hist(movies.AudienceRating, bins = 15)





#Stacked Histograms

#Filtering
movies[movies.Genre == 'Drama'].BudgetMillions
#Manual stacked histogram
plt.hist([movies[movies.Genre == 'Drama'].BudgetMillions,
         movies[movies.Genre == 'Action'].BudgetMillions,
         movies[movies.Genre == 'Thriller'].BudgetMillions],bins=15, stacked=True)
plt.show()



#movies[movies.Genre == 'Drama'].BudgetMillions gives us the row and budget value

#AUTOMATED

#First needed to apply list into loop
#Create empty list
#Append list with (movies[movies.Genre == gen].BudgetMillions. gen is for every iteration in the list e.g. Action, drama etc
#Apply it to plt.hist

#Legends are created by appending gen



list1 = list()
mylabels = list()

for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)

h1 = plt.hist(list1, bins=30, stacked = True, rwidth = 1, label=mylabels) #rwidth = 1 is 100% not gaps
plt.legend()
plt.show()




#KDE Plot
vis1 = sns.lmplot(data = movies, x ='CriticRating', y='AudienceRating', fit_reg=False, hue='Genre', size=5,aspect=1)

vis1 = sns.lmplot(data = movies, x ='CriticRating', y='AudienceRating', fit_reg=False, hue='Genre', size=5)
k1 = sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade = True, shade_lowest=False, cmap='Reds')
#TIP:
k1b = sns.kdeplot(movies.CriticRating,movies.AudienceRating, cmap='Reds')

#Read up on kernalDensity







#Checking to see whether budget millions affects the audience ratings.

#Working wih subplots
#Code below sets a dark background to see more clearly.
#sns.set_style('dark')
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating)

#insight:
#From this kdeplot we are analysing whether the budget millions can affect
#audience rating.
#we can see that films with a budget of around 25M have from 20-90 audience
#with 50 being the highest density as we can see its the most greenest part of the kdeplot.
#Budgets with around 100M shows us observations that there is a shorter range of audience ratings
#with only a few movies having 40-80 in rating. low density.
#we can see the density getting lower as the budget millions increases.
#higher budgets results in a decrease in audience ratingself.



k2 = sns.lmplot(data=movies, x='BudgetMillions', y='AudienceRating', fit_reg=False, hue='Genre')




#Checking to see whether budget millions affects the critic ratings.
k3 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating)
k4 = sns.lmplot(data=movies,x='BudgetMillions',y='CriticRating', fit_reg=False)

#insights:
#What we can see from this kdeplot is that there is a high density within the
#20-80 mark which then expands out
#We can see that movies with a budget of 50M and over reduces the density but a substantial Amount
#This is because low budget movies are more produced than the higher budgeting companies.


f, axes = plt.subplots(1,2, figsize=(10,5), sharex=True, sharey=True)
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0]) #format: row, columns
k3 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[1])
k1.set(xlim=(-20,160))

#The comparison:
#We can see that in the audience rating kde, we can see ratings is more compact whereas
#CriticRating is more spreadout


#ViolinPlots
x = sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating')


box1 = sns.boxplot(data=movies[movies.Genre=='Drama'], y='CriticRating', x='Year')

#in this boxplot we can compare movie genres to critic ratings
#Lets just say we  were to make a average film. which genre would we go for?
#Thriller would be the best choice because its lowest and highest critic rating is
#much larger than the rest. interquartile range is also one of the largest. Thrillers average
#is larger than the corresponding boxplots
#The smaller the box quartile the bigger the density as we can see in the violin plot





#FacetGrid

g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.scatter, 'CriticRating','AudienceRating')

g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kws = dict(s=5, linewidth=0.5, edgecolor='black')
g = g.map(plt.scatter, 'CriticRating','AudienceRating', **kws)
#Good for comparrison






#Controlling Axes and Adding Diagonals
g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kws = dict(s=50, linewidth=0.5, edgecolor='black')
g = g.map(plt.scatter, 'CriticRating','AudienceRating', **kws)
g.set(xlim=(0,100), ylim=(0,100))
for ax in g.axes.flat: #g.axes represents an array for each subplot. flat iterates it on every subplot
    ax.plot((0,100),(0,100), c='gray', ls='--')
g.add_legend()

#Movies that are above the diagonal line is in favour of audience rating. i.e. there are more audience ratings
#than the criticsa and vice versa
#The subplot above shows audience and critic ratings in genre over the years.



###Building Dashboards###

f, axes = plt.subplots(2,2, figsize=(15,15))
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0,0]) #format: row, columns
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[0,1])
k3 = sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade = True, shade_lowest=False, cmap='Reds',ax=axes[1,0])
#TIP:
k3b = sns.kdeplot(movies.CriticRating,movies.AudienceRating, cmap='Reds', ax=axes[1,0]) #Style is overlayed by using same axes coordinates
#box1 = sns.boxplot(data=movies[movies.Genre=='Drama'], y='CriticRating', x='Year', ax=axes[1,1])
axes[1,1].hist(movies.AudienceRating, bins = 15)#Non sns plot must be formatted with axes paremeter first.
k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))
plt.show()


#plt has axes property, seaborn is like a upgrade from plt however the format is different
#e.g. violin plot is from seaborn library and must be formatted with axes in the end
#plt.hist has axes property within the parameter but is not part of seaborn library and must be coded differently

##More styling. add names

sns.set_style('dark', {"axes.facecolor":"black"}) #Predefined colors: Dark, Darkgrid, White, Whitegrid. using axes to overide predefined color.
f, axes = plt.subplots(2,2, figsize=(15,15))
#Plot1 [0,0]
k1 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, shade = True, shade_lowest=False, cmap='Blues_r', ax=axes[0,0]) #format: row, columns
k1b = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, cmap='gist_gray_r', ax=axes[0,0])#Adds layer for outline no shade for sharper graphics

#Plot2 [0,1]
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, shade = True, shade_lowest=True, cmap='inferno', ax=axes[0,1])
#Plot3 [1,0]
k3 = sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade = True, shade_lowest=True, cmap='Purples',ax=axes[1,0])
k3b = sns.kdeplot(movies.CriticRating, movies.AudienceRating, cmap='Purples',ax=axes[1,0])
#TIP:
k3b = sns.kdeplot(movies.CriticRating,movies.AudienceRating, cmap='Blues', ax=axes[1,0]) #Style is overlayed by using same axes coordinates
#Plot4 [1,1]
box1 = sns.boxplot(data=movies[movies.Genre=='Drama'], y='CriticRating', x='Year', palette='YlOrRd', ax=axes[1,1]) #research sns pallette and cmap colors online or debugger
#axes[1,1].hist(movies.AudienceRating, bins = 15)#Non sns plot must be formatted with axes paremeter first.
k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))
plt.show()


#Touchups
import numpy as np
list1 = list()
mylabels = list()

color1=["Blue","Green","Red","Purple","Yellow","Lightblue","Navy"]

for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)

sns.set_style("whitegrid") #can use for plt libraries
fig, ax = plt.subplots() #create a single subplot in order to amend size
fig.set_size_inches(11.7, 8.27) #A4 paper
h1 = plt.hist(list1, bins=30, stacked = True, rwidth = 1, label=mylabels, color=color1) #rwidth = 1 is 100% not gaps
plt.legend(fancybox=True, shadow=True, frameon=True, framealpha=1,prop={'size':20})
plt.title("Movie budget distribution", fontsize=35, color="DarkBlue", fontname="Calbri")
plt.xlabel("Budget", fontsize=25, color="Green")
plt.ylabel("Number of Movies", fontsize=25, color="Red")
plt.xticks(np.arange(0, 300,step=50),fontsize=20)
plt.yticks(np.arange(0, 120,step=20),fontsize=20)
plt.show()
