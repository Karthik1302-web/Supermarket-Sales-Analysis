#What are the questions to solve in this dataset.
-------------------------------------------------------------------------
#1.Count the number of Peoples in each city.
#2.Count the number of Customer type in the Super Market(Member/Normal).
#3.Count the number of Gender(Male/Female).
#4.Count the number of Payment Methods.
#5.Check which products have achieved highest Revenue.
#6.Check which gender have spent most of the money.
#7.Check the relation b/w Quantity and total.
#8.Check total revenue Trend over Date.
#9.Check total revenue Trend over Time.
#10.Correlation Heatmaps.
----------------------------------------------------------

#Step1 : Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Step2 : Load Dataset and Basic Info
Market = pd.read_csv('supermarket_sales.csv')
print(Market.head())

#Checking the number of rows and columns
print(Market.info())

#Basic statistics 
print(Market.describe())

#Checkl for Number 0f missing values
print(Market.isnull().sum())

#Check for any duplicate values
print(Market.duplicated().sum())

#Step3 : converting date to datetime and droping the missing & duplicate values 

#Convetrting date column to datetime 
Market['Date'] = pd.to_datetime(Market['Date'])

Market['Time'] = pd.to_datetime(Market['Time'],format = '%H:%M').dt.hour

#Droping the missing values
Market.dropna(inplace=True)

#Droping Duplicates
Market.drop_duplicates(inplace=True)

Market.drop(columns = ['gross margin percentage'],inplace=True)

#Step 4 : Data Visualization

#1.Checking count of people from each city
sns.countplot(x=Market['City'],order=Market['City'].value_counts().index,label='City')
plt.title('Number of People from each city')
plt.savefig('city_count.png', dpi=300, bbox_inches='tight')
plt.show()
#This plot shows the count of number of peoples from each city.
#Here the more number of people are from both Yangon and Naypyitaw city.


#2.Checking customer type who visits the SuperMarket
sns.countplot(x=Market['Customer type'],order=Market['Customer type'].value_counts().index,label='Customer Type')
plt.title('Customer Type')
plt.savefig('customer_type_count.png', dpi=300, bbox_inches='tight')    
plt.show()
#This plot shows the count of customer type who visits SuperMarket.
#Both the member and normal type of customers visits almost similar to the Super Market.
 
#3.checking Gender count 
sns.countplot(x=Market['Gender'],order=Market['Gender'].value_counts().index,label='Gender')
plt.title('Gender count visiting Super Market')
plt.savefig('gender_count.png', dpi=300, bbox_inches='tight')
plt.show()
#This plot shows the count of female and male visitors of Super Market.
#As the plot shows that the slightly more Male customers visit the  Super Market than the female customers.

#4.Checking Payment Methods type
sns.countplot(x=Market['Payment'],order=Market['Payment'].value_counts().index,label='Payment Methods')
plt.title('Count Payment Methods')
plt.savefig('payment_methods_count.png', dpi=300, bbox_inches='tight')  
plt.show()
#This shows which payment methods are used to make the payment when people visit and buy the products.
#As the plot shows that EWallet is the most used payment method compared to Cash and Credit card.
#It shows People prefers to  make payment using EWallet.

#5.Total vs Product line
Product_Total = Market.groupby('Product line')['Total'].sum()
sns.barplot(x=Product_Total.index,y=Product_Total.values)
plt.xlabel('Product')
plt.ylabel('Total')
plt.title('Product vs Total Amount')
plt.savefig('product_total_amount.png', dpi=300, bbox_inches='tight')
plt.xticks(rotation=45)
plt.show()
#This plot shows that which product has achieved the highest Total revenue.
#The plot shows that Health and Beauty products generates highest revenue.
#Since Health and beauty has hihgest revenue, the Super Market may consider expanding the category.

#6.People(Gender wise) spending 
Spending = Market.groupby('Gender')['Total'].sum()

sns.barplot(x=Spending.index,y=Spending.values)
plt.xlabel('Gender')
plt.ylabel('Total')
plt.title('Gender vs Total Amount')
plt.savefig('gender_total_amount.png', dpi=300, bbox_inches='tight')    
plt.show()
#This plot is to show which Gender(Male/Female) has spent more on products.
#This plot shows that both male and female contribute almost equally to the revenue in the Super Market.

#7.Relation b/w quantity and total
sns.scatterplot(x=Market['Quantity'],y=Market['Total'])
plt.xlabel('Quantity')      
plt.ylabel('Total Amount')
plt.title('Quantity vs Total Amount')
plt.savefig('quantity_total_amount.png', dpi=300, bbox_inches='tight')
plt.show()
#This plot is to know the relation b/w quantity and total.
#The plot show Quantity is directly proportional to Total which mean Total increases proportionally as quantity increases. 

#8.Daily trends 
Trends = Market.groupby('Date')['Total'].sum()
sns.lineplot(x=Trends.index,y=Trends.values)
plt.xlabel('Date')
plt.ylabel('Total Amount')     
plt.title('Daily Trends of Total Amount')
plt.xticks(rotation=45)
plt.savefig('daily_trends_total_amount.png', dpi=300, bbox_inches='tight')
plt.show() 
#This plot shows the daily trends of total revenue in the Super Market.
#Some days show higher revenues, while others dip, indicating daily fluctuations.

#9.Trends over hours
Trend_Hours = Market.groupby('Time')['Total'].sum()

sns.lineplot(x=Trend_Hours.index,y=Trend_Hours.values)
plt.xlabel('Time')
plt.ylabel('Total')
plt.title('Trend over time')
plt.savefig('trend_over_time_total_amount.png', dpi=300, bbox_inches='tight')
plt.show() 
#This plot shows the time trends of total revenue in the Super Market.
#Revenue peaks at 10 AM, stays stable during 17–19, and drops after 20.

#10.Correlation
Num = Market.select_dtypes(include = 'number')

sns.heatmap(Num.corr(),annot=True)
plt.title('Correlation')
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()
#This plot is to know the relationship b/w the different columns.
#Total and the gross income has the good relation in the Super Market.
#Quantity and Total has strong relation.
#Where as total and time has no realtion.
------------------------------------------------------------------------------------------------------------------------------------------------
#Final Overall Conclusion
-----------------------------------------------------------------------------------------------------------------------------------------------
#Sales peak during afternoon hours, with Food & Beverages generating the highest revenue. 
# Customer activity is strongest in Yangon, and most payments are made digitally. 
# Ratings indicate overall good customer satisfaction, though some categories show inconsistent experiences and may need quality improvement.
