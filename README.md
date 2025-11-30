Finish 
Supermarket Sales EDA using Python, Pandas, NumPy, Matplotlib, and Seaborn — delivering insights on customer patterns, category trends, peak business hours, and payment preferences. Through clean visualizations and structured analysis, this project highlights important KPIs that support better retail decision-making.

**Dataset**

*File Used: supermarket_sales.csv*

Columns include: 

1.City 

2.Gender 

3.Customer Type 

4.Product line 

5.Unit Price 

6.Quantity 

7.Tax 

8.Total 

9.Date 

10.Time 

11.Payment method 

12.Rating 

13.Gross Income

**Libraries Used**

1.Pandas

2.Matplotlib 

3.Seaborn 

4.NumPy

**Data Cleaning Steps**

1. Converted the Date column to datetime 

2. Extracted hour from Time 

3. Removed missing values 

4. Removed duplicate rows 

5. Dropped unused column (gross margin percentage) 

6. Reset the index

**Business Questions Solved**

*1️. How many people visited from each city?

*→ Countplot of City → Countplot of City 

-> Yangon & Naypyitaw have the highest customer counts.



2️. What is the distribution of customer types (Member vs Normal)? 

-> Both Member and Normal customers visit almost equally.


3️. Gender distribution of visitors

-> Slightly more Males visit the supermarket.


4️. Which payment method is most used? 

-> E-Wallet is the most preferred payment option.


5️. Which product line generated the highest revenue? 

→ Barplot of Product line vs Total Revenue

-> Health & Beauty generates the highest total revenue.


6️. Which gender spent more money?

→ Barplot of Gender vs Total Spending 

-> Male and Female customers spend almost equally.


7️. What is the relationship between Quantity and Total? 

→ Scatterplot 

-> A positive linear relation

— total increases with quantity.


8️. How does total revenue vary daily? 

→ Line plot of Total vs Date 

-> Revenue fluctuates daily with several peak days.


9️. What are the busiest hours? 

→ Line plot of Total vs Time 

-> Peak activity at 10 AM, stable between 5 PM – 7 PM, drops after 8 PM.


10.Correlation between numerical features

→ Heatmap ➡ Total and Gross Income are highly correlated (expected). 

➡ Quantity shows moderate correlation with Total. 

-> Time has no relation with Total.

**Saved Visualizations**

All plots are saved as PNG files inside the project folder: 

1.city_count.png

2.customer_type_count.png 

3.gender_count.png 

4.payment_methods_count.png 

5.product_total_amount.png

6.gender_total_amount.png

7.quantity_total_amount.png

8.daily_trends_total_amount.png 

9.trend_over_time_total_amount.png

10.correlation_heatmap.png

**Final Insights**

1.Best-performing product: Health & Beauty 

2.City with highest visitors: Yangon & Naypyitaw 

3.Peak revenue hours: 10 AM and 5-7 PM 

4.Preferred payment method: E-Wallet

5.Customer mix: Equal Member & Normal; Male slightly more

6.Sales behavior: Higher quantity → higher total

**What I Learned**

1.Data cleaning using Pandas 

2.Visualizations with Seaborn 

3.Finding business insights from real-world data 

4.Exporting and saving charts

**Future Improvements**

1.Build a Power BI dashboard for the same dataset

2.Add product-wise monthly trends




