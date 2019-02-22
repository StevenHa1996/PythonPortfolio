# Import numpy
import numpy as np
import matplotlib.pyplot as plt



# Seasons
Seasons = ["2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]
Sdict = {"2005": 0, "2006": 1, "2007": 2, "2008": 3, "2009": 4, "2010": 5, "2011": 6, "2012": 7, "2013": 8, "2014": 9}

# Players
Players = ["KobeBryant", "JoeJohnson", "LeBronJames", "CarmeloAnthony", "DwightHoward", "ChrisBosh", "ChrisPaul",
           "KevinDurant", "DerrickRose", "DwayneWade"]
Pdict = {"KobeBryant": 0, "JoeJohnson": 1, "LeBronJames": 2, "CarmeloAnthony": 3, "DwightHoward": 4, "ChrisBosh": 5,
         "ChrisPaul": 6, "KevinDurant": 7, "DerrickRose": 8, "DwayneWade": 9}

# Salaries
KobeBryant_Salary = [15946875, 17718750, 19490625, 21262500, 23034375, 24806250, 25244493, 27849149, 30453805, 23500000]
JoeJohnson_Salary = [12000000, 12744189, 13488377, 14232567, 14976754, 16324500, 18038573, 19752645, 21466718, 23180790]
LeBronJames_Salary = [4621800, 5828090, 13041250, 14410581, 15779912, 14500000, 16022500, 17545000, 19067500, 20644400]
CarmeloAnthony_Salary = [3713640, 4694041, 13041250, 14410581, 15779912, 17149243, 18518574, 19450000, 22407474,
                         22458000]
DwightHoward_Salary = [4493160, 4806720, 6061274, 13758000, 15202590, 16647180, 18091770, 19536360, 20513178, 21436271]
ChrisBosh_Salary = [3348000, 4235220, 12455000, 14410581, 15779912, 14500000, 16022500, 17545000, 19067500, 20644400]
ChrisPaul_Salary = [3144240, 3380160, 3615960, 4574189, 13520500, 14940153, 16359805, 17779458, 18668431, 20068563]
KevinDurant_Salary = [0, 0, 4171200, 4484040, 4796880, 6053663, 15506632, 16669630, 17832627, 18995624]
DerrickRose_Salary = [0, 0, 0, 4822800, 5184480, 5546160, 6993708, 16402500, 17632688, 18862875]
DwayneWade_Salary = [3031920, 3841443, 13041250, 14410581, 15779912, 14200000, 15691000, 17182000, 18673000, 15000000]
# Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary,
                   ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])

# Games
KobeBryant_G = [80, 77, 82, 82, 73, 82, 58, 78, 6, 35]
JoeJohnson_G = [82, 57, 82, 79, 76, 72, 60, 72, 79, 80]
LeBronJames_G = [79, 78, 75, 81, 76, 79, 62, 76, 77, 69]
CarmeloAnthony_G = [80, 65, 77, 66, 69, 77, 55, 67, 77, 40]
DwightHoward_G = [82, 82, 82, 79, 82, 78, 54, 76, 71, 41]
ChrisBosh_G = [70, 69, 67, 77, 70, 77, 57, 74, 79, 44]
ChrisPaul_G = [78, 64, 80, 78, 45, 80, 60, 70, 62, 82]
KevinDurant_G = [35, 35, 80, 74, 82, 78, 66, 81, 81, 27]
DerrickRose_G = [40, 40, 40, 81, 78, 81, 39, 0, 10, 51]
DwayneWade_G = [75, 51, 51, 79, 77, 76, 49, 69, 54, 62]
# Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G,
                  KevinDurant_G, DerrickRose_G, DwayneWade_G])

# Minutes Played
KobeBryant_MP = [3277, 3140, 3192, 2960, 2835, 2779, 2232, 3013, 177, 1207]
JoeJohnson_MP = [3340, 2359, 3343, 3124, 2886, 2554, 2127, 2642, 2575, 2791]
LeBronJames_MP = [3361, 3190, 3027, 3054, 2966, 3063, 2326, 2877, 2902, 2493]
CarmeloAnthony_MP = [2941, 2486, 2806, 2277, 2634, 2751, 1876, 2482, 2982, 1428]
DwightHoward_MP = [3021, 3023, 3088, 2821, 2843, 2935, 2070, 2722, 2396, 1223]
ChrisBosh_MP = [2751, 2658, 2425, 2928, 2526, 2795, 2007, 2454, 2531, 1556]
ChrisPaul_MP = [2808, 2353, 3006, 3002, 1712, 2880, 2181, 2335, 2171, 2857]
KevinDurant_MP = [1255, 1255, 2768, 2885, 3239, 3038, 2546, 3119, 3122, 913]
DerrickRose_MP = [1168, 1168, 1168, 3000, 2871, 3026, 1375, 0, 311, 1530]
DwayneWade_MP = [2892, 1931, 1954, 3048, 2792, 2823, 1625, 2391, 1775, 1971]
# Matrix
MinutesPlayed = np.array(
    [KobeBryant_MP, JoeJohnson_MP, LeBronJames_MP, CarmeloAnthony_MP, DwightHoward_MP, ChrisBosh_MP, ChrisPaul_MP,
     KevinDurant_MP, DerrickRose_MP, DwayneWade_MP])

# Field Goals
KobeBryant_FG = [978, 813, 775, 800, 716, 740, 574, 738, 31, 266]
JoeJohnson_FG = [632, 536, 647, 620, 635, 514, 423, 445, 462, 446]
LeBronJames_FG = [875, 772, 794, 789, 768, 758, 621, 765, 767, 624]
CarmeloAnthony_FG = [756, 691, 728, 535, 688, 684, 441, 669, 743, 358]
DwightHoward_FG = [468, 526, 583, 560, 510, 619, 416, 470, 473, 251]
ChrisBosh_FG = [549, 543, 507, 615, 600, 524, 393, 485, 492, 343]
ChrisPaul_FG = [407, 381, 630, 631, 314, 430, 425, 412, 406, 568]
KevinDurant_FG = [306, 306, 587, 661, 794, 711, 643, 731, 849, 238]
DerrickRose_FG = [208, 208, 208, 574, 672, 711, 302, 0, 58, 338]
DwayneWade_FG = [699, 472, 439, 854, 719, 692, 416, 569, 415, 509]
# Matrix
FieldGoals = np.array(
    [KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG,
     KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])

# Field Goal Attempts
KobeBryant_FGA = [2173, 1757, 1690, 1712, 1569, 1639, 1336, 1595, 73, 713]
JoeJohnson_FGA = [1395, 1139, 1497, 1420, 1386, 1161, 931, 1052, 1018, 1025]
LeBronJames_FGA = [1823, 1621, 1642, 1613, 1528, 1485, 1169, 1354, 1353, 1279]
CarmeloAnthony_FGA = [1572, 1453, 1481, 1207, 1502, 1503, 1025, 1489, 1643, 806]
DwightHoward_FGA = [881, 873, 974, 979, 834, 1044, 726, 813, 800, 423]
ChrisBosh_FGA = [1087, 1094, 1027, 1263, 1158, 1056, 807, 907, 953, 745]
ChrisPaul_FGA = [947, 871, 1291, 1255, 637, 928, 890, 856, 870, 1170]
KevinDurant_FGA = [647, 647, 1366, 1390, 1668, 1538, 1297, 1433, 1688, 467]
DerrickRose_FGA = [436, 436, 436, 1208, 1373, 1597, 695, 0, 164, 835]
DwayneWade_FGA = [1413, 962, 937, 1739, 1511, 1384, 837, 1093, 761, 1084]
# Matrix
FieldGoalAttempts = np.array(
    [KobeBryant_FGA, JoeJohnson_FGA, LeBronJames_FGA, CarmeloAnthony_FGA, DwightHoward_FGA, ChrisBosh_FGA,
     ChrisPaul_FGA, KevinDurant_FGA, DerrickRose_FGA, DwayneWade_FGA])

# Points
KobeBryant_PTS = [2832, 2430, 2323, 2201, 1970, 2078, 1616, 2133, 83, 782]
JoeJohnson_PTS = [1653, 1426, 1779, 1688, 1619, 1312, 1129, 1170, 1245, 1154]
LeBronJames_PTS = [2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036, 2089, 1743]
CarmeloAnthony_PTS = [2122, 1881, 1978, 1504, 1943, 1970, 1245, 1920, 2112, 966]
DwightHoward_PTS = [1292, 1443, 1695, 1624, 1503, 1784, 1113, 1296, 1297, 646]
ChrisBosh_PTS = [1572, 1561, 1496, 1746, 1678, 1438, 1025, 1232, 1281, 928]
ChrisPaul_PTS = [1258, 1104, 1684, 1781, 841, 1268, 1189, 1186, 1185, 1564]
KevinDurant_PTS = [903, 903, 1624, 1871, 2472, 2161, 1850, 2280, 2593, 686]
DerrickRose_PTS = [597, 597, 597, 1361, 1619, 2026, 852, 0, 159, 904]
DwayneWade_PTS = [2040, 1397, 1254, 2386, 2045, 1941, 1082, 1463, 1028, 1331]
# Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS,
                   ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])



#-----------------------
mydata = np.arange(0,20) #np.arange creates array from range 0-20

#OOP Concept
#matrix1 = np.reshape(mydata, (5,4), order = 'C')
#matrix2 = np.reshape(mydata, (5,4), order = 'F')
matrix1 = mydata.reshape((5,4), order = 'C')#orders the data horizontally  C
matrix2 = mydata.reshape((5,4), order = 'F')#orders the data Verticallu F

#I dont have to call the function within the np package because
#i've already know that the object(mydata) already contains the .reshape method
#when i assigned it to np.array


#print(matrix1)


#print(matrix1)
#print(matrix1[2,2]) #locates data by the following format [row,column]
#print(matrix2)

list1 = ['Hello', 'How', 'You']
list2 = ['What', 'a', 'day']
list3 = [1,2,3]

new_matrix = np.array([list1,list2,list3]) #output is in strings. arrays can only run 1 variable type which is why the numbers has been turnt into a string

#print(new_matrix)
#print("Hello World")

#print(Games[2][9]) indexes can be printed this way

#--------------
#Dictionaries

#print(Games[Pdict['KobeBryant']][Sdict['2008']])


import warnings
warnings.filterwarnings('ignore')

FieldGoalsPerGame = np.matrix.round(FieldGoals / Games)

print("\n FieldGoalsPerGame Matrix")
print(FieldGoalsPerGame)
print(FieldGoalsPerGame[Pdict['KobeBryant']][Sdict['2009']])

accuracy = np.matrix.round(FieldGoals / FieldGoalAttempts * 100)
#fieldgoals divide by fieldgoalattempts will give me the stats.
#times by 100 with give me the percentages. e.g. Kobe Bryant will have a 45% chance of scoring in the hoop

print("\nThe Accuracy")
print("\n", accuracy)
plt.plot(accuracy[0], c='Red', ls='--', marker='o', ms=5, label=Players[0])
plt.plot(accuracy[1], c='Blue', ls='--', marker='o', ms=5, label=Players[1])
plt.plot(accuracy[2], c='Green', ls='--', marker='o', ms=5, label=Players[2])
plt.plot(accuracy[3], c='Orange', ls='--', marker='o', ms=5, label=Players[3])
plt.plot(accuracy[4], c='Yellow', ls='--', marker='o', ms=5, label=Players[4])
plt.plot(accuracy[5], c='Red', ls='--', marker='s', ms=5, label=Players[5])
plt.plot(accuracy[6], c='Blue', ls='--', marker='s', ms=5, label=Players[6])
plt.plot(accuracy[7], c='Green', ls='--', marker='s', ms=5, label=Players[7])
plt.plot(accuracy[8], c='Black', ls='--', marker='s', ms=5, label=Players[8])
plt.plot(accuracy[9], c='Grey', ls='--', marker='s', ms=5, label=Players[9])
plt.legend(loc="upper left", bbox_to_anchor=(1,1))  #loc pinches the location of the legend, bbox_to_anchor
                                                    #places the legend to where you want it. 0.5 meaning half of the graph and 1 being all of it.
plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
plt.title("Accuracy")
plt.xlabel("Years")
plt.ylabel("Percentage")
#Setting size
#plt.rcParams['figure.figsize'] = (20,10)
#plt.xticks(How many sticks u want on x axis, data, rotations)
plt.show()


#----------
#Data Visualisation


#plt.plot(data, color, linestyle, marker, markersize, label)
# s = square


##plt.plot(accuracy[0], c='Blue', ls='--', marker='s', ms=7, label=Players[0])
#plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
##plt.xticks(How many sticks u want on x axis, data, rotations)
#plt.show()
#
#plt.plot(Salary[0], c='Red', ls='--', marker='s', ms=7, label=Players[0])
#plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
##plt.xticks(How many sticks u want on x axis, data, rotations)
#plt.show()


#Adding legends
#Salary Visualisation
plt.plot(Salary[0], c='Red', ls='--', marker='o', ms=5, label=Players[0])
plt.plot(Salary[1], c='Blue', ls='--', marker='o', ms=5, label=Players[1])
plt.plot(Salary[2], c='Green', ls='--', marker='o', ms=5, label=Players[2])
plt.plot(Salary[3], c='Orange', ls='--', marker='o', ms=5, label=Players[3])
plt.plot(Salary[4], c='Yellow', ls='--', marker='o', ms=5, label=Players[4])
plt.plot(Salary[5], c='Red', ls='--', marker='s', ms=5, label=Players[5])
plt.plot(Salary[6], c='Blue', ls='--', marker='s', ms=5, label=Players[6])
plt.plot(Salary[7], c='Green', ls='--', marker='s', ms=5, label=Players[7])
plt.plot(Salary[8], c='Black', ls='--', marker='s', ms=5, label=Players[8])
plt.plot(Salary[9], c='Grey', ls='--', marker='s', ms=5, label=Players[9])
plt.legend(loc="upper left", bbox_to_anchor=(1,1))  #loc pinches the location of the legend, bbox_to_anchor
                                                    #places the legend to where you want it. 0.5 meaning half of the graph and 1 being all of it.
plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
plt.title("Salary")
plt.xlabel("Years")
plt.ylabel("Amount")
#Setting size
#plt.rcParams['figure.figsize'] = (20,10)
#plt.xticks(How many sticks u want on x axis, data, rotations)
plt.show()

#Games Visualisation
plt.plot(Games[0], c='Red', ls='--', marker='o', ms=5, label=Players[0])
plt.plot(Games[1], c='Blue', ls='--', marker='o', ms=5, label=Players[1])
plt.plot(Games[2], c='Green', ls='--', marker='o', ms=5, label=Players[2])
plt.plot(Games[3], c='Orange', ls='--', marker='o', ms=5, label=Players[3])
plt.plot(Games[4], c='Yellow', ls='--', marker='o', ms=5, label=Players[4])
plt.plot(Games[5], c='Red', ls='--', marker='s', ms=5, label=Players[5])
plt.plot(Games[6], c='Blue', ls='--', marker='s', ms=5, label=Players[6])
plt.plot(Games[7], c='Green', ls='--', marker='s', ms=5, label=Players[7])
plt.plot(Games[8], c='Black', ls='--', marker='s', ms=5, label=Players[8])
plt.plot(Games[9], c='Grey', ls='--', marker='s', ms=5, label=Players[9])
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
plt.title("Games")
plt.xlabel("Years")
plt.ylabel("Amount")
#plt.xticks(How many sticks u want on x axis, data, rotations)
plt.show()

#MinutesPlayed visualisation
plt.plot(MinutesPlayed[0], c='Red', ls='--', marker='o', ms=5, label=Players[0])
plt.plot(MinutesPlayed[1], c='Blue', ls='--', marker='o', ms=5, label=Players[1])
plt.plot(MinutesPlayed[2], c='Green', ls='--', marker='o', ms=5, label=Players[2])
plt.plot(MinutesPlayed[3], c='Orange', ls='--', marker='o', ms=5, label=Players[3])
plt.plot(MinutesPlayed[4], c='Yellow', ls='--', marker='o', ms=5, label=Players[4])
plt.plot(MinutesPlayed[5], c='Red', ls='--', marker='s', ms=5, label=Players[5])
plt.plot(MinutesPlayed[6], c='Blue', ls='--', marker='s', ms=5, label=Players[6])
plt.plot(MinutesPlayed[7], c='Green', ls='--', marker='s', ms=5, label=Players[7])
plt.plot(MinutesPlayed[8], c='Black', ls='--', marker='s', ms=5, label=Players[8])
plt.plot(MinutesPlayed[9], c='Grey', ls='--', marker='s', ms=5, label=Players[9])
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
plt.title("Minutes Played")
plt.xlabel("Years")
plt.ylabel("Minutes")
#plt.xticks(How many sticks u want on x axis, data, rotations)
plt.show()

#Average points visualisation
avg_points = np.matrix.round(Points / Games)

plt.plot(avg_points[0], c='Red', ls='--', marker='o', ms=5, label=Players[0])
plt.plot(avg_points[1], c='Blue', ls='--', marker='o', ms=5, label=Players[1])
plt.plot(avg_points[2], c='Green', ls='--', marker='o', ms=5, label=Players[2])
plt.plot(avg_points[3], c='Orange', ls='--', marker='o', ms=5, label=Players[3])
plt.plot(avg_points[4], c='Yellow', ls='--', marker='o', ms=5, label=Players[4])
plt.plot(avg_points[5], c='Red', ls='--', marker='s', ms=5, label=Players[5])
plt.plot(avg_points[6], c='Blue', ls='--', marker='s', ms=5, label=Players[6])
plt.plot(avg_points[7], c='Green', ls='--', marker='s', ms=5, label=Players[7])
plt.plot(avg_points[8], c='Black', ls='--', marker='s', ms=5, label=Players[8])
plt.plot(avg_points[9], c='Grey', ls='--', marker='s', ms=5, label=Players[9])
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
plt.title("Average Points Per Year")
plt.xlabel("Years")
plt.ylabel("Points")
#plt.xticks(How many sticks u want on x axis, data, rotations)
plt.show()

plt.plot(FieldGoals[0], c='Red', ls='--', marker='o', ms=5, label=Players[0])
plt.plot(FieldGoals[1], c='Blue', ls='--', marker='o', ms=5, label=Players[1])
plt.plot(FieldGoals[2], c='Green', ls='--', marker='o', ms=5, label=Players[2])
plt.plot(FieldGoals[3], c='Orange', ls='--', marker='o', ms=5, label=Players[3])
plt.plot(FieldGoals[4], c='Yellow', ls='--', marker='o', ms=5, label=Players[4])
plt.plot(FieldGoals[5], c='Red', ls='--', marker='s', ms=5, label=Players[5])
plt.plot(FieldGoals[6], c='Blue', ls='--', marker='s', ms=5, label=Players[6])
plt.plot(FieldGoals[7], c='Green', ls='--', marker='s', ms=5, label=Players[7])
plt.plot(FieldGoals[8], c='Black', ls='--', marker='s', ms=5, label=Players[8])
plt.plot(FieldGoals[9], c='Grey', ls='--', marker='s', ms=5, label=Players[9])
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
plt.title("Average Goals")
plt.xlabel("Years")
plt.ylabel("Goals")
plt.show()

#def theplot(playerlist):
#    for name in playerlist:
#        plt.plot(Games[Pdict[name]], c='Red', ls='--', marker='o', ms=5, label=name)
#    plt.legend(loc="upper left", bbox_to_anchor=(1,1))
#    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
#    #plt.xticks(How many sticks u want on x axis, data, rotations)
#    plt.show()
#
#print(theplot(["KobeBryant","JoeJohnson","LeBronJames"]))




#----------
#Adding colors by using dictionary

def theplot(data, playerlist = Players): #takes in 2 arguments
    Col1 = {"KobeBryant": "Red", "JoeJohnson": "Blue", "LeBronJames": "Black", "CarmeloAnthony": "Green", "DwightHoward": "Orange", "ChrisBosh": "Pink",
             "ChrisPaul": "Grey", "KevinDurant": "Navy", "DerrickRose": "Brown", "DwayneWade": "Yellow"}
    Mark= {"KobeBryant": "o", "JoeJohnson": "s", "LeBronJames": "x", "CarmeloAnthony": "X", "DwightHoward": "o", "ChrisBosh": "P",
             "ChrisPaul": "s", "KevinDurant": "<", "DerrickRose": ">", "DwayneWade": "1"}
    for name in playerlist: #For every name in playerlist:
        plt.plot(data[Pdict[name]], c=Col1[name], ls='--', marker=Mark[name], ms=5, label=name)#theplot.Salary is passed on as 1 of the arguements: data. This is then passed onto
    plt.legend(loc="upper left", bbox_to_anchor=(1,1))
                                 #plt.plot(data[Pdict[name]], Col1 used for colour: KobeBryant is passed as a name,
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')                                #the name in the Col1(dictionary) for KobrBryant is Red. Red is passed on as a color.
    #plt.xticks(How many sticks u want on x axis, data, rotations)
    plt.show()


#Free Throws
KobeBryant_FT = [696,667,623,483,439,483,381,525,18,196]
JoeJohnson_FT = [261,235,316,299,220,195,158,132,159,141]
LeBronJames_FT = [601,489,549,594,593,503,387,403,439,375]
CarmeloAnthony_FT = [573,459,464,371,508,507,295,425,459,189]
DwightHoward_FT = [356,390,529,504,483,546,281,355,349,143]
ChrisBosh_FT = [474,463,472,504,470,384,229,241,223,179]
ChrisPaul_FT = [394,292,332,455,161,337,260,286,295,289]
KevinDurant_FT = [209,209,391,452,756,594,431,679,703,146]
DerrickRose_FT = [146,146,146,197,259,476,194,0,27,152]
DwayneWade_FT = [629,432,354,590,534,494,235,308,189,284]

FreeThrows = np.array([KobeBryant_FT, JoeJohnson_FT, LeBronJames_FT, CarmeloAnthony_FT, DwightHoward_FT, ChrisBosh_FT, ChrisPaul_FT, KevinDurant_FT, DerrickRose_FT, DwayneWade_FT])

#Free Throw Attempts,
KobeBryant_FTA = [819,768,742,564,541,583,451,626,21,241]
JoeJohnson_FTA = [330,314,379,362,269,243,186,161,195,176]
LeBronJames_FTA = [814,701,771,762,773,663,502,535,585,528]
CarmeloAnthony_FTA = [709,568,590,468,612,605,367,512,541,237]
DwightHoward_FTA = [598,666,897,849,816,916,572,721,638,271]
ChrisBosh_FTA = [581,590,559,617,590,471,279,302,272,232]
ChrisPaul_FTA = [465,357,390,524,190,384,302,323,345,321]
KevinDurant_FTA = [256,256,448,524,840,675,501,750,805,171]
DerrickRose_FTA = [205,205,205,250,338,555,239,0,32,187]
DwayneWade_FTA = [803,535,467,771,702,652,297,425,258,370]

FreeThrowsAT = np.array([KobeBryant_FTA, JoeJohnson_FTA, LeBronJames_FTA, CarmeloAnthony_FTA, DwightHoward_FTA, ChrisBosh_FTA, ChrisPaul_FTA, KevinDurant_FTA, DerrickRose_FTA, DwayneWade_FTA])

FT_pergame = np.matrix.round(FreeThrowsAT / Games)
np.nan_to_num(FT_pergame,False)
plt.title("Free Throws")
plt.xlabel("Years")
plt.ylabel("Points")
print(theplot(FT_pergame))

accuracyFT = np.matrix.round(FreeThrows / FreeThrowsAT * 100)
np.nan_to_num(accuracyFT,False)
plt.title("Free Throw accuracy")
plt.xlabel("Years")
plt.ylabel("Percentage")
print(theplot(accuracyFT))

import warnings
warnings.filterwarnings('ignore')

#part3 = np.matrix.round((Points - FreeThrows) / FieldGoals)
print(theplot((Points - FreeThrows) / FieldGoals))
