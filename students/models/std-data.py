from sqlmodel import Field, SQLModel




# Similar to how we define a class in Pydantic with a custom name,

# we can also define a class here for example, `Students` 
# The class name will be used as the table name

# Setting "table=True" tells SQLModel to treat this class as a database table.
# If the table does not already exist, it will create!

class Student(SQLModel, table=True):
    # We can define the columns of the table.
    # primary_key=True means this is used to uniquely identify in each record in the table.
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    is_active: bool