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

