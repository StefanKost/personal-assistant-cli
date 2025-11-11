from models.values import Field


class Tag(Field):
    def __init__(self, tag: str):
        # TODO: Use validation + normalizer here
        super().__init__(tag)
