import unittest
from sqlalchemy import text

from app import create_app, db

class ConnectionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_db_connection(self):
        result = db.session.query(text("'Hello world'")).one()
        self.assertEqual(result[0], 'Hello world')

if __name__ == '__main__':
    unittest.main()