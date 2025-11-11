from models.note import Note


class NotesRepository:
    def __init__(self, storage):
        self.storage = storage
        self._notes: list[Note] = self.storage.load() or []  # should be list

    def add(self, note):
        pass

    def all(self):
        return self._notes

    def save(self):
        self.storage.save(self._notes)
