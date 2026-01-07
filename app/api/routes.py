from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db import models
from app.schemas.schemas import StudentCreate, GroupCreate
from app.services import students as service

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Создать
@router.post("/students")
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    return service.create_student(db, data.name)


@router.post("/groups")
def create_group(data: GroupCreate, db: Session = Depends(get_db)):
    return service.create_group(db, data.title)


# Получить студента по ID
@router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.get(models.Student, student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    return student


@router.get("/groups/{group_id}")
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = db.get(models.Group, group_id)
    if not group:
        raise HTTPException(404, "Group not found")
    return group


# Удалить студента
@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.get(models.Student, student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    db.delete(student)
    db.commit()
    return {"status": "deleted"}


@router.delete("/groups/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    group = db.get(models.Group, group_id)
    if not group:
        raise HTTPException(404, "Group not found")
    db.delete(group)
    db.commit()
    return {"status": "deleted"}


# Список
@router.get("/students")
def list_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@router.get("/groups")
def list_groups(db: Session = Depends(get_db)):
    return db.query(models.Group).all()


# Операции с группами
@router.post("/groups/{group_id}/students/{student_id}")
def add_student(group_id: int, student_id: int, db: Session = Depends(get_db)):
    if not service.add_student_to_group(db, student_id, group_id):
        raise HTTPException(404, "Student or group not found")
    return {"status": "added"}


@router.delete("/groups/{group_id}/students/{student_id}")
def remove_student(group_id: int, student_id: int, db: Session = Depends(get_db)):
    if not service.remove_student_from_group(db, student_id, group_id):
        raise HTTPException(404, "Student or group not found")
    return {"status": "removed"}


@router.get("/groups/{group_id}/students")
def get_students_in_group(group_id: int, db: Session = Depends(get_db)):
    group = db.get(models.Group, group_id)
    if not group:
        raise HTTPException(404, "Group not found")
    return group.students


@router.post("/groups/move")
def move_student(student_id: int, from_group: int, to_group: int, db: Session = Depends(get_db)):
    if not service.move_student(db, student_id, from_group, to_group):
        raise HTTPException(404, "Invalid ids")
    return {"status": "moved"}
