#!/usr/bin/env python
"""
Демонстрація роботи проекту
"""

import sys
from config import SessionLocal
from models import Teacher, Group, Student, Subject
from my_select import select_1, select_4, select_5, select_6


def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def demo():
    print_header("📊 ДЕМОНСТРАЦІЯ РОБОТИ БАЗИ ДАНИХ СТУДЕНТІВ")
    
    session = SessionLocal()
    
    try:
        # Показати статистику
        print_header("📈 Загальна статистика")
        
        teachers_count = session.query(Teacher).count()
        groups_count = session.query(Group).count()
        students_count = session.query(Student).count()
        subjects_count = session.query(Subject).count()
        
        print(f"👨‍🏫 Викладачів: {teachers_count}")
        print(f"👥 Груп: {groups_count}")
        print(f"👨‍🎓 Студентів: {students_count}")
        print(f"📚 Предметів: {subjects_count}")
        
        # Топ студентів
        print_header("🏆 ТОП 5 СТУДЕНТІВ")
        for i, student in enumerate(select_1(), 1):
            print(f"{i}. {student.name}: {student.avg_grade}")
        
        # Середній бал
        print_header("📊 ЗАГАЛЬНИЙ СЕРЕДНІЙ БАЛ")
        avg = select_4()
        print(f"Середній бал по всіх предметах: {avg}")
        
        # Викладачі та їх предмети
        print_header("👨‍🏫 ВИКЛАДАЧІ ТА ЇХ ПРЕДМЕТИ")
        teachers = session.query(Teacher).limit(3).all()
        for teacher in teachers:
            subjects = select_5(teacher.id)
            print(f"\n{teacher.name}:")
            for subj in subjects:
                print(f"  - {subj.name}")
        
        # Групи та студенти
        print_header("👥 ГРУПИ ТА КІЛЬКІСТЬ СТУДЕНТІВ")
        groups = session.query(Group).all()
        for group in groups:
            students = select_6(group.id)
            print(f"{group.name}: {len(students)} студентів")
        
        print_header("✅ ДЕМОНСТРАЦІЯ ЗАВЕРШЕНА")
        print("\nДля детальнішої інформації використовуйте:")
        print("  ./run.sh test       - протестувати всі запити")
        print("  ./run.sh cli -a list -m Teacher  - переглянути викладачів")
        print("  python test_queries.py           - повний тест всіх запитів\n")
        
    except Exception as e:
        print(f"\n❌ Помилка: {e}")
        sys.exit(1)
    finally:
        session.close()


if __name__ == '__main__':
    demo()
