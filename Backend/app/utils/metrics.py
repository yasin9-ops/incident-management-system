import time

signal_count = 0
start_time = time.time()

def increment():
    global signal_count
    signal_count += 1

def get_rate():
    elapsed = time.time() - start_time
    if elapsed == 0:
        return 0
    return signal_count / elapsed