import pandas as pd
import matplotlib.pyplot as plt

def analyze_cuisines(dataframe, col_name):
    """Analyzes and visualizes the top three cuisines in the dataset."""
    # Count cuisines manually
    cuisine_dict = {}
    for cuisine in dataframe[col_name]:
        cuisine_dict[cuisine] = cuisine_dict.get(cuisine, 0) + 1
    sorted_cuisines = sorted(cuisine_dict.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_cuisines[:3]
    total = len(dataframe)
    print("My Top 3 Cuisines Analysis:")
    for cuisine, count in top3:
        perc = (count / total) * 100
        print(f"{cuisine}: {count} restaurants ({perc:.1f}%)")
    # Visualization
    names = [c[0] for c in top3]
    counts = [c[1] for c in top3]
    percs = [(c/total)*100 for c in counts]
    fig, axs = plt.subplots(1, 2, figsize=(7, 3))
    axs[0].bar(names, counts, color=['#f7b267', '#f4845f', '#4f98ca'])
    axs[0].set_title('Top Cuisines (Count)')
    axs[1].pie(percs, labels=names, autopct='%1.1f%%')
    axs[1].set_title('Top Cuisines (%)')
    plt.tight_layout()
    plt.show()

# Load data and run analysis
file_path = r"C:\Users\yashi\Downloads\dataset.csv"
df = pd.read_csv(file_path)
analyze_cuisines(df, 'Cuisines')
