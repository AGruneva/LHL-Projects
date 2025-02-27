import re
from collections import Counter
from datetime import datetime

# Get the current day of the week (e.g., "Monday", "Thursday").
current_day = datetime.now().strftime("%A") 

# Set the threshold based on the day of the week:
THRESHOLD = 50 if current_day == "Thursday" else 10

# Initialize variables:
status_count = 0  # To count the number of 404 occurrences.
ip_addresses = []  # To store IP addresses associated with 404 errors.

# Path to the input log file.
LOG_FILE = r"Z:\windows\404_errors.log"

# Path to the output file where results will be saved.
OUTPUT_FILE = r"Z:\windows\404_results.txt"

# Open the log file in read mode.
with open(LOG_FILE, "r") as logFile:
    for line in logFile:  # Iterate through each line in the log file.
        # Use a regular expression to find lines containing:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+).*\s(404)\s', line)
        if match:
            ip = match.group(1)  # Extract the IP address.
            status_count += 1  # Increment the 404 error count.
            ip_addresses.append(ip)  # Add the IP address to the list.

# Count the occurrences of each IP address using Counter.
ip_counts = Counter(ip_addresses)
sorted_ips = sorted(ip_counts, key=ip_counts.get, reverse=True)

# Write the results to the output file.
with open(OUTPUT_FILE, "w") as outFile:
    outFile.write(f"Threshold for {current_day}: {THRESHOLD}\n")
    outFile.write(f"Number of occurrences of '404': {status_count}\n\n")
    outFile.write("Sorted IP addresses (most common to least):\n")
    for ip in sorted_ips:
        outFile.write(f"{ip}: {ip_counts[ip]}\n")
    outFile.write("\n")

    # Check if the total number of 404 errors exceeds the threshold.
    if status_count > THRESHOLD:
        outFile.write("ALERT: Unusual number of 404 errors detected!\n")
    else:
        outFile.write("No alert triggered.\n")

# Notify the user that the results have been saved.
print(f"Results have been saved to {OUTPUT_FILE}")