# importing required libraries 
# used to make plots
import matplotlib.pyplot as plt 
# read .csv  file
import pandas as pd 
# data visualization library based on matplotlib
import seaborn as sns 

# reading in the csv iris datafile
data = pd.read_csv("irisData.csv") 
# it outputs the data to a .txt file.
# The "w" specifies that the file is being written to.
text = open ("analysisSummary.txt", "w") 

# This function returns the first 5 rows for the object based on position.
data.head() 


# adding title
# file=text outputs the file to the .txt doc
print ("Summary", file = text)
# create space in line 2
print (" ", file = text) 
# title
print ("General layout of Fisher's Iris datafile:", file = text) 
# writes the data to the txt file
print (data, file = text) 

# create space
print (" ", file = text)
# title
print ("Summary of numerical values:", file = text)
# a numerical summary from the dataset (count, mean, std..)
print (data.describe(), file = text) 
print (" ", file = text)

print ("Types of iris species:", file = text)
# accurance of iris species
print (data["Species"].value_counts(), file = text) 
print (" ", file = text)


# the data was divided in species 
# it select the column species from the text
irisSetosa = data[data.Species == "Iris-setosa"]
irisVersicolor = data[data.Species == "Iris-versicolor"]
irisVirginica = data[data.Species == "Iris-virginica"]

# sns(seaborn library)
# seaborn.distplot lets you show the histogram 
# kde=False hide kernel and only display the histogram.
sns.distplot(irisSetosa['sepalLenghtCm'], kde = False, label = 'Iris Setosa', color = 'green')
sns.distplot(irisVersicolor['sepalLenghtCm'], kde = False, label = 'Iris Versicolor', color = 'red')
sns.distplot(irisVirginica['sepalLenghtCm'], kde = False, label = 'Iris Virginica', color = 'blue')
plt.xlabel ('Centimeters') 
plt.ylabel ('Frequency') 
plt.title ('Sepal Length')
plt.legend() 
plt.savefig('Sepal Length in CM')
plt.show()

#seplwidth histogram
sns.distplot(irisSetosa['sepalWidthCm'], kde = False, label = 'Iris Setosa', color = 'green')
sns.distplot(irisVersicolor['sepalWidthCm'], kde = False, label = 'Iris Versicolor', color = 'red')
sns.distplot(irisVirginica['sepalWidthCm'], kde = False, label = 'Iris Virginica', color = 'blue')
plt.ylabel ('Frequency')
plt.title ('Sepal Width')
plt.legend()
plt.savefig('Sepal Width in CM')
plt.show()

#Histogram for Petal Length 
sns.distplot(irisSetosa['petalLengthCm'], kde = False, label = 'Iris Setosa', color = 'green')
sns.distplot(irisVersicolor['petalLengthCm'], kde = False, label = 'Iris Versicolor', color = 'red')
sns.distplot(irisVirginica['petalLengthCm'], kde = False, label = 'Iris Virginica', color = 'blue')
plt.xlabel ('Centimeters')
plt.ylabel ('Frequency')
plt.title ('Petal Length')
plt.legend()
plt.savefig('Petal Length in CM')
plt.show()

#Histogram for Petal Width 
sns.distplot(irisSetosa['petalWidthCm'], kde = False, label = 'Iris Setosa', color = 'green')
sns.distplot(irisVersicolor['petalWidthCm'], kde = False, label = 'Iris Versicolor', color = 'red')
sns.distplot(irisVirginica['petalWidthCm'], kde = False, label = 'Iris Virginica', color = 'blue')
plt.xlabel ('Centimeters')
plt.ylabel ('Frequency')
plt.title ('Petal Width')
plt.legend()
plt.savefig('Petal Width in CM')
plt.show()

# 
sns.scatterplot(x = "sepalLenghtCm", y = "sepalWidthCm", data = data, hue = "Species", palette = ['green', 'red', 'blue']) 
# x-axis
plt.xlabel ('Length in Centimeters') 
# y-aixs
plt.ylabel ('Width in Centimeters') 
plt.title ('Sepal') 
plt.legend() 
# it saves the graph as a .png
plt.savefig('Sepal Scatter Plot')
plt.show()

#Scatter plot for Petal Comparasion
sns.scatterplot(x = "petalLengthCm", y = "petalWidthCm", data = data, hue = "Species", palette = ['green', 'red', 'blue']) 
plt.xlabel ('Length in Centimeters') 
plt.ylabel ('Width in Centimeters') 
plt.title ('Petal') 
plt.legend() 
plt.savefig('Petal Scatter Plot') 
plt.show()

#Scatter plot for Sepal Length and Petal Length Comparasion
sns.scatterplot(x = "sepalLenghtCm", y = "petalLengthCm", data = data, hue = "Species", palette = ['green', 'red', 'blue']) 
plt.xlabel ('Sepal Length in Centimeters') 
plt.ylabel ('Petal Length in Centimeters') 
plt.title ('Sepal and Petal Length') 
plt.legend() 
plt.savefig('Sepal Length and Petal Length Scatter Plot') 
plt.show()

#Scatter plot for Sepal Width and Petal Width Comparasion
sns.scatterplot(x = "sepalWidthCm", y = "petalWidthCm", data = data, hue = "Species", palette = ['green', 'red', 'blue']) 
plt.xlabel ('Sepal Width in Centimeters') 
plt.ylabel ('Petal Width in Centimeters') 
plt.title ('Sepal and Petal Width') 
plt.legend() 
plt.savefig('Sepal Width and Petal Width Scatter Plot') 
plt.show()


sns.pairplot(data, hue = 'Species', palette = ['green', 'red', 'blue'])
plt.savefig('Iris Pairplot') 
plt.show()



