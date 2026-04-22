# 🚀 FastAPI + PostgreSQL CRUD API

A backend project built with **FastAPI**, **SQLModel**, and **PostgreSQL** demonstrating full CRUD operations with proper API design and database integration.

---

## 📌 Features

- Create student records
- Get all students
- Get student by ID
- Update student data
- Delete student records
- PostgreSQL integration using SQLModel ORM

---

## 🛠️ Tech Stack

- FastAPI
- SQLModel (ORM + Pydantic)
- PostgreSQL (Supabase / Local)
- Uvicorn
- Python 3.10+

---

## 📂 Project Structure

```
fast-api-practice/
│
├── students/
│   ├── database_prac.py     # API routes
│   ├── models/
│   │   └── std_data.py      # Models (Student, UpdateStudent)
│   ├── config/
│   │   └── db.py            # Database connection & engine
│
├── .env                     # Environment variables
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone <your-repo-link>
cd fast-api-practice
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```
DATABASE_URL=your_postgresql_connection_string
```

---

## ▶️ Run the Server

```bash
uvicorn students.database_prac:app --reload
```

API will run on:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

### Get all students
```
GET /getstudents
```

### Get student by ID
```
GET /getstudentbyid?id=1
```

### Add student
```
POST /addstudents
```

### Update student
```
PUT /updatestudent/{id}
```

### Delete student
```
DELETE /deletestudent/{id}
```

---

## 🧠 Learning Outcomes

- Understanding RESTful API structure
- Working with SQLModel ORM
- Handling database sessions properly
- Performing CRUD operations with PostgreSQL
- Debugging real backend errors (schema mismatch, query issues)

---

## ⚠️ Notes

- Make sure your database schema is synced with your models
- Use migrations (Alembic) in production instead of manual changes
- Avoid hardcoding values — always use environment variables

---

## 📌 Future Improvements

- Add Alembic migrations
- Add authentication (JWT)
- Add validation & response schemas
- Dockerize the application
- Deploy on cloud (Render / Railway / AWS)

---

## 👨‍💻 Author

Huzaifa – Backend Developer (FastAPI, AI Agents, Next.js)

---