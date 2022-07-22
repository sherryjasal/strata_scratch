## Compare each employee's salary with the average salary of the corresponding department.
## Output the department, first name, and salary of employees along with the average salary of that department.



import pandas as pd

# Start writing code
#employee.head()
df = employee.groupby(['department'],as_index=False).agg({'salary':'mean'}).rename(columns={'salary':'avg_salary'})
pd.merge(employee[['department','first_name','salary']], df, on='department', how='left')

## link https://platform.stratascratch.com/coding/9917-average-salaries?code_type=2

## Approach:
## Create a new column that contains the average salary per group by using mean() within the transform() function to recombine the mean values to the grouped values
## Use [ [ column_name/s] ] to return a specified column of the dataframe


## lessons_learnt = [[]] while merging for columns, secondly treat the new counted field as a new table and merge with old one
