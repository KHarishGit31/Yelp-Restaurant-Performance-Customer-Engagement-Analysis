
# Yelp Restaurant Performance & Customer Engagement Analysis

## Project Overview

This project analyzes restaurant performance and customer engagement using the Yelp dataset. The goal is to understand how customer ratings, reviews, tips, and check-ins relate to restaurant popularity and success.

Using **Python for data analysis**, **SQL for data aggregation**, and **Power BI for visualization**, the project transforms raw Yelp data into meaningful insights that help identify high-performing restaurants and cities with strong customer engagement.

The final output of this project is an **interactive Power BI dashboard** that allows users to explore restaurant performance, geographic distribution, and customer interaction patterns.

---

# Project Objectives

The main objectives of this project are:

* Analyze restaurant performance based on customer ratings and engagement metrics
* Examine the relationship between restaurant ratings and popularity
* Identify cities with high restaurant activity and customer engagement
* Evaluate customer interaction through reviews, tips, and check-ins
* Develop an interactive **Power BI dashboard** to visualize restaurant performance insights

---

# Dataset Description

The dataset used in this project is derived from the Yelp dataset and contains information about restaurants and customer interactions.

Key attributes used in the analysis include:

* Restaurant name
* City and state
* Average rating
* Review count
* Tip count
* Check-in count

The original Yelp dataset contains multiple business categories. For this analysis, the dataset was **filtered to include only restaurant-related businesses** to focus specifically on restaurant performance and customer engagement.

---

# Project Workflow

The project follows a structured data analytics workflow:

```
Raw Yelp Dataset
        ↓
Data Cleaning & Filtering (Python)
        ↓
Data Aggregation & Feature Engineering (SQL)
        ↓
Interactive Dashboard Development (Power BI)
        ↓
Business Insights
```

---

# Tools & Technologies

| Tool         | Purpose                                     |
| ------------ | ------------------------------------------- |
| Python       | Data cleaning and exploratory data analysis |
| Pandas       | Data manipulation                           |
| SQLite / SQL | Data aggregation and summary table creation |
| Power BI     | Dashboard creation and data visualization   |

---

# Power BI Dashboard
![Dashboard Overview](images/Overview.jpg)
The final dashboard consists of **four analytical sections**:

### 1. Overview Dashboard

Provides key performance indicators such as:

* Average restaurant rating
* Total restaurants
* Total reviews
* Total tips
* Total check-ins
* Success score

### 2. Restaurant Performance Analysis

Analyzes restaurant popularity and performance using:

* Top restaurants by review count
* Rating vs popularity relationship
* Success score comparison

### 3. City Performance Analysis

Explores restaurant distribution across cities:

* Cities with the highest restaurant concentration
* Cities with the highest ratings
* Restaurant activity by location

### 4. Customer Engagement Analysis

Examines how customers interact with restaurants through:

* Reviews
* Tips
* Check-ins
* Engagement relationships

---

# Key Insights

Some important insights from the analysis include:

* Most restaurants have ratings between **3 and 4 stars**
* Highly rated restaurants tend to attract more customer engagement
* Customer reviews and tips show a strong positive relationship
* Some cities have significantly higher restaurant activity and engagement
* Customer engagement metrics are strong indicators of restaurant success

---

# Project Structure

```
yelp-restaurant-analysis
│
├── data
│   cleaned_dataset.csv
│
├── notebooks
│   data_analysis.ipynb
│
├── dashboard
│   yelp_restaurant_dashboard.pbix
│
├── report
│   project_report.pdf
│
└── README.md
```

---

# Future Improvements

Possible extensions of this project include:

* Analyzing restaurant categories and cuisine types
* Performing time-based trend analysis of reviews and engagement
* Applying machine learning models to predict restaurant success

---

# Author
# Harish Kumar
Project developed as part of a **data analytics project using Python and Power BI** to analyze Yelp restaurant data and customer engagement patterns.


