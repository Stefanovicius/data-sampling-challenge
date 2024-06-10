from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum

class MeasType(Enum):
    SPO2 = 1
    HR = 2
    TEMP = 3

@dataclass
class Measurement:
    measurementTime: datetime = datetime.min
    measurementType: MeasType = MeasType.SPO2
    value: float = 0.0

def sample_measurements(
    startOfSampling: datetime,
    unsampledMeasurements: list[Measurement]
) -> dict[MeasType, list[Measurement]]:
    # your implementation here
    return {MeasType.SPO2: [Measurement(datetime.min, MeasType.SPO2, 0.0)]}
