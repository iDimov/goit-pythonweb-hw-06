#!/usr/bin/env python
"""
Приклади використання всіх запитів з my_select.py
"""

from my_select import *


def print_separator(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def test_all_queries():
    # Query 1: Top 5 students
    print_separator("1. Топ 5 студентів з найвищим середнім балом")
    for student in select_1():
        print(f"   ID: {student.id}, Ім'я: {student.name}, Середній бал: {student.avg_grade}")
    
    # Query 2: Best student in subject 1
    print_separator("2. Найкращий студент з предмету #1")
    result = select_2(1)
    if result:
        print(f"   ID: {result.id}, Ім'я: {result.name}, Середній бал: {result.avg_grade}")
    
    # Query 3: Average grade by groups for subject 1
    print_separator("3. Середній бал по групах для предмету #1")
    for group in select_3(1):
        print(f"   Група: {group.name}, Середній бал: {group.avg_grade}")
    
    # Query 4: Overall average grade
    print_separator("4. Загальний середній бал")
    avg = select_4()
    print(f"   Середній бал: {avg}")
    
    # Query 5: Courses by teacher 1
    print_separator("5. Курси викладача #1")
    for subject in select_5(1):
        print(f"   Предмет: {subject.name}")
    
    # Query 6: Students in group 1
    print_separator("6. Студенти в групі #1")
    for student in select_6(1):
        print(f"   ID: {student.id}, Ім'я: {student.name}")
    
    # Query 7: Grades in group 1 for subject 1 (first 5)
    print_separator("7. Оцінки студентів групи #1 з предмету #1 (перші 5)")
    for i, grade in enumerate(select_7(1, 1)):
        if i >= 5:
            break
        print(f"   Студент: {grade.name}, Оцінка: {grade.grade}, Дата: {grade.date.strftime('%Y-%m-%d')}")
    
    # Query 8: Average grade by teacher 1
    print_separator("8. Середній бал викладача #1")
    avg = select_8(1)
    print(f"   Середній бал: {avg}")
    
    # Query 9: Courses for student 1
    print_separator("9. Курси студента #1")
    for subject in select_9(1):
        print(f"   Предмет: {subject.name}")
    
    # Query 10: Courses for student 1 from teacher 1
    print_separator("10. Курси студента #1 у викладача #1")
    for subject in select_10(1, 1):
        print(f"   Предмет: {subject.name}")
    
    # Query 11: Average grade from teacher 1 to student 1
    print_separator("11. БОНУС: Середній бал від викладача #1 студенту #1")
    avg = select_11(1, 1)
    if avg:
        print(f"   Середній бал: {avg}")
    else:
        print("   Немає даних")
    
    # Query 12: Last lesson grades in group 1 for subject 1
    print_separator("12. БОНУС: Оцінки на останньому занятті (група #1, предмет #1)")
    for grade in select_12(1, 1):
        print(f"   Студент: {grade.name}, Оцінка: {grade.grade}, Дата: {grade.date.strftime('%Y-%m-%d')}")
    
    print("\n" + "=" * 60)
    print("  Всі запити виконані успішно!")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    test_all_queries()
