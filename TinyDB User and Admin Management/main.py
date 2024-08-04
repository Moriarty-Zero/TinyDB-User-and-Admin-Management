import json
from tinydb import TinyDB, Query
from pydantic import BaseModel, Field
from typing import Union, Literal

#Ініціалізація бази даних
db = TinyDB('db.json')

class User(BaseModel):
    id: int
    name: str
    type: Literal["user"] = "user"

class Admin(BaseModel):
    id: int
    name: str
    privileges: list
    type: Literal["admin"] = "admin"

def add_data(data: Union[User, Admin]):
    db.insert(data.dict())

def find_person_by_id(person_id: int):
    PersonQuery = Query()
    result = db.search(PersonQuery.id == person_id)
    if result:
        return result[0] 
    return None

def format_db():
    with open('db.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        f.seek(0)
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.truncate()

#Додавання даних до бази
users_and_admins = [
    User(id=1, name="Alice"),
    Admin(id=2, name="Bob", privileges=["manage_users", "edit_settings"]),
    User(id=3, name="Olek"),
    Admin(id=4, name="Biden", privileges=["manage_policies", "edit_records"]),
    User(id=5, name="Jane"),
    User(id=6, name="John"),
    Admin(id=7, name="Moriarty", privileges=["correct_rules", "do_everything"]),
    Admin(id=8, name="Mister", privileges=["delete_system", "kill_terminal"])
]

for person in users_and_admins:
    add_data(person)

format_db()

#Пошук персони за ID
person = find_person_by_id(5)
print(person)
person3 = find_person_by_id(3)
print(person3)
