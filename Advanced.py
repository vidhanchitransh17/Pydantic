# Data Validation, field validator, model validator, computed_field,nested class, Annotated, Field Function, Seriaalization

from pydantic import BaseModel, Field , EmailStr , AnyUrl, field_validator, model_validator, computed_field
from typing import Annotated

class address(BaseModel):
    city : Annotated[str, Field(title = 'Name of city')]
    state : Annotated[str, Field(title = 'Name of state')]
    pincode : Annotated[int, Field(title = 'Pincode of address')]

class engineer(BaseModel):
    name : Annotated[str, Field(max_length=50, title="Name of Person")]
    age : Annotated[int, Field(gt=4, title="Age of person")]
    email : Annotated[EmailStr, Field(title="Email of the user")]
    url : Annotated[AnyUrl, Field(title="Linked Profile URL")]
    address : address

    # to validate specific field
    @ field_validator('email')
    @classmethod
    def email_validate(cls, value):
        valid = ['pwc.com','gmail.com']
        domain = value.split('@')[-1]
        if domain not in valid:
            raise ValueError("incorrect value for email")
        return value
    
    @field_validator('name', mode = 'after')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @model_validator(mode='after')
    def validate_person(cls, model):
        if model.age < 20 and model.name == 'VIDHAN':
            raise ValueError('Name should not be vidhan')
        return model
    
    @computed_field
    @property
    def sign(self) -> str:
        sign = str(self.name) + str(self.age)
        return sign

address_entry = {'city':'Kolkata',
              'state':'West Bengal',
              'pincode':'700156'}

engineer_entry = {'name' : 'Vidhan',
         'age' : 23,
         'email': 'vidhan@pwc.com',
         'url' : 'https://www.linkedin.com/in/vidhan-chitransh/',
         'address' : address_entry}

def details(eng:engineer):
    print(eng.name)
    print(eng.age)
    print(eng.email)
    print(eng.url)
    print(eng.sign)
    print(eng.address.city)
    print(eng.address.state)
    print(eng.address.pincode)
    print('success')

addobj = address(**address_entry)
engobj = engineer(**engineer_entry)

details(engobj)


# Model export (useful for FastAPI)
export_enginner = engobj.model_dump()
print(export_enginner)

export_enginner_json = engobj.model_dump_json()
print(export_enginner_json)