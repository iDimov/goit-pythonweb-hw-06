import random
from datetime import datetime, timedelta
from pathlib import Path

from alembic import command
from alembic.config import Config
from faker import Faker

from config import SessionLocal
from models import Group, Student, Teacher, Subject, Grade

fake = Faker('uk_UA')  # Ukrainian locale

# Number of records to create
NUM_GROUPS = 3
NUM_STUDENTS = random.randint(30, 50)
NUM_TEACHERS = random.randint(3, 5)
NUM_SUBJECTS = random.randint(5, 8)
MAX_GRADES_PER_STUDENT = 20


def create_groups(session):
    """Create groups"""
    groups = []
    group_names = ['КН-101', 'КН-102', 'КН-103']
    
    for name in group_names[:NUM_GROUPS]:
        group = Group(name=name)
        groups.append(group)
    
    session.add_all(groups)
    session.commit()
    print(f"Created {len(groups)} groups")
    return groups


def create_teachers(session):
    """Create teachers"""
    teachers = []
    
    for _ in range(NUM_TEACHERS):
        teacher = Teacher(name=fake.name())
        teachers.append(teacher)
    
    session.add_all(teachers)
    session.commit()
    print(f"Created {len(teachers)} teachers")
    return teachers


def create_subjects(session, teachers):
    """Create subjects"""
    subjects = []
    subject_names = [
        'Вища математика',
        'Фізика',
        'Програмування',
        'Бази даних',
        'Англійська мова',
        'Алгоритми та структури даних',
        'Операційні системи',
        'Комп\'ютерні мережі'
    ]
    
    for i in range(NUM_SUBJECTS):
        subject = Subject(
            name=subject_names[i],
            teacher_id=random.choice(teachers).id
        )
        subjects.append(subject)
    
    session.add_all(subjects)
    session.commit()
    print(f"Created {len(subjects)} subjects")
    return subjects


def create_students(session, groups):
    """Create students"""
    students = []
    
    for _ in range(NUM_STUDENTS):
        student = Student(
            name=fake.name(),
            group_id=random.choice(groups).id
        )
        students.append(student)
    
    session.add_all(students)
    session.commit()
    print(f"Created {len(students)} students")
    return students


def create_grades(session, students, subjects):
    """Create grades for students"""
    grades = []
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    
    for student in students:
        # Each student gets random number of grades (up to MAX_GRADES_PER_STUDENT)
        num_grades = random.randint(12, MAX_GRADES_PER_STUDENT)
        
        for _ in range(num_grades):
            grade = Grade(
                student_id=student.id,
                subject_id=random.choice(subjects).id,
                grade=round(random.uniform(60, 100), 2),
                date=fake.date_time_between(start_date=start_date, end_date=end_date)
            )
            grades.append(grade)
    
    session.add_all(grades)
    session.commit()
    print(f"Created {len(grades)} grades")
    return grades


def run_migrations():
    """Apply Alembic migrations up to head before populating the database."""
    alembic_cfg = Config(str(Path(__file__).resolve().parent / "alembic.ini"))
    command.upgrade(alembic_cfg, "head")
    print("Applied Alembic migrations (upgrade head)")


def seed_database():
    """Main function to seed the database"""
    # Schema is managed exclusively by Alembic — bring it up to date first.
    run_migrations()

    # Create session
    session = SessionLocal()
    
    try:
        # Clear existing data
        session.query(Grade).delete()
        session.query(Student).delete()
        session.query(Subject).delete()
        session.query(Teacher).delete()
        session.query(Group).delete()
        session.commit()
        print("Cleared existing data")
        
        # Create new data
        groups = create_groups(session)
        teachers = create_teachers(session)
        subjects = create_subjects(session, teachers)
        students = create_students(session, groups)
        grades = create_grades(session, students, subjects)
        
        print("\nDatabase seeded successfully!")
        print(f"Total: {len(groups)} groups, {len(teachers)} teachers, "
              f"{len(subjects)} subjects, {len(students)} students, {len(grades)} grades")
        
    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {e}")
        raise
    finally:
        session.close()


if __name__ == '__main__':
    seed_database()
