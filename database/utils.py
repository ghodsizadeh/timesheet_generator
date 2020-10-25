from .config import engine
from .user import User
from .timesheet import TimeSheet

def create_models():
    User.__table__.create(engine)
    TimeSheet.__table__.create(engine)