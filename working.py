######################################
## This script is exploring the exoplanet data set.
## Maintained by Jaylee. 
#######################################


from numpy import average
import pandas as pd  

exo = pd.read_csv("all_exoplanets_2021.csv") 
# print(exo) 
exo_columns = exo.columns 
# print(exo_columns)

# print(exo.shape)

# print(exo)

# Showing only the first five data sets 
exo.head()
# print(exo.head())

# tbh idk what this does 
info = pd.read_csv("all_exoplanets_2021.csv", index_col=0) 
# print(info)

# Listing only the distances and accosiated planet number 
Distance = exo['Distance']
info.Distance 
# print(info.Distance)

# print(info)

# Summary of distance information 
# print(info.Distance.describe())

# Average distance 
# print(info.Distance.mean())

# print(info.groupby('Distance').Distance.count())

# Identifying the dtypes of eac category 
# print(info.Distance.dtype)
# print(info.dtypes) 

# How to select all data with missing pieces 
# print(info[pd.isnull(info.Distance)])

# print(exo)

# renaming columns  
# print(info.rename(columns={'Stellar Metallicity Ratio': 'SMR'})) 

#########################################
# Functions Practice 
def multiplyanumber(x, y):

    # this function takes in a number and returns that number times itself

    answer = x*y

    return answer
# test = multiplyanumber(5, 6)
# print(test)


# function 1
# input: pandas dataframe
# output: number of rows and columns in the dataframe  
def rowscolumns(x): 
    answer = exo.shape 
    return answer 
testt = rowscolumns(exo) 
# print(testt)


# function 2
# input: pandas dataframe, name of numeric column
# output: mean, min, and max of that column



# function 3
# input: pandas dataframe, name of categorical column
# output: pandas dataframe, with additional column - count of characters in designated categorical column
def characters(x): 
    answer = len(x) 
    return answer 
testss = characters(Distance)
# print(testss)


# function 4
# input: pandas dataframe, name of categorical column, string to filter
# output: subsetted pandas dataframe, filtered by desired string
def filtered(df, x, n): 

    subset = df[df[x] > n]

    return subset
testttt = filtered(exo, 'Stellar Surface Gravity', 2)
# print(testttt) 


# function 5
# input: pandas dataframe, name of categorical column
# output: frequency table of unique values from that column
Discovery = exo['Discovery Facility']
def table(x): 
    answer = exo.value_counts(x)
    return answer 
#testtt = table(Discovery)

#print(testtt)


# Importing the graphing 
import matplotlib.pyplot as plt  

# Plotting a bar graph
Dataa = (Distance)
fig, simple_chart = plt.subplots()
simple_chart.plot(Dataa)
# Add graph labels 
plt.title('Exo Planet Distance Graph')
plt.xlabel('Planet') 
plt.ylabel('Distance (pc)') 
# Change the graph color 
#plt.plot(Dataa, color = 'pink')
#plt.show()  

# Plotting scatterplot 
df = pd.read_csv('all_exoplanets_2021.csv')
fig, ax = plt.subplots()
plt.scatter(x= df['Mass'], y= df['Distance'], color= 'purple') 
plt.title('Mass vs Distance Exoplanet Graph')
plt.xlabel('Mass')
plt.ylabel('Distance')
#  plt.show()

# Plotting Pie Chart 
labels = 'Radial Velocity', 'Eclipse Timing Variations', 'Transit',  'Astrometry', 'Imaging', 'Disk Kinematics', 'Orbital Brightness Modulation', 'Pulsation Timing Variations', 'Microlensing', 'Transit Timing Variations', 'Pulsar Timing'
sizes = [899, 16, 3444, 1, 54, 1, 9, 2, 120, 22, 7]
fig1, ax1 = plt.subplots()
ax1.pie(sizes) 
ax1.axis('equal') 
plt.title('Discovery Methods of Exoplanets') 
# Adding key bank 
plt.legend(labels, title='Key', loc='center left')
#plt.show ()

# Plotting a line graph 

#df_2 = exo[exo['Num Stars']]
#df_3 = exo[exo['Distance']]

#plt.plot(df_2, df_3)
#plt.title('Distance vs Num Stars')
#plt.xlabel('Num Stars')
#plt.ylabel('Distance')
#plt.show()



def maxminmean(x):

    answer = max(x), min(x), average(x) 

    return answer 
mass = exo['Mass']
tests = maxminmean(mass) 
print(tests)



