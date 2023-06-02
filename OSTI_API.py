import requests
import json
import time 

# pulling data from public API
base_url = "https://www.osti.gov/api/v1/records"
report_data = []  # List to store report data

# read report numbers from a text file
with open("report_numbers.txt", "r") as file:
    report_numbers = file.read().splitlines()

# iterating through report numbers
for report_number in report_numbers:
    param_url = f"{base_url}?identifier={report_number}"
    response = requests.get(param_url)

    if response.status_code == 200:
        # Process the response
        data = response.json()
        report_data.append(data)  # Append report data to the list

        print(f"Data fetched for report number {report_number}")

    else:
        print(f"Failed to fetch data for report number: {report_number}")
        
    # Optional delay between requests (to avoid overwhelming the API)
    time.sleep(1)

# Export all reports to a single JSON file
with open("all_reports.json", "w") as json_file:
    json.dump(report_data, json_file)

print("All reports exported to all_reports.json")