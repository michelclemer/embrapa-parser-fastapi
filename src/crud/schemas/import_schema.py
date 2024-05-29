
from src.crud.schemas.base import SearchOptions


from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class BaseImport(BaseModel):
    id: Optional[int] = Field(default=None)
    control_label: Optional[str] = Field(default=None)
    year: Optional[int] = Field(default=None)
    quantity_kg: Optional[int] = Field(default=None)
    price_uss: Optional[float] = Field(default=None)
    type_import_id: Optional[int] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)

class Import(BaseModel):  # Inherits from BaseImport
    pass

class FindImport(BaseModel):
    id: Optional[int] = Field(default=None)
    control_label: Optional[str] = Field(default=None)
    year: Optional[int] = Field(default=None)
    quantity_kg: Optional[int] = Field(default=None)
    price_uss: Optional[float] = Field(default=None)
    type_import_id: Optional[int] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)

class FindImportResult(BaseModel):
    founds: Optional[List[Import]] = None
    search_options: Optional[SearchOptions] = None
