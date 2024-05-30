from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from src.api.api import router
from src.infra.settings import settings
from src.infra.container import Container
from src.services.schedule_task_service import insert_data
from src.utils.class_object import singleton

@singleton
class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title=settings.PROJECT_NAME,
            openapi_url=f"{settings.API_V1_STR}/openapi.json",
            version="0.0.1",
        )

        self.container = Container()
        self.db = self.container.db()

        if settings.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        @self.app.get("/")
        def root():
            return "Service is working."

        self.app.include_router(router, prefix=settings.API_V1_STR)

        # Inicializa o scheduler no evento de startup
        self.scheduler_manager = None
        self.app.on_event("startup")(self.start_scheduler)
        self.app.on_event("shutdown")(self.shutdown_scheduler)

    async def start_scheduler(self):
        self.scheduler_manager = BackgroundScheduler(timezone='America/Sao_Paulo')
        self.scheduler_manager.add_job(
            func=insert_data.insert_all,
            trigger=CronTrigger(month='*', hour=17, minute=12)  # Corrige o cronograma para executar diariamente às 17:10
        )
        self.scheduler_manager.start()

    async def shutdown_scheduler(self):
        if self.scheduler_manager:
            self.scheduler_manager.shutdown()

app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container
