from repositories.contacts import ContactsRepository


class ContactsService:
    def __init__(self, repo: ContactsRepository):
        self.repo = repo

    def add_contact(self, record):
        self.repo.add(record)

    # TODO: implement other methods to deal with contacts service
