from fastapi import FastAPI, HTTPException, Depends , Form
from app.auth import get_current_user
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User
from app.auth import verify_password, create_access_token

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    db = SessionLocal()
    user = db.query(User).filter(User.username == request.username).first()

    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/user/")
def get_user(
    username: str ,
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return {
        "username": user.username,
        "birthday": user.birthday,
        "create_time": user.create_time,
        "last_login": user.last_login,
    }