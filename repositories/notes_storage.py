from typing import Protocol
from models.note import Note


class NotesStorage(Protocol):
    def load(self) -> list[Note]:
        ...

    def save(self, notes: list[Note]) -> None:
        ...
