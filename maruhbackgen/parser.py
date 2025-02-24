import sqlparse
import re

def parse_sql_schema(sql_schema: str):
    parsed = sqlparse.parse(sql_schema)
    tables = {}

    for stmt in parsed:
        if stmt.get_type() == "CREATE":
            tokens = [token for token in stmt.tokens if not token.is_whitespace]
            table_name = None
            columns = {}

            for token in tokens:
                if token.value.upper().startswith("CREATE TABLE"):
                    match = re.search(r'CREATE TABLE (\w+)', token.value, re.IGNORECASE)
                    if match:
                        table_name = match.group(1)

                elif "(" in token.value and ")" in token.value:
                    col_defs = token.value.strip("()").split(",")
                    for col_def in col_defs:
                        parts = col_def.strip().split()
                        col_name = parts[0]
                        col_type = parts[1].upper()
                        columns[col_name] = col_type

            if table_name:
                tables[table_name] = columns

    return tables
