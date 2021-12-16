
class stats():
    def __init__(self, API):
        self.API = API

    def statsViewStats(self, **kwargs):

        params = {
            "keyPrefix": kwargs.get("keyPrefix")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/view/stats/',
            params=params
        )

        return r.json

    def statsViewAllSitesStats(self, **kwargs):

        params = {
            "keyPrefix": kwargs.get("keyPrefix")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/view/allSitesStats/',
            params=params
        )

        return r.json

    def statsViewSiteStats(self, **kwargs):

        params = {
            "site": kwargs.get("site"),
"keyPrefix": kwargs.get("keyPrefix")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/view/siteStats/',
            params=params
        )

        return r.json

    def statsViewOptionStatsdHost(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/view/optionStatsdHost/',
        )

        return r.json

    def statsViewOptionStatsdPort(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/view/optionStatsdPort/',
        )

        return r.json

    def statsViewOptionStatsdPrefix(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/view/optionStatsdPrefix/',
        )

        return r.json

    def statsViewOptionInMemoryEnabled(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/view/optionInMemoryEnabled/',
        )

        return r.json

    def statsViewOptionStatsdEnabled(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/view/optionStatsdEnabled/',
        )

        return r.json

    def statsActionClearStats(self, **kwargs):

        params = {
            "keyPrefix": kwargs.get("keyPrefix")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/action/clearStats/',
            params=params
        )

        return r.json

    def statsActionSetOptionStatsdHost(self, **kwargs):

        params = {
            "String": kwargs.get("String")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/action/setOptionStatsdHost/',
            params=params
        )

        return r.json

    def statsActionSetOptionStatsdPrefix(self, **kwargs):

        params = {
            "String": kwargs.get("String")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/action/setOptionStatsdPrefix/',
            params=params
        )

        return r.json

    def statsActionSetOptionInMemoryEnabled(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/action/setOptionInMemoryEnabled/',
            params=params
        )

        return r.json

    def statsActionSetOptionStatsdPort(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/stats/action/setOptionStatsdPort/',
            params=params
        )

        return r.json
