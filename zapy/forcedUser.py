
class forcedUser():
    def __init__(self, API):
        self.API = API

    def forcedUserViewIsForcedUserModeEnabled(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/forcedUser/view/isForcedUserModeEnabled/',
        )

        return r.json

    def forcedUserViewGetForcedUser(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/forcedUser/view/getForcedUser/',
            params=params
        )

        return r.json

    def forcedUserActionSetForcedUser(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId"),
"userId": kwargs.get("userId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/forcedUser/action/setForcedUser/',
            params=params
        )

        return r.json

    def forcedUserActionSetForcedUserModeEnabled(self, **kwargs):

        params = {
            "boolean": kwargs.get("boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/forcedUser/action/setForcedUserModeEnabled/',
            params=params
        )

        return r.json
