from .base import FindBase, SearchOptions
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


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

