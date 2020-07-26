import json
import requests

from django.core.urlresolvers import reverse

from .. import  views


class TestMyView:

    def test_result_finished(self):
        request = get(reverse('insert'))
        response = views.insert()(request)

        assert response.status_code == 200

        content = json.loads(response.content)
        assert content['result'] == 'FINISHED'
