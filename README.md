# Fast API Practice

A simple FastAPI practice project implementing a lightweight in-memory student management API. This repository demonstrates building and testing CRUD endpoints using FastAPI and Pydantic models.

## Key Features

- Create a new student record with `POST /students`
- Retrieve all students with `GET /getAllstudents`
- Retrieve a student by ID with `GET /studentID{id}`
- Update an existing student with `PUT /updatestd{id}`
- Delete a student with `DELETE /deletestd{id}`

## Requirements

- Python 3.13+
- FastAPI
- uvicorn

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fast-api-practice
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

Start the FastAPI server using uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Create student

- Method: `POST`
- URL: `/students`
- Body:
  ```json
  {
    "name": "John Doe",
    "age": 20,
    "email": "john@example.com",
    "grade": "A"
  }
  ```

### Get all students

- Method: `GET`
- URL: `/getAllstudents`

### Get student by ID

- Method: `GET`
- URL: `/studentID{id}`

### Update student data

- Method: `PUT`
- URL: `/updatestd{id}`
- Body: same as create body

### Delete student

- Method: `DELETE`
- URL: `/deletestd{id}`

## Notes

- Data is stored in memory only and resets when the server restarts.
- This project is designed for learning FastAPI basics and API route creation.
- Review `main.py` for the current implementation details.
