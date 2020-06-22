import requests
import json
import utils
from connection import Connection
from requesttype import RequestType
import xmltodict


class Api(object):

    def __init__(self, username=None, password=None, options=None):
        if not options:
            options = {}
        self.options = options

        if not username or not password:
            # if not login specified, register a new account
            user = self._random_register()
            username = user.get('email')
            password = user.get('password')

        self.username = username
        self.password = password
        self.connection = Connection(self.username, self.password)
        self.connection.proxy = options.get('proxy')
        self.routes = self.populate_routes()

    def populate_routes(self):
        # TODO routes class populate
        xml_resp = self.connection.request(xml=None, type=RequestType.routes)
        routes = xmltodict.parse(xml_resp)

        if not routes.get('xaresponse'):
            raise Exception('Could not populate routes, malformed API response')
        return routes.get('xaresponse').get('entitylist').get('userroutepricing')

    def _get_route_id(self, number):
        # get the user route id for the current number
        # changes based on country of recipient
        user_route_id = None
        for route in self.routes:
            try:
                if number.startswith(route.get('countryCode')):
                    user_route_id = route.get('userRouteId')
                    break
            except Exception:
                user_route_id = self.routes.get('userRouteId')

        if not user_route_id:
            raise Exception('Could not determine user route id')
        return user_route_id

    def send(self, originator, recipient, message):
        route_id = self._get_route_id(recipient)
        data = {
            'originator': originator,
            'recipient':  recipient,
            'body': message,
            'reference': utils.random_number(),
            'routeId': route_id,
        }
        xml_resp = self.connection.request(xml=data, type=RequestType.single_message)
        resp = xmltodict.parse(xml_resp)

        if not resp.get('xaresponse').get('message').get('id'):
            raise Exception('Message send failed')
        return True
