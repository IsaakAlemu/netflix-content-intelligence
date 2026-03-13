import pandas as pd
from sqlalchemy import create_engine

titles = pd.read_csv("data/clean_titles.csv")
credits = pd.read_csv("data/clean_credits.csv")

engine = create_engine(
    "postgresql://postgres:%40Isaak123@localhost:5432/netflix_project"
)
titles.to_sql("titles", engine, if_exists="replace", index=False)
credits.to_sql("credits", engine, if_exists="replace", index=False)

print("Data successfully loaded into PostgreSQL.")