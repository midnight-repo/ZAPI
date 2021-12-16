
class context():
    def __init__(self, API):
        self.API = API

    def contextViewContextList(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/view/contextList/',
        )

        return r.json

    def contextViewExcludeRegexs(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/view/excludeRegexs/',
            params=params
        )

        return r.json

    def contextViewIncludeRegexs(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/view/includeRegexs/',
            params=params
        )

        return r.json

    def contextViewContext(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/view/context/',
            params=params
        )

        return r.json

    def contextViewTechnologyList(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/view/technologyList/',
        )

        return r.json

    def contextViewIncludedTechnologyList(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/view/includedTechnologyList/',
            params=params
        )

        return r.json

    def contextViewExcludedTechnologyList(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/view/excludedTechnologyList/',
            params=params
        )

        return r.json

    def contextViewUrls(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/view/urls/',
            params=params
        )

        return r.json

    def contextActionExcludeFromContext(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName"),
"regex": kwargs.get("regex")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/excludeFromContext/',
            params=params
        )

        return r.json

    def contextActionIncludeInContext(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName"),
"regex": kwargs.get("regex")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/includeInContext/',
            params=params
        )

        return r.json

    def contextActionSetContextRegexs(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName"),
"incRegexs": kwargs.get("incRegexs"),
"excRegexs": kwargs.get("excRegexs")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/setContextRegexs/',
            params=params
        )

        return r.json

    def contextActionNewContext(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/newContext/',
            params=params
        )

        return r.json

    def contextActionRemoveContext(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/removeContext/',
            params=params
        )

        return r.json

    def contextActionExportContext(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName"),
"contextFile": kwargs.get("contextFile")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/exportContext/',
            params=params
        )

        return r.json

    def contextActionImportContext(self, **kwargs):

        params = {
            "contextFile": kwargs.get("contextFile")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/importContext/',
            params=params
        )

        return r.json

    def contextActionIncludeContextTechnologies(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName"),
"technologyNames": kwargs.get("technologyNames")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/includeContextTechnologies/',
            params=params
        )

        return r.json

    def contextActionIncludeAllContextTechnologies(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/includeAllContextTechnologies/',
            params=params
        )

        return r.json

    def contextActionExcludeContextTechnologies(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName"),
"technologyNames": kwargs.get("technologyNames")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/excludeContextTechnologies/',
            params=params
        )

        return r.json

    def contextActionExcludeAllContextTechnologies(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/excludeAllContextTechnologies/',
            params=params
        )

        return r.json

    def contextActionSetContextInScope(self, **kwargs):

        params = {
            "contextName": kwargs.get("contextName"),
"booleanInScope": kwargs.get("booleanInScope")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/context/action/setContextInScope/',
            params=params
        )

        return r.json
