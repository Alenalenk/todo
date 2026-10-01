from datetime import datetime

from pytz import timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Todo(Base):
    __tablename__ = "todos"
    __table_args__ = {'schema': 'todos'}
    

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(Boolean, nullable=False, default=False)

    date_added = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone('Europe/Kyiv')))
    date_modify = Column(DateTime(timezone=True), nullable=True)