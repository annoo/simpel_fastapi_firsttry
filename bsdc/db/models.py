from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import declarative_base

_Base = declarative_base()

class Base(_Base): # IGNORE
    __abstract__ = True
    
class Participant(Base):
    __tablename__ = "participant"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    type_of_participant = Column(Enum(types))
    
    class Types(enum.Enum):
        regular = 1
        student = 2
        volunteer = 3
        teacher = 4