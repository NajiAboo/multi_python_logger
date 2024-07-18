from setuptools import setup, find_packages

setup(
    name="multi_python_logger",
    version="1.2",
    packages=find_packages(),
    # Metadata
    author="Mohamed Naji Aboo",
    author_email="aboonaji@gmail.com",
    description="Application to provide different logging mechanisms",
    keywords="python logger cloud_logger, aws_cloudwatch_logger",
    url="",
    install_requires= ["watchtower", "boto3", "python-dotenv"],
)
