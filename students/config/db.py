from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel
import os

load_dotenv()
database_url = os.getenv("DB_URL")

if not database_url:
    raise ValueError("Database URL not found!")

# this create_engine function we can connect to the database thorugh string url!
engine = create_engine(database_url,)



# when this line run it will create the table in database name Student and define the columns 
# that are in Student class!
def create_tables():
    SQLModel.metadata.create_all(engine)
