from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

student_group = Table(
    "student_group",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True),
)


class Student(Base):
    """
    Модель студента.
    """
    __tablename__ = "students"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(length=100), nullable=False)
    age: int = Column(Integer, nullable=False)

    groups = relationship(
        "Group",
        secondary=student_group,
        back_populates="students",
    )


class Group(Base):
    """
    Модель группы студентов.
    """
    __tablename__ = "groups"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(length=100), unique=True, nullable=False)

    students = relationship(
        "Student",
        secondary=student_group,
        back_populates="groups",
    )