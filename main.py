from data_cleaning import load_data, clean_data
from data_visualization import plot_rating_distribution, plot_reviews_per_category, plot_average_ratings_per_category
from data_analysis import calculate_age_rating_correlation, describe_numerical_columns, count_unique_values, analyze_low_ratings_by_age
from data_visualization import (plot_ratings_by_age_group, plot_sentiment_distribution, plot_reviews_per_category, plot_avg_rating_per_category,
                                plot_category_popularity_by_age, plot_liked_disliked_products, plot_low_ratings_by_age)
from sentiment_analysis import apply_sentiment_analysis, filter_negative_reviews, get_most_criticized_products
import pandas as pd
import numpy as np
import warnings
import seaborn as sns

# Ignore specific FutureWarning from pandas/seaborn
warnings.filterwarnings("ignore", category=FutureWarning)


# 1. Load the dataset
df = load_data('/Users/raphaelstanislas/Desktop/Portfolio Data Analysis/Women_Clothing/data/Womens Clothing E-Commerce Reviews.csv')

# 2. Clean the dataset
df_cleaned = clean_data(df)
# Summary statistics
# print(describe_numerical_columns(df_cleaned))

# Count unique values for key categorical columns
count_unique_values(df_cleaned)

# Calculate correlation between age and ratings
correlation_age_rating = calculate_age_rating_correlation(df_cleaned)
# print(f"Correlation between Age and Ratings: {correlation_age_rating}")

# 4. Visualize data
plot_rating_distribution(df_cleaned)
plot_reviews_per_category(df_cleaned)
plot_average_ratings_per_category(df_cleaned)

# # 5. Apply sentiment analysis
df_with_sentiment = apply_sentiment_analysis(df_cleaned)
# print(df_with_sentiment[['Review_Text', 'Sentiment']].head())

#
# # Optionally, save the cleaned data for further analysis
# df_cleaned.to_csv('data/cleaned_data.csv', index=False)

# # 1. Plot ratings distribution by age group
plot_ratings_by_age_group(df_cleaned)
# # Group by Age_Group and calculate descriptive statistics for ratings
# stats_by_age_group = df_cleaned.groupby('Age_Group')['Rating'].describe()
#
# # Print the statistics to examine Q1, Q3, and the median
# print(stats_by_age_group)

# # 2. Plot sentiment distribution
plot_sentiment_distribution(df_with_sentiment)

# # 3. Plot number of reviews per product category
plot_reviews_per_category(df_cleaned)
#
# # 4. Plot average rating per product category
plot_avg_rating_per_category(df_cleaned)
#
# # 5. Plot popularity of product categories by age group
plot_category_popularity_by_age(df_cleaned)



# # Identify the most criticized products
# most_criticized_products = get_most_criticized_products(df_with_sentiment)
# print("Most criticized products:\n", most_criticized_products)
#
# # Plot the top 10 liked/disliked products
plot_liked_disliked_products(df_with_sentiment)

# Create age groups
df_with_sentiment['Age_Group'] = pd.cut(df_with_sentiment['Age'],
                                        bins=[18, 25, 35, 45, 55, 65, 100],
                                        labels=['18-25', '26-35', '36-45', '46-55', '56-65', '65+'])

# Analyze and plot the categories with the lowest ratings by age group
low_ratings_analysis = analyze_low_ratings_by_age(df_with_sentiment)
plot_low_ratings_by_age(low_ratings_analysis)
