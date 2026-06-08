from pydantic import BaseModel

class SwipeModel(BaseModel):
    terminal_id: str
    card_number: str
    amount: float