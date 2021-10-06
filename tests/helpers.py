class MockDb:
    def __init__(self, data):
        self.data = data

    def connect(self):
        return MockConnection(self.data)


class MockConnection:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def execute(self, *args):
        return MockTransaction(self.data)

class MockTransaction:
    def __init__(self, data):
        self.data = data

    def fetchall(self):
        return self.data
