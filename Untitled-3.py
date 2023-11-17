# tests/test_engine.py

import unittest
from engine import Engine

class TestEngine(unittest.TestCase):
    def test_start(self):
        engine = Engine()
        engine.start()
        self.assertTrue(engine.is_running())

    def test_stop(self):
        engine = Engine()
        engine.start()
        engine.stop()
        self.assertFalse(engine.is_running())
