import unittest
from mindsdb.integrations.handlers.postgres_handler.postgres_handler import PostgresHandler
from mindsdb.api.mysql.mysql_proxy.libs.constants.response_type import RESPONSE_TYPE


class PostgresHandlerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kwargs = {
            "host": "localhost",
            "port": "5432",
            "user": "mindsdb",
            "password": "mindsdb",
            "database": "postgres"
        }
        cls.handler = PostgresHandler('test_postgres_handler', **cls.kwargs)

    def test_0_check_connection(self):
        assert self.handler.check_connection()

    def test_1_describe_table(self):
        described = self.handler.describe_table("test_mdb")
        assert described['type'] is not RESPONSE_TYPE.ERROR

    def test_2_get_tables(self):
        tables = self.handler.get_tables()
        assert tables['type'] is not RESPONSE_TYPE.ERROR

    def test_3_get_views(self):
        views = self.handler.get_views()
        assert views['type'] is not RESPONSE_TYPE.ERROR

    def test_4_select_query(self):
        query = "SELECT * FROM data.test_mdb WHERE 'id'='1'"
        result = self.handler.query(query)
        assert result['type'] is RESPONSE_TYPE.TABLE

if __name__ == "__main__":
    unittest.main(failfast=True)
