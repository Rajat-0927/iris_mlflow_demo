import requests
import json
import os
import sys

# Set TOKEN and DATABRICKS_HOST environment variables
TOKEN = 'Bearer ' + os.getenv('DATABRICKS_TOKEN')
DATABRICKS_HOST = os.getenv('DATABRICKS_HOST')

# Set headers for API requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': TOKEN
}

# Define payload for job reset API call
reset_payload = {
  "job_id": 507332960731543
}

# Define payload for job run API call
run_payload = {
  "job_id": 507332960731543
}

# Define API endpoint URLs
reset_url = DATABRICKS_HOST + "/api/2.1/jobs/reset"
run_url = DATABRICKS_HOST + "/api/2.1/jobs/run-now"

# Attempt to reset Databricks job
try:
  reset_response = requests.post(reset_url, headers=headers, json=reset_payload)
  reset_response.raise_for_status() # raise error if status code not in 200-299 range
  print("Databricks job reset successful")
except requests.exceptions.RequestException as e:
  print("Error resetting Databricks job:", e)
  sys.exit(1)

# Attempt to run Databricks job
try:
  run_response = requests.post(run_url, headers=headers, json=run_payload)
  run_response.raise_for_status() # raise error if status code not in 200-299 range
  print("Databricks job run successful")
except requests.exceptions.RequestException as e:
  print("Error running Databricks job:", e)
  sys.exit(1)
