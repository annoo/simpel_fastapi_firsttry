from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import declarative_base

_Base = declarative_base()


class Base(_Base):  # IGNORE
    __abstract__ = True


class Participant(Base):
    __tablename__ = "participant"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    type_of_participant = Column(Enum(Types))
    admin_rights = Column(Boolean, default=False)

    class Types(enum.Enum):
        regular = 1
        student = 2
        volunteer = 3
        teacher = 4


class Courses(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    topic = Column(Enum(Topics))
    level = Column(Enum(Levels))

    class Topics(enum.Enum):
        lindy_hop = 1
        jazz_solo = 2
        mix_jazz_lindy = 3
        technique = 4
        rhythm = 5
        balboa = 6
        shag = 7
        blues = 8
        show = 9

    class Levels(enum.Enum):
        beginner = 1
        beginner_intermediate = 2
        intermediate = 3
        intermeciate_advanced = 4
        advanced = 5
        mixed = 6
