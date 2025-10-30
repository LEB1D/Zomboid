from dataclasses import dataclass


@dataclass
class Item:
    id: int
    name: str
    type: str
    condition: str
    amount: int = 0

    def __post_init__(self):
        self.id = int(self.id)
        self.amount = int(self.amount) if self.amount else 0
