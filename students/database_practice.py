from sqlmodel import Session, select
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from .config.db import create_tables, engine
from .models.std_data import Student, UpdateStudent


app = FastAPI()

@app.get("/getstudents")
def GetStudents():
    # We can use the Session object to live connection with database and perform 
    # operations and when we are done it will automatically close the connection! 
    with Session(engine) as session:
        # We can use the select function to select all the records from the Student table 
        # and it will return a list of Student objects!
        statement = select(Student)
        # exec function will execute the statement and return the results and then 
        results = session.exec(statement)
        # we can use all() function to get all the records in a list!
        students_data = results.all()
        return students_data



# We just check student data by id through postman!

@app.get("/getstudentbyid")
def GetStudentById(id:int):
    with Session(engine) as session:
        statement = select(Student).where(Student.id == id)
        results = session.exec(statement)
        student_id = results.first()
        return student_id

# We are adding student data in database through postman, thunder client, frontend etc.
@app.post("/addstudents")
def AddStudents(student: Student):
    with Session (engine) as session:
        session.add(student)
        session.commit()
        session.refresh(student)
        return {"status": 200, "message": "Student added successfully", "data": student}


# Update Student data in database by id from frontend e.g postman, thunder client, frontend.
@app.put("/updatestudent/{id}")
def UpdateStudent(id: int, student: UpdateStudent):
    with Session(engine) as session:
        db_student = session.get(Student, id)
        if not db_student:
            raise HTTPException(status_code=404, detail="Student data not found")
        student_data = student.model_dump(exclude_unset=True)
        db_student.sqlmodel_update(student_data)
        session.add(db_student)
        session.commit()
        session.refresh(db_student)
        return {"status": 200, "message": "Student updated successfully", "data": db_student}


# Delete Student data in database by id from frontend e.g postman, thunder client, frontend.
@app.delete("/deletestudent/{id}")
def DeleteStudent(id: int):
    with Session(engine) as session:
        db_student = session.get(Student, id)
        if not db_student:
            raise HTTPException(status_code=404, detail="Student data not found")
        session.delete(db_student)
        session.commit()
        return {"status": 200, "message": "Student data deleted successfully", "data": db_student}