import instaloader
import psycopg2
from datetime import datetime

# Database connection information
DB_HOST = 'ep-tight-limit-a6uyk8mk.us-west-2.retooldb.com'
DB_USER = 'retool'
DB_PASSWORD = 'jr1cAFW3ZIwH'
DB_NAME = 'retool'

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    dbname=DB_NAME
)

# Initialize Instaloader
L = instaloader.Instaloader()

# List of Instagram usernames
usernames = ['aidahadzialic', 'carinaodebrink', 'lena_hallengren']  # Replace with actual usernames


def insert_post_into_db(caption, timestamp, post_type, owner_username, display_url, video_url):
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO igposts (caption, timestamp, type, ownerusername, displayurl, videourl)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (caption, timestamp, post_type, owner_username, display_url, video_url))
        connection.commit()
    except Exception as e:
        print(f"An error occurred while inserting into the database: {e}")


def get_last_5_posts(username):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()

        count = 0
        for post in posts:
            caption = post.caption
            timestamp = post.date_utc
            post_type = 'video' if post.is_video else 'image'
            display_url = post.url
            video_url = post.video_url if post.is_video else None

            insert_post_into_db(caption, timestamp, post_type, username, display_url, video_url)

            print(f"Inserted post from {username} into the database.")

            count += 1
            if count >= 5:
                break
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile {username} does not exist.")
    except instaloader.exceptions.ConnectionException:
        print("Connection error. Try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Iterate through the usernames
for username in usernames:
    print(f"Fetching posts for {username}")
    get_last_5_posts(username)
    print("\n" + "-" * 30 + "\n")

# Close the database connection
connection.close()
