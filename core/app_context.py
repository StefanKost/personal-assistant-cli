from services.contacts_service import ContactsService
from services.notes_service import NotesService


class AppContext:
    def __init__(self, contacts_service: ContactsService, notes_service: NotesService):
        self.contacts = contacts_service
        self.notes = notes_service
