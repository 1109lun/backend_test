from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    username = Column(String, primary_key=True)                     # 1. username
    password = Column(String, nullable=False)                       # 2. password (not null)
    birthday = Column(Date)                                         # 3. birthday (date)
    create_time = Column(DateTime, default=datetime.utcnow)         # 4. create_time (default)
    last_login = Column(DateTime, nullable=True)                    # 5. last_login (nullable)
