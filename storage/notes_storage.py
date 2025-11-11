from storage.base_storage import BaseStorage


class NotesStorage(BaseStorage):
    def __init__(self, path="storage/notes.pkl"):
        self.path = path

    def load(self):
        # TODO: implement pickle load
        pass

    def save(self, data):
        # TODO: implement pickle save
        pass
