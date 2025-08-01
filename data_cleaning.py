import pandas as pd 

#Load CSV file 

df = pd.read_csv("Global_Music_Streaming_Listener_Preferences.csv")

#Disply top 5 rows and column info
print("--------FIRST 5 ROWS--------")
print(df.head())

print("\n-------DATA INFO--------")
print(df.info())

# Step 4: Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 5: Drop rows with missing values
df.dropna(inplace=True)

# Optional: See cleaned data
print("\n------ CLEANED DATA ------")
print(df.head())

# Step 6: Save cleaned data to a new CSV
df.to_csv("cleaned_music_data.csv", index=False)
print("\nCleaned data saved to cleaned_music_data.csv")

