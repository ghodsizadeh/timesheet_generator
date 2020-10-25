from .config import *
from sqlalchemy.orm import relationship
import pandas as pd


class StockPrice(Base):
    __tablename__ = "timesheet"

    id = Column(Integer, primary_key=True)
    user = Column(id, ForeignKey("users.id"), index=True)
    time = Column(DateTime, nullable=False)
    terminal_id = Column(String, default = '0001 : 05'
    class_ = Column('class', String, default='User')
    mode = Column(String,default="Access")
    type_ =  Column('type', String, default='User')
    result = Column(String,default="Success")
    property = Column('type', Integer, default=1000)
