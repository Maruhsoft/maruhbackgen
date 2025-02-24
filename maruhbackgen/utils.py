import os
from cookiecutter.main import cookiecutter

def create_fastapi_project(parsed_schema, project_path, db, auth, microservices):
    cookiecutter("fastapi_template", no_input=True, extra_context={"project_slug": "generated_api"})

def create_graphql_project(parsed_schema, project_path, db, auth, microservices):
    cookiecutter("graphql_template", no_input=True, extra_context={"project_slug": "generated_api"})
