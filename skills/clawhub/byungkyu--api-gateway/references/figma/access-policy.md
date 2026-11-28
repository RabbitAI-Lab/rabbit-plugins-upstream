# Figma access policy

An access policy limits which endpoints Figma connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/figma#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Figma: its 40 read-only endpoints. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create figma --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v1/activity_logs"},
    {"method": "GET", "path": "v1/ai_usage/daily"},
    {"method": "GET", "path": "v1/analytics/libraries/{id}/component/actions"},
    {"method": "GET", "path": "v1/analytics/libraries/{id}/component/usages"},
    {"method": "GET", "path": "v1/analytics/libraries/{id}/style/actions"},
    {"method": "GET", "path": "v1/analytics/libraries/{id}/style/usages"},
    {"method": "GET", "path": "v1/analytics/libraries/{id}/variable/actions"},
    {"method": "GET", "path": "v1/analytics/libraries/{id}/variable/usages"},
    {"method": "GET", "path": "v1/files/{id}/comments"},
    {"method": "GET", "path": "v1/files/{id}/comments/{id}/reactions"},
    {"method": "GET", "path": "v1/component_sets/{id}"},
    {"method": "GET", "path": "v1/files/{id}/component_sets"},
    {"method": "GET", "path": "v1/teams/{id}/component_sets"},
    {"method": "GET", "path": "v1/components/{id}"},
    {"method": "GET", "path": "v1/files/{id}/components"},
    {"method": "GET", "path": "v1/teams/{id}/components"},
    {"method": "GET", "path": "v1/files/{id}/dev_resources"},
    {"method": "POST", "path": "v1/developer_logs"},
    {"method": "GET", "path": "v1/files/{id}"},
    {"method": "GET", "path": "v1/files/{id}/images"},
    {"method": "GET", "path": "v1/files/{id}/meta"},
    {"method": "GET", "path": "v1/files/{id}/nodes"},
    {"method": "GET", "path": "v1/images/{id}"},
    {"method": "GET", "path": "v2/folders/{id}/files"},
    {"method": "GET", "path": "v2/folders/{id}/folders"},
    {"method": "GET", "path": "v2/folders/{id}/meta"},
    {"method": "GET", "path": "v2/teams/{id}/folders"},
    {"method": "GET", "path": "v1/oembed"},
    {"method": "GET", "path": "v1/payments"},
    {"method": "GET", "path": "v1/projects/{id}/files"},
    {"method": "GET", "path": "v1/projects/{id}/meta"},
    {"method": "GET", "path": "v1/teams/{id}/projects"},
    {"method": "GET", "path": "v1/files/{id}/styles"},
    {"method": "GET", "path": "v1/styles/{id}"},
    {"method": "GET", "path": "v1/teams/{id}/styles"},
    {"method": "GET", "path": "v1/teams/{id}"},
    {"method": "GET", "path": "v1/me"},
    {"method": "GET", "path": "v1/files/{id}/variables/local"},
    {"method": "GET", "path": "v1/files/{id}/variables/published"},
    {"method": "GET", "path": "v1/files/{id}/versions"}
  ],
  "deny": []
}
```

## Endpoints

The Figma endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v1/activity_logs | read | activity_logs | Returns a list of activity log events. |
| GET | v1/ai_usage/daily | read | ai_usage | Returns per-user, per-day AI credit usage for the plan associated with the calling token. |
| GET | v1/analytics/libraries/{id}/component/actions | read | analytics | Returns a list of library analytics component actions data broken down by the requested dimension. |
| GET | v1/analytics/libraries/{id}/component/usages | read | analytics | Returns a list of library analytics component usage data broken down by the requested dimension. |
| GET | v1/analytics/libraries/{id}/style/actions | read | analytics | Returns a list of library analytics style actions data broken down by the requested dimension. |
| GET | v1/analytics/libraries/{id}/style/usages | read | analytics | Returns a list of library analytics style usage data broken down by the requested dimension. |
| GET | v1/analytics/libraries/{id}/variable/actions | read | analytics | Returns a list of library analytics variable actions data broken down by the requested dimension. |
| GET | v1/analytics/libraries/{id}/variable/usages | read | analytics | Returns a list of library analytics variable usage data broken down by the requested dimension. |
| GET | v1/files/{id}/comments | read | comments | Gets a list of comments left on the file. |
| POST | v1/files/{id}/comments | write | comments | Posts a new comment on the file. |
| DELETE | v1/files/{id}/comments/{id} | write | comments | Deletes a specific comment. |
| GET | v1/files/{id}/comments/{id}/reactions | read | comments | Gets a paginated list of reactions left on the comment. |
| POST | v1/files/{id}/comments/{id}/reactions | write | comments | Posts a new comment reaction on a file comment. |
| DELETE | v1/files/{id}/comments/{id}/reactions | write | comments | Deletes a specific comment reaction. |
| GET | v1/component_sets/{id} | read | component_sets | Get metadata on a published component set by key. |
| GET | v1/files/{id}/component_sets | read | component_sets | Get a list of published component sets within a file library. |
| GET | v1/teams/{id}/component_sets | read | component_sets | Get a paginated list of published component sets within a team library. |
| GET | v1/components/{id} | read | components | Get metadata on a component by key. |
| GET | v1/files/{id}/components | read | components | Get a list of published components within a file library. |
| GET | v1/teams/{id}/components | read | components | Get a paginated list of published components within a team library. |
| POST | v1/dev_resources | write | dev_resources | Bulk create dev resources across multiple files. |
| PUT | v1/dev_resources | write | dev_resources | Bulk update dev resources across multiple files. |
| GET | v1/files/{id}/dev_resources | read | dev_resources | Get dev resources in a file. |
| DELETE | v1/files/{id}/dev_resources/{id} | write | dev_resources | Delete a dev resource from a file. |
| POST | v1/developer_logs | read | developer_logs | Returns a list of developer log entries for REST API and MCP server requests made within the organization. |
| GET | v1/files/{id} | read | files | Returns the document identified by file_key as a JSON object. |
| POST | v1/files/{id}/duplicate | write | files | Duplicates a main file or branch into the specified folder as a new standalone file. |
| GET | v1/files/{id}/images | read | files | Returns download links for all images present in image fills in a document. |
| GET | v1/files/{id}/meta | read | files | Get file metadata. |
| GET | v1/files/{id}/nodes | read | files | Returns the nodes referenced to by ids as a JSON object. |
| GET | v1/images/{id} | read | files | Renders images from a file. |
| POST | v1/teams/{id}/folders | write | folders | Creates a top-level folder in a team. |
| GET | v2/folders/{id}/files | read | folders | Get a list of the files directly within the specified folder. |
| GET | v2/folders/{id}/folders | read | folders | Get a list of the direct subfolders within the specified folder. |
| GET | v2/folders/{id}/meta | read | folders | Get metadata for a folder (name, thumbnail, file count, timestamps) without enumerating its files. |
| GET | v2/teams/{id}/folders | read | folders | Get a list of the top-level folders (previously called "projects") within the specified team. |
| GET | v1/oembed | read | oembed | Returns oEmbed data for a Figma file or published Make site URL, following the oEmbed specification. |
| GET | v1/payments | read | payments | Returns payment information for a user of a plugin, widget or Community file. |
| GET | v1/projects/{id}/files | read | projects | Deprecated in favor of Get files in a folder. |
| GET | v1/projects/{id}/meta | read | projects | Deprecated in favor of Get folder metadata. |
| GET | v1/teams/{id}/projects | read | projects | Deprecated in favor of Get top-level folders in a team. |
| GET | v1/files/{id}/styles | read | styles | Get a list of published styles within a file library. |
| GET | v1/styles/{id} | read | styles | Get metadata on a style by key. |
| GET | v1/teams/{id}/styles | read | styles | Get a paginated list of published styles within a team library. |
| POST | v1/teams | write | teams | Creates a team in the Enterprise plan associated with a private OAuth app. |
| GET | v1/teams/{id} | read | teams | Returns metadata for a team the caller can access. |
| POST | v1/teams/{id}/invites | write | teams | Invites users to a team with the requested role. |
| GET | v1/me | read | users | Returns the user information for the currently authenticated user. |
| POST | v1/files/{id}/variables | write | variables | Creates, modifies and deletes variables, collections and modes in a file. |
| GET | v1/files/{id}/variables/local | read | variables | Returns the local variables and variable collections of a file. |
| GET | v1/files/{id}/variables/published | read | variables | Returns the published variables of a file. |
| GET | v1/files/{id}/versions | read | versions | This endpoint fetches the version history of a file, allowing you to see the progression of a file over time. |
| GET | v2/teams/{id}/webhooks | write | webhooks | Returns all webhooks registered under the specified team. Kept out of read: response includes the webhook passcode. |
| GET | v2/webhooks | write | webhooks | Returns a list of webhooks corresponding to the context or plan provided, if they exist. Kept out of read: response includes the webhook passcode. |
| POST | v2/webhooks | write | webhooks | Create a new webhook which will call the specified endpoint when the event triggers. |
| GET | v2/webhooks/{id} | write | webhooks | Get a webhook by ID. Kept out of read: response includes the webhook passcode. |
| PUT | v2/webhooks/{id} | write | webhooks | Update a webhook by ID. |
| DELETE | v2/webhooks/{id} | write | webhooks | Deletes the specified webhook. |
| GET | v2/webhooks/{id}/requests | write | webhooks | Returns all webhook requests sent within the last week. Kept out of read: response includes the webhook passcode. |
