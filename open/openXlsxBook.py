"""
Open an Excel file, reads an speciic sheet and writes its info on a new xlsx file
"""
import pandas as pd
save_path = "C:/Users/I746992/Desktop/Remove_Columns_Python/"
# TEST
#file = "C:/Users/I746992/OneDrive - SAP SE/General - Data Intelligence LAC/LOB-PE_ID-PE_name.xlsx"
#file = "C:/Users/I746992/OneDrive - SAP SE/General - Data Intelligence LAC/1. Mexico/2. Target List/3. Target Lists - Reports/MasterFile- MX.xlsx"
# booksheet_name = "Sheet1"
# MASTER FILE
booksheet_name = "EFECTIVAS"
file = "C:/Users/I746992/Desktop/MasterFile- MX.xlsx"
df = pd.read_excel(file, sheet_name=booksheet_name) 
#df.to_pickle(save_path + "dummyEfectivas.pkl", compression='zip')
# puts selected sheet into new excel book
df.to_excel(save_path + "lob_test.xlsx", index = False)
