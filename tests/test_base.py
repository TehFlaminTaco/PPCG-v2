import unittest

from app.instances.db import db
from app.start import server


class TestBase:
    class TestFlask(unittest.TestCase):
        def setUp(self):
            super().setUp()
            self.app = server.test_client()
            self.app.testing = True

    class TestDB(unittest.TestCase):
        def setUp(self):
            super().setUp()
            self.session = db.session
            self.session.begin_nested()

        def tearDown(self):
            self.session.rollback()
