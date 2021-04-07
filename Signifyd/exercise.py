# Created by Nick Rodriquez 4/6/21
# Coding exercise to clean sample data for ingest into Signifyd solution

# Load the Pandas libraries with alias pd and the OS library
import pandas as pd
import os

#Defining the present working directory if needed
pwd = os.getcwd()

# Define a variable for the Excel spreadsheet
excel_workbook = 'signifyd.xlsx'
# Read the raw data from the file signifyd.xlsx on the 'Raw' sheet and create a dataframe
df_with_null = pd.read_excel(excel_workbook, sheet_name='Raw')

#Remove the null value from all columns on df_with_null and create the df variable
df = df_with_null.fillna(" ")

# Concatenate the First and Last Name columns into Full_Name
full_name_list = []
full_name = df['First Name'] + " " + df['Last Name']
full_name_list.append(full_name)

#Creating blank lists to be filled by FOR loop below
street_address_list = []
city_list = []
state_zip_list = []
postal_code_list = []

# Defining variable for the delivery address from the column of the same name
delivery_address = df['Delivery Address']

#For loop to split the delivery address field into multiple columns and remove the "State"
for address in delivery_address:
    street_address, city, state = address.split(',', 3)
    street_address_list.append(street_address)
    city_list.append(city)
    state_zip_list.append(state)

# Zip code split

for item in df_with_null['Delivery Address']:
    zipcode = item.split()[-1]
    postal_code_list.append(zipcode)

# Delete function to remove columns not needed anymore
del df['First Name']
del df['Last Name']
del df['Delivery Address']

#Insert functions to append new columns of data
df.insert(0, "Full Name", full_name)
df.insert(3, "Street Adress", street_address_list)
df.insert(4, "City", city_list)
df.insert(5, "Postal Code", postal_code_list)

print(df)