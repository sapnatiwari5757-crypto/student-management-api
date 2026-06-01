#  Student Management API (FastAPI + JWT)

A secure and scalable Student Management System built using **FastAPI**, **SQLAlchemy**, and **JWT Authentication**.

This project provides login authentication and full CRUD operations for managing students with proper access control.

---

## Features

-  User Authentication using JWT Token
-  Secure Login System
-  Add, View, Update, Delete Students (CRUD)
-  Tracks which user created each student
-  Protected Routes (Login Required)
-  Student details include creator name
-  FastAPI + SQLite Database

---

##  Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)

---

##  API Endpoints

### 🔐 Auth
- POST `/login` → User login & get token

### 👨‍🎓 Students
- GET `/students` → List all students
- GET `/students/{id}` → Get single student
- POST `/students` → Add student
- PUT `/students/{id}` → Update student
- DELETE `/students/{id}` → Delete student

---

##  Authentication Flow

1. Login using email & password
2. Receive JWT token
3. Click **Authorize** in Swagger
4. Paste token as: