<h1 align="center">Multi Python Logger</h1>
<p align="center"><i>The Multi Python Logger is a versatile logging utility designed to simplify and enhance the logging process in Python applications. It supports logging to local files and integrates seamlessly with AWS CloudWatch, providing a unified interface for all your logging needs. Whether you're developing a small script or a large-scale application, this logger ensures your logs are easily accessible and well-organized..</i></p>
<div align="center">
  <a href="https://github.com/NajiAboo/multi_python_logger/stargazers"><img src="https://img.shields.io/github/stars/NajiAboo/multi_python_logger" alt="Stars Badge"/></a>
<a href="https://github.com/NajiAboo/multi_python_logger/network/members"><img src="https://img.shields.io/github/forks/NajiAboo/multi_python_logger" alt="Forks Badge"/></a>
<a href="https://github.com/NajiAboo/multi_python_logger/pulls"><img src="https://img.shields.io/github/issues-pr/NajiAboo/multi_python_logger" alt="Pull Requests Badge"/></a>
<a href="https://github.com/NajiAboo/multi_python_logger/issues"><img src="https://img.shields.io/github/issues/NajiAboo/multi_python_logger" alt="Issues Badge"/></a>
<a href="https://github.com/NajiAboo/multi_python_logger/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/NajiAboo/multi_python_logger?color=2b9348"></a>
<a href="https://github.com/NajiAboo/multi_python_logger/blob/master/LICENSE"><img src="https://img.shields.io/github/license/NajiAboo/multi_python_logger?color=2b9348" alt="License Badge"/></a>
</div>

## Installation

### Install with pip

Install `multi_python_logger`:

```
pip install multi_python_logger
```

### Sample code

```
from multi_python_logger import logger
logger.log("info", msg="This is the sample message", module_name="app",error_code="1001" )
```

## Logger Options

### Local File Logging
  Automatically logs messages to a local file for easy access and review.
  To set the file logger set the environment variable 
  ```
  LOGGING_TYPE = "file"
  ```

### AWS CloudWatch Logging
  Send your logs directly to AWS CloudWatch, enabling centralized log management and monitoring.

  To set the Cloudwatch logging set the following environement variables

  ```
  LOGGING_TYPE = "cloudwatch"

  CLOUDWATCH_LOG_GROUP = ""

  CLOUDWATCH_STREAM_NAME = ""

  AWS_REGION = ""

  AWS_ACCESS_KEY = ""

  AWS_SECRET_KEY = ""
  ```


### MongoDb Logging
  Send your logs directly to MongoDB, enabling centralized log management and monitoring.

  To set the MongoDB logging set the following environement variables

  ```
  LOGGING_TYPE = "mongodb"

  MONGODB_URI = "" #default set as "mongodb://localhost:27018"

  MONGODB_DB = "" #default set as logs

  MONGODB_COLLECTION = "" #log_entries

  
  ```