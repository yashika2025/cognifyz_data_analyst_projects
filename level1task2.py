import pandas as pd
import matplotlib.pyplot as plt

def get_city_counts(df, city_col):
    """Return a dictionary mapping each city to its restaurant count."""
    counts = {}
    for city in df[city_col]:
        counts[city] = counts.get(city, 0) + 1
    return counts

def get_average_ratings(df, city_col, rating_col):
    """Return a dictionary mapping each city to its average restaurant rating."""
    rating_totals = {}
    rating_counts = {}
    for idx, row in df.iterrows():
        city = row[city_col]
        rating = row[rating_col]
        if pd.notnull(rating):
            rating_totals[city] = rating_totals.get(city, 0) + rating
            rating_counts[city] = rating_counts.get(city, 0) + 1
    averages = {city: rating_totals[city]/rating_counts[city] for city in rating_totals}
    return averages

# Load your data
file_path = r"C:\Users\yashi\Downloads\dataset.csv"
df = pd.read_csv(file_path)

# Set your column names
city_column = 'City'
rating_column = 'Aggregate rating'  # Change if your column name is different

# 1. City with the most restaurants
city_counts = get_city_counts(df, city_column)
most_city = max(city_counts, key=city_counts.get)
print(f"City with the most restaurants: {most_city} ({city_counts[most_city]} restaurants)")

# 2. Average rating per city
avg_ratings = get_average_ratings(df, city_column, rating_column)
print("\nAverage restaurant ratings by city:")
for city, avg in sorted(avg_ratings.items(), key=lambda x: -x[1]):
    print(f"{city}: {avg:.2f}")

# 3. City with the highest average rating
top_avg_city = max(avg_ratings, key=avg_ratings.get)
print(f"\nCity with the highest average rating: {top_avg_city} ({avg_ratings[top_avg_city]:.2f})")

# Visualization
# Top 5 cities by restaurant count
sorted_cities = sorted(city_counts.items(), key=lambda x: -x[1])
top5_cities = sorted_cities[:5]
cities, counts = zip(*top5_cities)

# Top 5 cities by average rating
sorted_avg = sorted(avg_ratings.items(), key=lambda x: -x[1])
top5_avg = sorted_avg[:5]
avg_cities, avg_values = zip(*top5_avg)

fig, axs = plt.subplots(1, 2, figsize=(8, 3.5))
axs[0].bar(cities, counts, color='#9ecae1')
axs[0].set_title('Top 5 Cities by Restaurant Count')
axs[0].set_xlabel('City')
axs[0].set_ylabel('Number of Restaurants')

axs[1].bar(avg_cities, avg_values, color='#fdae6b')
axs[1].set_title('Top 5 Cities by Avg. Rating')
axs[1].set_xlabel('City')
axs[1].set_ylabel('Average Rating')

plt.tight_layout()
plt.show()
