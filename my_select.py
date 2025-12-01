from sqlalchemy import func, desc, and_, cast, Numeric
from models import Student, Teacher, Subject, Grade, Group
from config import SessionLocal


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    Find 5 students with the highest average grade across all subjects.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.id,
                Student.name,
                func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
            )
            .join(Grade)
            .group_by(Student.id)
            .order_by(desc('avg_grade'))
            .limit(5)
            .all()
        )
        return result
    finally:
        session.close()


def select_2(subject_id):
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    Find the student with the highest average grade in a specific subject.
    
    :param subject_id: ID of the subject
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.id,
                Student.name,
                func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
            )
            .join(Grade)
            .filter(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(desc('avg_grade'))
            .limit(1)
            .first()
        )
        return result
    finally:
        session.close()


def select_3(subject_id):
    """
    Знайти середній бал у групах з певного предмета.
    Find the average grade in groups for a specific subject.
    
    :param subject_id: ID of the subject
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Group.name,
                func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
            )
            .select_from(Group)
            .join(Student)
            .join(Grade)
            .filter(Grade.subject_id == subject_id)
            .group_by(Group.id)
            .all()
        )
        return result
    finally:
        session.close()


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    Find the average grade across all grades.
    """
    session = SessionLocal()
    try:
        result = session.query(
            func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
        ).scalar()
        return result
    finally:
        session.close()


def select_5(teacher_id):
    """
    Знайти які курси читає певний викладач.
    Find which courses a specific teacher teaches.
    
    :param teacher_id: ID of the teacher
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.name)
            .filter(Subject.teacher_id == teacher_id)
            .all()
        )
        return result
    finally:
        session.close()


def select_6(group_id):
    """
    Знайти список студентів у певній групі.
    Find the list of students in a specific group.
    
    :param group_id: ID of the group
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Student.id, Student.name)
            .filter(Student.group_id == group_id)
            .all()
        )
        return result
    finally:
        session.close()


def select_7(group_id, subject_id):
    """
    Знайти оцінки студентів у окремій групі з певного предмета.
    Find grades of students in a specific group for a specific subject.
    
    :param group_id: ID of the group
    :param subject_id: ID of the subject
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.name,
                Grade.grade,
                Grade.date
            )
            .join(Grade)
            .filter(and_(Student.group_id == group_id, Grade.subject_id == subject_id))
            .order_by(Student.name, Grade.date)
            .all()
        )
        return result
    finally:
        session.close()


def select_8(teacher_id):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    Find the average grade given by a specific teacher across their subjects.
    
    :param teacher_id: ID of the teacher
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
            )
            .join(Subject)
            .filter(Subject.teacher_id == teacher_id)
            .scalar()
        )
        return result
    finally:
        session.close()


def select_9(student_id):
    """
    Знайти список курсів, які відвідує певний студент.
    Find the list of courses attended by a specific student.
    
    :param student_id: ID of the student
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.name)
            .join(Grade)
            .filter(Grade.student_id == student_id)
            .distinct()
            .all()
        )
        return result
    finally:
        session.close()


def select_10(student_id, teacher_id):
    """
    Список курсів, які певному студенту читає певний викладач.
    List of courses that a specific teacher teaches to a specific student.
    
    :param student_id: ID of the student
    :param teacher_id: ID of the teacher
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.name)
            .join(Grade)
            .filter(and_(
                Grade.student_id == student_id,
                Subject.teacher_id == teacher_id
            ))
            .distinct()
            .all()
        )
        return result
    finally:
        session.close()


# Additional queries (bonus)
def select_11(teacher_id, student_id):
    """
    Середній бал, який певний викладач ставить певному студентові.
    Average grade that a specific teacher gives to a specific student.
    
    :param teacher_id: ID of the teacher
    :param student_id: ID of the student
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
            )
            .join(Subject)
            .filter(and_(
                Subject.teacher_id == teacher_id,
                Grade.student_id == student_id
            ))
            .scalar()
        )
        return result
    finally:
        session.close()


def select_12(group_id, subject_id):
    """
    Оцінки студентів у певній групі з певного предмета на останньому занятті.
    Grades of students in a specific group for a specific subject on the last lesson.
    
    :param group_id: ID of the group
    :param subject_id: ID of the subject
    """
    session = SessionLocal()
    try:
        # Find the date of the last lesson
        last_date_subquery = (
            session.query(func.max(Grade.date))
            .join(Student)
            .filter(and_(
                Student.group_id == group_id,
                Grade.subject_id == subject_id
            ))
            .scalar_subquery()
        )
        
        # Get grades from the last lesson
        result = (
            session.query(
                Student.name,
                Grade.grade,
                Grade.date
            )
            .join(Grade)
            .filter(and_(
                Student.group_id == group_id,
                Grade.subject_id == subject_id,
                Grade.date == last_date_subquery
            ))
            .all()
        )
        return result
    finally:
        session.close()


if __name__ == '__main__':
    # Example usage
    print("1. Top 5 students by average grade:")
    for student in select_1():
        print(f"   {student.name}: {student.avg_grade}")
    
    print("\n4. Average grade across all students:")
    print(f"   {select_4()}")
