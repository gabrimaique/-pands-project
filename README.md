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

## Basic Analysis

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

## Data Visualization

3 different variable types were established by selecting the column "species" from the file. 
```sh
irisSetosa = data[data.Species == "Iris-setosa"]
irisVersicolor = data[data.Species == "Iris-versicolor"]
irisVirginica = data[data.Species == "Iris-virginica"]
```
### Histograms 

Now that we have a basic idea about the data we need to extend that with some visualizations. I added 4 histograms to the project using Seaborn and Matloplib (Sepal length, sepal width, petal length and petal width). We used the Seaborn library to make the histograms using the information from the dataset. This will display the variables in an easy-to-read graphic that shows the frequency that individual variables appear in the data frame.

I used the following code to generate the histograms. This process is repeated for each histogram with the measurements changed.

```sh
sns.distplot(irisSetosa['sepalLenghtCm'], kde = False, label = 'Iris Setosa', color = 'green')
sns.distplot(irisVersicolor['sepalLenghtCm'], kde = False, label = 'Iris Versicolor', color = 'red')
sns.distplot(irisVirginica['sepalLenghtCm'], kde = False, label = 'Iris Virginica', color = 'blue')
plt.xlabel ('Centimeters') 
plt.ylabel ('Frequency') 
plt.title ('Sepal Length')
plt.legend() 
plt.savefig('Sepal Length in CM')
plt.show()
```
![Sepal Length in CM](https://github.com/gabrimaique/-pands-project/blob/main/Sepal%20Length%20in%20CM.png)

![Sepal Width in CM](https://github.com/gabrimaique/-pands-project/blob/main/Sepal%20Width%20in%20CM.png)

![Petal Length in CM](https://github.com/gabrimaique/-pands-project/blob/main/Petal%20Length%20in%20CM.png)

![Petal Width in CM](https://github.com/gabrimaique/-pands-project/blob/main/Petal%20Width%20in%20CM.png)

#### Observations: 
* the Iris Setosa is linearly separable from the others when looking at the Petals.
* The Petal are well divided in both width and length but in the sepal there are significant amounts of overlap, this is why the colours get mixed together 
* Iris Setosa has a much smaller petal length and petal width than the other 2 species.

### Scatter Plots

Scatter plots show how much one variable is affected by another, it is a quick and simple way to look at the relationship between the variables and easier for the inexperienced user to interpret the data. A Scatter (XY) Plot has points that show the relationship between two sets of data. I added 4 Scatter Plots to the project using Seaborn and Matloplib (Sepal comparasion, petal comparasion, sepal and petal lenght and sepal and petal width).

I used the following code to generate the Scatter Plosts. This process is repeated for each Scatter Plots with the measurements and the variable changed.

```sh
sns.scatterplot(x = "petalLengthCm", y = "petalWidthCm", data = data, hue = "Species", palette = ['green', 'red', 'blue') 
plt.xlabel ('Length in Centimeters') 
plt.ylabel ('Width in Centimeters') 
plt.title ('Petal') 
plt.legend() 
plt.savefig('Petal Scatter Plot') 
plt.show()
```

![Sepal Scatter Plot](https://github.com/gabrimaique/-pands-project/blob/main/Sepal%20Scatter%20Plot.png)

![Petal Scatter Plot](https://github.com/gabrimaique/-pands-project/blob/main/Petal%20Scatter%20Plot.png)

![Sepal Length and Petal Length Scatter Plot](https://github.com/gabrimaique/-pands-project/blob/main/Sepal%20Length%20and%20Petal%20Length%20Scatter%20Plot.png)

![Sepal Width and Petal Width Scatter Plot](https://github.com/gabrimaique/-pands-project/blob/main/Sepal%20Width%20and%20Petal%20Width%20Scatter%20Plot.png)

#### Observations:
* Sepal length vary from 4.0 to 8.0 while sepal width vary from 2.0 to 4.5
* Petal lengh vary from 1.0 to 7.0 while petal width vary from 0 to 2.5
* Setosa is the smallest of the three species, except for Sepal Width
* Setosa is very well separated than that of Versicolor and Virginica

### Pair Plots

The pairplot function gives an overview of different plots. It builds on two basic figures, the histogram and the scatter plot. The pairplot produces a matrix of relationships between each variable in the dataset for an instant examination of the data and even allows the data to be split by species type. 

I used the following code to generate the Pairplot:

```sh
sns.pairplot(data, hue = 'Species', palette = ['green', 'red', 'blue'])
plt.savefig('Iris Pairplot') 
plt.show()
```
![Iris Pairplot](https://github.com/gabrimaique/-pands-project/blob/main/Iris%20Pairplot.png)

#### Observations:
* The iris Setosa does not seem to have any relationship with the other two species
* Setosa can be easily identified but Versicolor and Virginica have some overlap
* The last two rows of the petal width and length show groupings with only a slight cross over in the iris versicolor and Iris virginica

### Conclusion: 

We've used Python libraries, like pandas and seaborn, to apply some data analysis techniques, to analyse the iris data set and have insights while we were exploring this data. 

By using all this data visualization tools is possible to have different conclusion, it all depends on which questions do you want to answer. 

Questions like: Which flower has the smallest petal or which 
variable you will find significant amounts of overlap, can be easily answered if you look all those graphics generated.

One insight that I have analysing the dataset is that it is quite easy to differentiate the setosa species from the versicolor and the virginica because the iris Setosa is very well separated than that of Versicolor and Virginica. 







