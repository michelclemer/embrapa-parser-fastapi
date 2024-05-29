from .base import BaseService
from src.crud.repository.embrapa_repository import ImportProductRepository


class ImportProductService(BaseService):
    def __init__(self, repository: ImportProductRepository) -> None:
        super().__init__(repository)


class ProductionService(BaseService):
    def __init__(self, repository) -> None:
        super().__init__(repository)


class ExportService(BaseService):
    def __init__(self, repository) -> None:
        super().__init__(repository)


class ComercializationService(BaseService):
    def __init__(self, repository) -> None:
        super().__init__(repository)


class ProcessProductService(BaseService):
    def __init__(self, repository) -> None:
        super().__init__(repository)
