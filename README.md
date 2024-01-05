# Python-Grow-Dataset-Assignment
Plotting the Grow Dataset of GROW Sensors in the United Kingdom on a UK Map Image

The bounding box for the map is as follows:
•	Longitude Min -10.592
•	Longitude Max 1.6848
•	Latitude Min 50.681
•	Latitude Max 57.985

The Provided files for the assignment:

•	The Grow dataset Growlocations.csv.  This file contains the locations of all the GROW sensors as Latitude and Longitude
•	A map of the UK from Openstreet map.

This Python program can read the dataset into a dataframe and plot the locations of the sensors on the map provided. Tutorial used for reference is "freecodecamp.org"s 'Data Analysis with Python Course', which teaches us the basics of pandas, numpy and matplotlib libraries of Python.

Code Explanation:
The code explained using comments in the .py file.

The Grow Dataset is loaded in a dataframe using the pandas library.

In the data cleaning part, the first step was to correct the latitude and longitude values. Then I filtered out data points with invalid geographic coordinates as instructed using the given max and min values for "Longitude" and "Latitude". Lastly, I removed the duplicate entries based on Latitude and Longitude values by using 'drop_duplicates' method. Then the cleaned dataset is written in to a new csv file.

The cleaned Dataset is loaded in a dataframe using the pandas library. Then I loaded the open street map image(.png format) of the United Kingdom. Then I created a scatter plot for the points on the map and plotted points on the map; displaying plot title, axis labels and the legend.

At last, I saved the plot as a PNG file in the same assignment directory. 
