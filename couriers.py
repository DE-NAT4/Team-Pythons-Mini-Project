import csv

# FUNCTION TO EXTRACT COURIER DATA FROM CSV
def load_couriers():
    result = []
    with open ('couriers.csv', mode='r', newline='') as data:
        reader = csv.reader(data)
        next(reader, None) #skips header
        for row in reader:
            result.append(row[0])
    return result
