import typer
from maruhbackgen.generator import generate_backend

app = typer.Typer()

@app.command()
def generate(schema: str, db: str, api: str, auth: bool = False, microservices: bool = False):
    generate_backend(schema, db, api, auth, microservices)

if __name__ == "__main__":
    app()
