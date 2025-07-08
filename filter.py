import sys
from parse_string import parse_string


operations = {
    '=': lambda a, b: a == b,
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
}




def filter_data(data: list[dict], filter: str) -> list:

    if not filter:
        return data

    column, operator, value = parse_string(filter)
    filtered_data = []

    for row in data:


        try:
            row_value = row[column]
        except KeyError:
            print(f'Столбец: {column} не найден')
            sys.exit()


        try:
            row_value_num = float(row_value)
            value_num = float(value)
        except ValueError:
            row_value_num = row_value
            value_num = value

        if operations[operator](row_value_num, value_num):
            filtered_data.append(row)

    return filtered_data