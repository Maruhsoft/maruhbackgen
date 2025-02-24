import os
from maruhbackgen.parser import parse_sql_schema
from maruhbackgen.utils import create_fastapi_project, create_graphql_project

def generate_backend(schema_path: str, db: str, api: str, auth: bool, microservices: bool):
    with open(schema_path, "r") as f:
        sql_schema = f.read()

    parsed_schema = parse_sql_schema(sql_schema)

    project_path = os.path.join(os.getcwd(), "generated_api")

    if api == "rest":
        create_fastapi_project(parsed_schema, project_path, db, auth, microservices)
    else:
        create_graphql_project(parsed_schema, project_path, db, auth, microservices)

    print(f"✅ API Generated in `{project_path}/`")
