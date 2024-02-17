from dataclasses import dataclass

@dataclass
class PriceActions:
    price: float
    price_fluctuation: float
    name: str
    description: str
