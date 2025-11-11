from models.values import Field
from validators.phone_validator import PhoneValidator


class Phone(Field):
    def __init__(self, phone: str):

        # TODO: Use validation + normalizer here
        if not PhoneValidator.validate(phone):
            raise ValueError('Invalid phone number')
        super().__init__(phone)
