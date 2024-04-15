import pandas as pd
import matplotlib.pyplot as plt

# Load all sheets from the Excel file into a list of DataFrames
excel_file = "Sep7.xlsx"
sheets_list = pd.read_excel(excel_file, sheet_name=None)

# Concatenate all dataframes into one dataframe
combined_df = pd.concat(sheets_list.values(), ignore_index=True)

# Extract Hour column from the combined DataFrame
hourly_distribution = combined_df['Hour'].value_counts().sort_index()

# Plot the hourly distribution
plt.figure(figsize=(10, 6))
hourly_distribution.plot(kind='bar', color='Green')
plt.title('Combined Hourly Distribution of Lightning Strikes (September 7th 18-23UTC) ')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Lightning Strikes')
plt.xticks(rotation=0)
plt.grid(axis='y')

# Show the plot
plt.show()
