import sys
from collections import Counter
from colorama import Fore

# Read the file and return its content as a list of lines.
def load_logs(filepath: str) -> list[dict]:
    logs = []

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            # Do not include empty string.
            if not line.strip():
                continue

            log = parse_log_line(line.strip())

            if log is not None:
                logs.append(log)

    return logs


# Parse log line and create a dictionary with its date,
# time, level and message.
def parse_log_line(line: str) -> dict | None:
    line_parts = line.split(maxsplit=3)

    if len(line_parts) != 4:
        print(f'{Fore.YELLOW}Warning: Missing or empty required fields in row "{line}".')
        return None

    date, time, level, message = line_parts

    return {
        'date': date,
        'time': time,
        'level': level,
        'message': message
    }

# Return all logs matching the specified level.
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

# Count the number of logs for each level.
def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log['level'] for log in logs))

# Display the number of logs for each level.
def display_log_counts(counts: dict) -> None:
    print('Logging level    | Count')
    print('-----------------|------')

    for level in ('INFO', 'DEBUG', 'ERROR', 'WARNING'):
        color = Fore.RED if level == 'ERROR' else ''
        print(f'{color}{level:<7}{Fore.RESET} | {counts.get(level, 0)}')

def main() -> None:
    # Check whether path to the log file is given.
    if len(sys.argv) <= 1:
        print('Please add a path to the log file: python main.py <directory_path>')
        return

    filepath = sys.argv[1]

    # Validate the level of the log lines to display.
    level = sys.argv[2].upper() if len(sys.argv) == 3 else None
    if level and level not in ('INFO', 'DEBUG', 'ERROR', 'WARNING'):
        print(f'{Fore.RED}Error: Invalid log level {level}')
        return

    try:
        logs = load_logs(filepath)
    except FileNotFoundError:
        print(f'{Fore.RED}The file "{filepath}" does not exist.')
        return
    except IsADirectoryError:
        print(f'{Fore.RED}The file "{filepath}" is not a file.')
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nLog details for level '{level}':")

        for log in filtered_logs:
            print(
                f"{log['date']} {log['time']} - {log['message']}"
            )
    

if __name__ == "__main__":
    main()
