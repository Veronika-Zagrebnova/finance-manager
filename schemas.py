from pydantic import BaseModel, Field
from typing import Annotated


class CreateUser(BaseModel):
    email: Annotated[str, Field(..., title='email of user', max_length=30)]
    password: Annotated[str, Field(..., title='password of user', min_length=6, max_length=50)]
    name: Annotated[str, Field(..., title='name of user', min_length=2, max_length=20)]

class UserSchema(CreateUser):
    id: Annotated[int, Field(..., title='id of user', ge=1)]
    
class CreateCategory(BaseModel):
    name: Annotated[str, Field(..., title='name of category', min_length=2, max_length=50)]

class CategorySchema(CreateCategory):
    id: Annotated[int, Field(..., title='id of category', ge=1)]
    
class CreateTransaction(BaseModel):
    type: Annotated[str, Field(..., title='in or out', min_length=2, max_length=50)]
    amount: Annotated[float, Field(..., title='amount of transaction', gt=0)] 
    date: Annotated[str, Field(..., title='date of transaction')] 
    description: Annotated[str, Field(title='description of transaction', min_length=2, max_length=100)] 
    user_id: Annotated[int, Field(..., title='id of user who do transaction', ge=1)]
    category_id: Annotated[int, Field(..., title='id of category which use in transaction', ge=1)]

class TransactionSchema(CreateTransaction):
    id: Annotated[int, Field(..., title='id of transaction', ge=1)]
    
class UserLogin(BaseModel):
    email: Annotated[str, Field(..., title='email of user', max_length=30)]
    password: Annotated[str, Field(..., title='password of user', min_length=6, max_length=50)]