from .config import *
from sqlalchemy.orm import relationship
import pandas as pd


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    user_id = Column(Integer,index=True)

