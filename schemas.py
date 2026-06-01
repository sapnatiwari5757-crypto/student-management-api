from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str


class StudentUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: str