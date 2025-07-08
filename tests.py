import pytest
from parse_string import parse_string
from read_csv import read_csv_file
from aggregate import aggregate
from filter import filter_data


@pytest.fixture
def file_path() -> str:
    with open('test.csv', 'w', encoding='utf-8'):
        ...
    return 'test.csv'


@pytest.fixture
def data() -> list[dict]:
    return [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
        {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'},
    ]


def test_filter_success(data: list[dict]):
    s = 'brand=xiaomi'
    res = filter_data(data=data, filter=s)
    assert len(res) == 2



def test_filter_fail(data: list[dict]):
    #столбец которого нет - year
    with pytest.raises(SystemExit):
        s = 'year=xiaomi'
        filter_data(data=data, filter=s)


def test_aggregate_success(data: list[dict]):
    s = parse_string(string='price=max')
    res = aggregate(data=data, aggregate_data=s)
    assert res['max'] == float(1199)

def test_aggregate_fail(data: list[dict]):
    #нет агрегации sum, только (min, max, avg)
    with pytest.raises(SystemExit):
        s = parse_string(string='price=sum')
        aggregate(data=data, aggregate_data=s)


def test_filter_aggregate(data: list[dict]):
    avg_price = parse_string(string='price=avg')
    filtered_res = filter_data(data=data, filter='brand=xiaomi')
    aggregated_res = aggregate(data=filtered_res, aggregate_data=avg_price)
    assert aggregated_res['avg'] == float(249)
    

def test_aggregate_non_num_field(data: list[dict]):
    s = parse_string('brand=max')
    res = aggregate(data, s)
    assert not res



def test_read_csv_file_success(file_path: str):
    read_csv_file(file_path=file_path)


def test_read_csv_file_fail():

    with pytest.raises(SystemExit):
        read_csv_file(file_path='test.txt')


def test_filter_empty_result(data: list[dict]):
    res = filter_data(data=data, filter='brand=nokia')
    assert len(res) == 0


def test_parse_string_success():

    s = 'price>500'

    res = parse_string(string=s)

    assert res[0] == 'price'
    assert res[1] == '>'
    assert res[2] == '500'



def test_parse_string_fail():

    with pytest.raises(SystemExit):
        s = 'price500'
        parse_string(string=s)