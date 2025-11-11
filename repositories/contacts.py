from models.contact import Contact


class ContactsRepository:
    def __init__(self, storage):
        self.storage = storage
        self._contacts: list[Contact] = self.storage.load() or []  # should be list

    def add(self, contact: Contact):
        # TODO: add contact
        pass

    def get(self, name):
        # TODO: return contact by name
        pass

    def delete(self, name):
        # TODO: delete contact
        pass

    # TODO: Implement other methods that works with collection

    def all(self):
        return self._contacts

    def save(self):
        self.storage.save(self._contacts)
