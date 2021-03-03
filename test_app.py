import requests
import json
host_url = "http://localhost:5000"
headers = {'Content-Type': 'application/json' } 

def test_balance():
    resp = requests.get(host_url+"/balance")
    assert(resp.status_code==200)

def test_transactions():
    data = {"payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z"}
    resp = requests.post(url=host_url+"/transactions",headers=headers,data=json.dumps(data))
    assert(resp.status_code==200)

def test_delete_points():
    data = {"points":100}
    resp = requests.post(url=host_url+"/delete_points",headers=headers,data=json.dumps(data))
    assert(resp.status_code==200)