from setuptools import setup

setup(
    name="prefix_infix_calculator",
    version="0.0.1",
    packages=["prefix_infix_calculator"],
    package_dir={"": "src"},
    install_requires=[
        "fastapi~=0.61.1",
        "gunicorn~=20.0.4",
        "uvicorn~=0.11.8",
        "requests",
        "pytest"
    ],
)
