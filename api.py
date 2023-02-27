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
payload={}
list_all_jobs_api = DATABRICKS_HOST + "/api/2.1/jobs/list"
response = requests.request("GET", list_all_jobs_api, headers=headers, data=payload)
response=response.json()
job_found=0
job_id="507332960731543"
for job in response['jobs']:
  if job['settings']['name'] == "ModelingAndPrediction":
    job_found = 1
    job_id = job['job_id']
    break;

if job_found == 1:
  payload = {
            "job_id": job_id,
            }
  payload = json.dumps(payload)
  update_job_api = DATABRICKS_HOST + "/api/2.1/jobs/reset"
  response = requests.request("POST", update_job_api, headers=headers, data=payload)
  print(response.text)
  if response.status_code == 200:
    print("flow updated")
  else:
    print("flow update failed")
    exit(1)
else:
  create_new_job_api = DATABRICKS_HOST + "/api/2.1/jobs/create"
run_workflow = DATABRICKS_HOST + "/api/2.1/jobs/run-now"
payload_run_workflow = json.dumps({
  "job_id": 507332960731543,
  
})
response_run = requests.request("POST",run_workflow, headers=headers, data=payload_run_workflow)
if response_run.status_code == 200:
  print("triggerd workflow")
else:
  print("Trigger failed")
  exit(1)
