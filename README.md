# ***Women's Clothing E-Commerce Reviews Analysis***

## ***Project Overview***
This project aims to analyze customer reviews from a women's clothing e-commerce dataset. The analysis will focus on customer satisfaction, product popularity, and sentiment analysis based on the review text. By understanding the data, we can extract valuable insights to help improve product offerings and the overall customer experience.

## ***Objectives***
The main objectives of this project are:

1. **Analyze sales and customer reviews**:
   - Identify the most popular and highest-rated products.
   - Examine customer satisfaction through product ratings and review texts.

2. **Customer segmentation**:
   - Segment customers by age and product preferences to understand different customer groups.

3. **Sentiment analysis**:
   - Classify review texts into three categories (positive, neutral, negative) based on customer sentiment.

4. **Strategic recommendations**:
   - Provide actionable insights for marketing and product teams to improve customer experience, increase sales, and adjust marketing strategies.

## ***Project Structure***
- `main.py`: The main script that orchestrates the project by loading data, cleaning it, performing analysis, and visualizing the results.
- `data_cleaning.py`: Contains functions to load and clean the dataset (handle missing values, rename columns, etc.).
- `data_visualization.py`: Contains functions to generate various data visualizations (ratings distribution, number of reviews per product, etc.).
- `data_analysis.py`: Performs statistical analyses such as calculating correlations and descriptive statistics.
- `sentiment_analysis.py`: Contains functions to perform sentiment analysis on the review texts using the TextBlob library.
- `data/`: Directory containing the raw dataset (`Womens_Clothing_E_Commerce_Reviews.csv`) and the cleaned dataset (`cleaned_data.csv`).

## ***Technologies and Libraries Used***
The following technologies and Python libraries were used in this project:

- **Python**: Main programming language for data manipulation and analysis.
- **pandas**: For data cleaning, manipulation, and handling missing values.
- **numpy**: For numerical operations and handling arrays.
- **seaborn**: For data visualization and creating insightful plots.
- **matplotlib**: For additional plotting and visual representation of data.
- **TextBlob**: For sentiment analysis of review texts to classify the sentiment.
- **scikit-learn**: (Optional) For machine learning if future sentiment classification models are applied.
- **Tableau/Power BI**: (Optional) For creating interactive dashboards and visualizations (if data export to these tools is considered).

## ***Dataset Overview***
The dataset used in this project is provided in the `data/` directory and includes the following columns:

- **Clothing ID**: Unique identifier for each product.
- **Age**: Age of the reviewer.
- **Title**: Title of the review.
- **Review Text**: Main body of the customer's review.
- **Rating**: Product rating given by the customer (on a 1–5 scale).
- **Recommended IND**: Binary indicator (1 if the customer recommends the product, 0 if not).
- **Positive Feedback Count**: Number of positive responses to the review.
- **Division Name**: High-level product division (e.g., General, Dresses, Bottoms).
- **Department Name**: Mid-level product department (e.g., Tops, Dresses, Pants).
- **Class Name**: Low-level product classification (e.g., Blouses, Knitwear).

## ***Key Insights***
Some key insights derived from the analysis include:

1. **Product Ratings**:
   - Most products tend to receive higher ratings (4 or 5), reflecting overall customer satisfaction.
   - Certain product categories such as "Bottoms" and "Knitwear" exhibit slightly lower ratings, suggesting potential areas for improvement.

2. **Sentiment Analysis**:
   - Positive reviews frequently contain words such as "love", "perfect", and "quality", while negative reviews mention issues like "poor", "disappointing", and "fit problems."
   - The sentiment aligns well with the numerical ratings in most cases, though there are instances where reviews with neutral or slightly negative sentiment still give high ratings.

3. **Customer Segmentation**:
   - Younger customers tend to give higher ratings, especially for trendy items like "Dresses" and "Tops", while older customers are generally more critical, particularly in categories like "Bottoms."

4. **Product Recommendations**:
   - Products in the "Dresses" and "Tops" categories are more frequently recommended by customers, likely due to better fit or quality.

## ***Recommendations***

1. **Improve Lower-Rated Product Categories**:
   - Focus on gathering customer feedback on product categories like "Bottoms" and "Knitwear" to address specific issues, such as fit or material quality.

2. **Enhance Customer Experience for Older Demographics**:
   - Provide more detailed product information, especially related to sizing, to help older customers make more informed purchasing decisions.

3. **Leverage Positive Reviews in Marketing**:
   - Highlight top-rated and frequently recommended products in marketing campaigns to attract new customers and drive sales.

4. **Encourage Detailed Reviews**:
   - Incentivize customers to leave more detailed reviews by offering rewards or creating easy-to-use review templates, which will help future customers make better decisions.

## ***Installation Instructions***

To run this project on your local machine, follow the steps below:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Raphstn/your-repo-name.git
