"""
Open an Excel file, reads an speciic sheet and writes its info on a new xlsx file
"""
import pandas as pd
save_path = "C:/Users/I746992/Desktop/Remove_Columns_Python/"
booksheet_name = "MX-DBoutreach-17042024"
file = "C:/Users/I746992/OneDrive - SAP SE/2024/Outreach/MX-DBoutreach-17042024.csv"

df = pd.read_csv(file, usecols=['Custom Field 32', 'Company','Title', 'Persona Name', 'Account ID','Website'])
df.to_excel(save_path + "OUT 17.04.2024.xlsx", index = False)
