import pandas as pd
import mysql.connector

# Load CSV
df = pd.read_csv('cleaned_music_data.csv')
print("✅ CSV loaded. Shape:", df.shape)

# Rename CSV columns to match MySQL table column names
df.columns = [
    'user_id',
    'age',
    'country',
    'streaming_platform',
    'top_genre',
    'minutes_streamed_per_day',
    'number_of_songs_liked',
    'most_played_artist',
    'subscription_type',
    'listening_time',
    'discover_weekly_engagement',
    'repeat_song_rate'
]

# Connect to MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='root',  # change if different
    password='gml@',  # change to your MySQL password
    database='music_analytics'
)
cursor = connection.cursor()

# Prepare insert query (exclude `id` as it's AUTO_INCREMENT)
insert_query = """
INSERT INTO music_users (
    user_id, age, country, streaming_platform, top_genre,
    minutes_streamed_per_day, number_of_songs_liked, most_played_artist,
    subscription_type, listening_time, discover_weekly_engagement, repeat_song_rate
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Insert rows with error handling
inserted = 0
for index, row in df.iterrows():
    try:
        cursor.execute(insert_query, tuple(row))
        inserted += 1
    except Exception as e:
        print(f"❌ Failed to insert row {index + 1}: {e}")

# Commit and close
connection.commit()
print(f"✅ Committed successfully — {inserted} rows inserted.")

cursor.close()
connection.close()
