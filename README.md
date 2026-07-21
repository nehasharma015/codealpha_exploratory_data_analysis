
# 📊 Exploratory Data Analysis (EDA) on Books Dataset

## Overview

This project performs **Exploratory Data Analysis (EDA)** on a custom dataset created through web scraping from the **Books to Scrape** website. The objective is to understand the dataset, identify patterns and trends, detect anomalies, validate assumptions using statistics, and generate meaningful visualizations.

This project was completed as part of a **Data Analytics Internship**.

---

## Objectives

The main objectives of this project are:

- Explore the structure of the dataset.
- Understand variables and their data types.
- Ask meaningful business questions before analysis.
- Identify trends, patterns, and anomalies.
- Test hypotheses using statistical analysis.
- Detect potential data quality issues.
- Visualize the dataset for better understanding.

---

## Dataset

The dataset was created by scraping the **Books to Scrape** website.

### Dataset Features

| Column | Description |
|---------|-------------|
| Title | Name of the book |
| Price | Price of the book (£) |
| Rating | Book rating (1–5 Stars) |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Project Workflow

```
Load Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Understand Dataset Structure
      │
      ▼
Descriptive Statistics
      │
      ▼
Business Questions
      │
      ▼
Pattern & Trend Analysis
      │
      ▼
Hypothesis Testing
      │
      ▼
Outlier Detection
      │
      ▼
Data Visualization
      │
      ▼
Summary & Insights
```

---

## Data Cleaning

The following preprocessing steps were performed:

- Removed currency symbols from the Price column.
- Removed unwanted special characters.
- Converted Price into float datatype.
- Converted Rating values into numeric format.
- Verified data types.
- Checked for missing values.

---

## Exploratory Data Analysis

The following analyses were performed:

### Dataset Exploration

- Dataset information
- Data types
- Missing value analysis
- Summary statistics

### Price Analysis

- Average price
- Maximum price
- Minimum price
- Median price
- Standard deviation

### Rating Analysis

- Average rating
- Most common rating
- Rating distribution
- Percentage of each rating

---

## Business Questions

The following questions were answered:

1. What is the average price of books?
2. What is the highest and lowest book price?
3. What is the average rating of books?
4. Which rating category is most common?
5. Are expensive books rated higher?
6. What percentage of books have ratings greater than 4?
7. How are book prices distributed?
8. Are there any price outliers?
9. What insights can be derived from the dataset?

---

## Statistical Analysis

The project includes:

- Descriptive Statistics
- Correlation Analysis
- Quartile Analysis
- Interquartile Range (IQR)
- Outlier Detection
- Distribution Analysis

---

## Visualizations

The following visualizations were created:

### Price Distribution

- Histogram
- Mean and Median indicators

### Rating Distribution

- Bar Chart

### Price vs Rating

- Scatter Plot
- Trend Line

### Outlier Detection

- Box Plot

---

## Key Insights

The analysis provides insights such as:

- Average price of books
- Most common book rating
- Price distribution
- Correlation between price and rating
- Percentage of highly rated books
- Presence of price outliers

---

## Project Structure

```
EDA-Books-Dataset/

│── eda_books.py
│── books_dataset.csv
│── requirements.txt
│── README.md
│── images/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/nehasharma015/EDA-Books-Dataset.git
```

Move to the project folder

```bash
cd EDA-Books-Dataset
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python eda_books.py
```

---

## Output

The project generates:

- Statistical Summary
- Business Insights
- Histogram
- Bar Chart
- Scatter Plot
- Box Plot

---

## Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Data Preprocessing
- Descriptive Statistics
- Correlation Analysis
- Outlier Detection
- Hypothesis Exploration
- Data Visualization
- Python Programming

---

## Future Improvements

- Perform category-wise analysis.
- Add hypothesis testing using statistical significance tests.
- Build an interactive dashboard using Streamlit or Power BI.
- Analyze larger datasets for deeper business insights.
- Export analysis reports in PDF format.

---

## Author

**Neha Sharma**

GitHub: https://github.com/kantisharma07
