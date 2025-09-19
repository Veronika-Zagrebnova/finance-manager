from json import loads
from fastapi import FastAPI, HTTPException, Depends, Form, Request
from database import Base, engine, session_local
from schemas import UserSchema, CategorySchema, TransactionSchema, CreateCategory, CreateTransaction, CreateUser, UserLogin
from sqlalchemy.orm import Session
from models import User, Category, Transaction

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Base.metadata.create_all(bind=engine)

def getDB():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


#Домашняя страница
@app.get("/")
async def getHome() -> dict:
    return {"data": "It's home!"} 


@app.post("/users", response_model=UserSchema)
async def makeUser(user: CreateUser, db: Session = Depends(getDB)) -> User:
    db_user = User(email=user.email, password=user.password, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@app.post("/categories", response_model=CategorySchema)
async def makeCategory(cat: CreateCategory, db: Session = Depends(getDB)):
    db_cat = Category(name=cat.name)
    db.add(db_cat)
    db.commit()
    #db.refresh(db_cat)
    return db_cat

@app.post("/transactions", response_model=TransactionSchema)
async def makeTransaction(trans: CreateTransaction, db: Session = Depends(getDB)):
    db_trans = Transaction(type=trans.type,
                           amount=trans.amount,
                           date=trans.date,
                           description=trans.description,
                           user_id=trans.user_id,
                           category_id=trans.category_id
                           )
    db.add(db_trans)
    db.commit()
    db.refresh(db_trans)
    return db_trans

@app.get("/get-users")
async def getUsers(db: Session = Depends(getDB)):
    return db.query(User).all()

# @app.post("/get-user")
# async def getUser(email: str = Form(...), password: str = Form(...), db: Session = Depends(getDB)):
    
#     user = db.query(User).filter(User.email == email, User.password == password).first()
#     return user

@app.post("/get-user")
async def getUser(user: UserLogin, db: Session = Depends(getDB)):
    
    user = db.query(User).filter(User.email == user.email, User.password == user.password).first()
    return user

# users = [
#     {'id': 1, 'email': 'emma@gmail.com', 'password': '123qwe', 'name': 'Emma'},
#     {'id': 2, 'email': 'superdog@gmail.com', 'password': 'superdognumder1', 'name': 'Bob'},
#     {'id': 3, 'email': 'piterparker@gmail.com', 'password': 'w0wl0l', 'name': 'Piter'},
#     {'id': 4, 'email': 'bitch@gmail.com', 'password': '1984', 'name': 'Liza'}
# ]

# categories = [
#     {'id': 1, 'name': 'food'},
#     {'id': 2, 'name': 'medicines'},
#     {'id': 3, 'name': 'clothes'},
#     {'id': 4, 'name': 'transport'},
#     {'id': 5, 'name': 'beauty'},
#     {'id': 6, 'name': 'study'},
#     {'id': 7, 'name': 'other'}
# ]

# transactions = [
#     {'id': 1, 'type': 'in', 'amount': 4000, 'date': '12-05-05', 'description': None, 'user_id': 1, 'category_id': 1},
#     {'id': 2, 'type': 'in', 'amount': 796, 'date': '17-05-05', 'description': None, 'user_id': 3, 'category_id': 2}
# ]



#Действия с пользователями
# @app.get("/users")
# async def getUsers() -> List[User]:
#     return [User(**user) for user in users]

# @app.get("/user/{id}")
# async def getUser(id: int) -> User:
#     for user in users:
#         if user['id'] == id:
#             return User(**user) 
        
#     raise HTTPException(status_code=404, detail='User not found')

# @app.post("/transaction/add")
# async def newTransaction(trans: createTransaction) -> Transaction:
#     new_trans = {'id': len(transactions)+1, 'type': trans.type, 'amount': trans.amount, 'date': trans.date, 'description': trans.description, 'user_id': trans.user_id, 'category_id': trans.category_id}

#     transactions.append(new_trans)
#     return Transaction(**new_trans)