import os
import pandas as pd
import json
import csv


def readCSVFiles():
    master_df = pd.DataFrame()
    for file in os.listdir(os.getcwd()):
        if file.endswith('.csv'):
            master_df = master_df.append(pd.read_csv(file))
    # Convert to one csv file
    if os.path.isfile('master_file.csv'):
        if os.stat('master_file.csv').st_size == 0:
            master_df.to_csv('master_file.csv', index=False)
        else:
            print('files has been already scanned')
    else:
        print('files has been scanned!')
        # dont write rows name index=False
        master_df.to_csv('master_file.csv', index=False)


def convertToJson():
    with open("master_file.csv", "r") as f:
        reader = csv.reader(f)
        title = next(reader)
        index1 = title.index('first_name')
        index2 = title.index('last_name')
        index3 = title.index('employee_id')
        index4 = title.index('date_of_birth')

        data = {"employees": []}
        for row in reader:
            data["employees"].append({"first_name":
                                      row[index1], "last_name": row[index2], "employee_id": row[index3], "date_of_birth": row[index4]})

    with open("employees.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    readCSVFiles()
    convertToJson()
    os.system('python3 server.py')
