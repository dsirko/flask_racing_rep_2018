from utils import read_text_file, split_data, sort_data, calculate_time_differences, format_timedelta, build_report, \
    print_report


def process_logs():
    # Process start log
    start_log = sort_data(split_data(read_text_file("log/start.log.txt")), key=lambda x: x[0])

    # Process end log
    end_log = sort_data(split_data(read_text_file("log/end.log.txt")), key=lambda x: x[0])

    # Process abbreviations
    abbreviations = sort_data(split_data(read_text_file("log/abbreviations.txt")), key=lambda x: x[0])

    # Calculate time differences
    time_differences = calculate_time_differences(start_log, end_log)

    # Build and print the report
    report = build_report(abbreviations, time_differences)

    return report

    # return report