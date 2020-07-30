import requests
import json



class test_view():
  def test_post_headers_body_json(self):
      url = 'http://127.0.0.1:8000/'

      # Body
      payload = {"empid": 405, "name": "rajesh","emp_num": 1796,"department": "IT"}

      # convert dict to json by json.dumps() for body data.
      resp = requests.post(url,data=json.dumps(payload))

      # Validate response headers and body contents, e.g. status code.
      assert resp.status_code == 201

      # print response full body as text
