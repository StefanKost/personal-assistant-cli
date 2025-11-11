from models.values import Field, Tag


class Note:

    def __init__(self, text: str):
        if not text or not text.strip():
            raise ValueError("Note cannot be empty")

        self.text = Field(text.strip())
        self.tags: list[Tag] = []

    # TODO: Implement logic to add tags and update text

    def __str__(self) -> str:
        # TODO: Implement not preview
        pass
