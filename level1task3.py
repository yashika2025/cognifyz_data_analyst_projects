import pandas as pd
import matplotlib.pyplot as plt

def analyze_price_ranges(data, price_column):
    """
    Summarizes how many restaurants fall into each price category,
    and calculates the percentage for each group.
    """
    # Manually tally the price ranges
    price_counts = {}
    for val in data[price_column]:
        price_counts[val] = price_counts.get(val, 0) + 1

    # Calculate percentages
    total = len(data)
    price_percentages = {}
    for k, v in price_counts.items():
        price_percentages[k] = (v / total) * 100

    return price_counts, price_percentages

# Load your dataset
file_path = r"C:\Users\yashi\Downloads\dataset.csv"
df = pd.read_csv(file_path)

# Specify your price range column
price_col = 'Price range'  # Change if your column is named differently

# Analyze price range distribution
counts, percents = analyze_price_ranges(df, price_col)

# Print the results in a sorted fashion
print("Distribution of restaurants by price range:")
for pr in sorted(counts):
    print(f"Price Range {pr}: {counts[pr]} restaurants ({percents[pr]:.2f}%)")

# Prepare data for plotting
labels = [str(pr) for pr in sorted(counts)]
values = [counts[pr] for pr in sorted(counts)]

# Create a bar chart for the distribution
plt.figure(figsize=(6, 3.5))
plt.bar(labels, values, color='#5bc0eb')
plt.title('Distribution of Restaurants by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.tight_layout()
plt.show()
