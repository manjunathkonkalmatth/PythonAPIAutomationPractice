import requests

class RESTServices:

    def getService(self, url, header, payload ):
        print('')

    def putService(self, url, header, payload ):
        response = requests.put(url, header=header, json=payload)
        print('')

    def postService(self, url, header, payload ):
        response = requests.post(url, header=header, json=payload)
        print('')

    def deleteService(self, url, header, payload ):
        print('')

    def patchService(self, url, header, payload ):
        response = requests.patch(url, header=header, json=payload)
        print('')

    def headService(self, url, header, payload ):
        print('')
