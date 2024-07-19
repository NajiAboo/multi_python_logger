import boto3
import watchtower
import concurrent.futures
from threading import Thread
import queue
from src.base_logger import BaseLogger


class CloudWatchLogger(BaseLogger):
    def create_handler(self):

        session = boto3.Session(
            region_name=self.config["aws_region"],
            aws_access_key_id=self.config["aws_access_key"],
            aws_secret_access_key=self.config["aws_secret_key"],
        )

        cloudwatch_client = session.client("logs")

        return AsyncCloudWatchHandler(
            log_group=self.config["cloudwatch_log_group"],
            stream_name=self.config["cloudwatch_stream_name"],
            boto3_client=cloudwatch_client,
            create_log_group=True,
            max_batch_size=1048576,  # Maximum batch size in bytes
            max_batch_count=10000,  # Maximum number of log events per batch
            send_interval=60,  # Interval in seconds to send logs
        )

class AsyncCloudWatchHandler(watchtower.CloudWatchLogHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_queue = queue.Queue()
        self.worker_thread = Thread(target=self._process_queue)
        self.worker_thread.daemon = True
        self.worker_thread.start()

    def emit(self, record):
        self.log_queue.put(record)

    def _process_queue(self):
        while True:
            record = self.log_queue.get()
            if record is None:
                break
            super().emit(record)
            self.log_queue.task_done()

    def close(self):
        self.log_queue.put(None)
        self.worker_thread.join()
        super().close()