import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import os

engine = create_engine(
    "postgresql://postgres:%40Isaak123@localhost:5432/netflix_project"
)

os.makedirs("visuals", exist_ok=True)

# 1 Content growth
query1 = """
SELECT release_year, COUNT(*) as total_titles
FROM titles
GROUP BY release_year
ORDER BY release_year;
"""

df1 = pd.read_sql(query1, engine)

plt.figure(figsize=(10,6))
sns.lineplot(data=df1, x="release_year", y="total_titles")
plt.title("Netflix Content Growth Over Time")
plt.savefig("visuals/content_growth.png")
plt.close()


# 2 Top genres
query2 = """
SELECT genres, COUNT(*) as total
FROM titles
GROUP BY genres
ORDER BY total DESC
LIMIT 10;
"""

df2 = pd.read_sql(query2, engine)

plt.figure(figsize=(10,6))
sns.barplot(data=df2, x="total", y="genres")
plt.title("Top Genres on Netflix")
plt.savefig("visuals/top_genres.png")
plt.close()


# 3 Movies vs Shows
query3 = """
SELECT type, COUNT(*) as total
FROM titles
GROUP BY type;
"""

df3 = pd.read_sql(query3, engine)

plt.figure(figsize=(8,6))
sns.barplot(data=df3, x="type", y="total")
plt.title("Movies vs TV Shows")
plt.savefig("visuals/content_type.png")
plt.close()


# 4 Top actors
query4 = """
SELECT name, COUNT(*) as appearances
FROM credits
GROUP BY name
ORDER BY appearances DESC
LIMIT 10;
"""

df4 = pd.read_sql(query4, engine)

plt.figure(figsize=(10,6))
sns.barplot(data=df4, x="appearances", y="name")
plt.title("Top Actors on Netflix")
plt.savefig("visuals/top_actors.png")
plt.close()


# 5 Runtime distribution
query5 = """
SELECT runtime
FROM titles
WHERE runtime IS NOT NULL;
"""

df5 = pd.read_sql(query5, engine)

plt.figure(figsize=(10,6))
sns.histplot(df5["runtime"], bins=30)
plt.title("Runtime Distribution")
plt.savefig("visuals/runtime_distribution.png")
plt.close()

print("Visualizations created successfully.")