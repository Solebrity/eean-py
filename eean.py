from endpoints import *
import inspect
import requests
class EEAN():
"""The EEAN class is the client object responsible for retrieving data from the
Ebay Enterprise Affiliate Network.  This version only support the GET operations
Used by the Publishers.  For more information go to:
http://help.pepperjamnetwork.com/publisher/api
"""
    CURRENT_VERSION = "20120402"
    ROOT_URL = 'https://api.pepperjamnetwork.com/'

    def __init__(self, api_key, output='json',debug=False):
        """Initializes the EEAN API Client
        Args:
            api_key (string): your EEAN API Key
            output (string): the output format returned by the API (csv, json,
                xml)
            debug (boolean): run the client in debug mode
        """
        self._api_key = api_key
        self._debug = debug
        self._format = output

    def _make_request(self, path, method='GET'):
        path += '&apiKey=' + self._api_key
        full_request = "%s%s/%s" % (EEAN.ROOT_URL, EEAN.CURRENT_VERSION, path)

        if(self._debug):
            print("%s => %s", (method, full_request))

        if(method == 'GET'):
            return requests.get(full_request).text

    def cleanup_args(self, keywords):
        del keywords['self']
        keywords['format'] = keywords['output']
        del keywords['output']
        return keywords

    def advertiser_details(self, status=[], category=[], programId=[], name=[],
                           firstName=[], lastName=[], currency=[],
                           mobileTracking=False, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Advertiser.generate_path_with_query(**self.cleanup_args(keywords)))

    def get_advanced(self, subType=[], id=[], programId=[], category=[],
                                 websiteId=[], sid=[], encrypted=0,
                                 startDate=None, endDate=None, output=None,page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Creative.generate_advanced_path_with_query(**self.cleanup_args(keywords)))

    def get_banner(self, id=[], programId=[], category=[], height=[], width=[],
                                 websiteId=[], sid=[], deepLink=None, encrypted=0,
                                 startDate=None, endDate=None, output=None, page=1):

        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Creative.generate_banner_path_with_query(**self.cleanup_args(keywords)))

    def get_coupon(self, id=[], programId=[], category=[],
                                 websiteId=[], sid=[], encrypted=0,
                                 startDate=None, endDate=None, output=None, page=1):

        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Creative.generate_coupon_path_with_query(**self.cleanup_args(keywords)))

    def get_text(self, id=[], programId=[], category=[],
                                 keywords=[], sid=[], deepLink=None, encrypted=0,
                                 startDate=None, endDate=None, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Creative.generate_tex_path_with_query(**self.cleanup_args(keywords)))

    def get_product(self, programIds=[], categories=[],
                                         keywords=[], output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Creative.generate_product_path_with_query(**self.cleanup_args(keywords)))


    def get_transaction_details(self, startDate, endDate,
                                         website=None, includeCoupons=False, deviceType=False, newToFile=None, removeCsvHeaders=False, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Report.generate_transaction_details_path_with_query(**self.cleanup_args(keywords)))


    def get_transaction_delta(self, startDate, endDate,
                                         website=None, removeCsvHeaders=False, optionalFields=None, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Report.generate_transaction_delta_path_with_query(**self.cleanup_args(keywords)))


    def get_transaction_summary(self, startDate, endDate,
                                         website=None, removeCsvHeaders=False, groupBy=None, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Report.generate_transaction_summary_path_with_query(**self.cleanup_args(keywords)))


    def get_payment(self, startDate, endDate, removeCsvHeaders=False, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Report.generate_payment_path_with_query(**self.cleanup_args(keywords)))


    def get_payment_details(self, paymentId=None, startDate=None, endDate=None, removeCsvHeaders=False, itemized=False, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Report.generate_payment_details_path_with_query(**self.cleanup_args(keywords)))


    def get_sku_details(self, orderId=None, sku=None, startDate=None, endDate=None, programId=None, transactionType=None, sid=None, creativeType=None, advancedSubType=None, websiteId=None, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Report.generate_sku_details_path_with_query(**self.cleanup_args(keywords)))


    def get_invalid_link(self, creativeType=None, advancedSubType=None, websiteId=None, output=None, page=1):
        if not output:
            output = self._format

        _, _, _, keywords = inspect.getargvalues(inspect.currentframe())

        return self._make_request(Report.generate_invalid_link_path_with_query(**self.cleanup_args(keywords)))
