
class users():
    def __init__(self, API):
        self.API = API

    def usersViewUsersList(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/view/usersList/',
            params=params
        )

        return r.json

    def usersViewGetUserById(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId"),
"userId": kwargs.get("userId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/view/getUserById/',
            params=params
        )

        return r.json

    def usersViewGetAuthenticationCredentialsConfigParams(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/view/getAuthenticationCredentialsConfigParams/',
            params=params
        )

        return r.json

    def usersViewGetAuthenticationCredentials(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId"),
"userId": kwargs.get("userId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/view/getAuthenticationCredentials/',
            params=params
        )

        return r.json

    def usersActionNewUser(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId"),
"name": kwargs.get("name")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/action/newUser/',
            params=params
        )

        return r.json

    def usersActionRemoveUser(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId"),
"userId": kwargs.get("userId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/action/removeUser/',
            params=params
        )

        return r.json

    def usersActionSetUserEnabled(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId"),
"userId": kwargs.get("userId"),
"enabled": kwargs.get("enabled")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/action/setUserEnabled/',
            params=params
        )

        return r.json

    def usersActionSetUserName(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId"),
"userId": kwargs.get("userId"),
"name": kwargs.get("name")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/action/setUserName/',
            params=params
        )

        return r.json

    def usersActionSetAuthenticationCredentials(self, **kwargs):

        params = {
            "contextId": kwargs.get("contextId"),
"userId": kwargs.get("userId"),
"authCredentialsConfigParams": kwargs.get("authCredentialsConfigParams")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/users/action/setAuthenticationCredentials/',
            params=params
        )

        return r.json
