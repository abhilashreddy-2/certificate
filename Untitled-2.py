# tests/test_battery.py

import unittest
from battery import Battery

class TestBattery(unittest.TestCase):
    def test_charge(self):
        battery = Battery()
        battery.charge(50)
        self.assertEqual(battery.get_charge(), 50)

    def test_discharge(self):
        battery = Battery()
        battery.charge(75)
        battery.discharge(25)
        self.assertEqual(battery.get_charge(), 50)
