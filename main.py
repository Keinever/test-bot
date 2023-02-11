from dataclasses import dataclass
from typing import *

@dataclass
class DbConfig:
    pswd : Optional[int]
    name : Union[str, int]


db = DbConfig(
    pswd=23424234234,
    name="dbBot"
    )
print(db.name)
