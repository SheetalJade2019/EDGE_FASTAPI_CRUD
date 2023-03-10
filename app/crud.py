from sqlalchemy.orm import Session
from model import Source
from schemas import SourceSchema
from datetime import datetime

def get_source(db:Session,skip:int=0,limit:int=100):
    return db.query(Source).offset(skip).limit(limit).all()

def get_source_by_id(db:Session,source_id:int):
    return db.query(Source).filter(Source.source_id == source_id).first()

def create_source(db:Session,s:SourceSchema):
    _source = Source(source=s.source,source_type=s.source_type,source_tag=s.source_tag,frequency=s.frequency,last_update_date=s.last_update_date,from_date=s.from_date,to_date=s.to_date)
    db.add(_source)
    db.commit()
    db.refresh(_source)
    return _source

# def update_source(db:Session,source_id:int,source:str,source_type:str,source_tag:str,frequency:str,last_update_date:datetime,from_date:datetime,to_date:datetime):
def update_source(db:Session,source_id:int,last_update_date:datetime,from_date:datetime,to_date:datetime):

    _source = get_source_by_id(db=db,source_id=source_id)
    # _source.source=source
    # _source.source_type=source_type
    # _source.source_tag=source_tag
    # _source.frequency = frequency
    _source.last_update_date = last_update_date
    _source.from_date =from_date
    _source.to_date=to_date
    db.commit()
    db.refresh(_source)
    return _source


def remove_source(db:Session,source_id:int):
    _source =  get_source_by_id(db=db,source_id=source_id)
    db.delete(_source)
    db.commit()