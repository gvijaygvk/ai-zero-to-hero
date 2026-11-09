"""Module 2 · Lesson 2 — POST requests and Pydantic models."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


class StudentIn(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age: int = Field(ge=5, le=100)
    skills: list[str] = []
    email: EmailStr
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"


class StudentOut(StudentIn):
    id: int
    skill_count: int


students: list[StudentOut] = []


@app.post("/students", status_code=201)
def create_student(student: StudentIn) -> StudentOut:
    new = StudentOut(
        id=len(students) + 1,
        skill_count=len(student.skills),
        **student.model_dump(),
    )
    students.append(new)
    return new


@app.get("/students")
def list_students() -> list[StudentOut]:
    return students
