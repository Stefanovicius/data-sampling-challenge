from datetime import datetime, timedelta

def get_nearest_five_min_interval(dt: datetime) -> datetime:
    # Calculate the number of seconds from the start of the hour
    seconds_past_hour = dt.minute * 60 + dt.second + dt.microsecond / 1e6
    # Calculate the number of seconds to the next 5-minute interval
    seconds_to_next_five_minute = (5 * 60) - (seconds_past_hour % (5 * 60))
    if seconds_to_next_five_minute == 5 * 60:
        seconds_to_next_five_minute = 0
    # Round up to the nearest 5-minute interval
    new_dt = dt + timedelta(seconds=seconds_to_next_five_minute)
    # Set seconds and microseconds to zero
    return new_dt.replace(second=0, microsecond=0)
