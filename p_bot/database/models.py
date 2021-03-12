import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserTG(Base):
    __tablename__ = "telegram_users"

    id =                Column(Integer, primary_key=True, autoincrement=True)
    telegram_id =       Column(Integer, nullable=False)
    login =             Column(String(length=255))
    purchase_date =     Column(DateTime(), default=datetime.datetime.now())
    license_end_date =  Column(DateTime(), nullable=False)
