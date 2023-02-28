import requests
import json
import os
import sys

#Set TOKEN
# Set TOKEN and DATABRICKS_HOST environment variables
TOKEN = 'Bearer ' + os.getenv('DATABRICKS_TOKEN')
DATABRICKS_HOST = os.getenv('DATABRICKS_HOST')

# Set headers for API requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': TOKEN
}

run_workflow = DATABRICKS_HOST + "/api/2.0/jobs/run-now"
payload_run_workflow = json.dumps({
  "job_id": 507332960731543,

})

response_run = requests.request("POST",run_workflow, headers=headers, data=payload_run_workflow)
print(response_run)

if response_run.status_code == 200:
  print("triggerd workflow")
else:
  print("Trigger failed")
  exit(1)
