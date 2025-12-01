# Домашня робота 6 - База даних студентів

## 📚 Документація

- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Повна структура проекту
- **[VIRTUALENV.md](VIRTUALENV.md)** - Робота з віртуальним середовищем
- **[EXAMPLES.md](EXAMPLES.md)** - Приклади всіх команд
- **README.md** (цей файл) - Загальний огляд проекту

## Структура проекту

```
.
├── alembic/                 # Міграції бази даних
│   ├── versions/           # Файли міграцій
│   ├── env.py             # Налаштування середовища Alembic
│   └── script.py.mako     # Шаблон для міграцій
├── alembic.ini             # Конфігурація Alembic
├── config.py               # Конфігурація бази даних та сесій
├── models.py               # SQLAlchemy моделі
├── seed.py                 # Скрипт для наповнення БД тестовими даними
├── my_select.py            # Запити до бази даних
├── main.py                 # CLI інтерфейс для CRUD операцій
├── requirements.txt        # Залежності проекту
└── README.md              # Цей файл
```

## Швидкий старт

Використовуйте скрипт `run.sh` для зручного запуску команд:

```bash
# Швидка демонстрація можливостей
./run.sh demo

# Заповнити базу даних
./run.sh seed

# Запустити запити
./run.sh select

# Протестувати всі запити
./run.sh test

# CLI команди
./run.sh cli -a list -m Teacher
./run.sh cli -a create -m Teacher -n "Boris Johnson"

# Міграції
./run.sh migrate "My migration name"
./run.sh upgrade
```

## Встановлення

### 1. Запустіть PostgreSQL контейнер

```bash
docker run --name postgres-hw6 -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

### 2. Створіть та активуйте віртуальне середовище

```bash
# Створити віртуальне середовище
python3 -m venv .venv

# Активувати (macOS/Linux)
source .venv/bin/activate

# Активувати (Windows)
.venv\Scripts\activate
```

### 3. Встановіть залежності

```bash
pip install -r requirements.txt
```

### 4. Створіть міграції та застосуйте їх

```bash
# Створити міграцію
alembic revision --autogenerate -m "Initial migration"

# Застосувати міграцію
alembic upgrade head
```

### 5. Наповніть базу даних тестовими даними

```bash
python seed.py
```

## Використання

### Запити до бази даних

Файл `my_select.py` містить 12 функцій для різних запитів:

1. `select_1()` - Топ 5 студентів з найвищим середнім балом
2. `select_2(subject_id)` - Студент з найвищим балом з предмету
3. `select_3(subject_id)` - Середній бал по групах з предмету
4. `select_4()` - Середній бал по всій таблиці оцінок
5. `select_5(teacher_id)` - Курси певного викладача
6. `select_6(group_id)` - Список студентів у групі
7. `select_7(group_id, subject_id)` - Оцінки студентів групи з предмету
8. `select_8(teacher_id)` - Середній бал викладача
9. `select_9(student_id)` - Курси студента
10. `select_10(student_id, teacher_id)` - Курси студента у викладача
11. `select_11(teacher_id, student_id)` - Середній бал викладача студенту (бонус)
12. `select_12(group_id, subject_id)` - Оцінки на останньому занятті (бонус)

## Особливості реалізації

- Використання SQLAlchemy ORM для роботи з базою даних
- Міграції через Alembic для версіонування схеми БД
- Faker для генерації тестових даних українською мовою
- CASCADE видалення для підтримки цілісності даних
- CLI інтерфейс з argparse для зручного управління
- Механізм сесій SQLAlchemy для всіх операцій
