import pandas as pd

def online_delivery_stats(data, delivery_col, rating_col):
    """
    Calculates the percentage of restaurants offering online delivery,
    and compares average ratings for those with and without the service.
    """
    # Count how many restaurants offer online delivery
    total = len(data)
    delivery_yes = data[data[delivery_col] == 'Yes']
    delivery_no = data[data[delivery_col] == 'No']

    # Calculate percentage
    percent_delivery = (len(delivery_yes) / total) * 100

    # Calculate average ratings
    avg_rating_delivery = delivery_yes[rating_col].mean()
    avg_rating_no_delivery = delivery_no[rating_col].mean()

    return percent_delivery, avg_rating_delivery, avg_rating_no_delivery

# Load your dataset
file_path = r"C:\Users\yashi\Downloads\dataset.csv"
df = pd.read_csv(file_path)

# Specify your column names
online_col = 'Has Online delivery'   # Change if your column is named differently
rating_col = 'Aggregate rating'      # Change if your column is named differently

# Get the results
percent, avg_yes, avg_no = online_delivery_stats(df, online_col, rating_col)

# Print the results
print(f"Percentage of restaurants offering online delivery: {percent:.2f}%")
print(f"Average rating (with online delivery): {avg_yes:.2f}")
print(f"Average rating (without online delivery): {avg_no:.2f}")
