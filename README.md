
Financial Data Analysis Project (Python)

This project is a full walkthrough of analyzing, cleaning, and visualizing financial data using Python. I built it to practice real-world data cleaning, exploratory analysis, and business-focused insights using Pandas, Matplotlib, Seaborn, and NumPy.

The dataset includes information like units sold, sales, discounts, COGS, profit, product category, segment, country, and dates. The goal is to understand how different business segments and countries perform, how discounts affect profitability, and how sales trends change over time.

* What This Project Covers
1. Data Cleaning & Preparation

Removed unwanted characters like $, commas, spaces, and dashes from numeric columns

Converted cleaned columns into numeric data types safely

Renamed columns for easier access

Handled missing values (e.g., filling missing discounts with 0)

Converted date strings into real datetime format

Extracted Year-Month for trend analysis

This step ensures the dataset is accurate before running any analysis.

* Key Analyses & Visualizations
1) Sales vs Profit Over Time

![Image Alt](https://github.com/sumanlamichhane984/Sales-data-Analysis/blob/main/Figure_1.png)

Plotted total sales and profit trends by date to see how the business performed across time.

2) Sales and Profit by Business Segment

Compared performance across segments to identify which areas drive the most revenue and profitability.

3)  Country Performance

Ranked countries based on their total sales and profits to understand regional strengths.

4)  Discounts vs Profit Relationship

Scatter plot showing how discount levels impact overall profit.

5) Correlation Heatmap

Used a correlation matrix and heatmap to spot relationships between numerical features like:

Units sold

Sale price

Gross sales

COGS

Profit

6) Monthly Trends

Aggregated data by year-month to observe monthly patterns in sales and profit.

7) Product Distribution Across Segments

A heatmap showing which products perform well in each segment.

8)  Manufacturing Price vs Sale Price

Scatter plot comparing product manufacturing costs to selling prices with product labels.

9)  Average Profit by Segment

Bar chart showing which business segments are the most profitable on average.

*  Tech Used

Python

Pandas

NumPy

Matplotlib

Seaborn

* What You Can Learn From This Project

This project is helpful if you want to learn how to:

Clean messy financial data

Handle missing values and inconsistent formatting

Explore trends using groupby operations

Visualize business metrics

Build charts that help with decision-making

Understand data patterns that affect revenue and profit
