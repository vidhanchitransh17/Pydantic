# using List , Dict , Optional , Default

from pydantic  import BaseModel
from typing import List , Dict , Optional

class engineer(BaseModel):
    name : str
    age : int
    married : bool = False
    language : List[str] = ['C++']


entry = {'name':'Vidhan', "age": 23, 'language':['Python','R']}

def insert(eng:engineer):
    print(eng.name)
    print(eng.age)
    print(eng.married)
    print(eng.language)

classobj = engineer(**entry)

insert(classobj)