import requests
import zapy

class API():
    def __init__(self, url, api_key):
        self.api_key = api_key
        self.url = url[:-1] if url.endswith('/') else url
        self.HTTP = requests.Session()
        self.HTTP.headers.update(
            {'X-ZAP-API-Key': self.api_key}
        )

        self.alert = zapy.alert
        self.acsrf = zapy.acsrf
        self.pscan = zapy.pscan
        self.search = zapy.search
        self.autoupdate = zapy.autoupdate
        self.spider = zapy.spider
        self.core = zapy.core
        self.params = zapy.params
        self.ascan = zapy.ascan
        self.context = zapy.context
        self.httpSessions = zapy.httpSessions
        self.Break = zapy.Break
        self.authentication = zapy.authentication
        self.authorization = zapy.authorization
        self.localProxies = zapy.localProxies
        self.ruleConfig = zapy.ruleConfig
        self.sessionManagement = zapy.sessionManagement
        self.users = zapy.users
        self.forcedUser = zapy.forcedUser
        self.script = zapy.script
        self.stats = zapy.stats
        self.Schemas = zapy.Schemas

    def close(self):
        self.HTTP.close()
