import sys


def parse_string(string: str) -> tuple[str, str, str]:
    operators: list[str] = ['>', '<', '=']
    for op in operators:
        if op in string:
            column, value = string.split(op)
            return column.strip(), op, value.strip()
    print(f'Неверный формат: {string}')
    sys.exit()