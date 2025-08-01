import pandas as pd

df = pd.read_csv("cleaned_music_data.csv")

# Print exact column names
print("🔍 Column names in the dataset:")
print(df.columns.tolist())
