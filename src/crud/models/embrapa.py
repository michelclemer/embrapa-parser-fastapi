from sqlmodel import Column, Field, String, Integer, ForeignKey, DateTime, func, SQLModel
from datetime import datetime


class ProductionModel(SQLModel, table=True):
    __tablename__ = "production"
    id: int = Field(primary_key=True, index=True)
    id_product: int = Field(sa_column=Column(Integer, primary_key=True))
    control_label: str = Field(sa_column=Column(String, index=True))
    production_name: str = Field(sa_column=Column(String, index=True))
    year: int = Field(sa_column=Column(Integer))
    quantity_liters: int = Field(sa_column=Column(Integer))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))


class TypeProcessModel(SQLModel, table=True):
    __tablename__ = "type_process"
    id: int = Field(primary_key=True, index=True)
    type_name: str = Field(sa_column=Column(String, index=True))
    description: str = Field(sa_column=Column(String, unique=True, index=True))



class TypeImportModel(SQLModel, table=True):
    __tablename__ = "type_import"
    id: int = Field(primary_key=True, index=True)
    type_name: str = Field(sa_column=Column(String, unique=True, index=True))
    description: str = Field(sa_column=Column(String, index=True))


class TypeExportModel(SQLModel, table=True):
    __tablename__ = "type_export"
    id: int = Field(primary_key=True, index=True)
    type_name: str = Field(sa_column=Column(String, unique=True, index=True))
    description: str = Field(sa_column=Column(String, index=True))


class ProcessProductModel(SQLModel, table=True):
    __tablename__ = "process_product"
    id: int = Field(primary_key=True, index=True)
    id_process: int = Field(sa_column=Column(Integer, primary_key=True))
    control_label: str = Field(sa_column=Column(String, index=True))
    cultivar_name: str = Field(sa_column=Column(String, index=True))
    year: int = Field(sa_column=Column(Integer))
    quantity_kg: int = Field(sa_column=Column(Integer))
    type_process_id: int = Field(sa_column=Column(Integer, ForeignKey("type_process.id")))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))


class ComercializationModel(SQLModel, table=True):
    __tablename__ = "comercialization"
    id: int = Field(primary_key=True, index=True)
    control_label: str = Field(sa_column=Column(String, index=True))
    year: int = Field(sa_column=Column(Integer))
    quantity_kg: int = Field(sa_column=Column(Integer))
    quantity_liters: int = Field(sa_column=Column(Integer))
    process_product_id: int = Field(sa_column=Column(Integer, ForeignKey("process_product.id")))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))


class ImportModel(SQLModel, table=True):
    __tablename__ = "import"
    id: int = Field(primary_key=True, index=True)
    control_label: str = Field(sa_column=Column(String, index=True))
    year: int = Field(sa_column=Column(Integer))
    quantity_kg: int = Field(sa_column=Column(Integer))
    price_uss: float = Field(sa_column=Column(Integer))
    type_import_id: int = Field(sa_column=Column(Integer, ForeignKey("type_import.id")))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))

class ExportModel(SQLModel, table=True):
    __tablename__ = "export"
    id: int = Field(primary_key=True, index=True)
    control_label: str = Field(sa_column=Column(String, index=True))
    year: int = Field(sa_column=Column(Integer))
    quantity_kg: int = Field(sa_column=Column(Integer))
    price_uss: float = Field(sa_column=Column(Integer))
    type_export_id: int = Field(sa_column=Column(Integer, ForeignKey("type_export.id")))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))
