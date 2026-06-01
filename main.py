from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import User, Student
from app.schemas import (
    LoginRequest,
    StudentCreate,
    StudentUpdate
)
from app.auth import (
    create_access_token,
    get_current_user
)

app = FastAPI(
    title="Student Management API"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Student Management API Running"}



@app.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.email == request.email,
        User.password == request.password
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token({"user_id": user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/students")
def get_students(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    students = db.query(Student).all()

    data = []

    for student in students:

        creator = db.query(User).filter(
            User.id == student.created_by
        ).first()

        data.append({
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "phone": student.phone,
            "created_by": student.created_by,
            "created_by_name": creator.name if creator else None
        })

    return data



@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    creator = db.query(User).filter(
        User.id == student.created_by
    ).first()

    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "created_by": student.created_by,
        "created_by_name": creator.name if creator else None
    }


@app.post("/students")
def create_student(
    request: StudentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    student = Student(
        name=request.name,
        email=request.email,
        phone=request.phone,
        created_by=current_user.id
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return {
        "message": "Student created successfully"
    }



@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    request: StudentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = request.name
    student.email = request.email
    student.phone = request.phone

    db.commit()

    return {
        "message": "Student updated successfully"
    }


@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }