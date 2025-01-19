import time

def calculate_response_time(start_time):
    """Calculates the elapsed time since the start time."""
    end_time = time.time()
    response_time = end_time - start_time
    return response_time