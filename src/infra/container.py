
from dependency_injector import containers, providers
from .db import Database
from .settings import settings
from src.crud.repository import *
from src.services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=['src.api.routers.embrapa']
    )

    db = providers.Singleton(Database, db_url=str(settings.SQLALCHEMY_DATABASE_URI))

    import_product_repository = providers.Factory(
        ImportProductRepository, session_factory=db.provided.session
    )

    production_repository = providers.Factory(
        ProductionRepository, session_factory=db.provided.session
    )

    export_repository = providers.Factory(
        ExportRepository, session_factory=db.provided.session
    )

    comercialization_repository = providers.Factory(
        ComercializationRepository, session_factory=db.provided.session
    )

    process_product_repository = providers.Factory(
        ProcessProductRepository, session_factory=db.provided.session
    )

    import_product_service = providers.Factory(
        ImportProductService, repository=import_product_repository
    )
    production_service = providers.Factory(
        ProductionService, production_repository=production_repository
    )
    export_service = providers.Factory(
        ExportService, export_repository=export_repository
    )
    comercialization_service = providers.Factory(
        ComercializationService, comercialization_repository=comercialization_repository
    )
    process_product_service = providers.Factory(
        ProcessProductService, process_product_repository=process_product_repository
    )
