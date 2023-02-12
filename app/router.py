from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema,RequestBook,Response, SourceSchema,RequestSource
import crud
from datetime import datetime

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
    # return Response(code=200,status="OK",message="Data Fetched",result=_book).dict(exclude=None)
    return Response(code=200,status="OK",message="Source Fetched",result=_source).dict(exclude_none=True)

@router.put("/update_data")
async def update_source(request:RequestSource,db:Session=Depends(get_db)):
    # _source = crud.update_source(db=db,source_id=request.parameter.source_id,source=request.parameter.source,source_type=request.parameter.source_type,source_tag=request.parameter.source_tag, frequency=request.parameter.frequency, to_date=request.parameter.to_date, last_update_date=request.parameter.last_update_date, from_date = request.parameter.from_date)

    _source = crud.update_source(db=db,source_id=request.parameter.source_id, to_date=request.parameter.to_date, last_update_date=request.parameter.last_update_date, from_date = request.parameter.from_date)
    return Response(code=200,status="OK",message="Source Updated",result=_source).dict(exclude_none=True)



@router.post("/create")
async def create(request:RequestBook,db:Session=Depends(get_db)):
    crud.create_book(db,book=request.parameter)
    return Response(code=200,status="OK",message="Book Created").dict(exclude_none=True)

@router.get("/")
async def get(db:Session=Depends(get_db)):
    _book = crud.get_book(db,0,100)
    return Response(code=200,status="OK",message="Data Fetched",result=_book).dict(exclude_none=True)

@router.get("/{id}")
async def get_by_id(id:int,db:Session=Depends(get_db)):
    _book = crud.get_book_by_id(db,id)
    # return Response(code=200,status="OK",message="Data Fetched",result=_book).dict(exclude=None)
    return Response(code=200,status="OK",message="Data Fetched",result=_book).dict(exclude_none=True)

@router.post("/update")
async def update_book(request:RequestBook,db:Session=Depends(get_db)):
    _book = crud.update_book(db=db,book_id=request.parameter.id,title=request.parameter.title,description=request.parameter.description)
    return Response(code=200,status="OK",message="Data Updated",result=_book).dict(exclude_none=True)

@router.delete("/{id}")
async def delete(id:int,db:Session=Depends(get_db)):
    crud.remove_book(db,book_id=id)
    return Response(code=200,status="OK",message="Data Deleted").dict(exclude_none=True)

@router.delete("/source/{source_id}")
async def delete(source_id:int,db:Session=Depends(get_db)):
    crud.remove_source(db,source_id=source_id)
    return Response(code=200,status="OK",message="Source Deleted").dict(exclude_none=True)
