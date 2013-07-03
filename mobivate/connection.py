import requests
from requesttype import RequestType
import xmltodict
import utils


class Connection():

    def __init__(self, username, password):
        self.authentication = 'http://app.mobivatebulksms.com/bulksms/xmlapi/login/{0}/{1}'
        self.send_single_sms = 'http://app.mobivatebulksms.com/bulksms/xmlapi/{0}/send/sms/single'
        self.send_batch_sms = 'http://app.mobivatebulksms.com/bulksms/xmlapi/{0}/send/sms/batch'
        self.routes_url = 'http://app.mobivatebulksms.com/bulksms/xmlapi/{0}/entity/user.UserRoutePricing/all/visible'

        self._username = username
        self._password = password
        self.session_id = None

    @classmethod
    def connection(cls, username, password):
        cls._username = username
        cls._password = password
        return cls

    def connect(self):
        try:
            r = self.request(type=RequestType.login)
            self.session_id = xmltodict.parse(r).get('xaresponse').get('session')
        except Exception:
            raise

    def request(self, xml=None, type=None):
        if not self.session_id and type != RequestType.login:
            self.connect()

        if xml:
            xml = {'message': utils.dict_to_xml(xml)}
            post_data = {'xml': xml}

        if type is RequestType.login:
            url = self.authentication.format(self._username, self._password)
        elif type is RequestType.batch_message:
            raise NotImplementedError()
        elif type is RequestType.single_message:
            url = self.send_single_sms.format(self.session_id)
        elif type is RequestType.routes:
            url = self.routes_url(self.session_id)
        else:
            raise Exception('Invalid RequestType')

        req_headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)'}

        if xml:
            r = requests.post(url, data=post_data, headers=req_headers)
        else:
            r = requests.get(url, headers=req_headers)
        return r.text

    def is_connected(self):
        if self.session_id:
            return True
        else:
            return False
