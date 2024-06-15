import os
import unittest
import sqlalchemy as sql

class TestPipeline(unittest.TestCase):

    def test_sqlite_db_exists(self):
        db_path = '../data/data.sqlite'
        self.assertTrue(os.path.exists(db_path), "SQLite database does not exist")

    def test_emissions_table_exists(self):
        engine = sql.create_engine('sqlite:///../data/data.sqlite')
        inspector = sql.inspect(engine)
        self.assertIn('emissions', inspector.get_table_names(), "Emissions table does not exist in the database")

    def test_temperature_table_exists(self):
        engine = sql.create_engine('sqlite:///../data/data.sqlite')
        inspector = sql.inspect(engine)
        self.assertIn('temperature', inspector.get_table_names(), "Temperature table does not exist in the database")

     #check the integer values int temperature column
    def test_temperature_column_integers(self):
        engine = sql.create_engine('sqlite:///../data/data.sqlite')
        with engine.connect() as connection:
            result = connection.execute

if __name__ == '__main__':
    unittest.main()

