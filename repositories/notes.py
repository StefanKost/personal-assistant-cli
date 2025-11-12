from typing import Optional, Iterable
from models.note import Note, Title, Tag
from repositories.notes_storage import NotesStorage


class NotesRepository:
    """Repository for the notes"""
    def __init__(self, storage: NotesStorage) -> None:
        self.storage: NotesStorage = storage
        self.notes: list[Note] = self.storage.load() or []

    def add(self, note: Note) -> None:
        """Add a note to the repository"""
        ...

    def get(self, title: Title) -> Optional[Note]:
        """Get a note from the repository"""
        ...

    def all(self) -> Iterable[Note]:
        """Get all notes from the repository"""
        ...

    def find_by_title(self, title_query: str) -> Iterable[Note]:
        """Search for notes by title"""
        ...

    def find_by_tags(self, *tags: Tag) -> Iterable[Note]:
        """Search for notes by tags"""
        ...

    def delete(self, title: Title) -> None:
        """Delete a note from the repository"""
        ...

    def save(self, note: Note) -> None:
        """Update a note in the repository"""
        ...


