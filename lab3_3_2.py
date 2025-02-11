import pandas as pd
import sys

# Part 1 #
# Get the CSV file path from command line argument
csv_file = sys.argv[1]
# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)
print('Dataframe loaded successfully')

# Part 2 #
# Remove any rows/records where there are NULL  or NaN values
print('Number of rows before removing NULL values: ', len(df))
df = df.dropna(axis=0)
print('Number of rows after removing NULL values: ', len(df))

# Part 3 #
# Remove any duplicate rows/records
print('Number of rows before removing duplicates: ', len(df))
df = df.drop_duplicates()
print('Number of rows after removing duplicates: ', len(df))

# Part 4 #
# See the printed outputs from Part 2 and Part 3

# Part 5 #
# Save the cleaned dataframe to a new CSV file
df.to_csv('cleaned_dataframe.csv', index=False)
print('Cleaned dataframe saved to cleaned_dataframe.csv')