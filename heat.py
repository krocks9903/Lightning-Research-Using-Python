import pandas as pd
import folium
from folium.plugins import HeatMap

# Load Excel data into DataFrame
excel_file = "april22.xlsx"
df = pd.read_excel('april22.xlsx')

# Function to create spatial distribution plot of lightning strikes
def create_spatial_distribution_plot(month, day, hour, minute):
    # Filter data based on user input for month, day, hour, and minute
    filtered_df = df[(df['Month'] == month) & 
                     (df['Day'] == day) & 
                     (df['Hour'] == hour) & 
                     (df['Minute'] == minute)]
    
    # Check if filtered DataFrame is not empty
    if not filtered_df.empty:
        # Create map centered around Florida
        m = folium.Map(location=[27.994402, -81.760254], zoom_start=7)

        # Add heatmap layer to visualize the spatial distribution of lightning strikes
        heat_data = filtered_df[['Latitude', 'Longitude']].values.tolist()
        HeatMap(heat_data, radius=10).add_to(m)

        # Add other geographical features such as terrain, cities, or land use (optional)
        folium.TileLayer('Stamen Terrain').add_to(m)
        folium.TileLayer('Stamen Toner').add_to(m)
        folium.TileLayer('Stamen Watercolor').add_to(m)
        folium.LayerControl().add_to(m)

        # Display the map
        display(m)
    else:
        print("No data available for the specified date and time.")

# Get user input for month, day, hour, and minute
try:
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day (1-31): "))
    hour = int(input("Enter the hour (0-23): "))
    minute = int(input("Enter the minute (0-59): "))

    # Call function to create spatial distribution plot
    create_spatial_distribution_plot(month, day, hour, minute)
except ValueError:
    print("Invalid input. Please enter integers for month, day, hour, and minute.")
