import sys


allowed_aggregate_data = {'min', 'max', 'avg'}

operations = {
    'avg': lambda x: sum(x) / len(x),
    'min': lambda x: min(x),
    'max': lambda x: max(x),
}


def aggregate(data: dict, aggregate_data: tuple[str, str, str]) -> dict[str, float] | None:

    if not aggregate_data:
        return None
    
    field, _, agg = aggregate_data

    if agg not in allowed_aggregate_data:
        print('--aggregate допустимые значения: min, max, avg')
        sys.exit()

    values = []
    for row in data:
        try:
            value = float(row[field])
            values.append(value)
        except ValueError:
            continue

    if not values:
        return None

    result = operations[agg](values)
    return {agg: result}
