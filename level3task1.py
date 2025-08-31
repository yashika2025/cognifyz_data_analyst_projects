import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string

file_path = r"C:\Users\yashi\Downloads\dataset.csv"
df = pd.read_csv(file_path)

print(df.columns)  # Check your actual column names

review_col = 'Rating text'      # Update if needed
rating_col = 'Aggregate rating'

# Ensure ratings are numeric
df[rating_col] = pd.to_numeric(df[rating_col], errors='coerce')

def get_words(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

df['words'] = df[review_col].apply(get_words)

positive_words = {'good', 'great', 'excellent', 'amazing', 'delicious', 'friendly', 'perfect', 'tasty', 'wonderful', 'love', 'best', 'fresh'}
negative_words = {'bad', 'worst', 'terrible', 'awful', 'rude', 'cold', 'slow', 'dirty', 'disappointing', 'overpriced', 'stale', 'unfriendly'}

all_positive = []
all_negative = []
for word_list in df['words']:
    all_positive += [word for word in word_list if word in positive_words]
    all_negative += [word for word in word_list if word in negative_words]

top_pos = Counter(all_positive).most_common(5)
top_neg = Counter(all_negative).most_common(5)

print("Most common positive keywords:", ', '.join([w for w, _ in top_pos]))
print("Most common negative keywords:", ', '.join([w for w, _ in top_neg]))

df['review_length'] = df['words'].apply(len)
avg_length = df['review_length'].mean()
print(f"Average review length: {avg_length:.2f} words")

# Drop rows with missing ratings for correlation/plot
df = df.dropna(subset=[rating_col])

correlation = df['review_length'].corr(df[rating_col])
print(f"Correlation between review length and rating: {correlation:.2f}")

plt.scatter(df['review_length'], df[rating_col], alpha=0.5)
plt.title('Review Length vs. Rating')
plt.xlabel('Review Length (words)')
plt.ylabel('Rating')
plt.tight_layout()
plt.show()
