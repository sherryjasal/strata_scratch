## Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.



# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()
airbnb_search_details.groupby(['city','property_type'], as_index=False)['bedrooms','bathrooms'].mean().rename({'bedrooms':'avg_bedrooms','bathrooms':'avg_bathrooms'})

## link : https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?code_type=2
## Approach:
## Use .groupby(column1, column2) to group the dataframe about the specifed columns then use [column1, column2].mean() function to get the mean of values of each column

## lessons learnt
## instead agg ::  groupby O/U columns with two columns(you want to calculate sum, mean, min or max) use list [].mean()(or whatever is the required field) and then rename
