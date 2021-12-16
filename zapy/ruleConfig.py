
class ruleConfig():
    def __init__(self, API):
        self.API = API

    def ruleConfigViewRuleConfigValue(self, **kwargs):

        params = {
            "key": kwargs.get("key")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ruleConfig/view/ruleConfigValue/',
            params=params
        )

        return r.json

    def ruleConfigViewAllRuleConfigs(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ruleConfig/view/allRuleConfigs/',
        )

        return r.json

    def ruleConfigActionResetRuleConfigValue(self, **kwargs):

        params = {
            "key": kwargs.get("key")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ruleConfig/action/resetRuleConfigValue/',
            params=params
        )

        return r.json

    def ruleConfigActionResetAllRuleConfigValues(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ruleConfig/action/resetAllRuleConfigValues/',
        )

        return r.json

    def ruleConfigActionSetRuleConfigValue(self, **kwargs):

        params = {
            "key": kwargs.get("key"),
"value": kwargs.get("value")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ruleConfig/action/setRuleConfigValue/',
            params=params
        )

        return r.json
