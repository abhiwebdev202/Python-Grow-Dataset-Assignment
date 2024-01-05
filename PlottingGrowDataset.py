import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Load the dataset containing GROW sensor locations
df = pd.read_csv(r"C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\GrowLocations.csv")

# Correct the latitude and longitude values
df['Latitude'], df['Longitude'] = df['Longitude'], df['Latitude']

# Filter out data points with invalid geographic coordinates
df = df[(df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985) &
        (df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848)]

# Remove duplicate entries based on Latitude and Longitude
df = df.drop_duplicates(subset=['Latitude', 'Longitude'])

# Load the map image of the United Kingdom
map = plt.imread(r'C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\map7.png')

#writing the cleaned data to a new csv file
df.to_csv('C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\cleaned_data_frame.csv', index=False)

# Load the cleaned DataFrame
df = pd.read_csv(r'C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\cleaned_data_frame.csv')

# Create a scatter plot for the points on the map
fig, ax = plt.subplots(figsize=(12,12))
ax.imshow(map, extent=[-10.592, 1.6848, 50.681, 57.985])

# Plot points on the map
ax.scatter(df['Longitude'], df['Latitude'], color='royalblue', s=20, label='Grow Sensor Locations')

# Set plot title and axis labels
plt.title("GROW Sensors' Geographic Distribution in the United Kingdom")
plt.xlabel('Longitude')
plt.ylabel('Latitude')

#Display the legend and the plot
plt.legend()
plt.show()

# Save the plot as a PNG file
plt.savefig('C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\GrowLocationsMap1.png')