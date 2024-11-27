import praw
import pandas as pd
import re

# Set up the Reddit API client using your credentials
reddit = praw.Reddit(
    client_id="CLIENT_ID",          # Replace with your client ID
    client_secret="CLIENT_SECRET",  # Replace with your client secret
    user_agent="YOUR_USER_AGENT"         # Replace with your app name (e.g., "PoetryScraper")
)

# Access the r/Poetry subreddit
subreddit = reddit.subreddit("Poetry")

# List to store the post data
poetry_posts = []

# Loop to scrape the top posts from r/Poetry
for post in subreddit.top(limit=10):  # Change the limit as needed
    # Skip posts without content
    if not post.selftext.strip():  # Check if the content is empty or whitespace
        continue

    post_data = {
        "title": post.title,
        "content": post.selftext,  # Content of the post
        "score": post.score,      # Upvotes/downvotes
        "author": post.author.name if post.author else "Unknown",  # Post author
        "created_utc": post.created_utc  # Time of post creation in UTC
    }

    poetry_posts.append(post_data)

# Convert the list into a pandas DataFrame
df = pd.DataFrame(poetry_posts)


# Save the data to a CSV file
df.to_csv("filtered_poetry.csv", index=False)

print("Scraping completed! Data saved to filtered_poetry.csv")
