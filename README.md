# CSV Tool

Инструмент для работы с CSV: фильтрация, агрегация и вывод в табличном виде.

---

### Клонирование репозитория

Клонируем репозиторий и переходим в папку проекта:

```bash
git clone https://github.com/xaslx/csv-tool.git
cd csv-tool
```

### Создание виртуального окружения и установка библиотек
```
python3 -m venv venv
source venv/bin/activate
pip install -r req.txt
```

### Доступные команды
```
python main.py --help - Посмотреть список доступных аргументов
python main.py --file products.csv - Получить всю таблицу из CSV файла
python main.py --file products.csv --where 'price>100' - Применить фильтр (например, цена больше 100)
python main.py --file products.csv --aggregate 'price=max' - Применить агрегацию (например, максимальная цена)
python main.py --file products.csv --where 'brand=apple' --aggregate 'price=avg' - Комбинированный запуск с фильтром и агрегацией
```

### Запуск тестов

```
pytest tests.py
```
