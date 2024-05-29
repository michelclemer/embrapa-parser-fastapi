from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger



class SchedulerManager:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def add_task(self, func, trigger, **kwargs):
        """ Adiciona uma nova tarefa ao agendador.

        Args:
            func (callable): A função a ser agendada.
            trigger (CronTrigger): O gatilho do cron para agendar a tarefa.
            **kwargs: Argumentos adicionais para a função.
        """
        self.scheduler.add_job(func, trigger, **kwargs)

    def remove_task(self, job_id):
        """ Remove uma tarefa do agendador.

        Args:
            job_id (str): O ID da tarefa a ser removida.
        """
        self.scheduler.remove_job(job_id)

    def shutdown(self):
        """ Desliga o agendador de tarefas. """
        self.scheduler.shutdown()