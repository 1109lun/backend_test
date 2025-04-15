import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User
from hashlib import sha256
from datetime import date, datetime

# 資料庫連線字串（記得跟 alembic.ini 保持一致）
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test"

# 建立 engine 和 session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# 建立三筆用戶資料
users = [
    User(
        username="alice",
        password=sha256("alice123".encode()).hexdigest(),
        birthday=date(2000, 1, 1),
        create_time=datetime.utcnow()
    ),
    User(
        username="bob",
        password=sha256("bob456".encode()).hexdigest(),
        birthday=date(1995, 5, 15),
        create_time=datetime.utcnow()
    ),
    User(
        username="charlie",
        password=sha256("charlie789".encode()).hexdigest(),
        birthday=date(1998, 12, 31),
        create_time=datetime.utcnow()
    ),
]

# 寫入資料庫
session.add_all(users)
session.commit()
print("Users inserted successfully ✅")
