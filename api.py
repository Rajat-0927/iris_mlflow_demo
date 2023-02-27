import requests
import json
import os

#Set TOKEN
TOKEN = 'Bearer ' + os.getenv('DATABRICKS_TOKEN')
DATABRICKS_HOST = os.getenv('DATABRICKS_HOST')
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': TOKEN
}
run_workflow = DATABRICKS_HOST 
print(DATABRICKS_HOST)
payload_run_workflow = json.dumps({
  "job_id": 507332960731543,
  
})
response_run = requests.request("POST",run_workflow, headers=headers, data=payload_run_workflow)
if response_run.status_code == 200:
  print("triggerd workflow")
else:
  print("Trigger failed")
  exit(1)
