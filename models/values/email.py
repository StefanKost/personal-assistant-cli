from models.values import Field


class Email(Field):

    def __init__(self, value: str):
        # TODO: call email validation
        super().__init__(value)
