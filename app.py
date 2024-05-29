from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from apscheduler.triggers.cron import CronTrigger
from src.api.api import router
from src.infra.settings import settings
from src.infra.container import Container
from src.utils.class_object import singleton
from src.services.schedule_task_service import TaskServices
from src.schedules.embrapa_schedule import SchedulerManager

@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=settings.PROJECT_NAME,
            openapi_url=f"{settings.API_V1_STR}/openapi.json",
            version="0.0.1",
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()
        # self.db.create_database()

        # set cors
        if settings.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(router, prefix=settings.API_V1_STR)


@router.on_event("startup")
def create_app():
    scheduler_manager = SchedulerManager()
    scheduler_manager.add_task(
        func=TaskServices.example_task,
        trigger=CronTrigger(second='*/10')  # Executa a tarefa a cada 10 segundos
    )

app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container
