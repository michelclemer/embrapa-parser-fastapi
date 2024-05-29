from .base import FindBase, SearchOptions
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


"""
class ProductionModel(SQLModel, table=True):
    __tablename__ = "production"
    id: int = Field(primary_key=True, index=True)
    id_product: int = Field(sa_column=Column(Integer, primary_key=True))
    control_label: str = Field(sa_column=Column(String, unique=True, index=True))
    production_name: str = Field(sa_column=Column(String, unique=True, index=True))
    year: int = Field(sa_column=Column(Integer))
    quantity_liters: int = Field(sa_column=Column(Integer))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))
"""

class Production(BaseModel):
    id: int
    id_product: int
    control_label: str
    production_name: str
    year: int
    quantity_liters: int
    created_at: datetime
    updated_at: datetime


class FindImportResult(BaseModel):
    founds: Optional[List[Production]]
    search_options: Optional[SearchOptions]

