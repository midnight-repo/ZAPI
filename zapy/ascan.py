
class ascan():
    def __init__(self, API):
        self.API = API

    def ascanViewStatus(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/status/',
            params=params
        )

        return r.json

    def ascanViewScanProgress(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/scanProgress/',
            params=params
        )

        return r.json

    def ascanViewMessagesIds(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/messagesIds/',
            params=params
        )

        return r.json

    def ascanViewAlertsIds(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/alertsIds/',
            params=params
        )

        return r.json

    def ascanViewScans(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/scans/',
        )

        return r.json

    def ascanViewScanPolicyNames(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/scanPolicyNames/',
        )

        return r.json

    def ascanViewExcludedFromScan(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/excludedFromScan/',
        )

        return r.json

    def ascanViewScanners(self, **kwargs):

        params = {
            "scanPolicyName": kwargs.get("scanPolicyName"),
"policyId": kwargs.get("policyId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/scanners/',
            params=params
        )

        return r.json

    def ascanViewPolicies(self, **kwargs):

        params = {
            "scanPolicyName": kwargs.get("scanPolicyName"),
"policyId": kwargs.get("policyId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/policies/',
            params=params
        )

        return r.json

    def ascanViewAttackModeQueue(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/attackModeQueue/',
        )

        return r.json

    def ascanViewExcludedParams(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/excludedParams/',
        )

        return r.json

    def ascanViewOptionExcludedParamList(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionExcludedParamList/',
        )

        return r.json

    def ascanViewExcludedParamTypes(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/excludedParamTypes/',
        )

        return r.json

    def ascanViewOptionAttackPolicy(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionAttackPolicy/',
        )

        return r.json

    def ascanViewOptionDefaultPolicy(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionDefaultPolicy/',
        )

        return r.json

    def ascanViewOptionDelayInMs(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionDelayInMs/',
        )

        return r.json

    def ascanViewOptionHandleAntiCSRFTokens(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionHandleAntiCSRFTokens/',
        )

        return r.json

    def ascanViewOptionHostPerScan(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionHostPerScan/',
        )

        return r.json

    def ascanViewOptionMaxChartTimeInMins(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionMaxChartTimeInMins/',
        )

        return r.json

    def ascanViewOptionMaxResultsToList(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionMaxResultsToList/',
        )

        return r.json

    def ascanViewOptionMaxRuleDurationInMins(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionMaxRuleDurationInMins/',
        )

        return r.json

    def ascanViewOptionMaxScanDurationInMins(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionMaxScanDurationInMins/',
        )

        return r.json

    def ascanViewOptionMaxScansInUI(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionMaxScansInUI/',
        )

        return r.json

    def ascanViewOptionTargetParamsEnabledRPC(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionTargetParamsEnabledRPC/',
        )

        return r.json

    def ascanViewOptionTargetParamsInjectable(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionTargetParamsInjectable/',
        )

        return r.json

    def ascanViewOptionThreadPerHost(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionThreadPerHost/',
        )

        return r.json

    def ascanViewOptionAddQueryParam(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionAddQueryParam/',
        )

        return r.json

    def ascanViewOptionAllowAttackOnStart(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionAllowAttackOnStart/',
        )

        return r.json

    def ascanViewOptionInjectPluginIdInHeader(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionInjectPluginIdInHeader/',
        )

        return r.json

    def ascanViewOptionPromptInAttackMode(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionPromptInAttackMode/',
        )

        return r.json

    def ascanViewOptionPromptToClearFinishedScans(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionPromptToClearFinishedScans/',
        )

        return r.json

    def ascanViewOptionRescanInAttackMode(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionRescanInAttackMode/',
        )

        return r.json

    def ascanViewOptionScanHeadersAllRequests(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionScanHeadersAllRequests/',
        )

        return r.json

    def ascanViewOptionShowAdvancedDialog(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/view/optionShowAdvancedDialog/',
        )

        return r.json

    def ascanActionScan(self, **kwargs):

        params = {
            "url": kwargs.get("url"),
"recurse": kwargs.get("recurse"),
"inScopeOnly": kwargs.get("inScopeOnly"),
"scanPolicyName": kwargs.get("scanPolicyName"),
"method": kwargs.get("method"),
"postData": kwargs.get("postData"),
"contextId": kwargs.get("contextId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/scan/',
            params=params
        )

        return r.json

    def ascanActionScanAsUser(self, **kwargs):

        params = {
            "url": kwargs.get("url"),
"contextId": kwargs.get("contextId"),
"userId": kwargs.get("userId"),
"recurse": kwargs.get("recurse"),
"scanPolicyName": kwargs.get("scanPolicyName"),
"method": kwargs.get("method"),
"postData": kwargs.get("postData")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/scanAsUser/',
            params=params
        )

        return r.json

    def ascanActionPause(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/pause/',
            params=params
        )

        return r.json

    def ascanActionResume(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/resume/',
            params=params
        )

        return r.json

    def ascanActionStop(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/stop/',
            params=params
        )

        return r.json

    def ascanActionRemoveScan(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/removeScan/',
            params=params
        )

        return r.json

    def ascanActionPauseAllScans(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/pauseAllScans/',
        )

        return r.json

    def ascanActionResumeAllScans(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/resumeAllScans/',
        )

        return r.json

    def ascanActionStopAllScans(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/stopAllScans/',
        )

        return r.json

    def ascanActionRemoveAllScans(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/removeAllScans/',
        )

        return r.json

    def ascanActionClearExcludedFromScan(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/clearExcludedFromScan/',
        )

        return r.json

    def ascanActionExcludeFromScan(self, **kwargs):

        params = {
            "regex": kwargs.get("regex")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/excludeFromScan/',
            params=params
        )

        return r.json

    def ascanActionEnableAllScanners(self, **kwargs):

        params = {
            "scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/enableAllScanners/',
            params=params
        )

        return r.json

    def ascanActionDisableAllScanners(self, **kwargs):

        params = {
            "scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/disableAllScanners/',
            params=params
        )

        return r.json

    def ascanActionEnableScanners(self, **kwargs):

        params = {
            "ids": kwargs.get("ids"),
"scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/enableScanners/',
            params=params
        )

        return r.json

    def ascanActionDisableScanners(self, **kwargs):

        params = {
            "ids": kwargs.get("ids"),
"scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/disableScanners/',
            params=params
        )

        return r.json

    def ascanActionSetEnabledPolicies(self, **kwargs):

        params = {
            "ids": kwargs.get("ids"),
"scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setEnabledPolicies/',
            params=params
        )

        return r.json

    def ascanActionSetPolicyAttackStrength(self, **kwargs):

        params = {
            "id": kwargs.get("id"),
"attackStrength": kwargs.get("attackStrength"),
"scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setPolicyAttackStrength/',
            params=params
        )

        return r.json

    def ascanActionSetPolicyAlertThreshold(self, **kwargs):

        params = {
            "id": kwargs.get("id"),
"alertThreshold": kwargs.get("alertThreshold"),
"scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setPolicyAlertThreshold/',
            params=params
        )

        return r.json

    def ascanActionSetScannerAttackStrength(self, **kwargs):

        params = {
            "id": kwargs.get("id"),
"attackStrength": kwargs.get("attackStrength"),
"scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setScannerAttackStrength/',
            params=params
        )

        return r.json

    def ascanActionSetScannerAlertThreshold(self, **kwargs):

        params = {
            "id": kwargs.get("id"),
"alertThreshold": kwargs.get("alertThreshold"),
"scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setScannerAlertThreshold/',
            params=params
        )

        return r.json

    def ascanActionAddScanPolicy(self, **kwargs):

        params = {
            "scanPolicyName": kwargs.get("scanPolicyName"),
"alertThreshold": kwargs.get("alertThreshold"),
"attackStrength": kwargs.get("attackStrength")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/addScanPolicy/',
            params=params
        )

        return r.json

    def ascanActionRemoveScanPolicy(self, **kwargs):

        params = {
            "scanPolicyName": kwargs.get("scanPolicyName")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/removeScanPolicy/',
            params=params
        )

        return r.json

    def ascanActionUpdateScanPolicy(self, **kwargs):

        params = {
            "scanPolicyName": kwargs.get("scanPolicyName"),
"alertThreshold": kwargs.get("alertThreshold"),
"attackStrength": kwargs.get("attackStrength")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/updateScanPolicy/',
            params=params
        )

        return r.json

    def ascanActionImportScanPolicy(self, **kwargs):

        params = {
            "path": kwargs.get("path")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/importScanPolicy/',
            params=params
        )

        return r.json

    def ascanActionAddExcludedParam(self, **kwargs):

        params = {
            "name": kwargs.get("name"),
"type": kwargs.get("type"),
"url": kwargs.get("url")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/addExcludedParam/',
            params=params
        )

        return r.json

    def ascanActionModifyExcludedParam(self, **kwargs):

        params = {
            "idx": kwargs.get("idx"),
"name": kwargs.get("name"),
"type": kwargs.get("type"),
"url": kwargs.get("url")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/modifyExcludedParam/',
            params=params
        )

        return r.json

    def ascanActionRemoveExcludedParam(self, **kwargs):

        params = {
            "idx": kwargs.get("idx")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/removeExcludedParam/',
            params=params
        )

        return r.json

    def ascanActionSkipScanner(self, **kwargs):

        params = {
            "scanId": kwargs.get("scanId"),
"scannerId": kwargs.get("scannerId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/skipScanner/',
            params=params
        )

        return r.json

    def ascanActionSetOptionAttackPolicy(self, **kwargs):

        params = {
            "String": kwargs.get("String")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionAttackPolicy/',
            params=params
        )

        return r.json

    def ascanActionSetOptionDefaultPolicy(self, **kwargs):

        params = {
            "String": kwargs.get("String")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionDefaultPolicy/',
            params=params
        )

        return r.json

    def ascanActionSetOptionAddQueryParam(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionAddQueryParam/',
            params=params
        )

        return r.json

    def ascanActionSetOptionAllowAttackOnStart(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionAllowAttackOnStart/',
            params=params
        )

        return r.json

    def ascanActionSetOptionDelayInMs(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionDelayInMs/',
            params=params
        )

        return r.json

    def ascanActionSetOptionHandleAntiCSRFTokens(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionHandleAntiCSRFTokens/',
            params=params
        )

        return r.json

    def ascanActionSetOptionHostPerScan(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionHostPerScan/',
            params=params
        )

        return r.json

    def ascanActionSetOptionInjectPluginIdInHeader(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionInjectPluginIdInHeader/',
            params=params
        )

        return r.json

    def ascanActionSetOptionMaxChartTimeInMins(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionMaxChartTimeInMins/',
            params=params
        )

        return r.json

    def ascanActionSetOptionMaxResultsToList(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionMaxResultsToList/',
            params=params
        )

        return r.json

    def ascanActionSetOptionMaxRuleDurationInMins(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionMaxRuleDurationInMins/',
            params=params
        )

        return r.json

    def ascanActionSetOptionMaxScanDurationInMins(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionMaxScanDurationInMins/',
            params=params
        )

        return r.json

    def ascanActionSetOptionMaxScansInUI(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionMaxScansInUI/',
            params=params
        )

        return r.json

    def ascanActionSetOptionPromptInAttackMode(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionPromptInAttackMode/',
            params=params
        )

        return r.json

    def ascanActionSetOptionPromptToClearFinishedScans(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionPromptToClearFinishedScans/',
            params=params
        )

        return r.json

    def ascanActionSetOptionRescanInAttackMode(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionRescanInAttackMode/',
            params=params
        )

        return r.json

    def ascanActionSetOptionScanHeadersAllRequests(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionScanHeadersAllRequests/',
            params=params
        )

        return r.json

    def ascanActionSetOptionShowAdvancedDialog(self, **kwargs):

        params = {
            "Boolean": kwargs.get("Boolean")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionShowAdvancedDialog/',
            params=params
        )

        return r.json

    def ascanActionSetOptionTargetParamsEnabledRPC(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionTargetParamsEnabledRPC/',
            params=params
        )

        return r.json

    def ascanActionSetOptionTargetParamsInjectable(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionTargetParamsInjectable/',
            params=params
        )

        return r.json

    def ascanActionSetOptionThreadPerHost(self, **kwargs):

        params = {
            "Integer": kwargs.get("Integer")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/ascan/action/setOptionThreadPerHost/',
            params=params
        )

        return r.json
