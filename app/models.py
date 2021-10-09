from typing import Optional
from pydantic import BaseModel


class ShowUpdate(BaseModel):
    type: Optional[str] = None
    title: Optional[str] = None
    director: Optional[str] = None
    cast: Optional[str] = None
    country: Optional[str] = None
    date_added: Optional[str] = None
    release_year: Optional[str] = None
    rating: Optional[str] = None
    duration: Optional[str] = None
    listed_in: Optional[str] = None
    description: Optional[str] = None


class ShowCreate(BaseModel):
    show_id: str
    type: str
    title: str
    director: str
    cast: str
    country: str
    date_added: str
    release_year: str
    rating: str
    duration: str
    listed_in: str
    description: str
