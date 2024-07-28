import os
import json
from dotenv import load_dotenv

from .file_logger import FileLogger
from .aws_logger import CloudWatchLogger
from .mongodb_logger import MongoDBLogger

load_dotenv()


def get_logger():
    config_file = os.path.join(os.path.dirname(__file__), "..", "logging_config.json")
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = json.load(f)
    else:
        config = {
            "logging_type": os.getenv("LOGGING_TYPE", "file"),
            "log_file": os.getenv("LOG_FILE", "app.log"),
            "cloudwatch_log_group": os.getenv("CLOUDWATCH_LOG_GROUP", "your-log-group"),
            "cloudwatch_stream_name": os.getenv(
                "CLOUDWATCH_STREAM_NAME", "your-stream-name"
            ),
            "aws_region": os.getenv("AWS_REGION", "us-east-1"),
            "aws_access_key": os.getenv("AWS_ACCESS_KEY", ""),
            "aws_secret_key": os.getenv("AWS_SECRET_KEY", ""),
            "mongodb_uri": os.getenv("MONGODB_URI", "mongodb://localhost:27017"),
            "mongodb_db": os.getenv("MONGODB_DB", "logs"),
            "mongodb_collection": os.getenv("MONGODB_COLLECTION", "log_entries")
        }

    logging_type = config["logging_type"]
    if logging_type == "cloudwatch":
        return CloudWatchLogger(config).get_logger()
    elif logging_type == 'mongodb':
        return MongoDBLogger(config).get_logger()
    else:
        return FileLogger(config).get_logger()


# Singleton pattern to ensure one logger instance
logger_instance = get_logger()
