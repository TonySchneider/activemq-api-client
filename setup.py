from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='activemq-api-client',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Tony Schneider',
    author_email='tonysch05@gmail.com',
    description='A Python client for ActiveMQ REST API',
    license='MIT',
    keywords='activemq api client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/TonySchneider/activemq-api-client',
)
