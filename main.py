from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

class ADDSTUDENT(BaseModel):
    name : str
    age : int
    email : str
    grade : str

class UpdateStudent(BaseModel):
    name : str
    age : int
    email : str
    grade : str


app = FastAPI()

Database = []

@app.post("/students")
def AddStudent(student:ADDSTUDENT):

    id = str(uuid4())
    student_data = {
        "id": id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "grade": student.grade
}
    print(student_data)
    Database.append(student_data)
    return {
        "message": "Student added successfully!",
        "student_id": id
    }

@app.get("/getAllstudents")
def getAllStudents():
    return Database


@app.get("/studentID{id}")
def getStudentID(student_id:str):
    for std in Database:
        if std['id'] == id:
            return std 
            return {
                "message": "user not found"
                }


@app.put("/updatestd{id}")
def UpdateStudentData(student_id:str, student: UpdateStudent):
    for std in Database:
        if std['id'] == student_id:
           std['name'] = student.name
           std['age'] = student.age,
           std['email'] = student.email,
           std['grade'] = student.grade
           return {
            "message": "Student data updated successfully!"
           }
    return {
        "message": "Student not found"
}


@app.delete("/deletestd{id}")
def DeleteStudent(student_id:str):
    for stdData in Database:
        if stdData['id'] == student_id:
            Database.remove(stdData)
            return {
                "message": "Student deleted successfully!"
            }
    return {
        "message": "Student not found"
}