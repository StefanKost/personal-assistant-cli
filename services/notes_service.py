from repositories.notes import NotesRepository


class NotesService:
    def __init__(self, repo: NotesRepository):
        self.repo = repo

    def add_note(self, record):
        self.repo.add(record)

    # TODO: implement other methods
