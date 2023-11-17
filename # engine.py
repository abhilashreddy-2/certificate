# engine.py

class Engine:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def is_running(self):
        return self.running
