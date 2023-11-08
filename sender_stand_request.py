import configuration
import requests
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_AN_ORDER,
                         json = data.order_body)

def receive_an_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_AN_ORDER_BY_ITS_NUMBER + str(track_number))