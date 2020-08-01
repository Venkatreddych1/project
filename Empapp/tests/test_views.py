import requests
import json
import pytest




def test_post_headers_body_json(self):
    url = 'http://127.0.0.1:8000/'
    # Body
    payload = {"empid": 4005, "name": "rajesh", "emp_num": 14126, "department": "IT"}

    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, data=json.dumps(payload))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 201

    # print response full body as text




def test_post_get_details(self):
    url = 'http://127.0.0.1:8000/api/employee/'

    resp=requests.get(url)
    k = resp.json()
    assert k.status_code == 200
