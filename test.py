import json
import sys
import uuid

def parse_sarif(sarif_data):
    """
    Parse SARIF data and convert it to SonarQube JSON format.
    """
    # Initialize a dictionary to hold SonarQube format data
    sonar_data = {
        "issues": []
    }

    # Iterate over runs in SARIF
    for run in sarif_data.get("runs", []):
        tool = run.get("tool", {}).get("driver", {}).get("name", "unknown tool")
        
        # Iterate over results
        for result in run.get("results", []):
            issue = {
                "engineId": tool,
                "ruleId": result.get("ruleId", ""),
                "severity": result.get("level", "INFO").upper(),
                "type": "VULNERABILITY",
                "primaryLocation": {
                    "message": result.get("message", {}).get("text", ""),
                    "filePath": result.get("locations", [{}])[0].get("physicalLocation", {}).get("artifactLocation", {}).get("uri", ""),
                    "textRange": {
                        "startLine": result.get("locations", [{}])[0].get("physicalLocation", {}).get("region", {}).get("startLine", 1)
                    }
                }
            }
            sonar_data["issues"].append(issue)

    return sonar_data

def convert_sarif_to_sonarjson(sarif_file, sonarjson_file):
    """
    Convert SARIF to SonarQube JSON and write to file.
    """
    # Load SARIF data
    with open(sarif_file, 'r') as file:
        sarif_data = json.load(file)
    
    # Parse SARIF and convert to SonarQube JSON format
    sonar_data = parse_sarif(sarif_data)
    
    # Write SonarQube JSON to output file
    with open(sonarjson_file, 'w') as file:
        json.dump(sonar_data, file, indent=4)
    print(f"Converted SARIF report saved to {sonarjson_file}")

convert_sarif_to_sonarjson(sys.argv[1],sys.argv[2])


