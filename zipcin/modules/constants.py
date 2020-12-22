from typing import Literal

DC_OUT = Literal[
    "circlename",
    "regionname",
    "divisionname",
    "officename",
    "pincode",
    "officetype",
    "delivery",
    "district",
    "statename",
]
EN_OUT = Literal["officename", "pincode"]
MODE = Literal[str, int]
