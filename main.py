from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from utilities import get_nearest_five_min_interval 

class MeasurementType(Enum):
    SPO2 = 1
    HR = 2
    TEMP = 3

@dataclass
class Measurement:
    measurement_time: datetime
    measurement_type: MeasurementType
    value: float

def sample_measurements(
    unsampled_measurements: list[Measurement],
) -> list[Measurement]:
    
    if not unsampled_measurements:
        return []

    sorted_measurements = sorted(unsampled_measurements, key = lambda x: x.measurement_time, reverse = True)
    sampled_measurements = {}

    latest_measurement_time = sorted_measurements[0].measurement_time
    first_measurement_time = sorted_measurements[-1].measurement_time
    current_interval = get_nearest_five_min_interval(latest_measurement_time)
    first_interval = get_nearest_five_min_interval(first_measurement_time)

    while current_interval >= first_interval:
        if current_interval not in sampled_measurements:
            sampled_measurements[current_interval] = {}

        for measurement in sorted_measurements:
            measurement_time = measurement.measurement_time
            measurement_type = measurement.measurement_type

            if measurement_time > current_interval:
                continue
            
            if measurement_time < current_interval - timedelta(minutes = 5):
                continue
            
            if measurement_type in sampled_measurements[current_interval]:
                continue
            
            sampled_measurements[current_interval][measurement_type] = measurement
            
        current_interval -= timedelta(minutes = 5)

    categorized_measurements = {}

    for interval in sampled_measurements:
        for measurement_type in sampled_measurements[interval]:
            if measurement_type not in categorized_measurements:
                categorized_measurements[measurement_type] = []

            measurement_value = sampled_measurements[interval][measurement_type].value
            measurement = Measurement(interval, measurement_type, measurement_value)
            categorized_measurements[measurement_type].insert(0, measurement)

    result = [measurement for measurement_type in categorized_measurements for measurement in categorized_measurements[measurement_type]]

    return result
