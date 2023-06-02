from setuptools import setup, find_packages

setup(
    name="prosa-demo",
    version="0.1.0",
    description="Paquete que incluye una aplicación Flask.",
    packages=find_packages(),
    package_data={'readme':['README.md']}
)
