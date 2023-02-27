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
#Set env variables. These are injected in env from azure pipeline
REPO_NAME = os.getenv('REPO_NAME')
BRANCH_NAME = os.getenv('BRANCH_NAME')
USER_EMAIL = os.getenv('USER_EMAIL')
REPO_URI = os.getenv('REPO_URI')
payload={}

payload_run_workflow = json.dumps({
  "job_id": 507332960731543,
  
})
response_run = requests.request("POST", run_workflow, headers=headers, data=payload_run_workflow)
if response_run.status_code == 200:
  print("triggerd workflow")
else:
  print("Trigger failed")
  exit(1)
