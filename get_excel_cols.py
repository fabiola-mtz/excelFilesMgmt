"""
Open an Excel file, reads an speciic sheet and writes its info on a new xlsx file
"""
import pandas as pd
save_path = "C:/Users/I746992/Desktop/Remove_Columns_Python/"
booksheet_name = "MX-DBoutreach-17042024"
file = "C:/Users/I746992/OneDrive - SAP SE/General - Data Intelligence LAC/1. Mexico/2024/Outreach/CII from Outreach/Prospects_2024-04-15_17263_CII.csv"

df = pd.read_csv(file, usecols=['Custom Field 32','Company','Title','Persona Name','Website'])
df.to_excel(save_path + "CII 19.04.2024.xlsx", index = False)
