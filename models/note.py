from typing import Self
from datetime import datetime as DateTime
from models.values import Field, Tag, Title


class Note:
    def __init__(self, title: str, body: str = "", tags: set[Tag] = {}):
        self.title: Title = Title(title.strip())
        self.body: Field = Field(body.strip())
        self.tags: set[Tag] = tags
        self.created_at: DateTime = DateTime.now()
        self.updated_at: DateTime = None

    def __str__(self) -> str:
        return (
            f"Title: {self.title}\n"
            f"Body: {self.body}\n"
            f"Tags: {', '.join(self.tags)}\n"
            f"Created at: {self.created_at}\n"
            f"Updated at: {self.updated_at}"
        )

    def edit_title(self, new_title: str) -> Self:
        """Edit the title of the note"""
        self.title = Title(new_title.strip())
        self.updated_at = DateTime.now()

        return self

    def edit_body(self, new_body: str) -> Self:
        """Edit the body of the note"""
        self.body = Title(new_body)
        self.updated_at = DateTime.now()

        return self

    def add_tags(self, *tags: Tag) -> Self:
        """Add tags to the note"""
        updated = False

        for tag in tags:
            if tag in self.tags:
                continue  # to track if it's required to updated_at

            updated = True
            self.tags.add(Tag(tag))

        if updated:
            self.updated_at = DateTime.now()

        return self

    def remove_tags(self, *tags: Tag) -> Self:
        """Remove tags from the note"""
        updated = False

        for tag in tags:
            if tag not in self.tags:
                continue  # to track if it's required to updated_at

            updated = True
            self.tags.remove(tag)

        if updated:
            self.updated_at = DateTime.now()

        return self
