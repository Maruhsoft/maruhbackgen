import unittest
from maruhbackgen.parser import parse_sql_schema

class TestParser(unittest.TestCase):
    def test_parse_sql_schema(self):
        sql = "CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(255));"
        parsed = parse_sql_schema(sql)
        self.assertEqual(parsed["users"]["id"], "SERIAL")
        self.assertEqual(parsed["users"]["name"], "VARCHAR(255)")

if __name__ == "__main__":
    unittest.main()