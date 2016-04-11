import inspect
from urllib.parse import quote
from datetime import datetime

class Endpoint():

    @staticmethod
    def append_options(start_string, **kwargs):
        for k, v in kwargs.items():
            if v:
                start_string += '&%s=' % quote(k) if '?' in start_string else '?%s=' % quote(k)
                if isinstance(v, datetime):
                    v = v.strftime("%Y-%m-%d")
                start_string += ','.join([quote(str(s)) for s in v]) if isinstance(v, list) else quote(str(v))
        return start_string


class Advertiser:
    path = "publisher/advertiser"

    @staticmethod
    def generate_path_with_query(status=[], category=[], programId=[], name=[],
                                 firstName=[], lastName=[], currency=[],
                                 mobileTracking=False, format='json',page=1):

        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Advertiser.path, **values)


class Creative:
    path = "publisher/creative"

    @staticmethod
    def generate_advanced_path_with_query(subType=[], id=[], programId=[], category=[],
                                 websiteId=[], sid=[], encrypted=0,
                                 startDate=None, endDate=None, format='json',page=1):

        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Creative.path + '/advanced', **values)

    @staticmethod
    def generate_banner_path_with_query(id=[], programId=[], category=[], height=[], width=[],
                                 websiteId=[], sid=[], deepLink=None, encrypted=0,
                                 startDate=None, endDate=None, format='json', page=1):

        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Creative.path + '/banner', **values)

    @staticmethod
    def generate_coupon_path_with_query(id=[], programId=[], category=[],
                                 websiteId=[], sid=[], encrypted=0,
                                 startDate=None, endDate=None, format='json', page=1):

        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Creative.path + '/coupon', **values)

    @staticmethod
    def generate_text_path_with_query(id=[], programId=[], category=[],
                                 keywords=[], sid=[], deepLink=None, encrypted=0,
                                 startDate=None, endDate=None, format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Creative.path + '/text', **values)

    @staticmethod
    def generate_product_path_with_query(programIds=[], categories=[],
                                         keywords=[], format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Creative.path + '/product', **values)

class Report:

    path = 'publisher/report'

    @staticmethod
    def generate_transaction_details_path_with_query(startDate, endDate,
                                         website=None, includeCoupons=False, deviceType=False, newToFile=None, removeCsvHeaders=False, format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Report.path + '/transaction-details', **values)

    @staticmethod
    def generate_transaction_delta_path_with_query(startDate, endDate,
                                         website=None, removeCsvHeaders=False, optionalFields=None, format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Report.path + '/transaction-delta', **values)

    @staticmethod
    def generate_transaction_summary_path_with_query(startDate, endDate,
                                         website=None, removeCsvHeaders=False, groupBy=None, format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Report.path + '/transaction-summary', **values)

    @staticmethod
    def generate_payment_path_with_query(startDate, endDate, removeCsvHeaders=False, format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Report.path + '/payment', **values)

    @staticmethod
    def generate_payment_details_path_with_query(paymentId=None, startDate=None, endDate=None, removeCsvHeaders=False, itemized=False, format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Report.path + '/payment-details', **values)

    @staticmethod
    def generate_sku_details_path_with_query(orderId=None, sku=None, startDate=None, endDate=None, programId=None, transactionType=None, sid=None, creativeType=None, advancedSubType=None, websiteId=None, format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Report.path + '/sku-details', **values)

    @staticmethod
    def generate_invalid_link_path_with_query(creativeType=None, advancedSubType=None, websiteId=None, format='json', page=1):
        _, _, _, values = inspect.getargvalues(inspect.currentframe())
        return Endpoint.append_options(Report.path + '/invalid-link', **values)
