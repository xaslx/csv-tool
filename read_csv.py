import csv
import sys


def read_csv_file(file_path: str):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f'Файл: {file_path} не найден')
        sys.exit()
