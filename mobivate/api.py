import requests
import json
import utils
from connection import Connection
from requesttype import RequestType


class Api:

    def __init__(self, username, password):
        self.session_id = None
        self.routes = None
        self.connection = Connection(username, password)

    def get_route(self):
        return NotImplemented

    def populate_routes(self):
        return NotImplemented

    def send(self, message):
        data = {
            'originator': '447800000000',
            'recipient':  '447800000000',
            'body': 'Hello world'
        }
        xml_resp = self.connection.request(xml=data, type=RequestType.single_message)
        return xml_resp

    def register(self):
        url = 'http://www.mobivate.com/do_signup.php'
        email = utils.random_number() + '@mailinator.com'
        password = utils.random_salt()
        data = {
            'company': '',
            'currency': 'GBP',
            'email':  email,
            'fullname': utils.random_salt(),
            'mobile': '4478' + utils.random_number(),
            'password': password,
            'password2': password,
        }
        r = requests.post(url, data=data)
        json_resp = json.loads(r.text)

        if json_resp.get('ok'):  # registration successful
            user = {
                'email': email,
                'password': password,
            }
            return user
        else:  # registration failed
            return {}