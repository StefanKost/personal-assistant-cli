class BaseStorage:
    def load(self):
        raise NotImplementedError

    def save(self, data):
        raise NotImplementedError
