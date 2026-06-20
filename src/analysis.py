import pandas as pd

titles = pd.read_csv("data/raw_titles.csv")
credits = pd.read_csv("data/raw_credits.csv")

print("TITLES DATASET")
print(titles.head())
print(titles.info())

print("\nCREDITS DATASET")
print(credits.head())
print(credits.info())
print(titles["id"].nunique())
print(credits["id"].nunique())
invalid_ids=credits[~credits["id"].isin(titles["id"])]
print(invalid_ids.shape)

print(titles.isnull().sum())
print("\n")
print(credits.isnull().sum())

print(titles.groupby("type")["seasons"].count())
print("\nTotal by type:")
print(titles["type"].value_counts())
titles.loc[titles["type"] == "MOVIE", "seasons"] = 0
print(credits["role"].value_counts())

titles = titles.drop(columns=["index"])
credits = credits.drop(columns=["index"])
print(titles.columns)
print(credits.columns)

# Drop row with missing title
titles = titles.dropna(subset=["title"])

# Replace missing age certification
titles["age_certification"] = titles["age_certification"].fillna("Not Rated")

# Replace missing seasons for movies
titles.loc[titles["type"] == "MOVIE", "seasons"] = 0

# Replace missing character for directors
credits.loc[credits["role"] == "DIRECTOR", "character"] = "N/A"

print(titles.isnull().sum())
print(credits.isnull().sum())

titles.to_csv("data/clean_titles.csv", index=False)
credits.to_csv("data/clean_credits.csv", index=False)

print("Clean files saved successfully.")
