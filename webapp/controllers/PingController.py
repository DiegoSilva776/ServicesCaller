# -*- coding: utf-8 -*-

import time
import datetime
import http.client
import urllib
import json

from bs4 import BeautifulSoup

from utils.NetworkingUtils import NetworkingUtils

'''
    Make requests to the services
'''
class PingController():

    def __init__(self):
        self.netUtils = NetworkingUtils()

    def pingServices(self):
        urls = [
            "fiocruz-app-oeds-api-dev.herokuapp.com"
        ]

        try:

            for url in urls:
                # Make a request to get the HTML which contains the list of Cities of SIOPS
                headers = {
                    'cache-control': "no-cache"
                }
                conn = http.client.HTTPConnection(url)
                conn.request('GET', "", headers = headers)

                # Process the response
                res = conn.getresponse()
                data = res.read()
                text = data.decode(self.netUtils.SIOPS_RESPONSE_DATA_DECODER)

                print("response: {0}".format(text))

            time.sleep(120)

        except urllib.error.HTTPError:
            print("Failed to pingService")

        except urllib.error.URLError:
            print("Failed to pingService")

        finally:

            return ""