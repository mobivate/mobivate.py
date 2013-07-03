import requests
import json
import utils
from connection import Connection
from requesttype import RequestType
import xmltodict


class Api(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.connection = Connection(self.username, self.password)
        self.routes = self.populate_routes()

    def get_route(self):
        return NotImplemented

    def populate_routes(self):
        # TODO routes class populate
        xml = self.connection.request(xml=None, type=RequestType.routes)
        routes = xmltodict.parse(xml)
        if not routes.get('xaresponse'):
            raise Exception('Could not popular routes, malformed response')
        return routes.get('xaresponse').get('entitylist').get('userroutepricing').get('userRouteId')

    def send(self, message):
        route_id = self.routes
        data = {
            'originator': '447899999999',
            'recipient':  '447800000000',
            'body': 'Hello world',
            'reference': utils.random_number(),
            'routeId': route_id,
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