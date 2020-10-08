import csv


def problem3_7(csv_pricefile, flower):
    with open(csv_pricefile, 'r') as f:
        for data in csv.reader(f):
            if data[0] == flower:
                print(data[1])


# problem3_7('flowers.csv', 'alyssum')
