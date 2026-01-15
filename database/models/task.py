from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database.connection import Base
from datetime import datetime


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(String, nullable=False)
    status = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)
    tags = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey("users.id"))
