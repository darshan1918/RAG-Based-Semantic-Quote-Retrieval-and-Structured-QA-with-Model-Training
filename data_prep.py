# data_prep.py
from datasets import load_dataset
import pandas as pd

# Load dataset
dataset = load_dataset("Abirate/english_quotes", split="train")
df = pd.DataFrame(dataset)

# Basic cleaning
df = df.dropna(subset=["quote", "author", "tags"])
df["quote"] = df["quote"].str.lower()
df["author"] = df["author"].str.lower()
df["tags"] = df["tags"].apply(lambda x: [tag.lower() for tag in x])

# Save CSV for reference
df.to_csv("quotes_clean.csv", index=False)



