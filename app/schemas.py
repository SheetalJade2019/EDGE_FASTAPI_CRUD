from typing import List,Generic, Optional,TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import datetime


T = TypeVar('T')


class Response(GenericModel, Generic[T]):
    code:str
    status:str
    message:str
    result:Optional[T]


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class SourceSchema(BaseModel):
    source_id:Optional[int]=None
    source:Optional[str]=None
    source_type:Optional[str]=None
    source_tag:Optional[str]=None
    last_update_date:Optional[datetime]=None
    from_date:Optional[datetime]=None
    to_date:Optional[datetime]=None
    frequency:Optional[str]=None
    

    class config:
        orm_mode=True

class RequestSource(BaseModel):
    parameter:SourceSchema = Field(...)

