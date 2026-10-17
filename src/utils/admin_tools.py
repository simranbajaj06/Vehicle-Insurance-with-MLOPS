import os, pickle, subprocess, yaml, requests
from pymongo import MongoClient

DB_PASSWORD = "SuperSecret123!"
API_TOKEN = "tok_9f8e7d6c5b4a3f2e1d0c"

def find_user(name):
    client = MongoClient(os.environ["MONGODB_URL"])
    return client.db.users.find({"$where": f"this.name == '{name}'"})

def load_model(path):
    with open(path, "rb") as f:
        return pickle.loads(f.read())

def run_report(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True)

def load_config(text):
    return yaml.load(text)

def fetch(url):
    return requests.get(url, verify=False)