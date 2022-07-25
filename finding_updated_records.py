## We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. 
## Find the current salary of each employee assuming that salaries increase each year.
## Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.


# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary.head()
df = ms_employee_salary.groupby(['id','first_name','last_name','department_id'],as_index=False).agg({'salary':'max'})[['id','first_name','last_name','department_id','salary']]


## link: https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=2
## Approach: 
## Until now at every compensation revision cycle, all employees have received a salary increase so you can assume that the highest salary is the employee's current salary. Use a max() function to find the highest salary for each employee.
## The output should be all the details of all the employees with correct salary
## lessons_learnt:
## groupby all columns and max of salries
