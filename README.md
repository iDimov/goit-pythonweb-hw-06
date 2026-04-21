# Домашня робота 6 - База даних студентів

## 📚 Документація

- **[VIRTUALENV.md](VIRTUALENV.md)** - Робота з віртуальним середовищем
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

### 4. Застосуйте міграції Alembic

Схема БД керується виключно Alembic — ніяких `Base.metadata.create_all`.

```bash
# Застосувати існуючі міграції (створить усі таблиці)
alembic upgrade head

# За потреби — згенерувати нову міграцію після змін у models.py
alembic revision --autogenerate -m "Опис змін"
alembic upgrade head
```

### 5. Наповніть базу даних тестовими даними

```bash
python seed.py
```

> `seed.py` сам викликає `alembic upgrade head` перед наповненням,
> тож схема завжди приводиться до актуальної версії через міграції.

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

### CLI (CRUD) — приклади

CRUD підтримано для всіх моделей: `Teacher`, `Group`, `Student`, `Subject`, `Grade`.

```bash
# Teacher / Group
python main.py -a create -m Teacher -n "Boris Jonson"
python main.py -a list   -m Teacher
python main.py -a update -m Teacher --id 3 -n "Andry Bezos"
python main.py -a remove -m Teacher --id 3

python main.py -a create -m Group -n "AD-101"

# Student / Subject
python main.py -a create -m Student -n "Ivan Ivanov" --group_id 1
python main.py -a create -m Subject -n "Математика" --teacher_id 2

# Grade
python main.py -a create -m Grade --student_id 1 --subject_id 2 -g 92.5
python main.py -a create -m Grade --student_id 1 --subject_id 2 -g 88 --date "2026-04-21 10:30"
python main.py -a list   -m Grade
python main.py -a update -m Grade --id 5 -g 95
python main.py -a remove -m Grade --id 5
```

## Особливості реалізації

- Використання SQLAlchemy ORM для роботи з базою даних
- Міграції через Alembic для версіонування схеми БД
- Faker для генерації тестових даних українською мовою
- CASCADE видалення для підтримки цілісності даних
- CLI інтерфейс з argparse для зручного управління
- Механізм сесій SQLAlchemy для всіх операцій
