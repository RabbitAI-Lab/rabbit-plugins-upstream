# Pipedrive access policy

An access policy limits which endpoints Pipedrive connections may call through Maton. Pipedrive doesn't offer a choice of OAuth scopes, so an access policy is the way to narrow a connection. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/pipedrive#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Pipedrive: its 213 read-only endpoints. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create pipedrive --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "api/v1/activities"},
    {"method": "GET", "path": "api/v1/activities/collection"},
    {"method": "GET", "path": "api/v1/activities/{id}"},
    {"method": "GET", "path": "api/v2/activities"},
    {"method": "GET", "path": "api/v2/activities/{id}"},
    {"method": "GET", "path": "api/v1/activityFields"},
    {"method": "GET", "path": "api/v2/activityFields"},
    {"method": "GET", "path": "api/v2/activityFields/{id}"},
    {"method": "GET", "path": "api/v1/activityTypes"},
    {"method": "GET", "path": "api/v1/billing/subscriptions/addons"},
    {"method": "GET", "path": "api/v1/callLogs"},
    {"method": "GET", "path": "api/v1/callLogs/{id}"},
    {"method": "GET", "path": "api/v1/currencies"},
    {"method": "GET", "path": "api/v1/dealFields"},
    {"method": "GET", "path": "api/v1/dealFields/{id}"},
    {"method": "GET", "path": "api/v2/dealFields"},
    {"method": "GET", "path": "api/v2/dealFields/{id}"},
    {"method": "GET", "path": "api/v2/deals/installments"},
    {"method": "GET", "path": "api/v2/deals/products"},
    {"method": "GET", "path": "api/v2/deals/{id}/products"},
    {"method": "GET", "path": "api/v1/deals"},
    {"method": "GET", "path": "api/v1/deals/archived"},
    {"method": "GET", "path": "api/v1/deals/collection"},
    {"method": "GET", "path": "api/v1/deals/search"},
    {"method": "GET", "path": "api/v1/deals/summary"},
    {"method": "GET", "path": "api/v1/deals/summary/archived"},
    {"method": "GET", "path": "api/v1/deals/timeline"},
    {"method": "GET", "path": "api/v1/deals/timeline/archived"},
    {"method": "GET", "path": "api/v1/deals/{id}"},
    {"method": "GET", "path": "api/v1/deals/{id}/activities"},
    {"method": "GET", "path": "api/v1/deals/{id}/changelog"},
    {"method": "GET", "path": "api/v1/deals/{id}/files"},
    {"method": "GET", "path": "api/v1/deals/{id}/flow"},
    {"method": "GET", "path": "api/v1/deals/{id}/followers"},
    {"method": "GET", "path": "api/v1/deals/{id}/mailMessages"},
    {"method": "GET", "path": "api/v1/deals/{id}/participants"},
    {"method": "GET", "path": "api/v1/deals/{id}/participantsChangelog"},
    {"method": "GET", "path": "api/v1/deals/{id}/permittedUsers"},
    {"method": "GET", "path": "api/v1/deals/{id}/persons"},
    {"method": "GET", "path": "api/v1/deals/{id}/products"},
    {"method": "GET", "path": "api/v2/deals"},
    {"method": "GET", "path": "api/v2/deals/archived"},
    {"method": "GET", "path": "api/v2/deals/search"},
    {"method": "GET", "path": "api/v2/deals/{id}"},
    {"method": "GET", "path": "api/v2/deals/{id}/convert/status/{id}"},
    {"method": "GET", "path": "api/v2/deals/{id}/discounts"},
    {"method": "GET", "path": "api/v2/deals/{id}/followers"},
    {"method": "GET", "path": "api/v2/deals/{id}/followers/changelog"},
    {"method": "GET", "path": "api/v1/files"},
    {"method": "GET", "path": "api/v1/files/{id}"},
    {"method": "GET", "path": "api/v1/files/{id}/download"},
    {"method": "GET", "path": "api/v1/filters"},
    {"method": "GET", "path": "api/v1/filters/helpers"},
    {"method": "GET", "path": "api/v1/filters/{id}"},
    {"method": "GET", "path": "api/v1/goals/find"},
    {"method": "GET", "path": "api/v1/goals/{id}/results"},
    {"method": "GET", "path": "api/v1/itemSearch"},
    {"method": "GET", "path": "api/v1/itemSearch/field"},
    {"method": "GET", "path": "api/v2/itemSearch"},
    {"method": "GET", "path": "api/v2/itemSearch/field"},
    {"method": "GET", "path": "api/v1/leadFields"},
    {"method": "GET", "path": "api/v1/leadLabels"},
    {"method": "GET", "path": "api/v1/leadSources"},
    {"method": "GET", "path": "api/v1/leads"},
    {"method": "GET", "path": "api/v1/leads/archived"},
    {"method": "GET", "path": "api/v1/leads/search"},
    {"method": "GET", "path": "api/v1/leads/{id}"},
    {"method": "GET", "path": "api/v1/leads/{id}/permittedUsers"},
    {"method": "GET", "path": "api/v2/leads/search"},
    {"method": "GET", "path": "api/v2/leads/{id}/convert/status/{id}"},
    {"method": "GET", "path": "api/v1/legacyTeams"},
    {"method": "GET", "path": "api/v1/legacyTeams/user/{id}"},
    {"method": "GET", "path": "api/v1/legacyTeams/{id}"},
    {"method": "GET", "path": "api/v1/legacyTeams/{id}/users"},
    {"method": "GET", "path": "api/v1/mailbox/mailMessages/{id}"},
    {"method": "GET", "path": "api/v1/mailbox/mailThreads"},
    {"method": "GET", "path": "api/v1/mailbox/mailThreads/{id}"},
    {"method": "GET", "path": "api/v1/mailbox/mailThreads/{id}/mailMessages"},
    {"method": "GET", "path": "api/v1/noteFields"},
    {"method": "GET", "path": "api/v1/notes"},
    {"method": "GET", "path": "api/v1/notes/{id}"},
    {"method": "GET", "path": "api/v1/notes/{id}/comments"},
    {"method": "GET", "path": "api/v1/notes/{id}/comments/{id}"},
    {"method": "GET", "path": "api/v1/organizationFields"},
    {"method": "GET", "path": "api/v1/organizationFields/{id}"},
    {"method": "GET", "path": "api/v2/organizationFields"},
    {"method": "GET", "path": "api/v2/organizationFields/{id}"},
    {"method": "GET", "path": "api/v1/organizationRelationships"},
    {"method": "GET", "path": "api/v1/organizationRelationships/{id}"},
    {"method": "GET", "path": "api/v1/organizations"},
    {"method": "GET", "path": "api/v1/organizations/collection"},
    {"method": "GET", "path": "api/v1/organizations/search"},
    {"method": "GET", "path": "api/v1/organizations/{id}"},
    {"method": "GET", "path": "api/v1/organizations/{id}/activities"},
    {"method": "GET", "path": "api/v1/organizations/{id}/changelog"},
    {"method": "GET", "path": "api/v1/organizations/{id}/deals"},
    {"method": "GET", "path": "api/v1/organizations/{id}/files"},
    {"method": "GET", "path": "api/v1/organizations/{id}/flow"},
    {"method": "GET", "path": "api/v1/organizations/{id}/followers"},
    {"method": "GET", "path": "api/v1/organizations/{id}/mailMessages"},
    {"method": "GET", "path": "api/v1/organizations/{id}/permittedUsers"},
    {"method": "GET", "path": "api/v1/organizations/{id}/persons"},
    {"method": "GET", "path": "api/v2/organizations"},
    {"method": "GET", "path": "api/v2/organizations/search"},
    {"method": "GET", "path": "api/v2/organizations/{id}"},
    {"method": "GET", "path": "api/v2/organizations/{id}/followers"},
    {"method": "GET", "path": "api/v2/organizations/{id}/followers/changelog"},
    {"method": "GET", "path": "api/v1/permissionSets"},
    {"method": "GET", "path": "api/v1/permissionSets/{id}"},
    {"method": "GET", "path": "api/v1/permissionSets/{id}/assignments"},
    {"method": "GET", "path": "api/v1/personFields"},
    {"method": "GET", "path": "api/v1/personFields/{id}"},
    {"method": "GET", "path": "api/v2/personFields"},
    {"method": "GET", "path": "api/v2/personFields/{id}"},
    {"method": "GET", "path": "api/v1/persons"},
    {"method": "GET", "path": "api/v1/persons/collection"},
    {"method": "GET", "path": "api/v1/persons/search"},
    {"method": "GET", "path": "api/v1/persons/{id}"},
    {"method": "GET", "path": "api/v1/persons/{id}/activities"},
    {"method": "GET", "path": "api/v1/persons/{id}/changelog"},
    {"method": "GET", "path": "api/v1/persons/{id}/deals"},
    {"method": "GET", "path": "api/v1/persons/{id}/files"},
    {"method": "GET", "path": "api/v1/persons/{id}/flow"},
    {"method": "GET", "path": "api/v1/persons/{id}/followers"},
    {"method": "GET", "path": "api/v1/persons/{id}/mailMessages"},
    {"method": "GET", "path": "api/v1/persons/{id}/permittedUsers"},
    {"method": "GET", "path": "api/v1/persons/{id}/products"},
    {"method": "GET", "path": "api/v2/persons"},
    {"method": "GET", "path": "api/v2/persons/search"},
    {"method": "GET", "path": "api/v2/persons/{id}"},
    {"method": "GET", "path": "api/v2/persons/{id}/followers"},
    {"method": "GET", "path": "api/v2/persons/{id}/followers/changelog"},
    {"method": "GET", "path": "api/v2/persons/{id}/picture"},
    {"method": "GET", "path": "api/v1/pipelines"},
    {"method": "GET", "path": "api/v1/pipelines/{id}"},
    {"method": "GET", "path": "api/v1/pipelines/{id}/conversion_statistics"},
    {"method": "GET", "path": "api/v1/pipelines/{id}/deals"},
    {"method": "GET", "path": "api/v1/pipelines/{id}/movement_statistics"},
    {"method": "GET", "path": "api/v2/pipelines"},
    {"method": "GET", "path": "api/v2/pipelines/{id}"},
    {"method": "GET", "path": "api/v1/productFields"},
    {"method": "GET", "path": "api/v1/productFields/{id}"},
    {"method": "GET", "path": "api/v2/productFields"},
    {"method": "GET", "path": "api/v2/productFields/{id}"},
    {"method": "GET", "path": "api/v1/products"},
    {"method": "GET", "path": "api/v1/products/search"},
    {"method": "GET", "path": "api/v1/products/{id}"},
    {"method": "GET", "path": "api/v1/products/{id}/deals"},
    {"method": "GET", "path": "api/v1/products/{id}/files"},
    {"method": "GET", "path": "api/v1/products/{id}/followers"},
    {"method": "GET", "path": "api/v1/products/{id}/permittedUsers"},
    {"method": "GET", "path": "api/v2/products"},
    {"method": "GET", "path": "api/v2/products/search"},
    {"method": "GET", "path": "api/v2/products/{id}"},
    {"method": "GET", "path": "api/v2/products/{id}/followers"},
    {"method": "GET", "path": "api/v2/products/{id}/followers/changelog"},
    {"method": "GET", "path": "api/v2/products/{id}/images"},
    {"method": "GET", "path": "api/v2/products/{id}/variations"},
    {"method": "GET", "path": "api/v1/projects/boards"},
    {"method": "GET", "path": "api/v1/projects/boards/{id}"},
    {"method": "GET", "path": "api/v2/boards"},
    {"method": "GET", "path": "api/v2/boards/{id}"},
    {"method": "GET", "path": "api/v2/projectFields"},
    {"method": "GET", "path": "api/v2/projectFields/{id}"},
    {"method": "GET", "path": "api/v1/projects/phases"},
    {"method": "GET", "path": "api/v1/projects/phases/{id}"},
    {"method": "GET", "path": "api/v2/phases"},
    {"method": "GET", "path": "api/v2/phases/{id}"},
    {"method": "GET", "path": "api/v1/projectTemplates"},
    {"method": "GET", "path": "api/v1/projectTemplates/{id}"},
    {"method": "GET", "path": "api/v2/projectTemplates"},
    {"method": "GET", "path": "api/v2/projectTemplates/{id}"},
    {"method": "GET", "path": "api/v1/projects"},
    {"method": "GET", "path": "api/v1/projects/{id}"},
    {"method": "GET", "path": "api/v1/projects/{id}/activities"},
    {"method": "GET", "path": "api/v1/projects/{id}/groups"},
    {"method": "GET", "path": "api/v1/projects/{id}/plan"},
    {"method": "GET", "path": "api/v1/projects/{id}/tasks"},
    {"method": "GET", "path": "api/v2/projects"},
    {"method": "GET", "path": "api/v2/projects/archived"},
    {"method": "GET", "path": "api/v2/projects/search"},
    {"method": "GET", "path": "api/v2/projects/{id}"},
    {"method": "GET", "path": "api/v2/projects/{id}/changelog"},
    {"method": "GET", "path": "api/v2/projects/{id}/permittedUsers"},
    {"method": "GET", "path": "api/v1/recents"},
    {"method": "GET", "path": "api/v1/roles"},
    {"method": "GET", "path": "api/v1/roles/{id}"},
    {"method": "GET", "path": "api/v1/roles/{id}/assignments"},
    {"method": "GET", "path": "api/v1/roles/{id}/pipelines"},
    {"method": "GET", "path": "api/v1/roles/{id}/settings"},
    {"method": "GET", "path": "api/v1/stages"},
    {"method": "GET", "path": "api/v1/stages/{id}"},
    {"method": "GET", "path": "api/v1/stages/{id}/deals"},
    {"method": "GET", "path": "api/v2/stages"},
    {"method": "GET", "path": "api/v2/stages/{id}"},
    {"method": "GET", "path": "api/v1/subscriptions/find/{id}"},
    {"method": "GET", "path": "api/v1/subscriptions/{id}"},
    {"method": "GET", "path": "api/v1/subscriptions/{id}/payments"},
    {"method": "GET", "path": "api/v1/tasks"},
    {"method": "GET", "path": "api/v1/tasks/{id}"},
    {"method": "GET", "path": "api/v2/tasks"},
    {"method": "GET", "path": "api/v2/tasks/{id}"},
    {"method": "GET", "path": "api/v1/userConnections"},
    {"method": "GET", "path": "api/v1/userSettings"},
    {"method": "GET", "path": "api/v1/users"},
    {"method": "GET", "path": "api/v1/users/find"},
    {"method": "GET", "path": "api/v1/users/me"},
    {"method": "GET", "path": "api/v1/users/{id}"},
    {"method": "GET", "path": "api/v1/users/{id}/followers"},
    {"method": "GET", "path": "api/v1/users/{id}/permissions"},
    {"method": "GET", "path": "api/v1/users/{id}/roleAssignments"},
    {"method": "GET", "path": "api/v1/users/{id}/roleSettings"},
    {"method": "GET", "path": "api/v2/users/{id}/followers"}
  ],
  "deny": []
}
```

## Endpoints

The Pipedrive endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | api/v1/activities | read | activities | Get all activities assigned to a particular user (legacy v1). |
| POST | api/v1/activities | write | activities | Add an activity (legacy v1). |
| DELETE | api/v1/activities | write | activities | Delete multiple activities in bulk (legacy v1). |
| GET | api/v1/activities/collection | read | activities | Get all activities collection (legacy v1). |
| GET | api/v1/activities/{id} | read | activities | Get details of an activity (legacy v1). |
| PUT | api/v1/activities/{id} | write | activities | Update an activity (legacy v1). |
| DELETE | api/v1/activities/{id} | write | activities | Delete an activity (legacy v1). |
| GET | api/v2/activities | read | activities | Get all activities (v2). |
| POST | api/v2/activities | write | activities | Add a new activity (v2). |
| GET | api/v2/activities/{id} | read | activities | Get details of an activity (v2). |
| PATCH | api/v2/activities/{id} | write | activities | Update an activity (v2). |
| DELETE | api/v2/activities/{id} | write | activities | Delete an activity (v2). |
| GET | api/v1/activityFields | read | activity fields | Get all activity fields. |
| GET | api/v2/activityFields | read | activity fields | Get all activity fields (v2). |
| GET | api/v2/activityFields/{id} | read | activity fields | Get one activity field (v2). |
| GET | api/v1/activityTypes | read | activity types | Get all activity types. |
| POST | api/v1/activityTypes | write | activity types | Add new activity type. |
| DELETE | api/v1/activityTypes | write | activity types | Delete multiple activity types in bulk (legacy v1). |
| PUT | api/v1/activityTypes/{id} | write | activity types | Update an activity type. |
| DELETE | api/v1/activityTypes/{id} | write | activity types | Delete an activity type. |
| GET | api/v1/billing/subscriptions/addons | read | billing | Get all add-ons for a single company. |
| GET | api/v1/callLogs | read | call logs | Get all call logs assigned to a particular user. |
| POST | api/v1/callLogs | write | call logs | Add a call log. |
| GET | api/v1/callLogs/{id} | read | call logs | Get details of a call log. |
| DELETE | api/v1/callLogs/{id} | write | call logs | Delete a call log. |
| POST | api/v1/callLogs/{id}/recordings | write | call logs | Attach an audio file to the call log. |
| POST | api/v1/channels | write | channels | Add a channel (deprecated). |
| POST | api/v1/channels/messages/receive | write | channels | Receives an incoming message (deprecated). |
| DELETE | api/v1/channels/{id} | write | channels | Delete a channel (deprecated). |
| DELETE | api/v1/channels/{id}/conversations/{id} | write | channels | Delete a conversation (deprecated). |
| GET | api/v1/currencies | read | currencies | Get all supported currencies. |
| GET | api/v1/dealFields | read | deal fields | Get all deal fields. |
| POST | api/v1/dealFields | write | deal fields | Add a new deal field. |
| DELETE | api/v1/dealFields | write | deal fields | Delete multiple deal fields in bulk. |
| GET | api/v1/dealFields/{id} | read | deal fields | Get one deal field. |
| PUT | api/v1/dealFields/{id} | write | deal fields | Update a deal field. |
| DELETE | api/v1/dealFields/{id} | write | deal fields | Delete a deal field. |
| GET | api/v2/dealFields | read | deal fields | Get all deal fields (v2). |
| POST | api/v2/dealFields | write | deal fields | Create one deal field (v2). |
| GET | api/v2/dealFields/{id} | read | deal fields | Get one deal field (v2). |
| PATCH | api/v2/dealFields/{id} | write | deal fields | Update one deal field (v2). |
| DELETE | api/v2/dealFields/{id} | write | deal fields | Delete one deal field (v2). |
| POST | api/v2/dealFields/{id}/options | write | deal fields | Add deal field options in bulk (v2). |
| PATCH | api/v2/dealFields/{id}/options | write | deal fields | Update deal field options in bulk (v2). |
| DELETE | api/v2/dealFields/{id}/options | write | deal fields | Delete deal field options in bulk (v2). |
| GET | api/v2/deals/installments | read | deal installments | List installments added to a list of deals (v2). |
| POST | api/v2/deals/{id}/installments | write | deal installments | Add an installment to a deal (v2). |
| PATCH | api/v2/deals/{id}/installments/{id} | write | deal installments | Update an installment added to a deal (v2). |
| DELETE | api/v2/deals/{id}/installments/{id} | write | deal installments | Delete an installment from a deal (v2). |
| GET | api/v2/deals/products | read | deal products | Get deal products of several deals (v2). |
| GET | api/v2/deals/{id}/products | read | deal products | List products attached to a deal (v2). |
| POST | api/v2/deals/{id}/products | write | deal products | Add a product to a deal (v2). |
| DELETE | api/v2/deals/{id}/products | write | deal products | Delete many products from a deal (v2). |
| POST | api/v2/deals/{id}/products/bulk | write | deal products | Add multiple products to a deal (v2). |
| PATCH | api/v2/deals/{id}/products/{id} | write | deal products | Update the product attached to a deal (v2). |
| DELETE | api/v2/deals/{id}/products/{id} | write | deal products | Delete an attached product from a deal (v2). |
| GET | api/v1/deals | read | deals | Get all deals (legacy v1). |
| POST | api/v1/deals | write | deals | Add a deal (legacy v1). |
| DELETE | api/v1/deals | write | deals | Delete multiple deals in bulk (legacy v1). |
| GET | api/v1/deals/archived | read | deals | Get all archived deals (deprecated). |
| GET | api/v1/deals/collection | read | deals | Get all deals collection (legacy v1). |
| GET | api/v1/deals/search | read | deals | Search deals (legacy v1). |
| GET | api/v1/deals/summary | read | deals | Get deals summary. |
| GET | api/v1/deals/summary/archived | read | deals | Get archived deals summary (deprecated). |
| GET | api/v1/deals/timeline | read | deals | Get deals timeline. |
| GET | api/v1/deals/timeline/archived | read | deals | Get archived deals timeline (deprecated). |
| GET | api/v1/deals/{id} | read | deals | Get details of a deal (legacy v1). |
| PUT | api/v1/deals/{id} | write | deals | Update a deal (legacy v1). |
| DELETE | api/v1/deals/{id} | write | deals | Delete a deal (legacy v1). |
| GET | api/v1/deals/{id}/activities | read | deals | List activities associated with a deal (legacy v1). |
| GET | api/v1/deals/{id}/changelog | read | deals | List updates about deal field values. |
| POST | api/v1/deals/{id}/duplicate | write | deals | Duplicate deal. |
| GET | api/v1/deals/{id}/files | read | deals | List files attached to a deal. |
| GET | api/v1/deals/{id}/flow | read | deals | List updates about a deal. |
| GET | api/v1/deals/{id}/followers | read | deals | List followers of a deal. |
| POST | api/v1/deals/{id}/followers | write | deals | Add a follower to a deal. |
| DELETE | api/v1/deals/{id}/followers/{id} | write | deals | Delete a follower from a deal. |
| GET | api/v1/deals/{id}/mailMessages | read | deals | List mail messages associated with a deal. |
| PUT | api/v1/deals/{id}/merge | write | deals | Merge two deals. |
| GET | api/v1/deals/{id}/participants | read | deals | List participants of a deal. |
| POST | api/v1/deals/{id}/participants | write | deals | Add a participant to a deal. |
| DELETE | api/v1/deals/{id}/participants/{id} | write | deals | Delete a participant from a deal. |
| GET | api/v1/deals/{id}/participantsChangelog | read | deals | List updates about participants of a deal. |
| GET | api/v1/deals/{id}/permittedUsers | read | deals | List permitted users. |
| GET | api/v1/deals/{id}/persons | read | deals | List all persons associated with a deal (legacy v1). |
| GET | api/v1/deals/{id}/products | read | deals | List products attached to a deal (legacy v1). |
| POST | api/v1/deals/{id}/products | write | deals | Add a product to a deal (legacy v1). |
| PUT | api/v1/deals/{id}/products/{id} | write | deals | Update the product attached to a deal (legacy v1). |
| DELETE | api/v1/deals/{id}/products/{id} | write | deals | Delete an attached product from a deal (legacy v1). |
| GET | api/v2/deals | read | deals | Get all deals (v2). |
| POST | api/v2/deals | write | deals | Add a new deal (v2). |
| GET | api/v2/deals/archived | read | deals | Get all archived deals (v2). |
| GET | api/v2/deals/search | read | deals | Search deals (v2). |
| GET | api/v2/deals/{id} | read | deals | Get details of a deal (v2). |
| PATCH | api/v2/deals/{id} | write | deals | Update a deal (v2). |
| DELETE | api/v2/deals/{id} | write | deals | Delete a deal (v2). |
| POST | api/v2/deals/{id}/convert/lead | write | deals | Convert a deal to a lead (v2). |
| GET | api/v2/deals/{id}/convert/status/{id} | read | deals | Get Deal conversion status (v2). |
| GET | api/v2/deals/{id}/discounts | read | deals | List discounts added to a deal (v2). |
| POST | api/v2/deals/{id}/discounts | write | deals | Add a discount to a deal (v2). |
| PATCH | api/v2/deals/{id}/discounts/{id} | write | deals | Update a discount added to a deal (v2). |
| DELETE | api/v2/deals/{id}/discounts/{id} | write | deals | Delete a discount from a deal (v2). |
| GET | api/v2/deals/{id}/followers | read | deals | List followers of a deal (v2). |
| POST | api/v2/deals/{id}/followers | write | deals | Add a follower to a deal (v2). |
| GET | api/v2/deals/{id}/followers/changelog | read | deals | List followers changelog of a deal (v2). |
| DELETE | api/v2/deals/{id}/followers/{id} | write | deals | Delete a follower from a deal (v2). |
| GET | api/v1/files | read | files | Get all files. |
| POST | api/v1/files | write | files | Add file. |
| POST | api/v1/files/remote | write | files | Create a remote file and link it to an item. |
| POST | api/v1/files/remoteLink | write | files | Link a remote file to an item. |
| GET | api/v1/files/{id} | read | files | Get one file. |
| PUT | api/v1/files/{id} | write | files | Update file details. |
| DELETE | api/v1/files/{id} | write | files | Delete a file. |
| GET | api/v1/files/{id}/download | read | files | Download one file. |
| GET | api/v1/filters | read | filters | Get all filters. |
| POST | api/v1/filters | write | filters | Add a new filter. |
| DELETE | api/v1/filters | write | filters | Delete multiple filters in bulk. |
| GET | api/v1/filters/helpers | read | filters | Get all filter helpers. |
| GET | api/v1/filters/{id} | read | filters | Get one filter. |
| PUT | api/v1/filters/{id} | write | filters | Update filter. |
| DELETE | api/v1/filters/{id} | write | filters | Delete a filter. |
| POST | api/v1/goals | write | goals | Add a new goal. |
| GET | api/v1/goals/find | read | goals | Find goals. |
| PUT | api/v1/goals/{id} | write | goals | Update existing goal. |
| DELETE | api/v1/goals/{id} | write | goals | Delete existing goal. |
| GET | api/v1/goals/{id}/results | read | goals | Get result of a goal. |
| GET | api/v1/itemSearch | read | item search | Perform a search from multiple item types (legacy v1). |
| GET | api/v1/itemSearch/field | read | item search | Perform a search using a specific field from an item type (legacy v1). |
| GET | api/v2/itemSearch | read | item search | Perform a search from multiple item types (v2). |
| GET | api/v2/itemSearch/field | read | item search | Perform a search using a specific field from an item type (v2). |
| GET | api/v1/leadFields | read | lead fields | Get all lead fields. |
| GET | api/v1/leadLabels | read | lead labels | Get all lead labels. |
| POST | api/v1/leadLabels | write | lead labels | Add a lead label. |
| PATCH | api/v1/leadLabels/{id} | write | lead labels | Update a lead label. |
| DELETE | api/v1/leadLabels/{id} | write | lead labels | Delete a lead label. |
| GET | api/v1/leadSources | read | lead sources | Get all lead sources. |
| GET | api/v1/leads | read | leads | Get all leads. |
| POST | api/v1/leads | write | leads | Add a lead. |
| GET | api/v1/leads/archived | read | leads | Get all archived leads. |
| GET | api/v1/leads/search | read | leads | Search leads. |
| GET | api/v1/leads/{id} | read | leads | Get one lead. |
| PATCH | api/v1/leads/{id} | write | leads | Update a lead. |
| DELETE | api/v1/leads/{id} | write | leads | Delete a lead. |
| GET | api/v1/leads/{id}/permittedUsers | read | leads | List permitted users. |
| GET | api/v2/leads/search | read | leads | Search leads (v2). |
| POST | api/v2/leads/{id}/convert/deal | write | leads | Convert a lead to a deal (v2). |
| GET | api/v2/leads/{id}/convert/status/{id} | read | leads | Get Lead conversion status (v2). |
| GET | api/v1/legacyTeams | read | legacy teams | Get all teams. |
| POST | api/v1/legacyTeams | write | legacy teams | Add a new team. |
| GET | api/v1/legacyTeams/user/{id} | read | legacy teams | Get all teams of a user. |
| GET | api/v1/legacyTeams/{id} | read | legacy teams | Get a single team. |
| PUT | api/v1/legacyTeams/{id} | write | legacy teams | Update a team. |
| GET | api/v1/legacyTeams/{id}/users | read | legacy teams | Get all users in a team. |
| POST | api/v1/legacyTeams/{id}/users | write | legacy teams | Add users to a team. |
| DELETE | api/v1/legacyTeams/{id}/users | write | legacy teams | Delete users from a team. |
| GET | api/v1/mailbox/mailMessages/{id} | read | mailbox | Get one mail message. |
| GET | api/v1/mailbox/mailThreads | read | mailbox | Get mail threads. |
| GET | api/v1/mailbox/mailThreads/{id} | read | mailbox | Get one mail thread. |
| PUT | api/v1/mailbox/mailThreads/{id} | write | mailbox | Update mail thread details. |
| DELETE | api/v1/mailbox/mailThreads/{id} | write | mailbox | Delete mail thread. |
| GET | api/v1/mailbox/mailThreads/{id}/mailMessages | read | mailbox | Get all mail messages of mail thread. |
| POST | api/v1/meetings/userProviderLinks | write | meetings | Link a user with the installed video call integration. |
| DELETE | api/v1/meetings/userProviderLinks/{id} | write | meetings | Delete the link between a user and the installed video call integration. |
| GET | api/v1/noteFields | read | note fields | Get all note fields. |
| GET | api/v1/notes | read | notes | Get all notes. |
| POST | api/v1/notes | write | notes | Add a note. |
| GET | api/v1/notes/{id} | read | notes | Get one note. |
| PUT | api/v1/notes/{id} | write | notes | Update a note. |
| DELETE | api/v1/notes/{id} | write | notes | Delete a note. |
| GET | api/v1/notes/{id}/comments | read | notes | Get all comments for a note. |
| POST | api/v1/notes/{id}/comments | write | notes | Add a comment to a note. |
| GET | api/v1/notes/{id}/comments/{id} | read | notes | Get one comment. |
| PUT | api/v1/notes/{id}/comments/{id} | write | notes | Update a comment related to a note. |
| DELETE | api/v1/notes/{id}/comments/{id} | write | notes | Delete a comment related to a note. |
| GET | api/v1/organizationFields | read | organization fields | Get all organization fields. |
| POST | api/v1/organizationFields | write | organization fields | Add a new organization field. |
| DELETE | api/v1/organizationFields | write | organization fields | Delete multiple organization fields in bulk. |
| GET | api/v1/organizationFields/{id} | read | organization fields | Get one organization field. |
| PUT | api/v1/organizationFields/{id} | write | organization fields | Update an organization field. |
| DELETE | api/v1/organizationFields/{id} | write | organization fields | Delete an organization field. |
| GET | api/v2/organizationFields | read | organization fields | Get all organization fields (v2). |
| POST | api/v2/organizationFields | write | organization fields | Create one organization field (v2). |
| GET | api/v2/organizationFields/{id} | read | organization fields | Get one organization field (v2). |
| PATCH | api/v2/organizationFields/{id} | write | organization fields | Update one organization field (v2). |
| DELETE | api/v2/organizationFields/{id} | write | organization fields | Delete one organization field (v2). |
| POST | api/v2/organizationFields/{id}/options | write | organization fields | Add organization field options in bulk (v2). |
| PATCH | api/v2/organizationFields/{id}/options | write | organization fields | Update organization field options in bulk (v2). |
| DELETE | api/v2/organizationFields/{id}/options | write | organization fields | Delete organization field options in bulk (v2). |
| GET | api/v1/organizationRelationships | read | organization relationships | Get all relationships for organization. |
| POST | api/v1/organizationRelationships | write | organization relationships | Create an organization relationship. |
| GET | api/v1/organizationRelationships/{id} | read | organization relationships | Get one organization relationship. |
| PUT | api/v1/organizationRelationships/{id} | write | organization relationships | Update an organization relationship. |
| DELETE | api/v1/organizationRelationships/{id} | write | organization relationships | Delete an organization relationship. |
| GET | api/v1/organizations | read | organizations | Get all organizations (legacy v1). |
| POST | api/v1/organizations | write | organizations | Add an organization (legacy v1). |
| DELETE | api/v1/organizations | write | organizations | Delete multiple organizations in bulk (legacy v1). |
| GET | api/v1/organizations/collection | read | organizations | Get all organizations collection (legacy v1). |
| GET | api/v1/organizations/search | read | organizations | Search organizations (legacy v1). |
| GET | api/v1/organizations/{id} | read | organizations | Get details of an organization (legacy v1). |
| PUT | api/v1/organizations/{id} | write | organizations | Update an organization (legacy v1). |
| DELETE | api/v1/organizations/{id} | write | organizations | Delete an organization (legacy v1). |
| GET | api/v1/organizations/{id}/activities | read | organizations | List activities associated with an organization (legacy v1). |
| GET | api/v1/organizations/{id}/changelog | read | organizations | List updates about organization field values. |
| GET | api/v1/organizations/{id}/deals | read | organizations | List deals associated with an organization (legacy v1). |
| GET | api/v1/organizations/{id}/files | read | organizations | List files attached to an organization. |
| GET | api/v1/organizations/{id}/flow | read | organizations | List updates about an organization. |
| GET | api/v1/organizations/{id}/followers | read | organizations | List followers of an organization. |
| POST | api/v1/organizations/{id}/followers | write | organizations | Add a follower to an organization. |
| DELETE | api/v1/organizations/{id}/followers/{id} | write | organizations | Delete a follower from an organization. |
| GET | api/v1/organizations/{id}/mailMessages | read | organizations | List mail messages associated with an organization. |
| PUT | api/v1/organizations/{id}/merge | write | organizations | Merge two organizations. |
| GET | api/v1/organizations/{id}/permittedUsers | read | organizations | List permitted users. |
| GET | api/v1/organizations/{id}/persons | read | organizations | List persons of an organization (legacy v1). |
| GET | api/v2/organizations | read | organizations | Get all organizations (v2). |
| POST | api/v2/organizations | write | organizations | Add a new organization (v2). |
| GET | api/v2/organizations/search | read | organizations | Search organizations (v2). |
| GET | api/v2/organizations/{id} | read | organizations | Get details of a organization (v2). |
| PATCH | api/v2/organizations/{id} | write | organizations | Update a organization (v2). |
| DELETE | api/v2/organizations/{id} | write | organizations | Delete a organization (v2). |
| GET | api/v2/organizations/{id}/followers | read | organizations | List followers of an organization (v2). |
| POST | api/v2/organizations/{id}/followers | write | organizations | Add a follower to an organization (v2). |
| GET | api/v2/organizations/{id}/followers/changelog | read | organizations | List followers changelog of an organization (v2). |
| DELETE | api/v2/organizations/{id}/followers/{id} | write | organizations | Delete a follower from an organization (v2). |
| GET | api/v1/permissionSets | read | permission sets | Get all permission sets. |
| GET | api/v1/permissionSets/{id} | read | permission sets | Get one permission set. |
| GET | api/v1/permissionSets/{id}/assignments | read | permission sets | List permission set assignments. |
| GET | api/v1/personFields | read | person fields | Get all person fields. |
| POST | api/v1/personFields | write | person fields | Add a new person field. |
| DELETE | api/v1/personFields | write | person fields | Delete multiple person fields in bulk. |
| GET | api/v1/personFields/{id} | read | person fields | Get one person field. |
| PUT | api/v1/personFields/{id} | write | person fields | Update a person field. |
| DELETE | api/v1/personFields/{id} | write | person fields | Delete a person field. |
| GET | api/v2/personFields | read | person fields | Get all person fields (v2). |
| POST | api/v2/personFields | write | person fields | Create one person field (v2). |
| GET | api/v2/personFields/{id} | read | person fields | Get one person field (v2). |
| PATCH | api/v2/personFields/{id} | write | person fields | Update one person field (v2). |
| DELETE | api/v2/personFields/{id} | write | person fields | Delete one person field (v2). |
| POST | api/v2/personFields/{id}/options | write | person fields | Add person field options in bulk (v2). |
| PATCH | api/v2/personFields/{id}/options | write | person fields | Update person field options in bulk (v2). |
| DELETE | api/v2/personFields/{id}/options | write | person fields | Delete person field options in bulk (v2). |
| GET | api/v1/persons | read | persons | Get all persons (legacy v1). |
| POST | api/v1/persons | write | persons | Add a person (legacy v1). |
| DELETE | api/v1/persons | write | persons | Delete multiple persons in bulk (legacy v1). |
| GET | api/v1/persons/collection | read | persons | Get all persons collection (legacy v1). |
| GET | api/v1/persons/search | read | persons | Search persons (legacy v1). |
| GET | api/v1/persons/{id} | read | persons | Get details of a person (legacy v1). |
| PUT | api/v1/persons/{id} | write | persons | Update a person (legacy v1). |
| DELETE | api/v1/persons/{id} | write | persons | Delete a person (legacy v1). |
| GET | api/v1/persons/{id}/activities | read | persons | List activities associated with a person (legacy v1). |
| GET | api/v1/persons/{id}/changelog | read | persons | List updates about person field values. |
| GET | api/v1/persons/{id}/deals | read | persons | List deals associated with a person (legacy v1). |
| GET | api/v1/persons/{id}/files | read | persons | List files attached to a person. |
| GET | api/v1/persons/{id}/flow | read | persons | List updates about a person. |
| GET | api/v1/persons/{id}/followers | read | persons | List followers of a person. |
| POST | api/v1/persons/{id}/followers | write | persons | Add a follower to a person. |
| DELETE | api/v1/persons/{id}/followers/{id} | write | persons | Delete a follower from a person. |
| GET | api/v1/persons/{id}/mailMessages | read | persons | List mail messages associated with a person. |
| PUT | api/v1/persons/{id}/merge | write | persons | Merge two persons. |
| GET | api/v1/persons/{id}/permittedUsers | read | persons | List permitted users. |
| POST | api/v1/persons/{id}/picture | write | persons | Add person picture. |
| DELETE | api/v1/persons/{id}/picture | write | persons | Delete person picture. |
| GET | api/v1/persons/{id}/products | read | persons | List products associated with a person. |
| GET | api/v2/persons | read | persons | Get all persons (v2). |
| POST | api/v2/persons | write | persons | Add a new person (v2). |
| GET | api/v2/persons/search | read | persons | Search persons (v2). |
| GET | api/v2/persons/{id} | read | persons | Get details of a person (v2). |
| PATCH | api/v2/persons/{id} | write | persons | Update a person (v2). |
| DELETE | api/v2/persons/{id} | write | persons | Delete a person (v2). |
| GET | api/v2/persons/{id}/followers | read | persons | List followers of a person (v2). |
| POST | api/v2/persons/{id}/followers | write | persons | Add a follower to a person (v2). |
| GET | api/v2/persons/{id}/followers/changelog | read | persons | List followers changelog of a person (v2). |
| DELETE | api/v2/persons/{id}/followers/{id} | write | persons | Delete a follower from a person (v2). |
| GET | api/v2/persons/{id}/picture | read | persons | Get picture of a person (v2). |
| GET | api/v1/pipelines | read | pipelines | Get all pipelines (legacy v1). |
| POST | api/v1/pipelines | write | pipelines | Add a new pipeline (legacy v1). |
| GET | api/v1/pipelines/{id} | read | pipelines | Get one pipeline (legacy v1). |
| PUT | api/v1/pipelines/{id} | write | pipelines | Update a pipeline (legacy v1). |
| DELETE | api/v1/pipelines/{id} | write | pipelines | Delete a pipeline (legacy v1). |
| GET | api/v1/pipelines/{id}/conversion_statistics | read | pipelines | Get deals conversion rates in pipeline. |
| GET | api/v1/pipelines/{id}/deals | read | pipelines | Get deals in a pipeline (deprecated). |
| GET | api/v1/pipelines/{id}/movement_statistics | read | pipelines | Get deals movements in pipeline. |
| GET | api/v2/pipelines | read | pipelines | Get all pipelines (v2). |
| POST | api/v2/pipelines | write | pipelines | Add a new pipeline (v2). |
| GET | api/v2/pipelines/{id} | read | pipelines | Get one pipeline (v2). |
| PATCH | api/v2/pipelines/{id} | write | pipelines | Update a pipeline (v2). |
| DELETE | api/v2/pipelines/{id} | write | pipelines | Delete a pipeline (v2). |
| GET | api/v1/productFields | read | product fields | Get all product fields. |
| POST | api/v1/productFields | write | product fields | Add a new product field. |
| DELETE | api/v1/productFields | write | product fields | Delete multiple product fields in bulk. |
| GET | api/v1/productFields/{id} | read | product fields | Get one product field. |
| PUT | api/v1/productFields/{id} | write | product fields | Update a product field. |
| DELETE | api/v1/productFields/{id} | write | product fields | Delete a product field. |
| GET | api/v2/productFields | read | product fields | Get all product fields (v2). |
| POST | api/v2/productFields | write | product fields | Create one product field (v2). |
| GET | api/v2/productFields/{id} | read | product fields | Get one product field (v2). |
| PATCH | api/v2/productFields/{id} | write | product fields | Update one product field (v2). |
| DELETE | api/v2/productFields/{id} | write | product fields | Delete one product field (v2). |
| POST | api/v2/productFields/{id}/options | write | product fields | Add product field options in bulk (v2). |
| PATCH | api/v2/productFields/{id}/options | write | product fields | Update product field options in bulk (v2). |
| DELETE | api/v2/productFields/{id}/options | write | product fields | Delete product field options in bulk (v2). |
| GET | api/v1/products | read | products | Get all products (legacy v1). |
| POST | api/v1/products | write | products | Add a product (legacy v1). |
| GET | api/v1/products/search | read | products | Search products (legacy v1). |
| GET | api/v1/products/{id} | read | products | Get one product (legacy v1). |
| PUT | api/v1/products/{id} | write | products | Update a product (legacy v1). |
| DELETE | api/v1/products/{id} | write | products | Delete a product (legacy v1). |
| GET | api/v1/products/{id}/deals | read | products | Get deals where a product is attached to. |
| GET | api/v1/products/{id}/files | read | products | List files attached to a product. |
| GET | api/v1/products/{id}/followers | read | products | List followers of a product. |
| POST | api/v1/products/{id}/followers | write | products | Add a follower to a product. |
| DELETE | api/v1/products/{id}/followers/{id} | write | products | Delete a follower from a product. |
| GET | api/v1/products/{id}/permittedUsers | read | products | List permitted users. |
| GET | api/v2/products | read | products | Get all products (v2). |
| POST | api/v2/products | write | products | Add a product (v2). |
| GET | api/v2/products/search | read | products | Search products (v2). |
| GET | api/v2/products/{id} | read | products | Get one product (v2). |
| PATCH | api/v2/products/{id} | write | products | Update a product (v2). |
| DELETE | api/v2/products/{id} | write | products | Delete a product (v2). |
| POST | api/v2/products/{id}/duplicate | write | products | Duplicate a product (v2). |
| GET | api/v2/products/{id}/followers | read | products | List followers of a product (v2). |
| POST | api/v2/products/{id}/followers | write | products | Add a follower to a product (v2). |
| GET | api/v2/products/{id}/followers/changelog | read | products | List followers changelog of a product (v2). |
| DELETE | api/v2/products/{id}/followers/{id} | write | products | Delete a follower from a product (v2). |
| GET | api/v2/products/{id}/images | read | products | Get image of a product (v2). |
| POST | api/v2/products/{id}/images | write | products | Upload an image for a product (v2). |
| PUT | api/v2/products/{id}/images | write | products | Update an image for a product (v2). |
| DELETE | api/v2/products/{id}/images | write | products | Delete an image of a product (v2). |
| GET | api/v2/products/{id}/variations | read | products | Get all product variations (v2). |
| POST | api/v2/products/{id}/variations | write | products | Add a product variation (v2). |
| PATCH | api/v2/products/{id}/variations/{id} | write | products | Update a product variation (v2). |
| DELETE | api/v2/products/{id}/variations/{id} | write | products | Delete a product variation (v2). |
| GET | api/v1/projects/boards | read | project boards | Get all project boards. |
| GET | api/v1/projects/boards/{id} | read | project boards | Get details of a board. |
| GET | api/v2/boards | read | project boards | Get all project boards (v2). |
| POST | api/v2/boards | write | project boards | Add a project board (v2). |
| GET | api/v2/boards/{id} | read | project boards | Get details of a project board (v2). |
| PATCH | api/v2/boards/{id} | write | project boards | Update a project board (v2). |
| DELETE | api/v2/boards/{id} | write | project boards | Delete a project board (v2). |
| GET | api/v2/projectFields | read | project fields | Get all project fields (v2). |
| POST | api/v2/projectFields | write | project fields | Create one project field (v2). |
| GET | api/v2/projectFields/{id} | read | project fields | Get one project field (v2). |
| PATCH | api/v2/projectFields/{id} | write | project fields | Update one project field (v2). |
| DELETE | api/v2/projectFields/{id} | write | project fields | Delete one project field (v2). |
| POST | api/v2/projectFields/{id}/options | write | project fields | Add project field options in bulk (v2). |
| PATCH | api/v2/projectFields/{id}/options | write | project fields | Update project field options in bulk (v2). |
| DELETE | api/v2/projectFields/{id}/options | write | project fields | Delete project field options in bulk (v2). |
| GET | api/v1/projects/phases | read | project phases | Get project phases. |
| GET | api/v1/projects/phases/{id} | read | project phases | Get details of a phase. |
| GET | api/v2/phases | read | project phases | Get project phases (v2). |
| POST | api/v2/phases | write | project phases | Add a project phase (v2). |
| GET | api/v2/phases/{id} | read | project phases | Get details of a project phase (v2). |
| PATCH | api/v2/phases/{id} | write | project phases | Update a project phase (v2). |
| DELETE | api/v2/phases/{id} | write | project phases | Delete a project phase (v2). |
| GET | api/v1/projectTemplates | read | project templates | Get all project templates. |
| GET | api/v1/projectTemplates/{id} | read | project templates | Get details of a template. |
| GET | api/v2/projectTemplates | read | project templates | Get all project templates (v2). |
| GET | api/v2/projectTemplates/{id} | read | project templates | Get details of a template (v2). |
| GET | api/v1/projects | read | projects | Get all projects. |
| POST | api/v1/projects | write | projects | Add a project. |
| GET | api/v1/projects/{id} | read | projects | Get details of a project. |
| PUT | api/v1/projects/{id} | write | projects | Update a project. |
| DELETE | api/v1/projects/{id} | write | projects | Delete a project. |
| GET | api/v1/projects/{id}/activities | read | projects | Returns project activities. |
| POST | api/v1/projects/{id}/archive | write | projects | Archive a project. |
| GET | api/v1/projects/{id}/groups | read | projects | Returns project groups. |
| GET | api/v1/projects/{id}/plan | read | projects | Returns project plan. |
| PUT | api/v1/projects/{id}/plan/activities/{id} | write | projects | Update activity in project plan. |
| PUT | api/v1/projects/{id}/plan/tasks/{id} | write | projects | Update task in project plan. |
| GET | api/v1/projects/{id}/tasks | read | projects | Returns project tasks. |
| GET | api/v2/projects | read | projects | Get all projects (v2). |
| POST | api/v2/projects | write | projects | Add a project (v2). |
| GET | api/v2/projects/archived | read | projects | Get all archived projects (v2). |
| GET | api/v2/projects/search | read | projects | Search projects (v2). |
| GET | api/v2/projects/{id} | read | projects | Get details of a project (v2). |
| PATCH | api/v2/projects/{id} | write | projects | Update a project (v2). |
| DELETE | api/v2/projects/{id} | write | projects | Delete a project (v2). |
| POST | api/v2/projects/{id}/archive | write | projects | Archive a project (v2). |
| GET | api/v2/projects/{id}/changelog | read | projects | List updates about project field values (v2). |
| GET | api/v2/projects/{id}/permittedUsers | read | projects | List permitted users (v2). |
| GET | api/v1/recents | read | recents | Get recents. |
| GET | api/v1/roles | read | roles | Get all roles. |
| POST | api/v1/roles | write | roles | Add a role. |
| GET | api/v1/roles/{id} | read | roles | Get one role. |
| PUT | api/v1/roles/{id} | write | roles | Update role details. |
| DELETE | api/v1/roles/{id} | write | roles | Delete a role. |
| GET | api/v1/roles/{id}/assignments | read | roles | List role assignments. |
| POST | api/v1/roles/{id}/assignments | write | roles | Add role assignment. |
| DELETE | api/v1/roles/{id}/assignments | write | roles | Delete a role assignment. |
| GET | api/v1/roles/{id}/pipelines | read | roles | List pipeline visibility for a role. |
| PUT | api/v1/roles/{id}/pipelines | write | roles | Update pipeline visibility for a role. |
| GET | api/v1/roles/{id}/settings | read | roles | List role settings. |
| POST | api/v1/roles/{id}/settings | write | roles | Add or update role setting. |
| GET | api/v1/stages | read | stages | Get all stages (legacy v1). |
| POST | api/v1/stages | write | stages | Add a new stage (legacy v1). |
| DELETE | api/v1/stages | write | stages | Delete multiple stages in bulk (legacy v1). |
| GET | api/v1/stages/{id} | read | stages | Get one stage (legacy v1). |
| PUT | api/v1/stages/{id} | write | stages | Update stage details (legacy v1). |
| DELETE | api/v1/stages/{id} | write | stages | Delete a stage (legacy v1). |
| GET | api/v1/stages/{id}/deals | read | stages | Get deals in a stage (deprecated). |
| GET | api/v2/stages | read | stages | Get all stages (v2). |
| POST | api/v2/stages | write | stages | Add a new stage (v2). |
| GET | api/v2/stages/{id} | read | stages | Get one stage (v2). |
| PATCH | api/v2/stages/{id} | write | stages | Update stage details (v2). |
| DELETE | api/v2/stages/{id} | write | stages | Delete a stage (v2). |
| GET | api/v1/subscriptions/find/{id} | read | subscriptions | Find subscription by deal (legacy v1). |
| POST | api/v1/subscriptions/installment | write | subscriptions | Add an installment subscription (legacy v1). |
| PUT | api/v1/subscriptions/installment/{id} | write | subscriptions | Update an installment subscription (legacy v1). |
| POST | api/v1/subscriptions/recurring | write | subscriptions | Add a recurring subscription (legacy v1). |
| PUT | api/v1/subscriptions/recurring/{id} | write | subscriptions | Update a recurring subscription (legacy v1). |
| PUT | api/v1/subscriptions/recurring/{id}/cancel | write | subscriptions | Cancel a recurring subscription (legacy v1). |
| GET | api/v1/subscriptions/{id} | read | subscriptions | Get details of a subscription (legacy v1). |
| DELETE | api/v1/subscriptions/{id} | write | subscriptions | Delete a subscription (legacy v1). |
| GET | api/v1/subscriptions/{id}/payments | read | subscriptions | Get all payments of a subscription (legacy v1). |
| GET | api/v1/tasks | read | tasks | Get all tasks. |
| POST | api/v1/tasks | write | tasks | Add a task. |
| GET | api/v1/tasks/{id} | read | tasks | Get details of a task. |
| PUT | api/v1/tasks/{id} | write | tasks | Update a task. |
| DELETE | api/v1/tasks/{id} | write | tasks | Delete a task. |
| GET | api/v2/tasks | read | tasks | Get all tasks (v2). |
| POST | api/v2/tasks | write | tasks | Add a task (v2). |
| GET | api/v2/tasks/{id} | read | tasks | Get details of a task (v2). |
| PATCH | api/v2/tasks/{id} | write | tasks | Update a task (v2). |
| DELETE | api/v2/tasks/{id} | write | tasks | Delete a task (v2). |
| GET | api/v1/userConnections | read | user connections | Get all user connections. |
| GET | api/v1/userSettings | read | user settings | List settings of an authorized user. |
| GET | api/v1/users | read | users | Get all users. |
| POST | api/v1/users | write | users | Add a new user. |
| GET | api/v1/users/find | read | users | Find users by name. |
| GET | api/v1/users/me | read | users | Get current user data. |
| GET | api/v1/users/{id} | read | users | Get one user. |
| PUT | api/v1/users/{id} | write | users | Update user details. |
| GET | api/v1/users/{id}/followers | read | users | List followers of a user. |
| GET | api/v1/users/{id}/permissions | read | users | List user permissions. |
| GET | api/v1/users/{id}/roleAssignments | read | users | List role assignments. |
| GET | api/v1/users/{id}/roleSettings | read | users | List user role settings. |
| GET | api/v2/users/{id}/followers | read | users | List followers of a user (v2). |
| GET | api/v1/webhooks | write | webhooks | List webhooks; kept out of read because the response includes each webhook’s HTTP basic-auth password. |
| POST | api/v1/webhooks | write | webhooks | Create a new Webhook. |
| DELETE | api/v1/webhooks/{id} | write | webhooks | Delete existing Webhook. |
