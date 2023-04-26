import requests


class Grecaptcha:
    def __init__(self, sitekey='6LfihLklAAAAAPpK7MGkiYI4iIhA-2WuUlfWWNrV', secretkey='6LfihLklAAAAAI1X3swQMRNJLAt0BAvk-sMhTp9c'):
        self.sitekey = sitekey
        self.secretkey = secretkey
        self.session = requests.Session()
        self.verifyURL = 'https://www.google.com/recaptcha/api/siteverify'

    def verify(self, response, remoteip='127.0.0.1'):
        self.response = response
        self.remoteip = remoteip

        self.requestData = {
            'secret': self.secretkey,
            'response': self.response,
            'remoteip': self.remoteip,
        }

        self.requestResponse = self.session.post(
            self.verifyURL, data=self.requestData)
        
        if self.requestResponse.json()['success']:
            return True

        return False

    def test(self):
        print(self.verify('lol', '192.168.1.12'))


if __name__ == "__main__":
    client = Grecaptcha()
    client.test()
