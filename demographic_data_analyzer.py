#Demographic Data Analyzer(FreeCodeCamp 2nd Project)
#26th of December, 2023

#Import the necessary libraries; Pandas and SQLAlchemy(To connect to the database server where the dataset is hosted)
import pandas as pd
from sqlalchemy import create_engine

# Database Credentials
user = 'root'
password = 'root'
host = '127.0.0.1'
port = 3306
database = 'demographic'

#Function to create the connector
def get_connection():
	return create_engine(
		url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database),
		pool_recycle=3600,
		echo=True
	)
 
try:
	#Get the connection (Object) for the database.
	engine = get_connection()
	print(f"Connection to the {host} for user {user} created successfully.")
except Exception as ex:
	print("Connection could not be made due to the following error: \n", ex)

#SQL cursor used to read the table into a dataframe.
engine = get_connection()
with engine.connect() as conn:
	df = pd.read_sql_table('adults',conn)

#Each race are represented in this dataset.
df['race'].value_counts()

#average age of men
men_df = df.loc[df['sex'].str.contains('Male'), ['age']]
average_age_men = round((men_df.mean()).sum(), 2)
print("The average of age of men in the dataset is",average_age_men,".")

#Percentage of Bachelors Degree Holders
bachelors_degree_df = df[df['education'].str.contains('Bachelors')]
bachelors_percentage = round((((bachelors_degree_df['education'].value_counts()).sum() / (df['education'].value_counts()).sum()) * 100), 1)
print("The percentage of Bachelors Degree Holders is",bachelors_percentage,"%.")

#Percentage of people with advanced education and makes more than 50K
more_than_50_df = df.loc[df['salary'].str.contains('>50K')]
with_advanced_education_df = more_than_50_df.query("education_num >= 13")
percent_with_adavanced_education = round((((with_advanced_education_df['education'].value_counts()).sum() / (df['education'].value_counts()).sum()) * 100), 1)
print("The percentage of people with advanced education and makes more than 50K is",percent_with_adavanced_education, "%.")

#Percentage of people without advanced education and makes more than 50K
without_advanced_education_df = more_than_50_df.query("education_num < 13")
percent_without_advanced_education = round((((without_advanced_education_df['education'].value_counts()).sum() / (df['education'].value_counts()).sum()) * 100), 1)
print("The percentage of people without advanced education and makes more than 50K is",percent_without_advanced_education,"%." )

#Minimum hours of work per week
minimum_hours = df['hours_per_week'].min()
print("Minimum number of hours of work in the dataset per week:",minimum_hours)

#Percentage of the people who work the minimum number of hours per week have a salary of more than 50K
people_with_minimum_hours = df[df['hours_per_week'] == minimum_hours]
scenario = people_with_minimum_hours.loc[people_with_minimum_hours['salary'].str.contains('>50K')]
percent_of_scenario = round(((scenario['salary'].value_counts()).sum() / (df.loc[df['salary'].str.contains('>50K'), ['id']].value_counts()).sum()) * 100, 1)
print("The percentage of the people who work the minimum number of hours per week have a salary of more than 50K is",percent_of_scenario,"%.")

#Country that has the highest percentage of people that earn >50K and the percentage.
country_in_scenario = more_than_50_df['native_country'].max()
print("Country with the highest percentage of people that earn greater than 50K is",country_in_scenario,".")
country_people_percent = round((((more_than_50_df[more_than_50_df['native_country'].str.contains(country_in_scenario)].value_counts()).sum()) / ((df['native_country'].value_counts()).sum())) * 100, 1)
print("The percentage of the people in this category is",country_people_percent,"%.")

#Most popular occupation for those who earn >50K in India.
country_df = more_than_50_df.loc[more_than_50_df['native_country'].str.contains('India'),['native_country', 'occupation']]
print(country_df['occupation'].value_counts())
print("\nThere is no popular occupation in India that who gives more than 50K.")
