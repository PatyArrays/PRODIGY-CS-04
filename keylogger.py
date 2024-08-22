import os

# File where the key logs will be stored
log_file = "key_log.txt"


# Function to write key press to the log file
def log_key(key):
    with open(log_file, "a") as f:
        # Special handling for certain keys
        if key == 'space':
            f.write(' ')
        elif key == 'enter':
            f.write('\n')
        elif key == 'tab':
            f.write('\t')
        else:
            f.write(key)


# Function to capture key press events
def capture_keys():
    print("Press 'esc' to stop logging...")
    while True:
        # Get a single character input
        key = os.read(0, 3).decode('utf-8')

        # Stop logging if 'esc' is pressed (ASCII value is 27)
        if key == '\x1b':
            print("Logging stopped.")
            break

        log_key(key)


# Start capturing key presses
capture_keys()
