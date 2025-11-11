from storage.base_storage import BaseStorage


class ContactsStorage(BaseStorage):
    def __init__(self, path="storage/contacts.pkl"):
        self.path = path

    def load(self):
        # TODO: implement pickle read
        pass

    def save(self, data):
        # TODO: implement pickle write
        pass
