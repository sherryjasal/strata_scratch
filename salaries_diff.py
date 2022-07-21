## Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. 
## Output just the absolute difference in salaries.


# Import your libraries
import pandas as pd

# Start writing code
## db_employee.head()
df = pd.merge(db_employee, db_dept, left_on='department_id', right_on='id', how='left')
df_1 = df[df["department"]=='marketing']
df_mar = df_1.groupby(['department'], as_index=False).agg({'salary': 'max'}).rename(columns = {'salary': 'mar_salary'})
df2 = df[df["department"]=='engineering']
df_eng = df2.groupby(['department'], as_index= False).agg({'salary': 'max'}).rename(columns={'salary':'eng_salary'})
df_diff = abs(pd.DataFrame(df_mar['mar_salary'] - df_eng['eng_salary']))
df_diff.columns = ['salary_diff']
df_diff

## link: https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=2

## lessons_learnt : 
## JOIN the department table with employee table to get a list of employees, salaries, and department
## GROUP BY max salary by department in two different data frames
## Extract difference of highest salaries between two departments in a different data frame
