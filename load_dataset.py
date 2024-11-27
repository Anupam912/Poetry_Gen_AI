import pandas as pd
import re

# Load the dataset
df = pd.read_csv("filtered_poetry.csv")

# Preview the dataset
print(df.head())

def clean_text(text):
    # Remove non-alphanumeric characters except spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)
    # Convert to lowercase
    return text.lower()

# Apply cleaning to the content column
df["content"] = df["content"].apply(clean_text)

# Save cleaned data
df.to_csv("cleaned_poetry.csv", index=False)

# Save poems as a single text file
with open("poetry_corpus.txt", "w", encoding="utf-8") as file:
    for poem in df["content"]:
        file.write(poem + "\n")

