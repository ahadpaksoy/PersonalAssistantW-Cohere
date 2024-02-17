# Description: This file contains the function to extract the duration of a timer from a string.
import re  # We'll bring in regular expressions

def extract_duration(text):
    duration_regex = re.compile(r"((?P<hours>\d+)\s?(hours|hour|h))?(\s?((?P<minutes>\d+)\s?(minutes|min|m)))?")
    match = duration_regex.fullmatch(text) 

    if match:
        hours = int(match.group('hours')) if match.group('hours') else 0
        minutes = int(match.group('minutes')) if match.group('minutes') else 0
        total_minutes = (hours * 60) + minutes
        return total_minutes 
    return None
