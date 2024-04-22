"""
Open an Excel file, reads an speciic sheet and writes its info on a new xlsx file
"""
import pandas as pd
from datetime import date

today = date.today()
save_path = "C:/Users/I746992/Desktop/Remove_Columns_Python/DataDriven files/"
sheet_name_list = {"IB"}
file = "C:/Users/I746992/OneDrive - SAP SE/2024/DataDriven/Descargas/dataDriven-abril.xlsx"

df = pd.read_excel(file)
for sheet in sheet_name_list:
    df.to_excel(save_path + "DD-" + sheet + "-" + today.strftime("%d.%m.%Y") + ".xlsx", sheet_name=sheet, index = False)

