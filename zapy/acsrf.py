
class acsrf():
    def __init__(self, API):
        self.API = API

    def acsrfViewOptionTokensNames(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/acsrf/view/optionTokensNames/',
        )

        return r.json

    def acsrfActionAddOptionToken(self, **kwargs):

        params = {
            "String": kwargs.get("String")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/acsrf/action/addOptionToken/',
            params=params
        )

        return r.json

    def acsrfActionRemoveOptionToken(self, **kwargs):

        params = {
            "String": kwargs.get("String")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/acsrf/action/removeOptionToken/',
            params=params
        )

        return r.json

    def acsrfOtherGenForm(self, **kwargs):

        params = {
            "hrefId": kwargs.get("hrefId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/OTHER/acsrf/other/genForm/',
            params=params
        )

        return r.json
