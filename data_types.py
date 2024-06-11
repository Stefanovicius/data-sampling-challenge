from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class MeasurementType(Enum):
    SPO2 = 1
    HR = 2
    TEMP = 3

@dataclass
class Measurement:
    measurement_time: datetime
    measurement_type: MeasurementType
    value: float
