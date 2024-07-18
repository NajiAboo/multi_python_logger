import boto3
import watchtower

from src.loggers.base_logger import BaseLogger


class CloudWatchLogger(BaseLogger):
    def create_handler(self):

        session = boto3.Session(
            region_name=self.config["aws_region"],
            aws_access_key_id=self.config["aws_access_key"],
            aws_secret_access_key=self.config["aws_secret_key"],
        )

        cloudwatch_client = session.client("logs")

        return watchtower.CloudWatchLogHandler(
            log_group=self.config["cloudwatch_log_group"],
            stream_name=self.config["cloudwatch_stream_name"],
            boto3_client=cloudwatch_client,
            create_log_group=True,
            max_batch_size=1048576,  # Maximum batch size in bytes
            max_batch_count=10000,  # Maximum number of log events per batch
            send_interval=30,  # Interval in seconds to send logs
        )
