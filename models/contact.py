from typing import Optional
from models.values import Name, Email, Phone, Address, Birthday


class Contact:
    def __init__(self, name: str):
        self.name = Name(name)
        self.email: Optional[Email] = None
        self.phones: list[Phone] = []
        self.birthday: Optional[Birthday] = None
        self.address: Optional[Address] = None

    # TODO: implemented to add phone, address, phone, email etc...

    def __str__(self) -> str:
        phones_str = "| ".join(p.value for p in self.phones) or "—"
        parts = [f"Contact: {self.name.value}", f"phones: {phones_str}"]

        if self.email:
            parts.append(f"email: {self.email}")
        if self.birthday:
            parts.append(f"birthday: {self.birthday}")
        if self.address:
            parts.append(f"address: {self.address}")

        return ", ".join(parts)
