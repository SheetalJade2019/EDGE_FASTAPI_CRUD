from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, SourceSchema,RequestSource
import crud
from datetime import datetime,timedelta

router = APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add_data")
async def create(request:RequestSource,db:Session=Depends(get_db)):
    crud.create_source(db,s=request.parameter)
    return Response(code=200,status="OK",message="Source Created").dict(exclude_none=True)

@router.get("/get_data")
async def get(db:Session=Depends(get_db)):
    _source = crud.get_source(db,0,100)
    return Response(code=200,status="OK",message="Source Fetched",result=_source).dict(exclude_none=True)

@router.get("/get_data/{source_id}")
async def get_sourcedata_by_id(source_id:int,db:Session=Depends(get_db)):
    _source = crud.get_source_by_id(db,source_id)
    return Response(code=200,status="OK",message="Source Fetched",result=_source).dict(exclude_none=True)

@router.get("/get_data_trigger/{source_id}")
async def get_source_data_trigger(source_id:int,db:Session=Depends(get_db)):
    _source = crud.get_source_by_id(db,source_id)
    print("\nResults ----->\n",_source.source,_source.to_date,_source.last_update_date, _source.from_date, _source.frequency)
    print(_source.to_date)
    _source.to_date + timedelta(minutes=int(_source.frequency[:-1]))
    
    src={}
    src["source_id"]=_source.source_id
    src["source"]=_source.source
    src["source_type"]=_source.source_type
    src["source_tag"]=_source.source_tag
    src["last_update_date"]=_source.last_update_date
    src["from_date"]= _source.from_date + timedelta(minutes=int(_source.frequency[:-1]))
    src["to_date"]=_source.to_date + timedelta(minutes=int(_source.frequency[:-1]))
    src["old_from_date"]= _source.from_date
    src["old_to_date"]=_source.to_date




    return Response(code=200,status="OK",message="Source Fetched",result=src).dict(exclude_none=True)


@router.put("/update_data")
async def update_source(request:RequestSource,db:Session=Depends(get_db)):

    _source = crud.update_source(db=db,source_id=request.parameter.source_id, to_date=request.parameter.to_date, last_update_date=request.parameter.last_update_date, from_date = request.parameter.from_date)
    return Response(code=200,status="OK",message="Source Updated",result=_source).dict(exclude_none=True)

@router.delete("/source/{source_id}")
async def delete(source_id:int,db:Session=Depends(get_db)):
    crud.remove_source(db,source_id=source_id)
    return Response(code=200,status="OK",message="Source Deleted").dict(exclude_none=True)
