from sqlmodel import Session, select
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from .config.db import create_tables, engine
from .models.std_data import Student


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


create_tables()