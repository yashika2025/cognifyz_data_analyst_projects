import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = r"C:\Users\yashi\Downloads\dataset.csv"
df = pd.read_csv(file_path)

# Set your column names (update if needed)
price_col = 'Price range'
online_col = 'Has Online delivery'
table_col = 'Has Table booking'

# Convert to string for grouping consistency
df[price_col] = df[price_col].astype(str)
df[online_col] = df[online_col].astype(str)
df[table_col] = df[table_col].astype(str)

# Calculate percentage of online delivery for each price range
online_summary = df.groupby([price_col, online_col]).size().unstack(fill_value=0)
online_percent = online_summary.div(online_summary.sum(axis=1), axis=0) * 100

# Calculate percentage of table booking for each price range
table_summary = df.groupby([price_col, table_col]).size().unstack(fill_value=0)
table_percent = table_summary.div(table_summary.sum(axis=1), axis=0) * 100

# Print the percentage tables
print("Online delivery availability by price range (%):")
print(online_percent)
print("\nTable booking availability by price range (%):")
print(table_percent)

# Visualize: Stacked bar charts
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Online delivery
online_percent.plot(kind='bar', stacked=True, ax=axs[0], color=['#b2df8a', '#1f78b4'])
axs[0].set_title('Online Delivery by Price Range')
axs[0].set_ylabel('Percentage (%)')
axs[0].set_xlabel('Price Range')

# Table booking
table_percent.plot(kind='bar', stacked=True, ax=axs[1], color=['#fdb462', '#386cb0'])
axs[1].set_title('Table Booking by Price Range')
axs[1].set_ylabel('Percentage (%)')
axs[1].set_xlabel('Price Range')

plt.tight_layout()
plt.show()

# Additional: Are higher-priced restaurants more likely to offer these?
if 'Yes' in online_percent.columns:
    print("\nOnline delivery rate by price range (Yes %):")
    print(online_percent['Yes'])
if 'Yes' in table_percent.columns:
    print("\nTable booking rate by price range (Yes %):")
    print(table_percent['Yes'])

# Simple interpretation
print("\nInterpretation tip: Look for increasing 'Yes' percentages as price range increases to see if higher-priced restaurants are more likely to offer these services.")
