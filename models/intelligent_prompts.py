import random

# Fetch trending topics
def fetch_trending_topics():
    return ["nature", "love", "technology", "adventure", "happiness", "solitude"]

# Suggest a random prompt
def suggest_prompt():
    topics = fetch_trending_topics()
    theme = random.choice(topics)
    prompts = [
        f"Write a {theme} poem about the stars.",
        f"Write a {theme} poem about a quiet evening.",
        f"Write a {theme} poem about the passage of time."
    ]
    return random.choice(prompts)
