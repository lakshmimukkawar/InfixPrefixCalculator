import os
import multiprocessing
from prometheus_client import multiprocess



def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)


bind = f"0.0.0.0:{os.getenv('APP_PORT', 3000)}"

timeout = 120
graceful_timeout = 120
worker_class = "uvicorn.workers.UvicornWorker"
workers = os.getenv("NUM_WORKERS", multiprocessing.cpu_count() + 1)
