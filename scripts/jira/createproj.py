#!/usr/bin/env python

import sys
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Creates JIRA Project based on inputs ')
parser.add_argument('--key', '-k',  help='Jira project key')
parser.add_argument('--lead', '-l',  help='Jira Project lead')
parser.add_argument('--name', '-n',  help='Jira project key')
parser.add_argument('--type', '-t', choices=['scrum','kanban','basic'], help='Type of Project')

args = parser.parse_args()

# Select the Project id based on the type selection
projecttype = {
     'scrum' : 10700,
     'basic' : 10701,
     'kanban' : 10702
}
projectid = str(projecttype[args.type])
print(projectid)

# defining the api-endpoint
API_URL = "https://dot-jira-d.lilly.com/rest/project-templates/1.0/createshared/"
API_ENDPOINT = API_URL + projectid

headers = {
    'Content-Type': 'application/json',
}

data1 = {
    'key': 'NEWK145',
    'lead': 'c261779',
    'name': 'NEWPROJAM145'
}

response = requests.post(url=API_ENDPOINT, headers=headers, auth=('pkalaiadmin', 'xx'), data=json.dumps(data1))

if response.status_code == 400:
    print ("JIRA Project already exists")
    sys.exit(1)
if response.status_code == 200:
    print ("JIRA Project created Successfully")
    sys.exit(0)
