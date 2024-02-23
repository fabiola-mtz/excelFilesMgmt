"""
Open an Excel file, reads an speciic sheet and writes its info on a new xlsx file
"""
import pandas as pd
# TEST
save_path = "C:/Users/I746992/Desktop/Remove_Columns_Python/"
# booksheet_name = "Sheet1"
# MASTER FILE
#save_path = "C:/Users/I746992/Desktop/MasterFile- MX.xlsx"
booksheet_name = "BASE"
# read sheet of an excel file
# TEST
#file = "C:/Users/I746992/OneDrive - SAP SE/General - Data Intelligence LAC/LOB-PE_ID-PE_name.xlsx"
#file = "C:/Users/I746992/OneDrive - SAP SE/General - Data Intelligence LAC/1. Mexico/2. Target List/3. Target Lists - Reports/MasterFile- MX.xlsx"
# MASTER FILE
file = "C:/Users/I746992/Desktop/MasterFile- MX.xlsx"
df = pd.read_excel(file, sheet_name='EFECTIVAS') 
print(list(df.keys()))
#df.to_pickle(save_path + "dummyEfectivas.pkl", compression='zip')
df.to_excel(save_path + "lob_test.xlsx", index = False)
