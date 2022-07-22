## Find order details made by Jill and Eva.
## Consider the Jill and Eva as first names of customers.
## Output the order date, details and cost along with the first name.
## Order records based on the customer id in ascending order.


# Import your libraries
import pandas as pd

# Start writing code
customers.head()
df = pd.merge(customers, orders, left_on='id', right_on='cust_id', how='left')
df1 = df[df['first_name'].isin(['Jill', 'Eva'])]
df_final = df1.sort_values(by='cust_id', ascending=True)[['first_name', 'order_date', 'order_details', 'total_order_cost']]


## Link: https://platform.stratascratch.com/coding/9913-order-details?code_type=2
## Approach:
## Perform inner join on orders and customers using pd.merge(dataframe1, dataframe2, on = common_table_keys) or left join
## Define or create a list containing the customer first_name to select
## Use .isin(customer_name) to filter rows if it is in the defined list. 
## Use [ [ column_name/s] ] to return a specified column of the dataframes

## lessons learnt: .isin for filtering rows
