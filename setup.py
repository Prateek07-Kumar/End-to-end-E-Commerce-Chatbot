from setuptools import find_packages, setup

setup(
    name="ecommchatbot",
    version="0.0.1",
    author="prateek",
    author_email="prateekchaurasia791@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)