from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from src.crud.schemas.import_schema import FindImport, FindImportResult
from src.infra.container import Container
from src.services.embrapa_service import ImportProductService, ExportService, ProductionService, ProcessProductService, ComercializationService

router = APIRouter()

@router.get("/list/import-product/", response_model=FindImportResult, tags=["Embrapa"])
@inject
def list_import_product(
        find_query: FindImport = Depends(),
        service: ImportProductService = Depends(Provide[Container.import_product_service])
):
    return service.get_list(find_query)


@router.get("/list/export-product/", response_model=FindImportResult, tags=["Embrapa"])
@inject
def list_export_product(
        find_query: FindImport = Depends(),
        service: ExportService = Depends(Provide[Container.export_service])
):
    return service.get_list(find_query)


@router.get("/list/production/", response_model=FindImportResult, tags=["Embrapa"])
@inject
def list_production(
        find_query: FindImport = Depends(),
        service: ProductionService = Depends(Provide[Container.production_service])
):
    return service.get_list(find_query)


@router.get("/list/process-product/", response_model=FindImportResult, tags=["Embrapa"])
@inject
def list_process_product(
        find_query: FindImport = Depends(),
        service: ProcessProductService = Depends(Provide[Container.process_product_service])
):
    return service.get_list(find_query)


@router.get("/list/comercialization/", response_model=FindImportResult, tags=["Embrapa"])
@inject
def list_comercialization(
        find_query: FindImport = Depends(),
        service: ComercializationService = Depends(Provide[Container.comercialization_service])
):
    return service.get_list(find_query)



