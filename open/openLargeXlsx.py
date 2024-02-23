"""
Open an Excel file, reads an speciic sheet and writes its info on a new xlsx file
"""
import pandas as pd
import traceback
import pickle

save_path = "C:/Users/I746992/Desktop/Remove_Columns_Python/"
# read sheet of an excel file
file = "C:/Users/I746992/Desktop/MasterFile- MX.xlsx"

try:
    f = open(file, 'r')  
    df = pd.read_excel(file, sheet_name="EFECTIVAS")
except Exception as error:
    print(error)
    traceback.print_exc()
#df.to_pickle(save_path + "dummyEfectivas.pkl", compression='zip') 
#file_bytestream = bytes()
pickle.dump(df, f)
