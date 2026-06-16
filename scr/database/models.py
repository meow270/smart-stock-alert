from . import session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, Date

Session = session.Session_start

class Base(DeclarativeBase): pass

class Data_Collect(Base):
    __tablename__ = f'base'

    id = Column(Integer, primary_key=True, index=True)
    ticket = Column(String)
    date = Column(Date)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

Base.metadata.create_all(bind=session.engine)