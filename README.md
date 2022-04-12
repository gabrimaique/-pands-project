# Fisher's Iris Data Set

## Introduction

The iris flower data set was introduced by the statistician and biologist Ronald Fisher in 1936. It is an example of linear discriminant analysis, which is the method used in statistics to classify observations into two or more groups or categories. The data set consists of 50 sample for each of three iris species: 

·   Iris setosa

·   Iris versicolor 

·   Iris virginica

Each specie has 4 measurements applies to it:

·   Sepal length

·   Sepal width

·   Petal length

·   Petal width
	
In this data, the length and width of the sepals and petals were measured in ceteminters.

![iris.png](https://github.com/gabrimaique/-pands-project/blob/main/iris.png)

## Dataset Analysis

### Libraries Used

* matplotlib.pyplot as plt: plotting library for creating static, animated, and interactive visualizations in Python.

* pandas as pd: library written for the Python programming language for data manipulation and analysis.

* seaborn as sns: library for making statistical graphics in Python.

### Dataset

The raw data was taken from UC Irvine Machine Learning Repository as a csv (comma separated values) file and imported into the program as follows:

```sh
    data = pd.read_csv("irisData.csv")
```    

I imported the pandas package in order to read the csv file(used to store tabular data, such as a spreadsheet or database) and convert the data into a pandas dataframe.

The output below was created to write information from it to a .txt file each time the program is running:

```sh
    text = open ("analysisSummary.txt", "w")
```    

## Basic 

### Head()
By using the function data.head() we add the first and last 5 rows from the .csv. It is useful for quickly testing if your object has the right type of data in it.

![firstandlast5rows.png](https://github.com/gabrimaique/-pands-project/blob/main/first%20and%20last%205%20rows.png)

There are five variables, four of them are type float(sepal length, sepal width, petal length and petal width) and one string(class).

### Adding information
The file = text adds the  title, create space and add information to the .txt file.

```sh
print ("Summary", file = text)
print (" ", file = text) 
print ("General layout of Fisher's Iris datafile:", file = text) 
print (data, file = text)
```  

### Describe()
The describe() method prints out a summary of the Dataframe containing the mean, max, standard deviation etc. of the data file. It gives some information and basic statistics of the 4 features.
```sh
print (data.describe(), file = text)
```
![describe.png](https://github.com/gabrimaique/-pands-project/blob/main/describe.png.png)

#### Observations: 
* Count represents the number of records in the data set
* Mean is the average of all data 
* A standard deviation is a measure of the average distance between the values of the data in the set and the mean

### Value_counts()
This operation prints out from the species column the Number of rows in each group as a Series. There are 50 entries for each species.
```sh
print (data["Species"].value_counts(), file = text) 
```
```sh
Types of iris species:
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
Name: Species, dtype: int64
```










