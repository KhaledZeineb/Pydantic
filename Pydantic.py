# Python
x = 10

# Java
int x = 10;

#
x = 10
x = 'hello'

#
ali = Person("Ali", 24)    # Correct
ali = Person("Ali", "24")  # Mistake

#
@dataclass
class Person:
    name: str
    age: str

# Using Pydantic
class Person(BaseModel):
    name: str
    email: EmailStr
    account_id: int

#
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int

#
user = User(
    name = "Salah",
    email = "salah@gmail.com",
    account_id = 12345
)

#
user_data = {
    'name': 'Salah',
    'email': 'salah@gmail.com',
    'account_id': 12345
}

user = User(**user_data)

#
print(user.name)    # Salah
print(user.email)    # salah@gmail.com
print(user.account_id)    # 12345

#
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int

# It will fail and show a validation error
user = User(name = 'Ali', email = 'ali@gmailcom', account_id = 'hello')
print(user)

#
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr     # pip install pydantic[email]
    account_id: int

# It will fail and show a validation error with email = 'ali'
user = User(name = 'Ali', email = 'ali', account_id = 1234)
print(user)

#
@field_validator("account_id")
def validate_account_id(cls, value):
    if value <= 0:
        raise ValueError(f"account_id must be positive: {value}")
    return value

#
# you will get a validation error with account_id = -12
user = User(name = 'Ali', email = 'ali', account_id = -12)
print(user)

#
user_json_str = user.model_dump_json()
# this will return a JSON strinf representation of the model's data
print(user_json_str)

#
user_json_obj = user.model_dump()

#
json_str = {"name": "Ali, "email": "ali@gmail.com", "account_id": 1234}
user = user.parse_raw(json_str)

#
# Python 3.6+
x: int = 0
y: str = "hello"

#
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    account_id: int