import pandas as pd
from stdnum.py import ruc

def main():
    # read an excel file            
    excel = pd.read_excel('file.xlsx')
    columns = excel.columns.to_list()
    columns.append('VALIDO')
    dataFrame = []

    # iterate each row
    for row in excel.iterrows():
        element = row[1].to_dict()
        array = row[1].to_list()

        # validate RUC format
        if ruc.is_valid(element['RUC']):
            array.append(1)
        else:
            array.append(0)

        dataFrame.append(array)

    # create a new file with the updated data
    df = pd.DataFrame(dataFrame, columns=columns)
    with pd.ExcelWriter("output/output.xlsx") as writer:
        df.to_excel(writer, sheet_name="Sheet1")  

main()