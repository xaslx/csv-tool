import argparse
import sys
from read_csv import read_csv_file
from filter import filter_data
from parse_string import parse_string
from aggregate import aggregate
from tabulate import tabulate





def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Путь до csv файла')
    parser.add_argument('--where', help='Фильтр: пример -> price>100', default=None)
    parser.add_argument('--aggregate', help='Агрегация: пример -> price=avg', default=None)

    args = parser.parse_args()
    data = read_csv_file(args.file)

    if args.where:
        data = filter_data(data=data, filter=args.where)

    if args.aggregate:
        aggr = parse_string(string=args.aggregate)
        result = aggregate(data=data, aggregate_data=aggr)
        if result:
            print(tabulate([result], headers='keys', tablefmt='github'))
        else:
            print('Нет данных для агрегации')
    else:
        if data:
            print(tabulate(data, headers='keys', tablefmt='github'))
        else:
            print('Нет данных, которые соответствуют данному фильтру')


if __name__ == '__main__':
    try:
        main()
    except TypeError:
        print('Введите аргумент --file и название файла, пример: --file products.csv')
        sys.exit()