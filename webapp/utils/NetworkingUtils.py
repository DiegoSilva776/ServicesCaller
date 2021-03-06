# -*- coding: utf-8 -*-

import json

from models.Service import Service

'''
    NetworkingUtils is responsible for holding the external URLs and the default parameters 
    of each URL used by the API.
'''
class NetworkingUtils():

    def __init__(self):
        self.TAG = "NetworkingUtils"
        self.PATH_SERVICES_CONFIG_FILE = "config/services.json"
        self.TIMEOUT_CALL_SERVICE = 60
        self.MANDATORY_TERM_SUCCESS_STATUS_RESPONSE = "API"
        self.ISO_DATA_DECODER = 'iso8859-15'
        self.UTF8_DECODER = 'utf-8'
        self.HTML_PARSER = 'html.parser'

        self.key = ""
        self.services = []
        self.initListServices()

    def initListServices(self):
        try:
            fileData = open(self.PATH_SERVICES_CONFIG_FILE).read()
            data = json.loads(fileData)

            self.key = data["key"]

            for serviceFromList in data["urls"]:
                service = Service()

                if "url" in serviceFromList:
                    service.url = serviceFromList["url"]

                if "name" in serviceFromList:
                    service.name = serviceFromList["name"]

                self.services.append(service)

        except Exception as e:
            print("{0}: Failed to initListServices: {1}".format(self.TAG, e))

    def getServiceByUrl(self, url):
        try:

            for service in self.services:

                if service.url == url:
                    return service

        except Exception as e:
            print("{0}: Failed to getServiceByUrl: {1}".format(self.TAG, e))

        return None