# Робота з локальним віртуальним середовищем

## Створено автоматично

Віртуальне середовище `.venv` вже налаштоване та активоване для цього проекту.

## Основні команди

### Активація віртуального середовища (якщо потрібно)

```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Деактивація

```bash
deactivate
```

### Запуск Python скриптів

Використовуйте wrapper скрипт `run.sh` для зручності:

```bash
./run.sh seed       # Заповнити БД
./run.sh test       # Протестувати всі запити
./run.sh cli -a list -m Teacher  # CLI команди
```

Або напряму через Python з віртуального середовища:

```bash
.venv/bin/python seed.py
.venv/bin/python test_queries.py
.venv/bin/python main.py -a list -m Teacher
```

## Встановлені пакети

- SQLAlchemy==2.0.23
- alembic==1.13.0
- psycopg2-binary==2.9.9
- faker==20.1.0

## Перевірка встановлених пакетів

```bash
.venv/bin/pip list
```

## Оновлення пакетів

```bash
.venv/bin/pip install --upgrade <package-name>
```

## Видалення віртуального середовища

```bash
rm -rf .venv
```

Після видалення створіть нове:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
