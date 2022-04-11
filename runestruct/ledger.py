class Ledger:
    ledger = None

    def __init__(self):
        self.ledger = {}

    def keys(self):
        return self.ledger.keys()

    def get(self, key):
        return self.ledger[key]

    def set(self, key, value):
        self.ledger[key] = value