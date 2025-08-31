import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = r"C:\Users\yashi\Downloads\dataset.csv"
df = pd.read_csv(file_path)

# Set your column names (update if needed)
votes_col = 'Votes'
rating_col = 'Aggregate rating'
name_col = 'Restaurant Name'  # Change if your dataset uses a different column name

# Ensure numeric types for calculations
df[votes_col] = pd.to_numeric(df[votes_col], errors='coerce')
df[rating_col] = pd.to_numeric(df[rating_col], errors='coerce')

# Drop rows with missing values in votes or rating
df_clean = df.dropna(subset=[votes_col, rating_col])

# 1. Find restaurant(s) with the highest and lowest number of votes
max_votes = df_clean[votes_col].max()
min_votes = df_clean[votes_col].min()

top_restaurants = df_clean[df_clean[votes_col] == max_votes][name_col].tolist()
bottom_restaurants = df_clean[df_clean[votes_col] == min_votes][name_col].tolist()

print(f"Restaurant(s) with the highest votes ({max_votes}): {', '.join(top_restaurants)}")
print(f"Restaurant(s) with the lowest votes ({min_votes}): {', '.join(bottom_restaurants)}")

# 2. Correlation between votes and rating
correlation = df_clean[votes_col].corr(df_clean[rating_col])
print(f"Correlation between number of votes and rating: {correlation:.2f}")

# 3. Scatter plot to visualize the relationship
plt.figure(figsize=(7, 4))
plt.scatter(df_clean[votes_col], df_clean[rating_col], alpha=0.5, color='purple')
plt.title('Votes vs. Aggregate Rating')
plt.xlabel('Number of Votes')
plt.ylabel('Aggregate Rating')
plt.tight_layout()
plt.show()
