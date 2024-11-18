import datetime
import pendulum
from constants import TIME_FORMAT, BEST_RACERS


def read_text_file(file_path):
    """Reads the contents of a text file."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def split_data(text_data):
    """Splits the text data into a list of lists."""
    for line in text_data:
        yield line.split('_')


def sort_data(data, key=lambda x: x[0]):
    """Sorts the data by the first element of each sublist."""
    return sorted(data, key=key)


def calculate_time_differences(start_log, end_log):
    """Calculates the time differences between start and end logs."""
    time_differences = []
    for start, end in zip(start_log, end_log):
        timestamp_start = datetime.datetime.strptime(start[1], TIME_FORMAT)
        timestamp_end = datetime.datetime.strptime(end[1], TIME_FORMAT)
        difference = timestamp_end - timestamp_start
        time_differences.append(difference)
    return time_differences


def format_timedelta(td):
    """Formats a timedelta object to MM:SS.mmm format."""
    duration = pendulum.duration(seconds=td.total_seconds())
    # Extract minutes, seconds, and milliseconds
    minutes = int(duration.minutes)
    seconds = int(duration.seconds) % 60
    milliseconds = int(duration.microseconds / 1000)
    return f"{minutes:02}:{seconds:02}.{milliseconds:03}"


def build_report(sorted_abbreviations, time_differences):
    """Combines the sorted abbreviations with the calculated time differences."""
    report = []
    for abbrev, time_diff in zip(sorted_abbreviations, time_differences):
        abbrev.append(time_diff)
        report.append(abbrev)
    return sorted(report, key=lambda x: x[3])  # Sort by time difference


def print_report(report):
    """Prints the formatted race report."""
    for i, entry in enumerate(report):
        if i == BEST_RACERS:
            print("---------------------------------------------------------")
        formatted_time = format_timedelta(entry[3])
        print(f"{i + 1}. {entry[1]} | {entry[2]} | {formatted_time}")


def find_driver_info(report, driver_id):
    for entry in report:
        if driver_id == entry[0]:
            formatted_time = format_timedelta(entry[3])
            return entry, formatted_time