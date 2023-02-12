from sqlalchemy import Column, Integer, String, DateTime
from config import Base 

class Book(Base):
    __tablename__="book"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    description=Column(String)

class Source(Base):
    __tablename__="source"
    source_id=Column(Integer,primary_key=True)
    source = Column(String)
    source_type = Column(String)
    source_tag = Column(String)
    last_update_date = Column(DateTime)
    from_date = Column(DateTime)
    to_date = Column(DateTime)
    frequency = Column(String)
    
