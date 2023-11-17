# battery.py

class Battery:
    def __init__(self):
        self.charge = 0

    def charge(self, amount):
        self.charge += amount

    def discharge(self, amount):
        self.charge -= amount

    def get_charge(self):
        return self.charge

