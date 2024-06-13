from datetime import timedelta
from collections import defaultdict
from data_types import Measurement
from utilities import get_nearest_five_min_interval

def sample_measurements(unsampled_measurements: list[Measurement]) -> list[Measurement]:
    if not unsampled_measurements:
        return []

    # Create a sorted copy of unsampled_measurements by measurement_time in descending order
    sorted_measurements = sorted(unsampled_measurements, key=lambda x: x.measurement_time, reverse=True)

    # Initialize data structures
    sampled_measurements = defaultdict(dict)
    categorized_measurements = defaultdict(list)

    # Determine boundaries for processing
    latest_measurement_time = sorted_measurements[0].measurement_time
    first_measurement_time = sorted_measurements[-1].measurement_time
    current_interval = get_nearest_five_min_interval(latest_measurement_time)
    first_interval = get_nearest_five_min_interval(first_measurement_time)

    # Iterate over intervals
    while current_interval >= first_interval:
        if current_interval not in sampled_measurements:
            sampled_measurements[current_interval] = {}

        for measurement in sorted_measurements:
            if measurement.measurement_time > current_interval:
                continue
            if measurement.measurement_time < current_interval - timedelta(minutes=5):
                continue
            if measurement.measurement_type in sampled_measurements[current_interval]:
                continue
            sampled_measurements[current_interval][measurement.measurement_type] = measurement

        current_interval -= timedelta(minutes=5)

    # Organize measurements by type and interval
    for interval, measurements_by_type in sampled_measurements.items():
        for measurement_type, measurement in measurements_by_type.items():
            categorized_measurements[measurement_type].insert(0, Measurement(interval, measurement_type, measurement.value))

    # Flatten categorized_measurements into a list of Measurement objects
    result = [measurement for measurement_list in categorized_measurements.values() for measurement in measurement_list]

    return result
