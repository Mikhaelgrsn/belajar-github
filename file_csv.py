import csv

def read_csv(csv_file):
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


csv_file_path = 'username.csv'
csv_data = read_csv(csv_file_path)
print(csv_data)