from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def main():
    return {
        "name": "Huzaifa",
        "email": "abc@gmail.com",
        "body": "Hello world all!"
    }

# Path Parameters

# In this case, we have to pass the parameters in the URL as path parameters and this is not a good way to do!

@app.get("/getstudents/{userName}/{id}")
def GetStudents(userName:str, id:int):
    print("Get Students called!",userName, id)
    return userName , id


# Query Parameters

# In this case, we have to pass the parameters in the FRONTEND form as query parameters and this is easiest way to do!

students = [
    {
        "Name": "Huzaifa",
        "RollNumber": 2121
    },
    {
        "Name": "Fatima",
        "RollNumber": 2123
    }
]


# In this case we can access all the students data by calling the /students endpoint.

@app.get("/students")
def getStudents():
    return students


 
# In this case we can add a student by calling the /addstudents endpoint and passing the parameters. This query parameters so we have to pass the values in the frontend form as query parameters. This is the easiest way to do!

@app.post("/addstudents")
def AddStudents(UserName:str, RollNumber:int):
    global students
    students.append({ "Name": UserName, "RollNumber": RollNumber })
    return students



# In this case we can update a student by calling the /students/{roll_number} endpoint and 
# passing the roll number as path parameter and the updated data as query parameters in body filed of thunder client.

@app.put("/students/{roll_number}")
def update_student(roll_number: int, updated_data: dict):
    for student in students:
        if student["RollNumber"] == roll_number:
            student["Name"] = updated_data.get("Name", student["Name"])
            return {"message": "Student updated", "student": student}
    
    return {"error": "Student not found"}


# In this case we can delete a student by calling the /delstudents/{roll_number} endpoint and 
# passing the roll number as path parameter.

@app.delete("/delstudents/{roll_number}")
def delete_student(roll_number: int):
    global students
    students = [student for student in students if student["RollNumber"] != roll_number]
    return {"message": "Student deleted", "students": students}




# CRUD Operations COMPLETE BY MY HANDS NOT BY CHATGPT.