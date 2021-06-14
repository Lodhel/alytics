import time

from test_pr.celery import app


@app.task(bind=True)
def create_task(self, instance):
    time.sleep(1)
    instance.create_graphic()
