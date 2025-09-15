# Basic pydantic model

from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

def insert_patient_record(patient : Patient):
    print(patient.name)
    print(patient.age)

entry = {'name':'Vidhan','age':23}

classobj = Patient(**entry)

insert_patient_record(classobj)