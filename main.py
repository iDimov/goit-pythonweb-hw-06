import argparse
import sys
from datetime import datetime
from config import SessionLocal
from models import Group, Student, Teacher, Subject, Grade


def create_teacher(name):
    """Create a new teacher"""
    session = SessionLocal()
    try:
        teacher = Teacher(name=name)
        session.add(teacher)
        session.commit()
        print(f"Teacher created: ID={teacher.id}, Name={teacher.name}")
        return teacher
    except Exception as e:
        session.rollback()
        print(f"Error creating teacher: {e}")
    finally:
        session.close()


def create_group(name):
    """Create a new group"""
    session = SessionLocal()
    try:
        group = Group(name=name)
        session.add(group)
        session.commit()
        print(f"Group created: ID={group.id}, Name={group.name}")
        return group
    except Exception as e:
        session.rollback()
        print(f"Error creating group: {e}")
    finally:
        session.close()


def create_student(name, group_id):
    """Create a new student"""
    session = SessionLocal()
    try:
        student = Student(name=name, group_id=group_id)
        session.add(student)
        session.commit()
        print(f"Student created: ID={student.id}, Name={student.name}, Group ID={student.group_id}")
        return student
    except Exception as e:
        session.rollback()
        print(f"Error creating student: {e}")
    finally:
        session.close()


def create_subject(name, teacher_id):
    """Create a new subject"""
    session = SessionLocal()
    try:
        subject = Subject(name=name, teacher_id=teacher_id)
        session.add(subject)
        session.commit()
        print(f"Subject created: ID={subject.id}, Name={subject.name}, Teacher ID={subject.teacher_id}")
        return subject
    except Exception as e:
        session.rollback()
        print(f"Error creating subject: {e}")
    finally:
        session.close()


def list_teachers():
    """List all teachers"""
    session = SessionLocal()
    try:
        teachers = session.query(Teacher).all()
        if teachers:
            print("Teachers:")
            for teacher in teachers:
                print(f"  ID={teacher.id}, Name={teacher.name}")
        else:
            print("No teachers found")
        return teachers
    finally:
        session.close()


def list_groups():
    """List all groups"""
    session = SessionLocal()
    try:
        groups = session.query(Group).all()
        if groups:
            print("Groups:")
            for group in groups:
                print(f"  ID={group.id}, Name={group.name}")
        else:
            print("No groups found")
        return groups
    finally:
        session.close()


def list_students():
    """List all students"""
    session = SessionLocal()
    try:
        students = session.query(Student).all()
        if students:
            print("Students:")
            for student in students:
                print(f"  ID={student.id}, Name={student.name}, Group ID={student.group_id}")
        else:
            print("No students found")
        return students
    finally:
        session.close()


def list_subjects():
    """List all subjects"""
    session = SessionLocal()
    try:
        subjects = session.query(Subject).all()
        if subjects:
            print("Subjects:")
            for subject in subjects:
                print(f"  ID={subject.id}, Name={subject.name}, Teacher ID={subject.teacher_id}")
        else:
            print("No subjects found")
        return subjects
    finally:
        session.close()


def update_teacher(teacher_id, name):
    """Update a teacher"""
    session = SessionLocal()
    try:
        teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
        if teacher:
            teacher.name = name
            session.commit()
            print(f"Teacher updated: ID={teacher.id}, Name={teacher.name}")
        else:
            print(f"Teacher with ID={teacher_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error updating teacher: {e}")
    finally:
        session.close()


def update_group(group_id, name):
    """Update a group"""
    session = SessionLocal()
    try:
        group = session.query(Group).filter(Group.id == group_id).first()
        if group:
            group.name = name
            session.commit()
            print(f"Group updated: ID={group.id}, Name={group.name}")
        else:
            print(f"Group with ID={group_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error updating group: {e}")
    finally:
        session.close()


def update_student(student_id, name=None, group_id=None):
    """Update a student"""
    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student:
            if name:
                student.name = name
            if group_id:
                student.group_id = group_id
            session.commit()
            print(f"Student updated: ID={student.id}, Name={student.name}, Group ID={student.group_id}")
        else:
            print(f"Student with ID={student_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error updating student: {e}")
    finally:
        session.close()


def update_subject(subject_id, name=None, teacher_id=None):
    """Update a subject"""
    session = SessionLocal()
    try:
        subject = session.query(Subject).filter(Subject.id == subject_id).first()
        if subject:
            if name:
                subject.name = name
            if teacher_id:
                subject.teacher_id = teacher_id
            session.commit()
            print(f"Subject updated: ID={subject.id}, Name={subject.name}, Teacher ID={subject.teacher_id}")
        else:
            print(f"Subject with ID={subject_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error updating subject: {e}")
    finally:
        session.close()


def remove_teacher(teacher_id):
    """Remove a teacher"""
    session = SessionLocal()
    try:
        teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
        if teacher:
            session.delete(teacher)
            session.commit()
            print(f"Teacher removed: ID={teacher_id}")
        else:
            print(f"Teacher with ID={teacher_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error removing teacher: {e}")
    finally:
        session.close()


def remove_group(group_id):
    """Remove a group"""
    session = SessionLocal()
    try:
        group = session.query(Group).filter(Group.id == group_id).first()
        if group:
            session.delete(group)
            session.commit()
            print(f"Group removed: ID={group_id}")
        else:
            print(f"Group with ID={group_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error removing group: {e}")
    finally:
        session.close()


def remove_student(student_id):
    """Remove a student"""
    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student:
            session.delete(student)
            session.commit()
            print(f"Student removed: ID={student_id}")
        else:
            print(f"Student with ID={student_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error removing student: {e}")
    finally:
        session.close()


def remove_subject(subject_id):
    """Remove a subject"""
    session = SessionLocal()
    try:
        subject = session.query(Subject).filter(Subject.id == subject_id).first()
        if subject:
            session.delete(subject)
            session.commit()
            print(f"Subject removed: ID={subject_id}")
        else:
            print(f"Subject with ID={subject_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error removing subject: {e}")
    finally:
        session.close()


def _parse_grade_date(value):
    if value is None:
        return None
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    raise ValueError(
        f"Invalid date format: {value!r}. Use 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM[:SS]'"
    )


def create_grade(student_id, subject_id, grade_value, date=None):
    """Create a new grade"""
    session = SessionLocal()
    try:
        grade = Grade(
            student_id=student_id,
            subject_id=subject_id,
            grade=grade_value,
            date=_parse_grade_date(date) or datetime.now(),
        )
        session.add(grade)
        session.commit()
        print(
            f"Grade created: ID={grade.id}, Student ID={grade.student_id}, "
            f"Subject ID={grade.subject_id}, Grade={grade.grade}, Date={grade.date}"
        )
        return grade
    except Exception as e:
        session.rollback()
        print(f"Error creating grade: {e}")
    finally:
        session.close()


def list_grades():
    """List all grades"""
    session = SessionLocal()
    try:
        grades = session.query(Grade).all()
        if grades:
            print("Grades:")
            for grade in grades:
                print(
                    f"  ID={grade.id}, Student ID={grade.student_id}, "
                    f"Subject ID={grade.subject_id}, Grade={grade.grade}, Date={grade.date}"
                )
        else:
            print("No grades found")
        return grades
    finally:
        session.close()


def update_grade(grade_id, student_id=None, subject_id=None, grade_value=None, date=None):
    """Update a grade"""
    session = SessionLocal()
    try:
        grade = session.query(Grade).filter(Grade.id == grade_id).first()
        if grade:
            if student_id is not None:
                grade.student_id = student_id
            if subject_id is not None:
                grade.subject_id = subject_id
            if grade_value is not None:
                grade.grade = grade_value
            if date is not None:
                grade.date = _parse_grade_date(date)
            session.commit()
            print(
                f"Grade updated: ID={grade.id}, Student ID={grade.student_id}, "
                f"Subject ID={grade.subject_id}, Grade={grade.grade}, Date={grade.date}"
            )
        else:
            print(f"Grade with ID={grade_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error updating grade: {e}")
    finally:
        session.close()


def remove_grade(grade_id):
    """Remove a grade"""
    session = SessionLocal()
    try:
        grade = session.query(Grade).filter(Grade.id == grade_id).first()
        if grade:
            session.delete(grade)
            session.commit()
            print(f"Grade removed: ID={grade_id}")
        else:
            print(f"Grade with ID={grade_id} not found")
    except Exception as e:
        session.rollback()
        print(f"Error removing grade: {e}")
    finally:
        session.close()


def main():
    parser = argparse.ArgumentParser(description='CRUD operations for the database')
    parser.add_argument('-a', '--action', required=True, 
                       choices=['create', 'list', 'update', 'remove'],
                       help='Action to perform')
    parser.add_argument('-m', '--model', required=True,
                       choices=['Teacher', 'Group', 'Student', 'Subject', 'Grade'],
                       help='Model to operate on')
    parser.add_argument('-n', '--name', help='Name for create/update operations')
    parser.add_argument('--id', type=int, help='ID for update/remove operations')
    parser.add_argument('--teacher_id', type=int, help='Teacher ID for Subject operations')
    parser.add_argument('--group_id', type=int, help='Group ID for Student operations')
    parser.add_argument('--student_id', type=int, help='Student ID for Grade operations')
    parser.add_argument('--subject_id', type=int, help='Subject ID for Grade operations')
    parser.add_argument('-g', '--grade', type=float, help='Grade value for Grade operations')
    parser.add_argument('--date', help='Date for Grade (YYYY-MM-DD or YYYY-MM-DD HH:MM[:SS])')
    
    args = parser.parse_args()
    
    # Handle actions
    if args.action == 'create':
        if args.model != 'Grade' and not args.name:
            print("Error: --name is required for create action")
            sys.exit(1)

        if args.model == 'Teacher':
            create_teacher(args.name)
        elif args.model == 'Group':
            create_group(args.name)
        elif args.model == 'Student':
            if not args.group_id:
                print("Error: --group_id is required for creating a student")
                sys.exit(1)
            create_student(args.name, args.group_id)
        elif args.model == 'Subject':
            if not args.teacher_id:
                print("Error: --teacher_id is required for creating a subject")
                sys.exit(1)
            create_subject(args.name, args.teacher_id)
        elif args.model == 'Grade':
            if not args.student_id or not args.subject_id or args.grade is None:
                print("Error: --student_id, --subject_id and --grade are required for creating a grade")
                sys.exit(1)
            create_grade(args.student_id, args.subject_id, args.grade, args.date)

    elif args.action == 'list':
        if args.model == 'Teacher':
            list_teachers()
        elif args.model == 'Group':
            list_groups()
        elif args.model == 'Student':
            list_students()
        elif args.model == 'Subject':
            list_subjects()
        elif args.model == 'Grade':
            list_grades()

    elif args.action == 'update':
        if not args.id:
            print("Error: --id is required for update action")
            sys.exit(1)

        if args.model == 'Teacher':
            if not args.name:
                print("Error: --name is required for updating a teacher")
                sys.exit(1)
            update_teacher(args.id, args.name)
        elif args.model == 'Group':
            if not args.name:
                print("Error: --name is required for updating a group")
                sys.exit(1)
            update_group(args.id, args.name)
        elif args.model == 'Student':
            update_student(args.id, args.name, args.group_id)
        elif args.model == 'Subject':
            update_subject(args.id, args.name, args.teacher_id)
        elif args.model == 'Grade':
            update_grade(args.id, args.student_id, args.subject_id, args.grade, args.date)

    elif args.action == 'remove':
        if not args.id:
            print("Error: --id is required for remove action")
            sys.exit(1)

        if args.model == 'Teacher':
            remove_teacher(args.id)
        elif args.model == 'Group':
            remove_group(args.id)
        elif args.model == 'Student':
            remove_student(args.id)
        elif args.model == 'Subject':
            remove_subject(args.id)
        elif args.model == 'Grade':
            remove_grade(args.id)


if __name__ == '__main__':
    main()
