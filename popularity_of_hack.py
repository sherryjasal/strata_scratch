## Meta/Facebook has developed a new programing language called Hack.
## To measure the popularity of Hack they ran a survey with their employees. 
## The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. 
## Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. 
## Luckily the user IDs of employees completing the surveys were stored.
## Based on the above, find the average popularity of the Hack per office location.
## Output the location along with the average popularity.



# Import your libraries
import pandas as pd

# Start writing code
facebook_employees.head()
df = pd.merge(facebook_employees, facebook_hack_survey, left_on='id', right_on='employee_id',how='left')
df1 = df.groupby('location', as_index=False).agg({'popularity':'mean'}).rename(columns={'popularity':'avg_popularity'})

## link: https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=2
## approach
## Perform an inner merge on dataframe using pd.merge(df1,df2, left_on = common_key_left_df, right_on = common_key_right_table, how = 'inner')
## Use .groupby(column_name) to group the dataframe about the specifed column and use mean() to get the average value per group
