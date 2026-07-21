import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better visuals
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load and clean data
df = pd.read_csv(r"C:\Users\nehasharma\Desktop\python\Internship_Projects\Project_1\books_dataset.csv")

# Clean Price column
df["Price"] = df["Price"].str.replace(r'[^\d.]', '', regex=True).astype(float)

# Clean Rating column
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["Rating"] = df["Rating"].map(rating_map)

print("=" * 60)
print("BOOKS DATA ANALYSIS - EDA REPORT")
print("=" * 60)

# ===================== PRICE ANALYSIS =====================
print("\n PRICE ANALYSIS")
print("-" * 40)
print(f"Average Book Price: £{df['Price'].mean():.2f}")
print(f"Maximum Price: £{df['Price'].max():.2f}")
print(f"Minimum Price: £{df['Price'].min():.2f}")
print(f"Median Price: £{df['Price'].median():.2f}")
print(f"Standard Deviation: £{df['Price'].std():.2f}")

# ===================== RATING ANALYSIS =====================
print("\n RATING ANALYSIS")
print("-" * 40)
print(f"Most Common Rating: {df['Rating'].mode()[0]} stars")
print(f"Average Rating: {df['Rating'].mean():.2f} stars")
print(f"Median Rating: {df['Rating'].median():.0f} stars")

# Rating distribution
rating_counts = df['Rating'].value_counts().sort_index()
print("\nRating Distribution:")
for rating, count in rating_counts.items():
    print(f"  {rating} Star: {count} books ({count/len(df)*100:.1f}%)")

# ===================== SOME ANOTHER RELATED QUESTIONS =====================
print("\n SOME ANOTHER RELATED QUESTIONS")
print("-" * 40)

# 1. Are expensive books rated higher?
print("\n1. Price vs Rating Correlation:")
correlation = df['Price'].corr(df['Rating'])
print(f"   Correlation coefficient: {correlation:.3f}")
if correlation > 0.3:
    print("    Positive correlation: Expensive books tend to have higher ratings")
elif correlation < -0.3:
    print("    Negative correlation: Cheaper books tend to have higher ratings")
else:
    print("    Weak correlation: Price and rating are not strongly related")

# 2. Which rating category dominates?
print("\n2. Rating Category Dominance:")
dominant_rating = df['Rating'].mode()[0]
dominant_percentage = (df['Rating'].value_counts()[dominant_rating] / len(df)) * 100
print(f"   {dominant_rating}-star rating dominates with {dominant_percentage:.1f}% of books")

# 3. What percentage of books have rating > 4?
high_rating_pct = (df[df['Rating'] > 4].shape[0] / len(df)) * 100
print(f"\n3. Books with Rating > 4: {high_rating_pct:.1f}%")

# 4. Price distribution
print("\n4. Price Distribution:")
price_quartiles = df['Price'].quantile([0.25, 0.5, 0.75])
print(f"   25th Percentile: £{price_quartiles[0.25]:.2f}")
print(f"   50th Percentile (Median): £{price_quartiles[0.5]:.2f}")
print(f"   75th Percentile: £{price_quartiles[0.75]:.2f}")

# 5. Outlier detection
print("\n5. Outlier Analysis:")
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['Price'] < lower_bound) | (df['Price'] > upper_bound)]
print(f"   Number of price outliers: {len(outliers)}")
print(f"   Outlier percentage: {len(outliers)/len(df)*100:.1f}%")
if len(outliers) > 0:
    print(f"   Outlier price range: £{outliers['Price'].min():.2f} - £{outliers['Price'].max():.2f}")

# ===================== VISUALIZATIONS =====================
print("\n Generating Visualizations]")

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Price Distribution (Histogram)
axes[0, 0].hist(df['Price'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 0].axvline(df['Price'].mean(), color='red', linestyle='--', label=f'Mean: £{df["Price"].mean():.2f}')
axes[0, 0].axvline(df['Price'].median(), color='green', linestyle='--', label=f'Median: £{df["Price"].median():.2f}')
axes[0, 0].set_xlabel('Price (£)')
axes[0, 0].set_ylabel('Number of Books')
axes[0, 0].set_title('Price Distribution')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 2. Rating Distribution (Bar Chart)
rating_counts = df['Rating'].value_counts().sort_index()
colors = ['#ff9999', '#ffcc99', '#99cc99', '#66b3ff', '#c2c2f0']
bars = axes[0, 1].bar(rating_counts.index, rating_counts.values, color=colors, edgecolor='black')
for bar, count in zip(bars, rating_counts.values):
    axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                    f'{count}', ha='center', va='bottom')
axes[0, 1].set_xlabel('Rating (Stars)')
axes[0, 1].set_ylabel('Number of Books')
axes[0, 1].set_title('Rating Distribution')
axes[0, 1].grid(True, alpha=0.3)

# 3. Price vs Rating (Scatter Plot)
scatter = axes[1, 0].scatter(df['Rating'], df['Price'], alpha=0.6, c=df['Price'], 
                             cmap='viridis', s=50)
axes[1, 0].set_xlabel('Rating (Stars)')
axes[1, 0].set_ylabel('Price (£)')
axes[1, 0].set_title('Price vs Rating Correlation')
axes[1, 0].grid(True, alpha=0.3)
plt.colorbar(scatter, ax=axes[1, 0], label='Price (£)')

# Add trend line
z = np.polyfit(df['Rating'], df['Price'], 1)
p = np.poly1d(z)
axes[1, 0].plot(df['Rating'].sort_values(), p(df['Rating'].sort_values()), 
                "r--", linewidth=2, label=f'Trend (r={correlation:.3f})')
axes[1, 0].legend()

# 4. Box Plot for Outliers
box = axes[1, 1].boxplot(df['Price'], patch_artist=True, 
                         boxprops=dict(facecolor='lightblue'))
axes[1, 1].set_ylabel('Price (£)')
axes[1, 1].set_title('Price Box Plot (Outlier Detection)')
axes[1, 1].grid(True, alpha=0.3)

# Add outlier count annotation
axes[1, 1].text(1, df['Price'].max() * 0.95, 
                f'Outliers: {len(outliers)} books\n({len(outliers)/len(df)*100:.1f}%)',
                ha='center', bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.5))

plt.tight_layout()

# ===================== SUMMARY =====================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"• Total Books Analyzed: {len(df)}")
print(f"• Average Book Price: £{df['Price'].mean():.2f}")
print(f"• Most Common Rating: {df['Rating'].mode()[0]} stars")
print(f"• Books with Rating > 4: {high_rating_pct:.1f}%")
print(f"• Price-Rating Correlation: {correlation:.3f}")

# Additional insights
print("\n KEY INSIGHTS:")
if high_rating_pct > 50:
    print("Majority of books have high ratings (>4 stars)")
else:
    print("Less than half of books have high ratings (>4 stars)")

if len(outliers) > len(df) * 0.05:
    print("Significant number of price outliers detected")
else:
    print("Few price outliers detected")
# Show the plots
plt.show()

print("\nEDA Complete, Visualizations displayed above")