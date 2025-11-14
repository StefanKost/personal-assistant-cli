from models.values import Field


class Name(Field):
    def __init__(self, value: str):
        Name.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value: str):
        if not value:
            raise ValueError("Name should not be empty")

        if not all(char.isalpha() or char == ' ' for char in value):
            raise ValueError("Name can contain only letters and spaces")

        if "  " in value or value.startswith(" ") or value.endswith(" "):
            raise ValueError("Incorrect usage of spaces in name")
