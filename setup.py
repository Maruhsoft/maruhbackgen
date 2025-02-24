from setuptools import setup, find_packages

setup(
    name="maruhbackgen",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "sqlparse",
        "cookiecutter",
        "fastapi",
        "uvicorn",
        "pydantic",
        "motor",
    ],
    entry_points={
        "console_scripts": [
            "maruhbackgen = maruhbackgen.cli:app",
        ],
    },
)
