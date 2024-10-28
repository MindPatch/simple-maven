import requests
import json
import sys

# Configuration variables
sonarqube_url = "http://localhost:9000"  # Replace with your SonarQube URL
project_key = "test-1"                        # Replace with your SonarQube project key
sonarqube_token = "sqp_9e2f0c0b899d4ff07ed6400b05bfb5aa91d66ab6"                # Replace with your SonarQube authentication token
sarif_file_path = sys.argv[1]     # Replace with the path to your SARIF report file

# API Endpoint for submitting SARIF report
api_url = f"{sonarqube_url}/api/ce/submit?projectKey={project_key}"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {sonarqube_token}"
}

# Open the SARIF report file in binary mode and send it as 'multipart/form-data'
with open(sarif_file_path, "rb") as file:
    files = {
        "report": ("report.sarif", file, "application/json")  # Send as a named file with the correct content type
    }

    try:
        response = requests.post(api_url, headers=headers, files=files)

        # Check if submission was successful
        if response.status_code == 200:
            print("SARIF report submitted successfully.")
        else:
            print(f"Failed to submit SARIF report. Status code: {response.status_code}")
            print("Response:", response.text)

    except Exception as e:
        print("An error occurred:", str(e))
