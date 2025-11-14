import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ensure images folder exists so savefig works
os.makedirs("images", exist_ok=True)

# load raw dataset
df = pd.read_csv("C:\\Users\\sabin\\OneDrive\\Desktop\\Python\\data for python\\Financial_data.csv")

print(df.head)
print(df.columns)

# clean column names so they are easier to work with
df.columns = df.columns.str.strip().str.replace(' ' , '_')
print(df.columns)

# rename for shorter reference
df = df.rename(columns= {'Units_Sold': 'Un'})
print(df.columns)

print(df.head)
print(df.dtypes)

# columns that need numeric fixing (symbols, commas, etc.)
cols_to_convert = [
    'Un',
    'Manufacturing_Price',
    'Sale_Price',
    'Gross_Sales',
    'Discounts',
    'Sales',
    'COGS',
    'Profit'
]

# clean numeric fields
for col in cols_to_convert:
    df[col] = (
        df[col]
        .replace(r'[\$,]', '', regex=True)     # remove $ and comma formatting
        .replace(' ', '', regex=False)         # remove random spaces
        .replace('-', '0', regex=False)        # convert "-" entries to zero
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')  # convert to proper numeric

print(df.dtypes)

# quick check for negative values
(df[cols_to_convert] < 0).values.sum()

print(df.head)

# handle missing discounts (common in messy datasets)
print(df['Discounts'].isnull().sum())
df['Discounts'] = df['Discounts'].fillna(0)
print(df['Discounts'].isnull().sum())

# ===================== SALES & PROFIT TREND =====================

grouped_df = df.groupby('Date').agg({'Sales': 'sum', 'Profit': 'sum'})

plt.plot(grouped_df.index, grouped_df['Sales'], label='Sales')
plt.plot(grouped_df.index, grouped_df['Profit'], label='Profit')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.grid()
plt.legend()

# save the main time series chart you liked
plt.savefig("images/sales_trend.png", dpi=300)

# ===================== SEGMENT ANALYSIS =========================

grouped_segment = df.groupby('Segment').agg({'Sales': 'sum', 'Profit':'sum'})

fig, ax = plt.subplots(2, 1, figsize=(12, 10))

ax[0].bar(grouped_segment.index, grouped_segment['Sales'], color='blue', alpha=0.8)
ax[0].set_title('Sales by Business Segment')
ax[0].set_xlabel('')
ax[0].set_ylabel('Amount')
ax[0].grid()

ax[1].bar(grouped_segment.index, grouped_segment['Profit'], color='green', alpha=0.8)
ax[1].set_title('Profit by Business Segment')
ax[1].set_xlabel('Segment')
ax[1].set_ylabel('Amount')
ax[1].grid()

plt.tight_layout()
plt.savefig("images/sales_profit_by_segment.png", dpi=300)  # save segment charts

# ===================== COUNTRY ANALYSIS =========================

grouped_country = df.groupby('Country').agg({'Sales': 'sum', 'Profit': 'sum'})
grouped_country = grouped_country.sort_values(by='Sales', ascending=False)

fig, ax = plt.subplots(2, 1, figsize=(12, 12))

ax[0].bar(grouped_country.index, grouped_country['Sales'], color='green', alpha=0.7)
ax[0].set_title('Sales by Country')
ax[0].set_xlabel('Country')
ax[0].set_ylabel('Amount')
ax[0].grid()

ax[1].bar(grouped_country.index, grouped_country['Profit'], color='blue', alpha=0.7)
ax[1].set_title('Profit by country')
ax[1].set_xlabel('Country')
ax[1].set_ylabel('Amount')
ax[1].grid()

plt.tight_layout()
plt.savefig("images/sales_profit_by_country.png", dpi=300)  # save country charts

# ===================== DISCOUNTS VS PROFIT =====================

plt.figure(figsize=(12,12))
plt.scatter(df['Discounts'], df['Profit'], alpha=0.8)
plt.title('Discounts vs Profit')
plt.xlabel('Discounts')
plt.ylabel('Profit')
plt.grid()
plt.savefig("images/discounts_vs_profit.png", dpi=300)  # save scatter

import seaborn as sns

# correlation check for numeric fields
corr_matrix = df.select_dtypes('number').corr()
print(corr_matrix)

plt.figure(figsize=(15,15))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5, square=True)
plt.title('correlation heatmap', fontsize=15, pad=15)
plt.savefig("images/correlation_heatmap.png", dpi=300)  # save heatmap

print(df.columns)
print(df['Date'].describe())

# convert date column into a usable datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')
print(df['Date'].dtypes)
print(df['Date'].head())

# extract monthly period for trend analysis
df['Year-Month'] = df['Date'].dt.to_period('M')
print(df['Date'].head())

# ===================== MONTHLY TREND =====================

monthly_data = df.groupby('Year-Month').agg({'Sales': 'sum', 'Profit':'sum'})
monthly_data.plot(kind='line', figsize=(12,12))
plt.title('Monthly sales and profit')
plt.xlabel('Year-month')
plt.ylabel('Amount')
plt.grid(True)
plt.legend()
plt.savefig("images/monthly_sales_profit.png", dpi=300)  # save monthly trend

# ===================== PRODUCT SEGMENT DISTRIBUTION =====================

product_distribution_market = pd.crosstab(df['Product'], df['Segment'])

plt.figure(figsize=(15,15))
sns.heatmap(product_distribution_market, annot=True, fmt='.2f', cmap='viridis', linewidths=0.5, square=True)
plt.title('Product distribution across the Market Segment')
plt.savefig("images/product_distribution.png", dpi=300)  # save product heatmap

print(df.head())

# ===================== PRICE RELATIONSHIP =====================

average_price = df.groupby('Product').agg({'Manufacturing_Price': 'mean', 'Sale_Price': 'mean'})

plt.figure(figsize=(14,14))
plt.scatter(average_price['Manufacturing_Price'], average_price['Sale_Price'], color='blue')
plt.title('Manufacturing Price vs Sale Price by Product')
plt.xlabel('Product')
plt.ylabel('Amount')
plt.grid(True)

# label points with product name
for i, product in enumerate(average_price.index):
    plt.text(average_price['Manufacturing_Price'][i],
             average_price['Sale_Price'][i],
             product, fontsize=9)

plt.savefig("images/manufacturing_vs_sale_price.png", dpi=300)  # save price scatter

print(df.head())

# ===================== AVG PROFIT BY SEGMENT =====================

profit_by_segment = df.groupby('Segment')['Profit'].mean().sort_values(ascending=False)

profit_by_segment.plot(kind='bar', figsize=(8,5), color='skyblue')
plt.title('Average Profit by Segment')
plt.ylabel('Average Profit')
plt.grid(True)
plt.savefig("images/avg_profit_by_segment.png", dpi=300)  # save final bar chart
plt.show()

