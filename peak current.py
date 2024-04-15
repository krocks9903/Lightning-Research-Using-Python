import pandas as pd
import folium
from IPython.display import display

# Load Excel data into DataFrame
excel_file = "april22.xlsx"
df = pd.read_excel('april22.xlsx')

# Function to filter data, find highest absolute Ip, and map it
def filter_and_map_data(month, day, hour, minute, second):
    # Filter data based on Month, Day, Hour, Minute, Second
    filtered_df = df[(df['Month'] == month) & 
                     (df['Day'] == day) & 
                     (df['Hour'] == hour) & 
                     (df['Minute'] == minute) &
                     (df['Second'] == second)]
    
    # Check if filtered DataFrame is not empty
    if not filtered_df.empty:
        # Extract relevant columns: nano second, Latitude, Longitude, Ip, IC/CG
        filtered_data = filtered_df[['nano second', 'Latitude', 'Longitude', 'Ip', 'IC/CG']]
        
        # Find highest absolute value of 'Ip'
        max_abs_ip = filtered_data['Ip'].abs().max()
        
        # Get the row with the highest absolute 'Ip' value
        max_abs_ip_row = filtered_data.loc[filtered_data['Ip'].abs() == max_abs_ip].iloc[0]
        
        # Extract longitude and latitude of the row with highest absolute 'Ip'
        max_ip_longitude = max_abs_ip_row['Longitude']
        max_ip_latitude = max_abs_ip_row['Latitude']
        
        # Print highest absolute 'Ip' value and its location
        print("Highest Absolute Value of 'Ip(peak current)':", max_abs_ip)
        print("Location (Longitude, Latitude):", max_ip_longitude, max_ip_latitude)
        
        # Print other values without the highest peak current
        other_values_df = filtered_data[filtered_data['Ip'] != max_abs_ip]
        if not other_values_df.empty:
            print("\nOther values without the highest peak current:")
            print(other_values_df)
        else:
            print("\nNo other values available without the highest peak current.")
        
        # Create map centered at the location of the highest absolute 'Ip'
        m = folium.Map(location=[max_ip_latitude, max_ip_longitude], zoom_start=10)
        
        # Add marker for the location with the highest absolute 'Ip' (in red)
        folium.Marker(location=[max_ip_latitude, max_ip_longitude],
                      popup=f"Highest Absolute Ip: {max_abs_ip}",
                      icon=folium.Icon(color='red')).add_to(m)
        
        # Add markers for other peak currents (in blue)
        for _, row in filtered_data.iterrows():
            if row['Ip'] != max_abs_ip:
                folium.Marker(location=[row['Latitude'], row['Longitude']],
                              popup=f"Ip: {row['Ip']}").add_to(m)
        
        # Display the map within Jupyter Notebook
        display(m)
    else:
        print("No data available for the specified Month, Day, Hour, Minute, and Second.")

# Input Month, Day, Hour, Minute, and Second
month = int(input("Enter the Month (1-12): "))
day = int(input("Enter the Day (1-31): "))
hour = int(input("Enter the Hour (0-23): "))
minute = int(input("Enter the Minute (0-59): "))
second = int(input("Enter the Second (0-59): "))

# Call function to filter data, find highest absolute Ip, and map it
filter_and_map_data(month, day, hour, minute, second)
