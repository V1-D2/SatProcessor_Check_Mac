import sys
import traceback
import pathlib

def log_error():
    if getattr(sys, 'frozen', False):
        log_file = pathlib.Path.home() / "SatelliteProcessor_error.log"
        with open(log_file, 'w') as f:
            f.write(traceback.format_exc())