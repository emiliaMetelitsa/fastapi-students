from sqlalchemy.orm import Session
from typing import List
from app.db.models import Student, Group
import logging

logger = logging.getLogger(__name__)


class StudentService:
    """
    Сервис для работы со студентами.
    """

    def __init__(self, db: Session):
        self.db = db

    def create_student(self, name: str, age: int) -> Student:
        """Создание нового студента"""
        student = Student(name=name, age=age)
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def get_student(self, student_id: int) -> Student | None:
        """Получение студента по ID"""
        return self.db.query(Student).filter(Student.id == student_id).first()

    def list_students(self) -> List[Student]:
        """Получение всех студентов"""
        return self.db.query(Student).all()

    def delete_student(self, student_id: int) -> bool:
        """Удаление студента по ID"""
        student = self.get_student(student_id)
        if not student:
            logger.warning("Попытка удалить несуществующего студента: %s", student_id)
            return False
        self.db.delete(student)
        self.db.commit()
        return True
