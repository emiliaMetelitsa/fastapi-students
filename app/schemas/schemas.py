from pydantic import BaseModel
from typing import List


class StudentCreate(BaseModel):
    name: str


class GroupCreate(BaseModel):
    title: str


class StudentOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class GroupOut(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
