from storage.contacts_storage import ContactsStorage
from repositories.contacts import ContactsRepository
from services.contacts_service import ContactsService

from storage.notes_storage import NotesStorage
from repositories.notes import NotesRepository
from services.notes_service import NotesService

from core.app_context import AppContext
from ui.commands import handle_command


def main():
    ctx = AppContext(
        ContactsService(ContactsRepository(ContactsStorage())),
        NotesService(NotesRepository(NotesStorage()))
    )

    while True:
        try:
            user_input = input("Enter a command: ").strip()
            if not user_input:
                continue
            result = handle_command(user_input, ctx)
            if result == "exit":
                break
            if result:
                print(result)
        except KeyboardInterrupt:
            handle_command("exit", ctx)
            break


if __name__ == "__main__":
    main()
