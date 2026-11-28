# Jira access policy

An access policy limits which endpoints Jira connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/jira#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Jira: its 329 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create jira --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/filter/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/backlog"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/configuration"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/epic"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/epic/none/issue"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/epic/{id}/issue"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/features"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/issue"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/project/full"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/properties/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/quickfilter"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/quickfilter/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/reports"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/sprint"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/sprint/{id}/issue"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/board/{id}/version"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/epic/none/issue"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/epic/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/epic/{id}/issue"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/issue/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/issue/{id}/estimation"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/sprint/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/sprint/{id}/issue"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/sprint/{id}/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/agile/1.0/sprint/{id}/properties/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/announcementBanner"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/data-policy"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/data-policy/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/applicationrole"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/applicationrole/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/auditing/record"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/avatar/{id}/system"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/universal_avatar/type/{id}/owner/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/universal_avatar/view/type/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/universal_avatar/view/type/{id}/avatar/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/universal_avatar/view/type/{id}/owner/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/classification-levels"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/dashboard"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/dashboard/gadgets"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/dashboard/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/dashboard/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/dashboard/{id}/gadget"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/dashboard/{id}/items/{id}/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/dashboard/{id}/items/{id}/properties/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/config/fieldschemes"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/config/fieldschemes/projects"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/config/fieldschemes/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/config/fieldschemes/{id}/fields"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/config/fieldschemes/{id}/fields/{id}/parameters"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/config/fieldschemes/{id}/projects"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/filter/defaultShareScope"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/filter/{id}/permission"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/filter/{id}/permission/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/filter/favourite"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/filter/my"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/filter/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/filter/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/filter/{id}/columns"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/groupuserpicker"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/group"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/group/bulk"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/group/member"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/groups/picker"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/attachment/content/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/attachment/meta"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/attachment/thumbnail/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/attachment/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/attachment/{id}/expand/human"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/attachment/{id}/expand/raw"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/bulk/issues/fields"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/bulk/issues/transition"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/bulk/queue/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/comment/{id}/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/comment/{id}/properties/{id}"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/comment/list"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/comment"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/comment/{id}"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/app/field/context/configuration/list"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/app/field/{id}/context/configuration"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/context"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/context/defaultValue"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/context/defaultValues"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/context/issuetypemapping"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/field/{id}/context/mapping"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/context/projectmapping"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/customFieldOption/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/context/{id}/option"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/option"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/option/suggestions/edit"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/option/suggestions/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/option/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/fieldconfiguration"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/fieldconfiguration/{id}/fields"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/fieldconfigurationscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/fieldconfigurationscheme/mapping"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/fieldconfigurationscheme/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/search/trashed"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/association/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/contexts"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/projects/fields"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issueLinkType"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issueLinkType/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issueLink/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/settings/columns"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/notificationscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/notificationscheme/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/notificationscheme/{id}"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/forge/panel/action/bulk/status"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/priority"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/priority/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/priority/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/properties/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/redact/status/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/remotelink"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/remotelink/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/resolution"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/resolution/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/resolution/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/picker"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/jql/match"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/search"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/search"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/search/approximate-count"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/search/jql"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/search/jql"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuesecurityschemes/{id}/members"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/securitylevel/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuesecurityschemes"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuesecurityschemes/level"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuesecurityschemes/level/member"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuesecurityschemes/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuesecurityschemes/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuesecurityschemes/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetype/{id}/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetype/{id}/properties/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetypescheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetypescheme/mapping"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetypescheme/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetypescreenscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetypescreenscheme/mapping"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetypescreenscheme/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetypescreenscheme/{id}/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetype"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetype/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetype/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issuetype/{id}/alternatives"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/votes"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/issue/watching"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/watchers"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id}/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id}/properties/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/worklog"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/worklog/deleted"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/worklog/list"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/worklog/updated"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/changelog/bulkfetch"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/events"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/issue/bulkfetch"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/createmeta"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/createmeta/{id}/issuetypes"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/createmeta/{id}/issuetypes/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/limit/adf/report"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/limit/report"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/changelog"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/issue/{id}/changelog/list"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/editmeta"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/issue/{id}/transitions"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/expression/analyse"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/expression/eval"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/expression/evaluate"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/application-properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/application-properties/advanced-settings"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/configuration"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/invalid-jqls-access-log"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/jql/autocompletedata"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/jql/autocompletedata"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/jql/autocompletedata/suggestions"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/jql/parse"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/jql/pdcleaner"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/jql/sanitize"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/jql/function/computation"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/jql/function/computation/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/label"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/instance/license"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/license/approximateLicenseCount"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/license/approximateLicenseCount/product/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/mypreferences"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/mypreferences/locale"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/myself"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/permissionscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/permissionscheme/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/permissionscheme/{id}/permission"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/permissionscheme/{id}/permission/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/mypermissions"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/permissions"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/permissions/check"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/permissions/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/plans/plan"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/plans/plan/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/policies"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/policies/project/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/policies/project/{id}/rules"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/priorityscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/priorityscheme/priorities/available"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/priorityscheme/{id}/priorities"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/priorityscheme/{id}/projects"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/avatars"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/projectCategory"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/projectCategory/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/classification-config"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/classification-level/default"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/component"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/component/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/component/{id}/relatedIssueCounts"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/component"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/components"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/email"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/features"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/projectvalidate/key"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/projectvalidate/validProjectKey"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/projectvalidate/validProjectName"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/issuesecuritylevelscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/permissionscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/securitylevel"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/properties/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/role/{id}/actors"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/role"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/role/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/roledetails"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/role"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/role/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project-template/live-template"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/type"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/type/accessible"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/type/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/type/{id}/accessible"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/version"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/versions"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/version/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/version/{id}/relatedIssueCounts"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/version/{id}/relatedwork"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/version/{id}/unresolvedIssueCount"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/recent"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/hierarchy"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/notificationscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/project/{id}/statuses"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/screenscheme"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/screens/{id}/tabs/{id}/fields"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/screens/tabs"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/screens/{id}/tabs"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/field/{id}/screens"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/screens"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/screens/{id}/availableFields"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/serverInfo"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/statuses"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/statuses/byNames"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/statuses/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/statuses/{id}/project/{id}/issueTypeUsages"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/statuses/{id}/projectUsages"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/statuses/{id}/workflowUsages"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/task/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/plans/plan/{id}/team"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/plans/plan/{id}/team/atlassian/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/plans/plan/{id}/team/planonly/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/configuration/timetracking"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/configuration/timetracking/list"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/configuration/timetracking/options"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/uiModifications"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/properties"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/properties/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/assignable/multiProjectSearch"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/assignable/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/permission/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/picker"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/search/query"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/search/query/key"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/viewissue/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/bulk"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/bulk/migration"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/columns"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/email"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/email/bulk"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/user/groups"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/users"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/users/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/webhook"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/webhook/failed"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/default"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/issuetype/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/workflow"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/project"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/workflowscheme/read"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/workflowscheme/update/mappings"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}/default"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}/issuetype/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}/projectUsages"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflowscheme/{id}/workflow"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/statuscategory"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/statuscategory/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/status"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/status/{id}"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflow/rule/config"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/workflow/history/list"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflow/search"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflow/{id}/project/{id}/issueTypeUsages"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflow/{id}/projectUsages"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflow/{id}/workflowSchemes"},
    {"method": "POST", "path": "ex/jira/{id}/rest/api/3/workflows"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflows/capabilities"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflows/defaultEditor"},
    {"method": "GET", "path": "ex/jira/{id}/rest/api/3/workflows/search"}
  ],
  "deny": []
}
```

## Endpoints

The Jira endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| POST | ex/jira/{id}/rest/api/3/agents/bulk/invoke/batch | write | agents | Bulk start agent sessions (batch). |
| POST | ex/jira/{id}/rest/api/3/agents/bulk/invoke/uniform | write | agents | Bulk start agent sessions (uniform). |
| POST | ex/jira/{id}/rest/agile/1.0/backlog/issue | write | agile-backlog | Move issues to backlog. |
| POST | ex/jira/{id}/rest/agile/1.0/backlog/{id}/issue | write | agile-backlog | Move issues to backlog for board. |
| GET | ex/jira/{id}/rest/agile/1.0/board | read | agile-board | Get all boards. |
| POST | ex/jira/{id}/rest/agile/1.0/board | write | agile-board | Create board. |
| GET | ex/jira/{id}/rest/agile/1.0/board/filter/{id} | read | agile-board | Get board by filter id. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id} | read | agile-board | Get board. |
| DELETE | ex/jira/{id}/rest/agile/1.0/board/{id} | write | agile-board | Delete board. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/backlog | read | agile-board | Get issues for backlog. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/configuration | read | agile-board | Get configuration. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/epic | read | agile-board | Get epics. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/epic/none/issue | read | agile-board | Get issues without epic for board. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/epic/{id}/issue | read | agile-board | Get board issues for epic. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/features | read | agile-board | Get features for board. |
| PUT | ex/jira/{id}/rest/agile/1.0/board/{id}/features | write | agile-board | Toggle features. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/issue | read | agile-board | Get issues for board. |
| POST | ex/jira/{id}/rest/agile/1.0/board/{id}/issue | write | agile-board | Move issues to board. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/project | read | agile-board | Get projects. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/project/full | read | agile-board | Get projects full. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/properties | read | agile-board | Get board property keys. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/properties/{id} | read | agile-board | Get board property. |
| PUT | ex/jira/{id}/rest/agile/1.0/board/{id}/properties/{id} | write | agile-board | Set board property. |
| DELETE | ex/jira/{id}/rest/agile/1.0/board/{id}/properties/{id} | write | agile-board | Delete board property. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/quickfilter | read | agile-board | Get all quick filters. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/quickfilter/{id} | read | agile-board | Get quick filter. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/reports | read | agile-board | Get reports for board. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/sprint | read | agile-board | Get all sprints. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/sprint/{id}/issue | read | agile-board | Get board issues for sprint. |
| GET | ex/jira/{id}/rest/agile/1.0/board/{id}/version | read | agile-board | Get all versions. |
| GET | ex/jira/{id}/rest/agile/1.0/epic/none/issue | read | agile-epic | Get issues without epic. |
| POST | ex/jira/{id}/rest/agile/1.0/epic/none/issue | write | agile-epic | Remove issues from epic. |
| GET | ex/jira/{id}/rest/agile/1.0/epic/{id} | read | agile-epic | Get epic. |
| POST | ex/jira/{id}/rest/agile/1.0/epic/{id} | write | agile-epic | Partially update epic. |
| GET | ex/jira/{id}/rest/agile/1.0/epic/{id}/issue | read | agile-epic | Get issues for epic. |
| POST | ex/jira/{id}/rest/agile/1.0/epic/{id}/issue | write | agile-epic | Move issues to epic. |
| PUT | ex/jira/{id}/rest/agile/1.0/epic/{id}/rank | write | agile-epic | Rank epics. |
| PUT | ex/jira/{id}/rest/agile/1.0/issue/rank | write | agile-issue | Rank issues. |
| GET | ex/jira/{id}/rest/agile/1.0/issue/{id} | read | agile-issue | Get issue. |
| GET | ex/jira/{id}/rest/agile/1.0/issue/{id}/estimation | read | agile-issue | Get issue estimation for board. |
| PUT | ex/jira/{id}/rest/agile/1.0/issue/{id}/estimation | write | agile-issue | Estimate issue for board. |
| POST | ex/jira/{id}/rest/agile/1.0/sprint | write | agile-sprint | Create sprint. |
| GET | ex/jira/{id}/rest/agile/1.0/sprint/{id} | read | agile-sprint | Get sprint. |
| POST | ex/jira/{id}/rest/agile/1.0/sprint/{id} | write | agile-sprint | Partially update sprint. |
| PUT | ex/jira/{id}/rest/agile/1.0/sprint/{id} | write | agile-sprint | Update sprint. |
| DELETE | ex/jira/{id}/rest/agile/1.0/sprint/{id} | write | agile-sprint | Delete sprint. |
| GET | ex/jira/{id}/rest/agile/1.0/sprint/{id}/issue | read | agile-sprint | Get issues for sprint. |
| POST | ex/jira/{id}/rest/agile/1.0/sprint/{id}/issue | write | agile-sprint | Move issues to sprint and rank. |
| GET | ex/jira/{id}/rest/agile/1.0/sprint/{id}/properties | read | agile-sprint | Get properties keys. |
| GET | ex/jira/{id}/rest/agile/1.0/sprint/{id}/properties/{id} | read | agile-sprint | Get property. |
| PUT | ex/jira/{id}/rest/agile/1.0/sprint/{id}/properties/{id} | write | agile-sprint | Set property. |
| DELETE | ex/jira/{id}/rest/agile/1.0/sprint/{id}/properties/{id} | write | agile-sprint | Delete property. |
| POST | ex/jira/{id}/rest/agile/1.0/sprint/{id}/swap | write | agile-sprint | Swap sprint. |
| GET | ex/jira/{id}/rest/api/3/announcementBanner | read | announcement-banner | Get announcement banner configuration. |
| PUT | ex/jira/{id}/rest/api/3/announcementBanner | write | announcement-banner | Update announcement banner configuration. |
| GET | ex/jira/{id}/rest/api/3/data-policy | read | app-data-policies | Get data policy for the workspace. |
| GET | ex/jira/{id}/rest/api/3/data-policy/project | read | app-data-policies | Get data policy for projects. |
| GET | ex/jira/{id}/rest/api/3/applicationrole | read | application-roles | Get all application roles. |
| GET | ex/jira/{id}/rest/api/3/applicationrole/{id} | read | application-roles | Get application role. |
| GET | ex/jira/{id}/rest/api/3/auditing/record | read | audit-records | Get audit records. |
| GET | ex/jira/{id}/rest/api/3/avatar/{id}/system | read | avatars | Get system avatars by type. |
| GET | ex/jira/{id}/rest/api/3/universal_avatar/type/{id}/owner/{id} | read | avatars | Get avatars. |
| POST | ex/jira/{id}/rest/api/3/universal_avatar/type/{id}/owner/{id} | write | avatars | Load avatar. |
| DELETE | ex/jira/{id}/rest/api/3/universal_avatar/type/{id}/owner/{id}/avatar/{id} | write | avatars | Delete avatar. |
| GET | ex/jira/{id}/rest/api/3/universal_avatar/view/type/{id} | read | avatars | Get avatar image by type. |
| GET | ex/jira/{id}/rest/api/3/universal_avatar/view/type/{id}/avatar/{id} | read | avatars | Get avatar image by ID. |
| GET | ex/jira/{id}/rest/api/3/universal_avatar/view/type/{id}/owner/{id} | read | avatars | Get avatar image by owner. |
| GET | ex/jira/{id}/rest/api/3/classification-levels | read | classification-levels | Get all classification levels. |
| GET | ex/jira/{id}/rest/api/3/dashboard | read | dashboards | Get all dashboards. |
| POST | ex/jira/{id}/rest/api/3/dashboard | write | dashboards | Create dashboard. |
| PUT | ex/jira/{id}/rest/api/3/dashboard/bulk/edit | write | dashboards | Bulk edit dashboards. |
| GET | ex/jira/{id}/rest/api/3/dashboard/gadgets | read | dashboards | Get available gadgets. |
| GET | ex/jira/{id}/rest/api/3/dashboard/search | read | dashboards | Search for dashboards. |
| GET | ex/jira/{id}/rest/api/3/dashboard/{id} | read | dashboards | Get dashboard. |
| PUT | ex/jira/{id}/rest/api/3/dashboard/{id} | write | dashboards | Update dashboard. |
| DELETE | ex/jira/{id}/rest/api/3/dashboard/{id} | write | dashboards | Delete dashboard. |
| POST | ex/jira/{id}/rest/api/3/dashboard/{id}/copy | write | dashboards | Copy dashboard. |
| GET | ex/jira/{id}/rest/api/3/dashboard/{id}/gadget | read | dashboards | Get gadgets. |
| POST | ex/jira/{id}/rest/api/3/dashboard/{id}/gadget | write | dashboards | Add gadget to dashboard. |
| PUT | ex/jira/{id}/rest/api/3/dashboard/{id}/gadget/{id} | write | dashboards | Update gadget on dashboard. |
| DELETE | ex/jira/{id}/rest/api/3/dashboard/{id}/gadget/{id} | write | dashboards | Remove gadget from dashboard. |
| GET | ex/jira/{id}/rest/api/3/dashboard/{id}/items/{id}/properties | read | dashboards | Get dashboard item property keys. |
| GET | ex/jira/{id}/rest/api/3/dashboard/{id}/items/{id}/properties/{id} | read | dashboards | Get dashboard item property. |
| PUT | ex/jira/{id}/rest/api/3/dashboard/{id}/items/{id}/properties/{id} | write | dashboards | Set dashboard item property. |
| DELETE | ex/jira/{id}/rest/api/3/dashboard/{id}/items/{id}/properties/{id} | write | dashboards | Delete dashboard item property. |
| GET | ex/jira/{id}/rest/api/3/config/fieldschemes | read | field-schemes | Get field schemes. |
| POST | ex/jira/{id}/rest/api/3/config/fieldschemes | write | field-schemes | Create field scheme. |
| PUT | ex/jira/{id}/rest/api/3/config/fieldschemes/fields | write | field-schemes | Update fields associated with field schemes. |
| DELETE | ex/jira/{id}/rest/api/3/config/fieldschemes/fields | write | field-schemes | Remove fields associated with field schemes. |
| PUT | ex/jira/{id}/rest/api/3/config/fieldschemes/fields/parameters | write | field-schemes | Update field parameters. |
| DELETE | ex/jira/{id}/rest/api/3/config/fieldschemes/fields/parameters | write | field-schemes | Remove field parameters. |
| GET | ex/jira/{id}/rest/api/3/config/fieldschemes/projects | read | field-schemes | Get projects with field schemes. |
| PUT | ex/jira/{id}/rest/api/3/config/fieldschemes/projects | write | field-schemes | Associate projects to field schemes. |
| GET | ex/jira/{id}/rest/api/3/config/fieldschemes/{id} | read | field-schemes | Get field scheme. |
| PUT | ex/jira/{id}/rest/api/3/config/fieldschemes/{id} | write | field-schemes | Update field scheme. |
| DELETE | ex/jira/{id}/rest/api/3/config/fieldschemes/{id} | write | field-schemes | Delete a field scheme. |
| POST | ex/jira/{id}/rest/api/3/config/fieldschemes/{id}/clone | write | field-schemes | Clone field scheme. |
| GET | ex/jira/{id}/rest/api/3/config/fieldschemes/{id}/fields | read | field-schemes | Search field scheme fields. |
| GET | ex/jira/{id}/rest/api/3/config/fieldschemes/{id}/fields/{id}/parameters | read | field-schemes | Get field parameters. |
| GET | ex/jira/{id}/rest/api/3/config/fieldschemes/{id}/projects | read | field-schemes | Search field scheme projects. |
| GET | ex/jira/{id}/rest/api/3/filter/defaultShareScope | read | filter-sharing | Get default share scope. |
| PUT | ex/jira/{id}/rest/api/3/filter/defaultShareScope | write | filter-sharing | Set default share scope. |
| GET | ex/jira/{id}/rest/api/3/filter/{id}/permission | read | filter-sharing | Get share permissions. |
| POST | ex/jira/{id}/rest/api/3/filter/{id}/permission | write | filter-sharing | Add share permission. |
| GET | ex/jira/{id}/rest/api/3/filter/{id}/permission/{id} | read | filter-sharing | Get share permission. |
| DELETE | ex/jira/{id}/rest/api/3/filter/{id}/permission/{id} | write | filter-sharing | Delete share permission. |
| POST | ex/jira/{id}/rest/api/3/filter | write | filters | Create filter. |
| GET | ex/jira/{id}/rest/api/3/filter/favourite | read | filters | Get favorite filters. |
| GET | ex/jira/{id}/rest/api/3/filter/my | read | filters | Get my filters. |
| GET | ex/jira/{id}/rest/api/3/filter/search | read | filters | Search for filters. |
| GET | ex/jira/{id}/rest/api/3/filter/{id} | read | filters | Get filter. |
| PUT | ex/jira/{id}/rest/api/3/filter/{id} | write | filters | Update filter. |
| DELETE | ex/jira/{id}/rest/api/3/filter/{id} | write | filters | Delete filter. |
| GET | ex/jira/{id}/rest/api/3/filter/{id}/columns | read | filters | Get columns. |
| PUT | ex/jira/{id}/rest/api/3/filter/{id}/columns | write | filters | Set columns. |
| DELETE | ex/jira/{id}/rest/api/3/filter/{id}/columns | write | filters | Reset columns. |
| PUT | ex/jira/{id}/rest/api/3/filter/{id}/favourite | write | filters | Add filter as favorite. |
| DELETE | ex/jira/{id}/rest/api/3/filter/{id}/favourite | write | filters | Remove filter as favorite. |
| PUT | ex/jira/{id}/rest/api/3/filter/{id}/owner | write | filters | Change filter owner. |
| GET | ex/jira/{id}/rest/api/3/groupuserpicker | read | group-and-user-picker | Find users and groups. |
| GET | ex/jira/{id}/rest/api/3/group | read | groups | Get group. |
| POST | ex/jira/{id}/rest/api/3/group | write | groups | Create group. |
| DELETE | ex/jira/{id}/rest/api/3/group | write | groups | Remove group. |
| GET | ex/jira/{id}/rest/api/3/group/bulk | read | groups | Bulk get groups. |
| GET | ex/jira/{id}/rest/api/3/group/member | read | groups | Get users from group. |
| POST | ex/jira/{id}/rest/api/3/group/user | write | groups | Add user to group. |
| DELETE | ex/jira/{id}/rest/api/3/group/user | write | groups | Remove user from group. |
| GET | ex/jira/{id}/rest/api/3/groups/picker | read | groups | Find groups. |
| GET | ex/jira/{id}/rest/api/3/attachment/content/{id} | read | issue-attachments | Get attachment content. |
| GET | ex/jira/{id}/rest/api/3/attachment/meta | read | issue-attachments | Get Jira attachment settings. |
| GET | ex/jira/{id}/rest/api/3/attachment/thumbnail/{id} | read | issue-attachments | Get attachment thumbnail. |
| GET | ex/jira/{id}/rest/api/3/attachment/{id} | read | issue-attachments | Get attachment metadata. |
| DELETE | ex/jira/{id}/rest/api/3/attachment/{id} | write | issue-attachments | Delete attachment. |
| GET | ex/jira/{id}/rest/api/3/attachment/{id}/expand/human | read | issue-attachments | Get all metadata for an expanded attachment. |
| GET | ex/jira/{id}/rest/api/3/attachment/{id}/expand/raw | read | issue-attachments | Get contents metadata for an expanded attachment. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/attachments | write | issue-attachments | Add attachment. |
| POST | ex/jira/{id}/rest/api/3/bulk/issues/delete | write | issue-bulk-operations | Bulk delete issues. |
| GET | ex/jira/{id}/rest/api/3/bulk/issues/fields | read | issue-bulk-operations | Get bulk editable fields. |
| POST | ex/jira/{id}/rest/api/3/bulk/issues/fields | write | issue-bulk-operations | Bulk edit issues. |
| POST | ex/jira/{id}/rest/api/3/bulk/issues/move | write | issue-bulk-operations | Bulk move issues. |
| GET | ex/jira/{id}/rest/api/3/bulk/issues/transition | read | issue-bulk-operations | Get available transitions. |
| POST | ex/jira/{id}/rest/api/3/bulk/issues/transition | write | issue-bulk-operations | Bulk transition issue statuses. |
| POST | ex/jira/{id}/rest/api/3/bulk/issues/unwatch | write | issue-bulk-operations | Bulk unwatch issues. |
| POST | ex/jira/{id}/rest/api/3/bulk/issues/watch | write | issue-bulk-operations | Bulk watch issues. |
| GET | ex/jira/{id}/rest/api/3/bulk/queue/{id} | read | issue-bulk-operations | Get bulk issue operation progress. |
| GET | ex/jira/{id}/rest/api/3/comment/{id}/properties | read | issue-comment-properties | Get comment property keys. |
| GET | ex/jira/{id}/rest/api/3/comment/{id}/properties/{id} | read | issue-comment-properties | Get comment property. |
| PUT | ex/jira/{id}/rest/api/3/comment/{id}/properties/{id} | write | issue-comment-properties | Set comment property. |
| DELETE | ex/jira/{id}/rest/api/3/comment/{id}/properties/{id} | write | issue-comment-properties | Delete comment property. |
| POST | ex/jira/{id}/rest/api/3/comment/list | read | issue-comments | Get comments by IDs. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/comment | read | issue-comments | Get comments. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/comment | write | issue-comments | Add comment. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/comment/{id} | read | issue-comments | Get comment. |
| PUT | ex/jira/{id}/rest/api/3/issue/{id}/comment/{id} | write | issue-comments | Update comment. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/comment/{id} | write | issue-comments | Delete comment. |
| PUT | ex/jira/{id}/rest/api/3/field/association | write | issue-custom-field-associations | Create associations. |
| DELETE | ex/jira/{id}/rest/api/3/field/association | write | issue-custom-field-associations | Remove associations. |
| POST | ex/jira/{id}/rest/api/3/app/field/context/configuration/list | read | issue-custom-field-configuration-apps | Bulk get custom field configurations. |
| GET | ex/jira/{id}/rest/api/3/app/field/{id}/context/configuration | read | issue-custom-field-configuration-apps | Get custom field configurations. |
| PUT | ex/jira/{id}/rest/api/3/app/field/{id}/context/configuration | write | issue-custom-field-configuration-apps | Update custom field configurations. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/context | read | issue-custom-field-contexts | Get custom field contexts. |
| POST | ex/jira/{id}/rest/api/3/field/{id}/context | write | issue-custom-field-contexts | Create custom field context. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/context/defaultValue | read | issue-custom-field-contexts | Get custom field contexts default values. |
| PUT | ex/jira/{id}/rest/api/3/field/{id}/context/defaultValue | write | issue-custom-field-contexts | Set custom field contexts default values. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/context/defaultValues | read | issue-custom-field-contexts | Get default values for a custom field grouped by context and issue type. |
| PUT | ex/jira/{id}/rest/api/3/field/{id}/context/defaultValues | write | issue-custom-field-contexts | Set default values for a custom field by context and issue type. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/context/issuetypemapping | read | issue-custom-field-contexts | Get issue types for custom field context. |
| POST | ex/jira/{id}/rest/api/3/field/{id}/context/mapping | read | issue-custom-field-contexts | Get custom field contexts for projects and issue types. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/context/projectmapping | read | issue-custom-field-contexts | Get project mappings for custom field context. |
| PUT | ex/jira/{id}/rest/api/3/field/{id}/context/{id} | write | issue-custom-field-contexts | Update custom field context. |
| DELETE | ex/jira/{id}/rest/api/3/field/{id}/context/{id} | write | issue-custom-field-contexts | Delete custom field context. |
| PUT | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/issuetype | write | issue-custom-field-contexts | Add issue types to context. |
| POST | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/issuetype/remove | write | issue-custom-field-contexts | Remove issue types from context. |
| PUT | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/project | write | issue-custom-field-contexts | Assign custom field context to projects. |
| POST | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/project/remove | write | issue-custom-field-contexts | Remove custom field context from projects. |
| GET | ex/jira/{id}/rest/api/3/customFieldOption/{id} | read | issue-custom-field-options | Get custom field option. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/option | read | issue-custom-field-options | Get custom field options (context). |
| POST | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/option | write | issue-custom-field-options | Create custom field options (context). |
| PUT | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/option | write | issue-custom-field-options | Update custom field options (context). |
| PUT | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/option/move | write | issue-custom-field-options | Reorder custom field options (context). |
| DELETE | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/option/{id} | write | issue-custom-field-options | Delete custom field options (context). |
| DELETE | ex/jira/{id}/rest/api/3/field/{id}/context/{id}/option/{id}/issue | write | issue-custom-field-options | Replace custom field options. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/option | read | issue-custom-field-options-apps | Get all issue field options. |
| POST | ex/jira/{id}/rest/api/3/field/{id}/option | write | issue-custom-field-options-apps | Create issue field option. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/option/suggestions/edit | read | issue-custom-field-options-apps | Get selectable issue field options. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/option/suggestions/search | read | issue-custom-field-options-apps | Get visible issue field options. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/option/{id} | read | issue-custom-field-options-apps | Get issue field option. |
| PUT | ex/jira/{id}/rest/api/3/field/{id}/option/{id} | write | issue-custom-field-options-apps | Update issue field option. |
| DELETE | ex/jira/{id}/rest/api/3/field/{id}/option/{id} | write | issue-custom-field-options-apps | Delete issue field option. |
| DELETE | ex/jira/{id}/rest/api/3/field/{id}/option/{id}/issue | write | issue-custom-field-options-apps | Replace issue field option. |
| POST | ex/jira/{id}/rest/api/3/app/field/value | write | issue-custom-field-values-apps | Update custom fields. |
| PUT | ex/jira/{id}/rest/api/3/app/field/{id}/value | write | issue-custom-field-values-apps | Update custom field value. |
| GET | ex/jira/{id}/rest/api/3/fieldconfiguration | read | issue-field-configurations | Get all field configurations. |
| POST | ex/jira/{id}/rest/api/3/fieldconfiguration | write | issue-field-configurations | Create field configuration. |
| PUT | ex/jira/{id}/rest/api/3/fieldconfiguration/{id} | write | issue-field-configurations | Update field configuration. |
| DELETE | ex/jira/{id}/rest/api/3/fieldconfiguration/{id} | write | issue-field-configurations | Delete field configuration. |
| GET | ex/jira/{id}/rest/api/3/fieldconfiguration/{id}/fields | read | issue-field-configurations | Get field configuration items. |
| PUT | ex/jira/{id}/rest/api/3/fieldconfiguration/{id}/fields | write | issue-field-configurations | Update field configuration items. |
| GET | ex/jira/{id}/rest/api/3/fieldconfigurationscheme | read | issue-field-configurations | Get all field configuration schemes. |
| POST | ex/jira/{id}/rest/api/3/fieldconfigurationscheme | write | issue-field-configurations | Create field configuration scheme. |
| GET | ex/jira/{id}/rest/api/3/fieldconfigurationscheme/mapping | read | issue-field-configurations | Get field configuration issue type items. |
| GET | ex/jira/{id}/rest/api/3/fieldconfigurationscheme/project | read | issue-field-configurations | Get field configuration schemes for projects. |
| PUT | ex/jira/{id}/rest/api/3/fieldconfigurationscheme/project | write | issue-field-configurations | Assign field configuration scheme to project. |
| PUT | ex/jira/{id}/rest/api/3/fieldconfigurationscheme/{id} | write | issue-field-configurations | Update field configuration scheme. |
| DELETE | ex/jira/{id}/rest/api/3/fieldconfigurationscheme/{id} | write | issue-field-configurations | Delete field configuration scheme. |
| PUT | ex/jira/{id}/rest/api/3/fieldconfigurationscheme/{id}/mapping | write | issue-field-configurations | Assign issue types to field configurations. |
| POST | ex/jira/{id}/rest/api/3/fieldconfigurationscheme/{id}/mapping/delete | write | issue-field-configurations | Remove issue types from field configuration scheme. |
| GET | ex/jira/{id}/rest/api/3/field | read | issue-fields | Get fields. |
| POST | ex/jira/{id}/rest/api/3/field | write | issue-fields | Create custom field. |
| GET | ex/jira/{id}/rest/api/3/field/search | read | issue-fields | Get fields paginated. |
| GET | ex/jira/{id}/rest/api/3/field/search/trashed | read | issue-fields | Get fields in trash paginated. |
| PUT | ex/jira/{id}/rest/api/3/field/{id} | write | issue-fields | Update custom field. |
| DELETE | ex/jira/{id}/rest/api/3/field/{id} | write | issue-fields | Delete custom field. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/association/project | read | issue-fields | Get field project associations. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/contexts | read | issue-fields | Get contexts for a field. |
| POST | ex/jira/{id}/rest/api/3/field/{id}/restore | write | issue-fields | Restore custom field from trash. |
| POST | ex/jira/{id}/rest/api/3/field/{id}/trash | write | issue-fields | Move custom field to trash. |
| GET | ex/jira/{id}/rest/api/3/projects/fields | read | issue-fields | Get fields for projects. |
| GET | ex/jira/{id}/rest/api/3/issueLinkType | read | issue-link-types | Get issue link types. |
| POST | ex/jira/{id}/rest/api/3/issueLinkType | write | issue-link-types | Create issue link type. |
| GET | ex/jira/{id}/rest/api/3/issueLinkType/{id} | read | issue-link-types | Get issue link type. |
| PUT | ex/jira/{id}/rest/api/3/issueLinkType/{id} | write | issue-link-types | Update issue link type. |
| DELETE | ex/jira/{id}/rest/api/3/issueLinkType/{id} | write | issue-link-types | Delete issue link type. |
| POST | ex/jira/{id}/rest/api/3/issueLink | write | issue-links | Create issue link. |
| GET | ex/jira/{id}/rest/api/3/issueLink/{id} | read | issue-links | Get issue link. |
| DELETE | ex/jira/{id}/rest/api/3/issueLink/{id} | write | issue-links | Delete issue link. |
| GET | ex/jira/{id}/rest/api/3/settings/columns | read | issue-navigator-settings | Get issue navigator default columns. |
| PUT | ex/jira/{id}/rest/api/3/settings/columns | write | issue-navigator-settings | Set issue navigator default columns. |
| GET | ex/jira/{id}/rest/api/3/notificationscheme | read | issue-notification-schemes | Get notification schemes paginated. |
| POST | ex/jira/{id}/rest/api/3/notificationscheme | write | issue-notification-schemes | Create notification scheme. |
| GET | ex/jira/{id}/rest/api/3/notificationscheme/project | read | issue-notification-schemes | Get projects using notification schemes paginated. |
| GET | ex/jira/{id}/rest/api/3/notificationscheme/{id} | read | issue-notification-schemes | Get notification scheme. |
| PUT | ex/jira/{id}/rest/api/3/notificationscheme/{id} | write | issue-notification-schemes | Update notification scheme. |
| DELETE | ex/jira/{id}/rest/api/3/notificationscheme/{id} | write | issue-notification-schemes | Delete notification scheme. |
| PUT | ex/jira/{id}/rest/api/3/notificationscheme/{id}/notification | write | issue-notification-schemes | Add notifications to notification scheme. |
| DELETE | ex/jira/{id}/rest/api/3/notificationscheme/{id}/notification/{id} | write | issue-notification-schemes | Remove notification from notification scheme. |
| POST | ex/jira/{id}/rest/api/3/forge/panel/action/bulk/async | write | issue-panels | Bulk pin or unpin issue panel to projects. |
| POST | ex/jira/{id}/rest/api/3/forge/panel/action/bulk/status | read | issue-panels | Get issue panel pin status for projects. |
| GET | ex/jira/{id}/rest/api/3/priority | read | issue-priorities | Get priorities. |
| POST | ex/jira/{id}/rest/api/3/priority | write | issue-priorities | Create priority. |
| PUT | ex/jira/{id}/rest/api/3/priority/default | write | issue-priorities | Set default priority. |
| PUT | ex/jira/{id}/rest/api/3/priority/move | write | issue-priorities | Move priorities. |
| GET | ex/jira/{id}/rest/api/3/priority/search | read | issue-priorities | Search priorities. |
| GET | ex/jira/{id}/rest/api/3/priority/{id} | read | issue-priorities | Get priority. |
| PUT | ex/jira/{id}/rest/api/3/priority/{id} | write | issue-priorities | Update priority. |
| DELETE | ex/jira/{id}/rest/api/3/priority/{id} | write | issue-priorities | Delete priority. |
| POST | ex/jira/{id}/rest/api/3/issue/properties | write | issue-properties | Bulk set issues properties by list. |
| POST | ex/jira/{id}/rest/api/3/issue/properties/multi | write | issue-properties | Bulk set issue properties by issue. |
| PUT | ex/jira/{id}/rest/api/3/issue/properties/{id} | write | issue-properties | Bulk set issue property. |
| DELETE | ex/jira/{id}/rest/api/3/issue/properties/{id} | write | issue-properties | Bulk delete issue property. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/properties | read | issue-properties | Get issue property keys. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/properties/{id} | read | issue-properties | Get issue property. |
| PUT | ex/jira/{id}/rest/api/3/issue/{id}/properties/{id} | write | issue-properties | Set issue property. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/properties/{id} | write | issue-properties | Delete issue property. |
| POST | ex/jira/{id}/rest/api/3/redact | write | issue-redaction | Redact. |
| GET | ex/jira/{id}/rest/api/3/redact/status/{id} | read | issue-redaction | Get redaction status. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/remotelink | read | issue-remote-links | Get remote issue links. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/remotelink | write | issue-remote-links | Create or update remote issue link. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/remotelink | write | issue-remote-links | Delete remote issue link by global ID. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/remotelink/{id} | read | issue-remote-links | Get remote issue link by ID. |
| PUT | ex/jira/{id}/rest/api/3/issue/{id}/remotelink/{id} | write | issue-remote-links | Update remote issue link by ID. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/remotelink/{id} | write | issue-remote-links | Delete remote issue link by ID. |
| GET | ex/jira/{id}/rest/api/3/resolution | read | issue-resolutions | Get resolutions. |
| POST | ex/jira/{id}/rest/api/3/resolution | write | issue-resolutions | Create resolution. |
| PUT | ex/jira/{id}/rest/api/3/resolution/default | write | issue-resolutions | Set default resolution. |
| PUT | ex/jira/{id}/rest/api/3/resolution/move | write | issue-resolutions | Move resolutions. |
| GET | ex/jira/{id}/rest/api/3/resolution/search | read | issue-resolutions | Search resolutions. |
| GET | ex/jira/{id}/rest/api/3/resolution/{id} | read | issue-resolutions | Get resolution. |
| PUT | ex/jira/{id}/rest/api/3/resolution/{id} | write | issue-resolutions | Update resolution. |
| DELETE | ex/jira/{id}/rest/api/3/resolution/{id} | write | issue-resolutions | Delete resolution. |
| GET | ex/jira/{id}/rest/api/3/issue/picker | read | issue-search | Get issue picker suggestions. |
| POST | ex/jira/{id}/rest/api/3/jql/match | read | issue-search | Check issues against JQL. |
| GET | ex/jira/{id}/rest/api/3/search | read | issue-search | Search for issues using JQL (GET). |
| POST | ex/jira/{id}/rest/api/3/search | read | issue-search | Search for issues using JQL (POST). |
| POST | ex/jira/{id}/rest/api/3/search/approximate-count | read | issue-search | Count issues using JQL. |
| GET | ex/jira/{id}/rest/api/3/search/jql | read | issue-search | Search for issues using JQL enhanced search (GET). |
| POST | ex/jira/{id}/rest/api/3/search/jql | read | issue-search | Search for issues using JQL enhanced search (POST). |
| GET | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id}/members | read | issue-security-level | Get issue security level members by issue security scheme. |
| GET | ex/jira/{id}/rest/api/3/securitylevel/{id} | read | issue-security-level | Get issue security level. |
| GET | ex/jira/{id}/rest/api/3/issuesecurityschemes | read | issue-security-schemes | Get issue security schemes. |
| POST | ex/jira/{id}/rest/api/3/issuesecurityschemes | write | issue-security-schemes | Create issue security scheme. |
| GET | ex/jira/{id}/rest/api/3/issuesecurityschemes/level | read | issue-security-schemes | Get issue security levels. |
| PUT | ex/jira/{id}/rest/api/3/issuesecurityschemes/level/default | write | issue-security-schemes | Set default issue security levels. |
| GET | ex/jira/{id}/rest/api/3/issuesecurityschemes/level/member | read | issue-security-schemes | Get issue security level members. |
| GET | ex/jira/{id}/rest/api/3/issuesecurityschemes/project | read | issue-security-schemes | Get projects using issue security schemes. |
| PUT | ex/jira/{id}/rest/api/3/issuesecurityschemes/project | write | issue-security-schemes | Associate security scheme to project. |
| GET | ex/jira/{id}/rest/api/3/issuesecurityschemes/search | read | issue-security-schemes | Search issue security schemes. |
| GET | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id} | read | issue-security-schemes | Get issue security scheme. |
| PUT | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id} | write | issue-security-schemes | Update issue security scheme. |
| DELETE | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id} | write | issue-security-schemes | Delete issue security scheme. |
| PUT | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id}/level | write | issue-security-schemes | Add issue security levels. |
| PUT | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id}/level/{id} | write | issue-security-schemes | Update issue security level. |
| DELETE | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id}/level/{id} | write | issue-security-schemes | Remove issue security level. |
| PUT | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id}/level/{id}/member | write | issue-security-schemes | Add issue security level members. |
| DELETE | ex/jira/{id}/rest/api/3/issuesecurityschemes/{id}/level/{id}/member/{id} | write | issue-security-schemes | Remove member from issue security level. |
| GET | ex/jira/{id}/rest/api/3/issuetype/{id}/properties | read | issue-type-properties | Get issue type property keys. |
| GET | ex/jira/{id}/rest/api/3/issuetype/{id}/properties/{id} | read | issue-type-properties | Get issue type property. |
| PUT | ex/jira/{id}/rest/api/3/issuetype/{id}/properties/{id} | write | issue-type-properties | Set issue type property. |
| DELETE | ex/jira/{id}/rest/api/3/issuetype/{id}/properties/{id} | write | issue-type-properties | Delete issue type property. |
| GET | ex/jira/{id}/rest/api/3/issuetypescheme | read | issue-type-schemes | Get all issue type schemes. |
| POST | ex/jira/{id}/rest/api/3/issuetypescheme | write | issue-type-schemes | Create issue type scheme. |
| GET | ex/jira/{id}/rest/api/3/issuetypescheme/mapping | read | issue-type-schemes | Get issue type scheme items. |
| GET | ex/jira/{id}/rest/api/3/issuetypescheme/project | read | issue-type-schemes | Get issue type schemes for projects. |
| PUT | ex/jira/{id}/rest/api/3/issuetypescheme/project | write | issue-type-schemes | Assign issue type scheme to project. |
| PUT | ex/jira/{id}/rest/api/3/issuetypescheme/{id} | write | issue-type-schemes | Update issue type scheme. |
| DELETE | ex/jira/{id}/rest/api/3/issuetypescheme/{id} | write | issue-type-schemes | Delete issue type scheme. |
| PUT | ex/jira/{id}/rest/api/3/issuetypescheme/{id}/issuetype | write | issue-type-schemes | Add issue types to issue type scheme. |
| PUT | ex/jira/{id}/rest/api/3/issuetypescheme/{id}/issuetype/move | write | issue-type-schemes | Change order of issue types. |
| DELETE | ex/jira/{id}/rest/api/3/issuetypescheme/{id}/issuetype/{id} | write | issue-type-schemes | Remove issue type from issue type scheme. |
| GET | ex/jira/{id}/rest/api/3/issuetypescreenscheme | read | issue-type-screen-schemes | Get issue type screen schemes. |
| POST | ex/jira/{id}/rest/api/3/issuetypescreenscheme | write | issue-type-screen-schemes | Create issue type screen scheme. |
| GET | ex/jira/{id}/rest/api/3/issuetypescreenscheme/mapping | read | issue-type-screen-schemes | Get issue type screen scheme items. |
| GET | ex/jira/{id}/rest/api/3/issuetypescreenscheme/project | read | issue-type-screen-schemes | Get issue type screen schemes for projects. |
| PUT | ex/jira/{id}/rest/api/3/issuetypescreenscheme/project | write | issue-type-screen-schemes | Assign issue type screen scheme to project. |
| PUT | ex/jira/{id}/rest/api/3/issuetypescreenscheme/{id} | write | issue-type-screen-schemes | Update issue type screen scheme. |
| DELETE | ex/jira/{id}/rest/api/3/issuetypescreenscheme/{id} | write | issue-type-screen-schemes | Delete issue type screen scheme. |
| PUT | ex/jira/{id}/rest/api/3/issuetypescreenscheme/{id}/mapping | write | issue-type-screen-schemes | Append mappings to issue type screen scheme. |
| PUT | ex/jira/{id}/rest/api/3/issuetypescreenscheme/{id}/mapping/default | write | issue-type-screen-schemes | Update issue type screen scheme default screen scheme. |
| POST | ex/jira/{id}/rest/api/3/issuetypescreenscheme/{id}/mapping/remove | write | issue-type-screen-schemes | Remove mappings from issue type screen scheme. |
| GET | ex/jira/{id}/rest/api/3/issuetypescreenscheme/{id}/project | read | issue-type-screen-schemes | Get issue type screen scheme projects. |
| GET | ex/jira/{id}/rest/api/3/issuetype | read | issue-types | Get all issue types for user. |
| POST | ex/jira/{id}/rest/api/3/issuetype | write | issue-types | Create issue type. |
| GET | ex/jira/{id}/rest/api/3/issuetype/project | read | issue-types | Get issue types for project. |
| GET | ex/jira/{id}/rest/api/3/issuetype/{id} | read | issue-types | Get issue type. |
| PUT | ex/jira/{id}/rest/api/3/issuetype/{id} | write | issue-types | Update issue type. |
| DELETE | ex/jira/{id}/rest/api/3/issuetype/{id} | write | issue-types | Delete issue type. |
| GET | ex/jira/{id}/rest/api/3/issuetype/{id}/alternatives | read | issue-types | Get alternative issue types. |
| POST | ex/jira/{id}/rest/api/3/issuetype/{id}/avatar2 | write | issue-types | Load issue type avatar. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/votes | read | issue-votes | Get votes. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/votes | write | issue-votes | Add vote. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/votes | write | issue-votes | Delete vote. |
| POST | ex/jira/{id}/rest/api/3/issue/watching | read | issue-watchers | Get is watching issue bulk. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/watchers | read | issue-watchers | Get issue watchers. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/watchers | write | issue-watchers | Add watcher. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/watchers | write | issue-watchers | Delete watcher. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id}/properties | read | issue-worklog-properties | Get worklog property keys. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id}/properties/{id} | read | issue-worklog-properties | Get worklog property. |
| PUT | ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id}/properties/{id} | write | issue-worklog-properties | Set worklog property. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id}/properties/{id} | write | issue-worklog-properties | Delete worklog property. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/worklog | read | issue-worklogs | Get issue worklogs. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/worklog | write | issue-worklogs | Add worklog. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/worklog | write | issue-worklogs | Bulk delete worklogs. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/worklog/move | write | issue-worklogs | Bulk move worklogs. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id} | read | issue-worklogs | Get worklog. |
| PUT | ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id} | write | issue-worklogs | Update worklog. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id}/worklog/{id} | write | issue-worklogs | Delete worklog. |
| GET | ex/jira/{id}/rest/api/3/worklog/deleted | read | issue-worklogs | Get IDs of deleted worklogs. |
| POST | ex/jira/{id}/rest/api/3/worklog/list | read | issue-worklogs | Get worklogs. |
| GET | ex/jira/{id}/rest/api/3/worklog/updated | read | issue-worklogs | Get IDs of updated worklogs. |
| POST | ex/jira/{id}/rest/api/3/changelog/bulkfetch | read | issues | Bulk fetch changelogs. |
| GET | ex/jira/{id}/rest/api/3/events | read | issues | Get events. |
| POST | ex/jira/{id}/rest/api/3/issue | write | issues | Create issue. |
| POST | ex/jira/{id}/rest/api/3/issue/archive | write | issues | Archive issue(s) by JQL. |
| PUT | ex/jira/{id}/rest/api/3/issue/archive | write | issues | Archive issue(s) by issue ID/key. |
| POST | ex/jira/{id}/rest/api/3/issue/bulk | write | issues | Bulk create issue. |
| POST | ex/jira/{id}/rest/api/3/issue/bulkfetch | read | issues | Bulk fetch issues. |
| GET | ex/jira/{id}/rest/api/3/issue/createmeta | read | issues | Get create issue metadata. |
| GET | ex/jira/{id}/rest/api/3/issue/createmeta/{id}/issuetypes | read | issues | Get create metadata issue types for a project. |
| GET | ex/jira/{id}/rest/api/3/issue/createmeta/{id}/issuetypes/{id} | read | issues | Get create field metadata for a project and issue type id. |
| GET | ex/jira/{id}/rest/api/3/issue/limit/adf/report | read | issues | Get issue adf limit report. |
| GET | ex/jira/{id}/rest/api/3/issue/limit/report | read | issues | Get issue limit report. |
| PUT | ex/jira/{id}/rest/api/3/issue/unarchive | write | issues | Unarchive issue(s) by issue keys/ID. |
| GET | ex/jira/{id}/rest/api/3/issue/{id} | read | issues | Get issue. |
| PUT | ex/jira/{id}/rest/api/3/issue/{id} | write | issues | Edit issue. |
| DELETE | ex/jira/{id}/rest/api/3/issue/{id} | write | issues | Delete issue. |
| PUT | ex/jira/{id}/rest/api/3/issue/{id}/assignee | write | issues | Assign issue. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/changelog | read | issues | Get changelogs. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/changelog/list | read | issues | Get changelogs by IDs. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/editmeta | read | issues | Get edit issue metadata. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/notify | write | issues | Send notification for issue. |
| GET | ex/jira/{id}/rest/api/3/issue/{id}/transitions | read | issues | Get transitions. |
| POST | ex/jira/{id}/rest/api/3/issue/{id}/transitions | write | issues | Transition issue. |
| PUT | ex/jira/{id}/rest/api/3/issues/archive/export | write | issues | Export archived issue(s). Kept out of read: starts an export task. |
| POST | ex/jira/{id}/rest/api/3/expression/analyse | read | jira-expressions | Analyse Jira expression. |
| POST | ex/jira/{id}/rest/api/3/expression/eval | read | jira-expressions | Evaluate Jira expression. |
| POST | ex/jira/{id}/rest/api/3/expression/evaluate | read | jira-expressions | Evaluate Jira expression using enhanced search API. |
| GET | ex/jira/{id}/rest/api/3/application-properties | read | jira-settings | Get application property. |
| GET | ex/jira/{id}/rest/api/3/application-properties/advanced-settings | read | jira-settings | Get advanced settings. |
| PUT | ex/jira/{id}/rest/api/3/application-properties/{id} | write | jira-settings | Set application property. |
| GET | ex/jira/{id}/rest/api/3/configuration | read | jira-settings | Get global settings. |
| GET | ex/jira/{id}/rest/api/3/invalid-jqls-access-log | read | jql | Get invalid JQL searches. |
| GET | ex/jira/{id}/rest/api/3/jql/autocompletedata | read | jql | Get field reference data (GET). |
| POST | ex/jira/{id}/rest/api/3/jql/autocompletedata | read | jql | Get field reference data (POST). |
| GET | ex/jira/{id}/rest/api/3/jql/autocompletedata/suggestions | read | jql | Get field auto complete suggestions. |
| POST | ex/jira/{id}/rest/api/3/jql/parse | read | jql | Parse JQL query. |
| POST | ex/jira/{id}/rest/api/3/jql/pdcleaner | read | jql | Convert user identifiers to account IDs in JQL queries. |
| POST | ex/jira/{id}/rest/api/3/jql/sanitize | read | jql | Sanitize JQL queries. |
| GET | ex/jira/{id}/rest/api/3/jql/function/computation | read | jql-functions-apps | Get precomputations (apps). |
| POST | ex/jira/{id}/rest/api/3/jql/function/computation | write | jql-functions-apps | Update precomputations (apps). |
| POST | ex/jira/{id}/rest/api/3/jql/function/computation/search | read | jql-functions-apps | Get precomputations by ID (apps). |
| GET | ex/jira/{id}/rest/api/3/label | read | labels | Get all labels. |
| GET | ex/jira/{id}/rest/api/3/instance/license | read | license-metrics | Get license. |
| GET | ex/jira/{id}/rest/api/3/license/approximateLicenseCount | read | license-metrics | Get approximate license count. |
| GET | ex/jira/{id}/rest/api/3/license/approximateLicenseCount/product/{id} | read | license-metrics | Get approximate application license count. |
| GET | ex/jira/{id}/rest/api/3/mypreferences | read | myself | Get preference. |
| PUT | ex/jira/{id}/rest/api/3/mypreferences | write | myself | Set preference. |
| DELETE | ex/jira/{id}/rest/api/3/mypreferences | write | myself | Delete preference. |
| GET | ex/jira/{id}/rest/api/3/mypreferences/locale | read | myself | Get locale. |
| PUT | ex/jira/{id}/rest/api/3/mypreferences/locale | write | myself | Set locale. |
| GET | ex/jira/{id}/rest/api/3/myself | read | myself | Get current user. |
| GET | ex/jira/{id}/rest/api/3/permissionscheme | read | permission-schemes | Get all permission schemes. |
| POST | ex/jira/{id}/rest/api/3/permissionscheme | write | permission-schemes | Create permission scheme. |
| GET | ex/jira/{id}/rest/api/3/permissionscheme/{id} | read | permission-schemes | Get permission scheme. |
| PUT | ex/jira/{id}/rest/api/3/permissionscheme/{id} | write | permission-schemes | Update permission scheme. |
| DELETE | ex/jira/{id}/rest/api/3/permissionscheme/{id} | write | permission-schemes | Delete permission scheme. |
| GET | ex/jira/{id}/rest/api/3/permissionscheme/{id}/permission | read | permission-schemes | Get permission scheme grants. |
| POST | ex/jira/{id}/rest/api/3/permissionscheme/{id}/permission | write | permission-schemes | Create permission grant. |
| GET | ex/jira/{id}/rest/api/3/permissionscheme/{id}/permission/{id} | read | permission-schemes | Get permission scheme grant. |
| DELETE | ex/jira/{id}/rest/api/3/permissionscheme/{id}/permission/{id} | write | permission-schemes | Delete permission scheme grant. |
| GET | ex/jira/{id}/rest/api/3/mypermissions | read | permissions | Get my permissions. |
| GET | ex/jira/{id}/rest/api/3/permissions | read | permissions | Get all permissions. |
| POST | ex/jira/{id}/rest/api/3/permissions/check | read | permissions | Get bulk permissions. |
| POST | ex/jira/{id}/rest/api/3/permissions/project | read | permissions | Get permitted projects. |
| GET | ex/jira/{id}/rest/api/3/plans/plan | read | plans | Get plans paginated. |
| POST | ex/jira/{id}/rest/api/3/plans/plan | write | plans | Create plan. |
| GET | ex/jira/{id}/rest/api/3/plans/plan/{id} | read | plans | Get plan. |
| PUT | ex/jira/{id}/rest/api/3/plans/plan/{id} | write | plans | Update plan. |
| PUT | ex/jira/{id}/rest/api/3/plans/plan/{id}/archive | write | plans | Archive plan. |
| POST | ex/jira/{id}/rest/api/3/plans/plan/{id}/duplicate | write | plans | Duplicate plan. |
| PUT | ex/jira/{id}/rest/api/3/plans/plan/{id}/trash | write | plans | Trash plan. |
| GET | ex/jira/{id}/rest/api/3/policies | read | policies | Get all policies. |
| GET | ex/jira/{id}/rest/api/3/policies/project/{id} | read | policies | Get project policy state. |
| PUT | ex/jira/{id}/rest/api/3/policies/project/{id}/policies | write | policies | Set the policies applied to a project. |
| GET | ex/jira/{id}/rest/api/3/policies/project/{id}/rules | read | policies | Get project policy rules. |
| POST | ex/jira/{id}/rest/api/3/policies/project/{id}/validate | write | policies | Validate policy application to a project. |
| POST | ex/jira/{id}/rest/api/3/policies/{id}/apply | write | policies | Apply a policy to projects. |
| POST | ex/jira/{id}/rest/api/3/policies/{id}/remove | write | policies | Remove a policy from projects. |
| GET | ex/jira/{id}/rest/api/3/priorityscheme | read | priority-schemes | Get priority schemes. |
| POST | ex/jira/{id}/rest/api/3/priorityscheme | write | priority-schemes | Create priority scheme. |
| POST | ex/jira/{id}/rest/api/3/priorityscheme/mappings | write | priority-schemes | Suggested priorities for mappings. |
| GET | ex/jira/{id}/rest/api/3/priorityscheme/priorities/available | read | priority-schemes | Get available priorities by priority scheme. |
| PUT | ex/jira/{id}/rest/api/3/priorityscheme/{id} | write | priority-schemes | Update priority scheme. |
| DELETE | ex/jira/{id}/rest/api/3/priorityscheme/{id} | write | priority-schemes | Delete priority scheme. |
| GET | ex/jira/{id}/rest/api/3/priorityscheme/{id}/priorities | read | priority-schemes | Get priorities by priority scheme. |
| GET | ex/jira/{id}/rest/api/3/priorityscheme/{id}/projects | read | priority-schemes | Get projects by priority scheme. |
| PUT | ex/jira/{id}/rest/api/3/project/{id}/avatar | write | project-avatars | Set project avatar. |
| DELETE | ex/jira/{id}/rest/api/3/project/{id}/avatar/{id} | write | project-avatars | Delete project avatar. |
| POST | ex/jira/{id}/rest/api/3/project/{id}/avatar2 | write | project-avatars | Load project avatar. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/avatars | read | project-avatars | Get all project avatars. |
| GET | ex/jira/{id}/rest/api/3/projectCategory | read | project-categories | Get all project categories. |
| POST | ex/jira/{id}/rest/api/3/projectCategory | write | project-categories | Create project category. |
| GET | ex/jira/{id}/rest/api/3/projectCategory/{id} | read | project-categories | Get project category by ID. |
| PUT | ex/jira/{id}/rest/api/3/projectCategory/{id} | write | project-categories | Update project category. |
| DELETE | ex/jira/{id}/rest/api/3/projectCategory/{id} | write | project-categories | Delete project category. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/classification-config | read | project-classification-levels | Get the classification configuration for a project. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/classification-level/default | read | project-classification-levels | Get the default data classification level of a project. |
| PUT | ex/jira/{id}/rest/api/3/project/{id}/classification-level/default | write | project-classification-levels | Update the default data classification level of a project. |
| DELETE | ex/jira/{id}/rest/api/3/project/{id}/classification-level/default | write | project-classification-levels | Remove the default data classification level from a project. |
| GET | ex/jira/{id}/rest/api/3/component | read | project-components | Find components for projects. |
| POST | ex/jira/{id}/rest/api/3/component | write | project-components | Create component. |
| GET | ex/jira/{id}/rest/api/3/component/{id} | read | project-components | Get component. |
| PUT | ex/jira/{id}/rest/api/3/component/{id} | write | project-components | Update component. |
| DELETE | ex/jira/{id}/rest/api/3/component/{id} | write | project-components | Delete component. |
| GET | ex/jira/{id}/rest/api/3/component/{id}/relatedIssueCounts | read | project-components | Get component issues count. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/component | read | project-components | Get project components paginated. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/components | read | project-components | Get project components. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/email | read | project-email | Get project's sender email. |
| PUT | ex/jira/{id}/rest/api/3/project/{id}/email | write | project-email | Set project's sender email. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/features | read | project-features | Get project features. |
| PUT | ex/jira/{id}/rest/api/3/project/{id}/features/{id} | write | project-features | Set project feature state. |
| GET | ex/jira/{id}/rest/api/3/projectvalidate/key | read | project-key-and-name-validation | Validate project key. |
| GET | ex/jira/{id}/rest/api/3/projectvalidate/validProjectKey | read | project-key-and-name-validation | Get valid project key. |
| GET | ex/jira/{id}/rest/api/3/projectvalidate/validProjectName | read | project-key-and-name-validation | Get valid project name. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/issuesecuritylevelscheme | read | project-permission-schemes | Get project issue security scheme. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/permissionscheme | read | project-permission-schemes | Get assigned permission scheme. |
| PUT | ex/jira/{id}/rest/api/3/project/{id}/permissionscheme | write | project-permission-schemes | Assign permission scheme. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/securitylevel | read | project-permission-schemes | Get project issue security levels. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/properties | read | project-properties | Get project property keys. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/properties/{id} | read | project-properties | Get project property. |
| PUT | ex/jira/{id}/rest/api/3/project/{id}/properties/{id} | write | project-properties | Set project property. |
| DELETE | ex/jira/{id}/rest/api/3/project/{id}/properties/{id} | write | project-properties | Delete project property. |
| POST | ex/jira/{id}/rest/api/3/project/{id}/role/{id} | write | project-role-actors | Add actors to project role. |
| PUT | ex/jira/{id}/rest/api/3/project/{id}/role/{id} | write | project-role-actors | Set actors for project role. |
| DELETE | ex/jira/{id}/rest/api/3/project/{id}/role/{id} | write | project-role-actors | Delete actors from project role. |
| GET | ex/jira/{id}/rest/api/3/role/{id}/actors | read | project-role-actors | Get default actors for project role. |
| POST | ex/jira/{id}/rest/api/3/role/{id}/actors | write | project-role-actors | Add default actors to project role. |
| DELETE | ex/jira/{id}/rest/api/3/role/{id}/actors | write | project-role-actors | Delete default actors from project role. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/role | read | project-roles | Get project roles for project. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/role/{id} | read | project-roles | Get project role for project. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/roledetails | read | project-roles | Get project role details. |
| GET | ex/jira/{id}/rest/api/3/role | read | project-roles | Get all project roles. |
| POST | ex/jira/{id}/rest/api/3/role | write | project-roles | Create project role. |
| GET | ex/jira/{id}/rest/api/3/role/{id} | read | project-roles | Get project role by ID. |
| POST | ex/jira/{id}/rest/api/3/role/{id} | write | project-roles | Partial update project role. |
| PUT | ex/jira/{id}/rest/api/3/role/{id} | write | project-roles | Fully update project role. |
| DELETE | ex/jira/{id}/rest/api/3/role/{id} | write | project-roles | Delete project role. |
| POST | ex/jira/{id}/rest/api/3/project-template | write | project-templates | Create custom project. |
| PUT | ex/jira/{id}/rest/api/3/project-template/edit-template | write | project-templates | Edit a custom project template. |
| GET | ex/jira/{id}/rest/api/3/project-template/live-template | read | project-templates | Gets a custom project template. |
| DELETE | ex/jira/{id}/rest/api/3/project-template/remove-template | write | project-templates | Deletes a custom project template. |
| POST | ex/jira/{id}/rest/api/3/project-template/save-template | write | project-templates | Save a custom project template. |
| GET | ex/jira/{id}/rest/api/3/project/type | read | project-types | Get all project types. |
| GET | ex/jira/{id}/rest/api/3/project/type/accessible | read | project-types | Get licensed project types. |
| GET | ex/jira/{id}/rest/api/3/project/type/{id} | read | project-types | Get project type by key. |
| GET | ex/jira/{id}/rest/api/3/project/type/{id}/accessible | read | project-types | Get accessible project type by key. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/version | read | project-versions | Get project versions paginated. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/versions | read | project-versions | Get project versions. |
| POST | ex/jira/{id}/rest/api/3/version | write | project-versions | Create version. |
| GET | ex/jira/{id}/rest/api/3/version/{id} | read | project-versions | Get version. |
| PUT | ex/jira/{id}/rest/api/3/version/{id} | write | project-versions | Update version. |
| DELETE | ex/jira/{id}/rest/api/3/version/{id} | write | project-versions | Delete version. |
| PUT | ex/jira/{id}/rest/api/3/version/{id}/mergeto/{id} | write | project-versions | Merge versions. |
| POST | ex/jira/{id}/rest/api/3/version/{id}/move | write | project-versions | Move version. |
| GET | ex/jira/{id}/rest/api/3/version/{id}/relatedIssueCounts | read | project-versions | Get version's related issues count. |
| GET | ex/jira/{id}/rest/api/3/version/{id}/relatedwork | read | project-versions | Get related work. |
| POST | ex/jira/{id}/rest/api/3/version/{id}/relatedwork | write | project-versions | Create related work. |
| PUT | ex/jira/{id}/rest/api/3/version/{id}/relatedwork | write | project-versions | Update related work. |
| DELETE | ex/jira/{id}/rest/api/3/version/{id}/relatedwork/{id} | write | project-versions | Delete related work. |
| POST | ex/jira/{id}/rest/api/3/version/{id}/removeAndSwap | write | project-versions | Delete and replace version. |
| GET | ex/jira/{id}/rest/api/3/version/{id}/unresolvedIssueCount | read | project-versions | Get version's unresolved issues count. |
| GET | ex/jira/{id}/rest/api/3/project | read | projects | Get all projects. |
| POST | ex/jira/{id}/rest/api/3/project | write | projects | Create project. |
| GET | ex/jira/{id}/rest/api/3/project/recent | read | projects | Get recent projects. |
| GET | ex/jira/{id}/rest/api/3/project/search | read | projects | Get projects paginated. |
| GET | ex/jira/{id}/rest/api/3/project/{id} | read | projects | Get project. |
| PUT | ex/jira/{id}/rest/api/3/project/{id} | write | projects | Update project. |
| DELETE | ex/jira/{id}/rest/api/3/project/{id} | write | projects | Delete project. |
| POST | ex/jira/{id}/rest/api/3/project/{id}/archive | write | projects | Archive project. |
| POST | ex/jira/{id}/rest/api/3/project/{id}/delete | write | projects | Delete project asynchronously. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/hierarchy | read | projects | Get project issue type hierarchy. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/notificationscheme | read | projects | Get project notification scheme. |
| POST | ex/jira/{id}/rest/api/3/project/{id}/restore | write | projects | Restore deleted or archived project. |
| GET | ex/jira/{id}/rest/api/3/project/{id}/statuses | read | projects | Get all statuses for project. |
| GET | ex/jira/{id}/rest/api/3/screenscheme | read | screen-schemes | Get screen schemes. |
| POST | ex/jira/{id}/rest/api/3/screenscheme | write | screen-schemes | Create screen scheme. |
| PUT | ex/jira/{id}/rest/api/3/screenscheme/{id} | write | screen-schemes | Update screen scheme. |
| DELETE | ex/jira/{id}/rest/api/3/screenscheme/{id} | write | screen-schemes | Delete screen scheme. |
| GET | ex/jira/{id}/rest/api/3/screens/{id}/tabs/{id}/fields | read | screen-tab-fields | Get all screen tab fields. |
| POST | ex/jira/{id}/rest/api/3/screens/{id}/tabs/{id}/fields | write | screen-tab-fields | Add screen tab field. |
| DELETE | ex/jira/{id}/rest/api/3/screens/{id}/tabs/{id}/fields/{id} | write | screen-tab-fields | Remove screen tab field. |
| POST | ex/jira/{id}/rest/api/3/screens/{id}/tabs/{id}/fields/{id}/move | write | screen-tab-fields | Move screen tab field. |
| GET | ex/jira/{id}/rest/api/3/screens/tabs | read | screen-tabs | Get bulk screen tabs. |
| GET | ex/jira/{id}/rest/api/3/screens/{id}/tabs | read | screen-tabs | Get all screen tabs. |
| POST | ex/jira/{id}/rest/api/3/screens/{id}/tabs | write | screen-tabs | Create screen tab. |
| PUT | ex/jira/{id}/rest/api/3/screens/{id}/tabs/{id} | write | screen-tabs | Update screen tab. |
| DELETE | ex/jira/{id}/rest/api/3/screens/{id}/tabs/{id} | write | screen-tabs | Delete screen tab. |
| POST | ex/jira/{id}/rest/api/3/screens/{id}/tabs/{id}/move/{id} | write | screen-tabs | Move screen tab. |
| GET | ex/jira/{id}/rest/api/3/field/{id}/screens | read | screens | Get screens for a field. |
| GET | ex/jira/{id}/rest/api/3/screens | read | screens | Get screens. |
| POST | ex/jira/{id}/rest/api/3/screens | write | screens | Create screen. |
| POST | ex/jira/{id}/rest/api/3/screens/addToDefault/{id} | write | screens | Add field to default screen. |
| PUT | ex/jira/{id}/rest/api/3/screens/{id} | write | screens | Update screen. |
| DELETE | ex/jira/{id}/rest/api/3/screens/{id} | write | screens | Delete screen. |
| GET | ex/jira/{id}/rest/api/3/screens/{id}/availableFields | read | screens | Get available screen fields. |
| GET | ex/jira/{id}/rest/api/3/serverInfo | read | server-info | Get Jira instance info. |
| GET | ex/jira/{id}/rest/api/3/statuses | read | status | Bulk get statuses. |
| POST | ex/jira/{id}/rest/api/3/statuses | write | status | Bulk create statuses. |
| PUT | ex/jira/{id}/rest/api/3/statuses | write | status | Bulk update statuses. |
| DELETE | ex/jira/{id}/rest/api/3/statuses | write | status | Bulk delete Statuses. |
| GET | ex/jira/{id}/rest/api/3/statuses/byNames | read | status | Bulk get statuses by name. |
| GET | ex/jira/{id}/rest/api/3/statuses/search | read | status | Search statuses paginated. |
| GET | ex/jira/{id}/rest/api/3/statuses/{id}/project/{id}/issueTypeUsages | read | status | Get issue type usages by status and project. |
| GET | ex/jira/{id}/rest/api/3/statuses/{id}/projectUsages | read | status | Get project usages by status. |
| GET | ex/jira/{id}/rest/api/3/statuses/{id}/workflowUsages | read | status | Get workflow usages by status. |
| GET | ex/jira/{id}/rest/api/3/task/{id} | read | tasks | Get task. |
| POST | ex/jira/{id}/rest/api/3/task/{id}/cancel | write | tasks | Cancel task. |
| GET | ex/jira/{id}/rest/api/3/plans/plan/{id}/team | read | teams-in-plan | Get teams in plan paginated. |
| POST | ex/jira/{id}/rest/api/3/plans/plan/{id}/team/atlassian | write | teams-in-plan | Add Atlassian team to plan. |
| GET | ex/jira/{id}/rest/api/3/plans/plan/{id}/team/atlassian/{id} | read | teams-in-plan | Get Atlassian team in plan. |
| PUT | ex/jira/{id}/rest/api/3/plans/plan/{id}/team/atlassian/{id} | write | teams-in-plan | Update Atlassian team in plan. |
| DELETE | ex/jira/{id}/rest/api/3/plans/plan/{id}/team/atlassian/{id} | write | teams-in-plan | Remove Atlassian team from plan. |
| POST | ex/jira/{id}/rest/api/3/plans/plan/{id}/team/planonly | write | teams-in-plan | Create plan-only team. |
| GET | ex/jira/{id}/rest/api/3/plans/plan/{id}/team/planonly/{id} | read | teams-in-plan | Get plan-only team. |
| PUT | ex/jira/{id}/rest/api/3/plans/plan/{id}/team/planonly/{id} | write | teams-in-plan | Update plan-only team. |
| DELETE | ex/jira/{id}/rest/api/3/plans/plan/{id}/team/planonly/{id} | write | teams-in-plan | Delete plan-only team. |
| GET | ex/jira/{id}/rest/api/3/configuration/timetracking | read | time-tracking | Get selected time tracking provider. |
| PUT | ex/jira/{id}/rest/api/3/configuration/timetracking | write | time-tracking | Select time tracking provider. |
| GET | ex/jira/{id}/rest/api/3/configuration/timetracking/list | read | time-tracking | Get all time tracking providers. |
| GET | ex/jira/{id}/rest/api/3/configuration/timetracking/options | read | time-tracking | Get time tracking settings. |
| PUT | ex/jira/{id}/rest/api/3/configuration/timetracking/options | write | time-tracking | Set time tracking settings. |
| GET | ex/jira/{id}/rest/api/3/uiModifications | read | ui-modifications-apps | Get UI modifications. |
| POST | ex/jira/{id}/rest/api/3/uiModifications | write | ui-modifications-apps | Create UI modification. |
| PUT | ex/jira/{id}/rest/api/3/uiModifications/{id} | write | ui-modifications-apps | Update UI modification. |
| DELETE | ex/jira/{id}/rest/api/3/uiModifications/{id} | write | ui-modifications-apps | Delete UI modification. |
| GET | ex/jira/{id}/rest/api/3/user/properties | read | user-properties | Get user property keys. |
| GET | ex/jira/{id}/rest/api/3/user/properties/{id} | read | user-properties | Get user property. |
| PUT | ex/jira/{id}/rest/api/3/user/properties/{id} | write | user-properties | Set user property. |
| DELETE | ex/jira/{id}/rest/api/3/user/properties/{id} | write | user-properties | Delete user property. |
| GET | ex/jira/{id}/rest/api/3/user/assignable/multiProjectSearch | read | user-search | Find users assignable to projects. |
| GET | ex/jira/{id}/rest/api/3/user/assignable/search | read | user-search | Find users assignable to issues. |
| GET | ex/jira/{id}/rest/api/3/user/permission/search | read | user-search | Find users with permissions. |
| GET | ex/jira/{id}/rest/api/3/user/picker | read | user-search | Find users for picker. |
| GET | ex/jira/{id}/rest/api/3/user/search | read | user-search | Find users. |
| GET | ex/jira/{id}/rest/api/3/user/search/query | read | user-search | Find users by query. |
| GET | ex/jira/{id}/rest/api/3/user/search/query/key | read | user-search | Find user keys by query. |
| GET | ex/jira/{id}/rest/api/3/user/viewissue/search | read | user-search | Find users with browse permission. |
| GET | ex/jira/{id}/rest/api/3/user | read | users | Get user. |
| POST | ex/jira/{id}/rest/api/3/user | write | users | Create user. |
| DELETE | ex/jira/{id}/rest/api/3/user | write | users | Delete user. |
| GET | ex/jira/{id}/rest/api/3/user/bulk | read | users | Bulk get users. |
| GET | ex/jira/{id}/rest/api/3/user/bulk/migration | read | users | Get account IDs for users. |
| GET | ex/jira/{id}/rest/api/3/user/columns | read | users | Get user default columns. |
| PUT | ex/jira/{id}/rest/api/3/user/columns | write | users | Set user default columns. |
| DELETE | ex/jira/{id}/rest/api/3/user/columns | write | users | Reset user default columns. |
| GET | ex/jira/{id}/rest/api/3/user/email | read | users | Get user email. |
| GET | ex/jira/{id}/rest/api/3/user/email/bulk | read | users | Get user email bulk. |
| GET | ex/jira/{id}/rest/api/3/user/groups | read | users | Get user groups. |
| GET | ex/jira/{id}/rest/api/3/users | read | users | Get all users default. |
| GET | ex/jira/{id}/rest/api/3/users/search | read | users | Get all users. |
| GET | ex/jira/{id}/rest/api/3/webhook | read | webhooks | Get dynamic webhooks for app. |
| POST | ex/jira/{id}/rest/api/3/webhook | write | webhooks | Register dynamic webhooks. |
| DELETE | ex/jira/{id}/rest/api/3/webhook | write | webhooks | Delete webhooks by ID. |
| GET | ex/jira/{id}/rest/api/3/webhook/failed | read | webhooks | Get failed webhooks. |
| PUT | ex/jira/{id}/rest/api/3/webhook/refresh | write | webhooks | Extend webhook life. |
| POST | ex/jira/{id}/rest/api/3/workflowscheme/{id}/createdraft | write | workflow-scheme-drafts | Create draft workflow scheme. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft | read | workflow-scheme-drafts | Get draft workflow scheme. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft | write | workflow-scheme-drafts | Update draft workflow scheme. |
| DELETE | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft | write | workflow-scheme-drafts | Delete draft workflow scheme. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/default | read | workflow-scheme-drafts | Get draft default workflow. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/default | write | workflow-scheme-drafts | Update draft default workflow. |
| DELETE | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/default | write | workflow-scheme-drafts | Delete draft default workflow. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/issuetype/{id} | read | workflow-scheme-drafts | Get workflow for issue type in draft workflow scheme. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/issuetype/{id} | write | workflow-scheme-drafts | Set workflow for issue type in draft workflow scheme. |
| DELETE | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/issuetype/{id} | write | workflow-scheme-drafts | Delete workflow for issue type in draft workflow scheme. |
| POST | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/publish | write | workflow-scheme-drafts | Publish draft workflow scheme. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/workflow | read | workflow-scheme-drafts | Get issue types for workflows in draft workflow scheme. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/workflow | write | workflow-scheme-drafts | Set issue types for workflow in workflow scheme. |
| DELETE | ex/jira/{id}/rest/api/3/workflowscheme/{id}/draft/workflow | write | workflow-scheme-drafts | Delete issue types for workflow in draft workflow scheme. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/project | read | workflow-scheme-project-associations | Get workflow scheme project associations. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/project | write | workflow-scheme-project-associations | Assign workflow scheme to project. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme | read | workflow-schemes | Get all workflow schemes. |
| POST | ex/jira/{id}/rest/api/3/workflowscheme | write | workflow-schemes | Create workflow scheme. |
| POST | ex/jira/{id}/rest/api/3/workflowscheme/project/switch | write | workflow-schemes | Switch workflow scheme for project. |
| POST | ex/jira/{id}/rest/api/3/workflowscheme/read | read | workflow-schemes | Bulk get workflow schemes. |
| POST | ex/jira/{id}/rest/api/3/workflowscheme/update | write | workflow-schemes | Update workflow scheme. |
| POST | ex/jira/{id}/rest/api/3/workflowscheme/update/mappings | read | workflow-schemes | Get required status mappings for workflow scheme update. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id} | read | workflow-schemes | Get workflow scheme. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/{id} | write | workflow-schemes | Classic update workflow scheme. |
| DELETE | ex/jira/{id}/rest/api/3/workflowscheme/{id} | write | workflow-schemes | Delete workflow scheme. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id}/default | read | workflow-schemes | Get default workflow. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/{id}/default | write | workflow-schemes | Update default workflow. |
| DELETE | ex/jira/{id}/rest/api/3/workflowscheme/{id}/default | write | workflow-schemes | Delete default workflow. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id}/issuetype/{id} | read | workflow-schemes | Get workflow for issue type in workflow scheme. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/{id}/issuetype/{id} | write | workflow-schemes | Set workflow for issue type in workflow scheme. |
| DELETE | ex/jira/{id}/rest/api/3/workflowscheme/{id}/issuetype/{id} | write | workflow-schemes | Delete workflow for issue type in workflow scheme. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id}/projectUsages | read | workflow-schemes | Get projects which are using a given workflow scheme. |
| GET | ex/jira/{id}/rest/api/3/workflowscheme/{id}/workflow | read | workflow-schemes | Get issue types for workflows in workflow scheme. |
| PUT | ex/jira/{id}/rest/api/3/workflowscheme/{id}/workflow | write | workflow-schemes | Set issue types for workflow in workflow scheme. |
| DELETE | ex/jira/{id}/rest/api/3/workflowscheme/{id}/workflow | write | workflow-schemes | Delete issue types for workflow in workflow scheme. |
| GET | ex/jira/{id}/rest/api/3/statuscategory | read | workflow-status-categories | Get all status categories. |
| GET | ex/jira/{id}/rest/api/3/statuscategory/{id} | read | workflow-status-categories | Get status category. |
| GET | ex/jira/{id}/rest/api/3/status | read | workflow-statuses | Get all statuses. |
| GET | ex/jira/{id}/rest/api/3/status/{id} | read | workflow-statuses | Get status. |
| GET | ex/jira/{id}/rest/api/3/workflow/rule/config | read | workflow-transition-rules | Get workflow transition rule configurations. |
| PUT | ex/jira/{id}/rest/api/3/workflow/rule/config | write | workflow-transition-rules | Update workflow transition rule configurations. |
| PUT | ex/jira/{id}/rest/api/3/workflow/rule/config/delete | write | workflow-transition-rules | Delete workflow transition rule configurations. |
| POST | ex/jira/{id}/rest/api/3/workflow/history | write | workflows | Read workflow version from history. |
| POST | ex/jira/{id}/rest/api/3/workflow/history/list | read | workflows | List workflow history entries. |
| GET | ex/jira/{id}/rest/api/3/workflow/search | read | workflows | Get workflows paginated. |
| DELETE | ex/jira/{id}/rest/api/3/workflow/{id} | write | workflows | Delete inactive workflow. |
| GET | ex/jira/{id}/rest/api/3/workflow/{id}/project/{id}/issueTypeUsages | read | workflows | Get issue types in a project that are using a given workflow. |
| GET | ex/jira/{id}/rest/api/3/workflow/{id}/projectUsages | read | workflows | Get projects using a given workflow. |
| GET | ex/jira/{id}/rest/api/3/workflow/{id}/workflowSchemes | read | workflows | Get workflow schemes which are using a given workflow. |
| POST | ex/jira/{id}/rest/api/3/workflows | read | workflows | Bulk get workflows. |
| GET | ex/jira/{id}/rest/api/3/workflows/capabilities | read | workflows | Get available workflow capabilities. |
| POST | ex/jira/{id}/rest/api/3/workflows/copy | write | workflows | Copy workflow. |
| POST | ex/jira/{id}/rest/api/3/workflows/create | write | workflows | Bulk create workflows. |
| POST | ex/jira/{id}/rest/api/3/workflows/create/validation | write | workflows | Validate create workflows. |
| GET | ex/jira/{id}/rest/api/3/workflows/defaultEditor | read | workflows | Get the user's default workflow editor. |
| POST | ex/jira/{id}/rest/api/3/workflows/preview | write | workflows | Preview workflow. |
| GET | ex/jira/{id}/rest/api/3/workflows/search | read | workflows | Search workflows. |
| POST | ex/jira/{id}/rest/api/3/workflows/update | write | workflows | Bulk update workflows. |
| POST | ex/jira/{id}/rest/api/3/workflows/update/validation | write | workflows | Validate update workflows. |
