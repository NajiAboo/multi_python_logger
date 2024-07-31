import os
from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

cwd = os.getcwd()

setup(
    name="multi_python_logger",
    version="3.0.0",
    packages=find_packages(),
    # Metadata
    author="Mohamed Naji Aboo",
    author_email="aboonaji@gmail.com",
    description="Application to provide different logging mechanisms",
    keywords="python logger cloud_logger, aws_cloudwatch_logger",
    url="",
    install_requires=["watchtower==3.2.0", "boto3==1.34.144","python-dotenv","motor==3.5.1"],
    long_description = long_description,
    long_description_content_type="text/markdown"
)
