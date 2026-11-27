# Box access policy

An access policy limits which endpoints Box connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/box#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Box: its 121 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create box --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "2.0/ai_agent_default"},
    {"method": "GET", "path": "2.0/ai_agents"},
    {"method": "GET", "path": "2.0/ai_agents/{id}"},
    {"method": "GET", "path": "2.0/collaboration_whitelist_entries"},
    {"method": "GET", "path": "2.0/collaboration_whitelist_entries/{id}"},
    {"method": "GET", "path": "2.0/collaboration_whitelist_exempt_targets"},
    {"method": "GET", "path": "2.0/collaboration_whitelist_exempt_targets/{id}"},
    {"method": "GET", "path": "2.0/collaborations"},
    {"method": "GET", "path": "2.0/collaborations/{id}"},
    {"method": "GET", "path": "2.0/collections"},
    {"method": "GET", "path": "2.0/collections/{id}"},
    {"method": "GET", "path": "2.0/collections/{id}/items"},
    {"method": "GET", "path": "2.0/comments/{id}"},
    {"method": "GET", "path": "2.0/device_pinners/{id}"},
    {"method": "GET", "path": "2.0/enterprises/{id}/device_pinners"},
    {"method": "GET", "path": "2.0/events"},
    {"method": "GET", "path": "2.0/file_requests/{id}"},
    {"method": "GET", "path": "2.0/file_version_legal_holds"},
    {"method": "GET", "path": "2.0/file_version_legal_holds/{id}"},
    {"method": "GET", "path": "2.0/file_version_retentions"},
    {"method": "GET", "path": "2.0/file_version_retentions/{id}"},
    {"method": "GET", "path": "2.0/files/{id}"},
    {"method": "GET", "path": "2.0/files/{id}/app_item_associations"},
    {"method": "GET", "path": "2.0/files/{id}/collaborations"},
    {"method": "GET", "path": "2.0/files/{id}/comments"},
    {"method": "GET", "path": "2.0/files/{id}/content"},
    {"method": "GET", "path": "2.0/files/{id}/metadata"},
    {"method": "GET", "path": "2.0/files/{id}/metadata/enterprise/securityClassification-6VMVochwUWo"},
    {"method": "GET", "path": "2.0/files/{id}/metadata/global/boxSkillsCards"},
    {"method": "GET", "path": "2.0/files/{id}/metadata/{id}/{id}"},
    {"method": "GET", "path": "2.0/files/{id}/tasks"},
    {"method": "GET", "path": "2.0/files/{id}/trash"},
    {"method": "GET", "path": "2.0/files/{id}/versions"},
    {"method": "GET", "path": "2.0/files/{id}/versions/{id}"},
    {"method": "GET", "path": "2.0/files/{id}/watermark"},
    {"method": "GET", "path": "api/2.0/files/upload_sessions/{id}"},
    {"method": "GET", "path": "api/2.0/files/upload_sessions/{id}/parts"},
    {"method": "GET", "path": "2.0/folder_locks"},
    {"method": "GET", "path": "2.0/folders/trash/items"},
    {"method": "GET", "path": "2.0/folders/{id}"},
    {"method": "GET", "path": "2.0/folders/{id}/app_item_associations"},
    {"method": "GET", "path": "2.0/folders/{id}/collaborations"},
    {"method": "GET", "path": "2.0/folders/{id}/items"},
    {"method": "GET", "path": "2.0/folders/{id}/metadata"},
    {"method": "GET", "path": "2.0/folders/{id}/metadata/enterprise/securityClassification-6VMVochwUWo"},
    {"method": "GET", "path": "2.0/folders/{id}/metadata/{id}/{id}"},
    {"method": "GET", "path": "2.0/folders/{id}/trash"},
    {"method": "GET", "path": "2.0/folders/{id}/watermark"},
    {"method": "GET", "path": "2.0/group_memberships/{id}"},
    {"method": "GET", "path": "2.0/groups"},
    {"method": "GET", "path": "2.0/groups/{id}"},
    {"method": "GET", "path": "2.0/groups/{id}/collaborations"},
    {"method": "GET", "path": "2.0/groups/{id}/memberships"},
    {"method": "GET", "path": "2.0/integration_mappings/slack"},
    {"method": "GET", "path": "2.0/integration_mappings/teams"},
    {"method": "GET", "path": "2.0/invites/{id}"},
    {"method": "GET", "path": "2.0/legal_hold_policies"},
    {"method": "GET", "path": "2.0/legal_hold_policies/{id}"},
    {"method": "GET", "path": "2.0/legal_hold_policy_assignments"},
    {"method": "GET", "path": "2.0/legal_hold_policy_assignments/{id}"},
    {"method": "GET", "path": "2.0/legal_hold_policy_assignments/{id}/file_versions_on_hold"},
    {"method": "GET", "path": "2.0/legal_hold_policy_assignments/{id}/files_on_hold"},
    {"method": "GET", "path": "2.0/metadata_cascade_policies"},
    {"method": "GET", "path": "2.0/metadata_cascade_policies/{id}"},
    {"method": "POST", "path": "2.0/metadata_queries/execute_read"},
    {"method": "GET", "path": "2.0/metadata_taxonomies/{id}"},
    {"method": "GET", "path": "2.0/metadata_taxonomies/{id}/{id}"},
    {"method": "GET", "path": "2.0/metadata_taxonomies/{id}/{id}/nodes"},
    {"method": "GET", "path": "2.0/metadata_taxonomies/{id}/{id}/nodes/{id}"},
    {"method": "GET", "path": "2.0/metadata_templates"},
    {"method": "GET", "path": "2.0/metadata_templates/enterprise"},
    {"method": "GET", "path": "2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema"},
    {"method": "GET", "path": "2.0/metadata_templates/global"},
    {"method": "GET", "path": "2.0/metadata_templates/{id}"},
    {"method": "GET", "path": "2.0/metadata_templates/{id}/{id}/fields/{id}/options"},
    {"method": "GET", "path": "2.0/metadata_templates/{id}/{id}/schema"},
    {"method": "GET", "path": "2.0/recent_items"},
    {"method": "GET", "path": "2.0/retention_policies"},
    {"method": "GET", "path": "2.0/retention_policies/{id}"},
    {"method": "GET", "path": "2.0/retention_policies/{id}/assignments"},
    {"method": "GET", "path": "2.0/retention_policy_assignments/{id}"},
    {"method": "GET", "path": "2.0/retention_policy_assignments/{id}/file_versions_under_retention"},
    {"method": "GET", "path": "2.0/retention_policy_assignments/{id}/files_under_retention"},
    {"method": "GET", "path": "2.0/search"},
    {"method": "GET", "path": "2.0/shared_items"},
    {"method": "GET", "path": "2.0/shield_information_barrier_reports"},
    {"method": "GET", "path": "2.0/shield_information_barrier_reports/{id}"},
    {"method": "GET", "path": "2.0/shield_information_barrier_segment_members"},
    {"method": "GET", "path": "2.0/shield_information_barrier_segment_members/{id}"},
    {"method": "GET", "path": "2.0/shield_information_barrier_segment_restrictions"},
    {"method": "GET", "path": "2.0/shield_information_barrier_segment_restrictions/{id}"},
    {"method": "GET", "path": "2.0/shield_information_barrier_segments"},
    {"method": "GET", "path": "2.0/shield_information_barrier_segments/{id}"},
    {"method": "GET", "path": "2.0/shield_information_barriers"},
    {"method": "GET", "path": "2.0/shield_information_barriers/{id}"},
    {"method": "GET", "path": "2.0/sign_requests"},
    {"method": "GET", "path": "2.0/sign_requests/{id}"},
    {"method": "GET", "path": "2.0/sign_templates"},
    {"method": "GET", "path": "2.0/sign_templates/{id}"},
    {"method": "GET", "path": "2.0/storage_policies"},
    {"method": "GET", "path": "2.0/storage_policies/{id}"},
    {"method": "GET", "path": "2.0/storage_policy_assignments"},
    {"method": "GET", "path": "2.0/storage_policy_assignments/{id}"},
    {"method": "GET", "path": "2.0/task_assignments/{id}"},
    {"method": "GET", "path": "2.0/tasks/{id}"},
    {"method": "GET", "path": "2.0/tasks/{id}/assignments"},
    {"method": "GET", "path": "2.0/terms_of_service_user_statuses"},
    {"method": "GET", "path": "2.0/terms_of_services"},
    {"method": "GET", "path": "2.0/terms_of_services/{id}"},
    {"method": "GET", "path": "2.0/users"},
    {"method": "GET", "path": "2.0/users/me"},
    {"method": "GET", "path": "2.0/users/{id}"},
    {"method": "GET", "path": "2.0/users/{id}/avatar"},
    {"method": "GET", "path": "2.0/users/{id}/email_aliases"},
    {"method": "GET", "path": "2.0/users/{id}/memberships"},
    {"method": "GET", "path": "2.0/web_links/{id}"},
    {"method": "GET", "path": "2.0/web_links/{id}/trash"},
    {"method": "GET", "path": "2.0/webhooks"},
    {"method": "GET", "path": "2.0/webhooks/{id}"},
    {"method": "GET", "path": "2.0/workflows"},
    {"method": "GET", "path": "2.0/zip_downloads/{id}/status"}
  ],
  "deny": []
}
```

## Endpoints

The Box endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| POST | 2.0/ai/ask | write | ai | Sends an AI request to supported LLMs and returns an answer specifically focused on the user's question given the provided context. |
| POST | 2.0/ai/extract | write | ai | Sends an AI request to supported Large Language Models (LLMs) and extracts metadata in form of key-value pairs. |
| POST | 2.0/ai/extract_structured | write | ai | Sends an AI request to supported Large Language Models (LLMs) and returns extracted metadata as a set of key-value pairs. |
| POST | 2.0/ai/text_gen | write | ai | Sends an AI request to supported Large Language Models (LLMs) and returns generated text based on the provided prompt. |
| GET | 2.0/ai_agent_default | read | ai_agent_default | Get the AI agent default config. |
| GET | 2.0/ai_agents | read | ai_agents | Lists AI agents based on the provided parameters. |
| POST | 2.0/ai_agents | write | ai_agents | Creates an AI agent. |
| GET | 2.0/ai_agents/{id} | read | ai_agents | Gets an AI Agent using the agent_id parameter. |
| PUT | 2.0/ai_agents/{id} | write | ai_agents | Updates an AI agent. |
| DELETE | 2.0/ai_agents/{id} | write | ai_agents | Deletes an AI agent using the provided parameters. |
| GET | 2.0/collaboration_whitelist_entries | read | collaboration_whitelist_entries | Returns the list domains that have been deemed safe to create collaborations for within the current enterprise. |
| POST | 2.0/collaboration_whitelist_entries | write | collaboration_whitelist_entries | Creates a new entry in the list of allowed domains to allow collaboration for. |
| GET | 2.0/collaboration_whitelist_entries/{id} | read | collaboration_whitelist_entries | Returns a domain that has been deemed safe to create collaborations for within the current enterprise. |
| DELETE | 2.0/collaboration_whitelist_entries/{id} | write | collaboration_whitelist_entries | Removes a domain from the list of domains that have been deemed safe to create collaborations for within the current enterprise. |
| GET | 2.0/collaboration_whitelist_exempt_targets | read | collaboration_whitelist_exempt_targets | Returns a list of users who have been exempt from the collaboration domain restrictions. |
| POST | 2.0/collaboration_whitelist_exempt_targets | write | collaboration_whitelist_exempt_targets | Exempts a user from the restrictions set out by the allowed list of domains for collaborations. |
| GET | 2.0/collaboration_whitelist_exempt_targets/{id} | read | collaboration_whitelist_exempt_targets | Returns a users who has been exempt from the collaboration domain restrictions. |
| DELETE | 2.0/collaboration_whitelist_exempt_targets/{id} | write | collaboration_whitelist_exempt_targets | Removes a user's exemption from the restrictions set out by the allowed list of domains for collaborations. |
| GET | 2.0/collaborations | read | collaborations | Retrieves all pending collaboration invites for this user. |
| POST | 2.0/collaborations | write | collaborations | Adds a collaboration for a single user or a single group to a file or folder. |
| GET | 2.0/collaborations/{id} | read | collaborations | Retrieves a single collaboration. |
| PUT | 2.0/collaborations/{id} | write | collaborations | Updates a collaboration. |
| DELETE | 2.0/collaborations/{id} | write | collaborations | Deletes a single collaboration. |
| GET | 2.0/collections | read | collections | Retrieves all collections for a given user. |
| GET | 2.0/collections/{id} | read | collections | Retrieves a collection by its ID. |
| GET | 2.0/collections/{id}/items | read | collections | Retrieves the files and/or folders contained within this collection. |
| POST | 2.0/comments | write | comments | Adds a comment by the user to a specific file, or as a reply to an other comment. |
| GET | 2.0/comments/{id} | read | comments | Retrieves the message and metadata for a specific comment, as well as information on the user who created the comment. |
| PUT | 2.0/comments/{id} | write | comments | Update the message of a comment. |
| DELETE | 2.0/comments/{id} | write | comments | Permanently deletes a comment. |
| GET | 2.0/device_pinners/{id} | read | device_pinners | Retrieves information about an individual device pin. |
| DELETE | 2.0/device_pinners/{id} | write | device_pinners | Deletes an individual device pin. |
| GET | 2.0/enterprises/{id}/device_pinners | read | enterprises | Retrieves all the device pins within an enterprise. |
| GET | 2.0/events | read | events | Returns up to a year of past events for a given user or for the entire enterprise. |
| GET | 2.0/file_requests/{id} | read | file_requests | Retrieves the information about a file request. |
| PUT | 2.0/file_requests/{id} | write | file_requests | Updates a file request. |
| DELETE | 2.0/file_requests/{id} | write | file_requests | Deletes a file request permanently. |
| POST | 2.0/file_requests/{id}/copy | write | file_requests | Copies an existing file request that is already present on one folder, and applies it to another folder. |
| GET | 2.0/file_version_legal_holds | read | file_version_legal_holds | Get a list of file versions on legal hold for a legal hold assignment. |
| GET | 2.0/file_version_legal_holds/{id} | read | file_version_legal_holds | Retrieves information about the legal hold policies assigned to a file version. |
| GET | 2.0/file_version_retentions | read | file_version_retentions | Retrieves all file version retentions for the given enterprise. |
| GET | 2.0/file_version_retentions/{id} | read | file_version_retentions | Returns information about a file version retention. |
| GET | 2.0/files/{id} | read | files | Retrieves the details about a file. |
| POST | 2.0/files/{id} | write | files | Restores a file that has been moved to the trash. |
| PUT | 2.0/files/{id} | write | files | Updates a file. |
| DELETE | 2.0/files/{id} | write | files | Deletes a file, either permanently or by moving it to the trash. |
| GET | 2.0/files/{id}/app_item_associations | read | files | **This is a beta feature, which means that its availability might be limited.** Returns all app items the file is associated with. |
| GET | 2.0/files/{id}/collaborations | read | files | Retrieves a list of pending and active collaborations for a file. |
| GET | 2.0/files/{id}/comments | read | files | Retrieves a list of comments for a file. |
| GET | 2.0/files/{id}/content | read | files | Returns the contents of a file in binary format. |
| POST | 2.0/files/{id}/copy | write | files | Creates a copy of a file. |
| GET | 2.0/files/{id}/metadata | read | files | Retrieves all metadata for a given file. |
| GET | 2.0/files/{id}/metadata/enterprise/securityClassification-6VMVochwUWo | read | files | Retrieves the classification metadata instance that has been applied to a file. |
| POST | 2.0/files/{id}/metadata/enterprise/securityClassification-6VMVochwUWo | write | files | Adds a classification to a file by specifying the label of the classification to add. |
| PUT | 2.0/files/{id}/metadata/enterprise/securityClassification-6VMVochwUWo | write | files | Updates a classification on a file. |
| DELETE | 2.0/files/{id}/metadata/enterprise/securityClassification-6VMVochwUWo | write | files | Removes any classifications from a file. |
| GET | 2.0/files/{id}/metadata/global/boxSkillsCards | read | files | List the Box Skills metadata cards that are attached to a file. |
| POST | 2.0/files/{id}/metadata/global/boxSkillsCards | write | files | Applies one or more Box Skills metadata cards to a file. |
| PUT | 2.0/files/{id}/metadata/global/boxSkillsCards | write | files | Updates one or more Box Skills metadata cards to a file. |
| DELETE | 2.0/files/{id}/metadata/global/boxSkillsCards | write | files | Removes any Box Skills cards metadata from a file. |
| GET | 2.0/files/{id}/metadata/{id}/{id} | read | files | Retrieves the instance of a metadata template that has been applied to a file. |
| POST | 2.0/files/{id}/metadata/{id}/{id} | write | files | Applies an instance of a metadata template to a file. |
| PUT | 2.0/files/{id}/metadata/{id}/{id} | write | files | Updates a piece of metadata on a file. |
| DELETE | 2.0/files/{id}/metadata/{id}/{id} | write | files | Deletes a piece of file metadata. |
| GET | 2.0/files/{id}/tasks | read | files | Retrieves a list of all the tasks for a file. |
| GET | 2.0/files/{id}/trash | read | files | Retrieves a file that has been moved to the trash. |
| DELETE | 2.0/files/{id}/trash | write | files | Permanently deletes a file that is in the trash. |
| GET | 2.0/files/{id}/versions | read | files | Retrieve a list of the past versions for a file. |
| POST | 2.0/files/{id}/versions/current | write | files | Promote a specific version of a file. |
| GET | 2.0/files/{id}/versions/{id} | read | files | Retrieve a specific version of a file. |
| PUT | 2.0/files/{id}/versions/{id} | write | files | Restores a specific version of a file after it was deleted. |
| DELETE | 2.0/files/{id}/versions/{id} | write | files | Move a file version to the trash. |
| GET | 2.0/files/{id}/watermark | read | files | Retrieve the watermark for a file. |
| PUT | 2.0/files/{id}/watermark | write | files | Applies or update a watermark on a file. |
| DELETE | 2.0/files/{id}/watermark | write | files | Removes the watermark from a file. |
| POST | api/2.0/files/content | write | files | Uploads a small file to Box. |
| POST | api/2.0/files/upload_sessions | write | files | Creates an upload session for a new file. |
| GET | api/2.0/files/upload_sessions/{id} | read | files | Return information about an upload session. |
| PUT | api/2.0/files/upload_sessions/{id} | write | files | Uploads a chunk of a file for an upload session. |
| DELETE | api/2.0/files/upload_sessions/{id} | write | files | Abort an upload session and discard all data uploaded. |
| POST | api/2.0/files/upload_sessions/{id}/commit | write | files | Close an upload session and create a file from the uploaded chunks. |
| GET | api/2.0/files/upload_sessions/{id}/parts | read | files | Return a list of the chunks uploaded to the upload session so far. |
| POST | api/2.0/files/upload_sessions/{id}/plan | write | files | Plan an upload session by checking which parts already exist on the server. |
| POST | api/2.0/files/{id}/content | write | files | Update a file's content. |
| POST | api/2.0/files/{id}/upload_sessions | write | files | Creates an upload session for an existing file. |
| GET | 2.0/folder_locks | read | folder_locks | Retrieves folder lock details for a given folder. |
| POST | 2.0/folder_locks | write | folder_locks | Creates a folder lock on a folder, preventing it from being moved and/or deleted. |
| DELETE | 2.0/folder_locks/{id} | write | folder_locks | Deletes a folder lock on a given folder. |
| POST | 2.0/folders | write | folders | Creates a new empty folder within the specified parent folder. |
| GET | 2.0/folders/trash/items | read | folders | Retrieves the files and folders that have been moved to the trash. |
| GET | 2.0/folders/{id} | read | folders | Retrieves details for a folder, including the first 100 entries in the folder. |
| POST | 2.0/folders/{id} | write | folders | Restores a folder that has been moved to the trash. |
| PUT | 2.0/folders/{id} | write | folders | Updates a folder. |
| DELETE | 2.0/folders/{id} | write | folders | Deletes a folder, either permanently or by moving it to the trash. |
| GET | 2.0/folders/{id}/app_item_associations | read | folders | **This is a beta feature, which means that its availability might be limited.** Returns all app items the folder is associated with. |
| GET | 2.0/folders/{id}/collaborations | read | folders | Retrieves a list of pending and active collaborations for a folder. |
| POST | 2.0/folders/{id}/copy | write | folders | Creates a copy of a folder within a destination folder. |
| GET | 2.0/folders/{id}/items | read | folders | Retrieves a page of items in a folder. |
| GET | 2.0/folders/{id}/metadata | read | folders | Retrieves all metadata for a given folder. |
| GET | 2.0/folders/{id}/metadata/enterprise/securityClassification-6VMVochwUWo | read | folders | Retrieves the classification metadata instance that has been applied to a folder. |
| POST | 2.0/folders/{id}/metadata/enterprise/securityClassification-6VMVochwUWo | write | folders | Adds a classification to a folder by specifying the label of the classification to add. |
| PUT | 2.0/folders/{id}/metadata/enterprise/securityClassification-6VMVochwUWo | write | folders | Updates a classification on a folder. |
| DELETE | 2.0/folders/{id}/metadata/enterprise/securityClassification-6VMVochwUWo | write | folders | Removes any classifications from a folder. |
| GET | 2.0/folders/{id}/metadata/{id}/{id} | read | folders | Retrieves the instance of a metadata template that has been applied to a folder. |
| POST | 2.0/folders/{id}/metadata/{id}/{id} | write | folders | Applies an instance of a metadata template to a folder. |
| PUT | 2.0/folders/{id}/metadata/{id}/{id} | write | folders | Updates a piece of metadata on a folder. |
| DELETE | 2.0/folders/{id}/metadata/{id}/{id} | write | folders | Deletes a piece of folder metadata. |
| GET | 2.0/folders/{id}/trash | read | folders | Retrieves a folder that has been moved to the trash. |
| DELETE | 2.0/folders/{id}/trash | write | folders | Permanently deletes a folder that is in the trash. |
| GET | 2.0/folders/{id}/watermark | read | folders | Retrieve the watermark for a folder. |
| PUT | 2.0/folders/{id}/watermark | write | folders | Applies or update a watermark on a folder. |
| DELETE | 2.0/folders/{id}/watermark | write | folders | Removes the watermark from a folder. |
| POST | 2.0/group_memberships | write | group_memberships | Creates a group membership. |
| GET | 2.0/group_memberships/{id} | read | group_memberships | Retrieves a specific group membership. |
| PUT | 2.0/group_memberships/{id} | write | group_memberships | Updates a user's group membership. |
| DELETE | 2.0/group_memberships/{id} | write | group_memberships | Deletes a specific group membership. |
| GET | 2.0/groups | read | groups | Retrieves all of the groups for a given enterprise. |
| POST | 2.0/groups | write | groups | Creates a new group of users in an enterprise. |
| POST | 2.0/groups/terminate_sessions | write | groups | Validates the roles and permissions of the group, and creates asynchronous jobs to terminate the group's sessions. |
| GET | 2.0/groups/{id} | read | groups | Retrieves information about a group. |
| PUT | 2.0/groups/{id} | write | groups | Updates a specific group. |
| DELETE | 2.0/groups/{id} | write | groups | Permanently deletes a group. |
| GET | 2.0/groups/{id}/collaborations | read | groups | Retrieves all the collaborations for a group. |
| GET | 2.0/groups/{id}/memberships | read | groups | Retrieves all the members for a group. |
| GET | 2.0/integration_mappings/slack | read | integration_mappings | Lists Slack integration mappings in a users' enterprise. |
| POST | 2.0/integration_mappings/slack | write | integration_mappings | Creates a Slack integration mapping by mapping a Slack channel to a Box item. |
| PUT | 2.0/integration_mappings/slack/{id} | write | integration_mappings | Updates a Slack integration mapping. |
| DELETE | 2.0/integration_mappings/slack/{id} | write | integration_mappings | Deletes a Slack integration mapping. |
| GET | 2.0/integration_mappings/teams | read | integration_mappings | Lists Teams integration mappings in a users' enterprise. |
| POST | 2.0/integration_mappings/teams | write | integration_mappings | Creates a Teams integration mapping by mapping a Teams channel to a Box item. |
| PUT | 2.0/integration_mappings/teams/{id} | write | integration_mappings | Updates a Teams integration mapping. |
| DELETE | 2.0/integration_mappings/teams/{id} | write | integration_mappings | Deletes a Teams integration mapping. |
| POST | 2.0/invites | write | invites | Invites an existing external user to join an enterprise. |
| GET | 2.0/invites/{id} | read | invites | Returns the status of a user invite. |
| GET | 2.0/legal_hold_policies | read | legal_hold_policies | Retrieves a list of legal hold policies that belong to an enterprise. |
| POST | 2.0/legal_hold_policies | write | legal_hold_policies | Create a new legal hold policy. |
| GET | 2.0/legal_hold_policies/{id} | read | legal_hold_policies | Retrieve a legal hold policy. |
| PUT | 2.0/legal_hold_policies/{id} | write | legal_hold_policies | Update legal hold policy. |
| DELETE | 2.0/legal_hold_policies/{id} | write | legal_hold_policies | Delete an existing legal hold policy. |
| GET | 2.0/legal_hold_policy_assignments | read | legal_hold_policy_assignments | Retrieves a list of items a legal hold policy has been assigned to. |
| POST | 2.0/legal_hold_policy_assignments | write | legal_hold_policy_assignments | Assign a legal hold to an item type of: file, file version, folder, user, ownership, interactions, or metadata template. |
| GET | 2.0/legal_hold_policy_assignments/{id} | read | legal_hold_policy_assignments | Retrieve a legal hold policy assignment. |
| DELETE | 2.0/legal_hold_policy_assignments/{id} | write | legal_hold_policy_assignments | Remove a legal hold from an item. |
| GET | 2.0/legal_hold_policy_assignments/{id}/file_versions_on_hold | read | legal_hold_policy_assignments | Get a list of previous file versions for a legal hold assignment. |
| GET | 2.0/legal_hold_policy_assignments/{id}/files_on_hold | read | legal_hold_policy_assignments | Get a list of files with current file versions for a legal hold assignment. |
| GET | 2.0/metadata_cascade_policies | read | metadata_cascade_policies | Retrieves a list of all the metadata cascade policies that are applied to a given folder. |
| POST | 2.0/metadata_cascade_policies | write | metadata_cascade_policies | Creates a new metadata cascade policy that applies a given metadata template to a given folder and automatically cascades it down to any files within that folder. |
| GET | 2.0/metadata_cascade_policies/{id} | read | metadata_cascade_policies | Retrieve a specific metadata cascade policy assigned to a folder. |
| DELETE | 2.0/metadata_cascade_policies/{id} | write | metadata_cascade_policies | Deletes a metadata cascade policy. |
| POST | 2.0/metadata_cascade_policies/{id}/apply | write | metadata_cascade_policies | Force the metadata on a folder with a metadata cascade policy to be applied to all of its children. |
| POST | 2.0/metadata_queries/execute_read | read | metadata_queries | For new integrations, use the v2026.0 Query API. |
| POST | 2.0/metadata_taxonomies | write | metadata_taxonomies | Creates a new metadata taxonomy that can be used in metadata templates. |
| GET | 2.0/metadata_taxonomies/{id} | read | metadata_taxonomies | Used to retrieve all metadata taxonomies in a namespace. |
| GET | 2.0/metadata_taxonomies/{id}/{id} | read | metadata_taxonomies | Used to retrieve a metadata taxonomy by taxonomy key. |
| PATCH | 2.0/metadata_taxonomies/{id}/{id} | write | metadata_taxonomies | Updates an existing metadata taxonomy. |
| DELETE | 2.0/metadata_taxonomies/{id}/{id} | write | metadata_taxonomies | Delete a metadata taxonomy. |
| POST | 2.0/metadata_taxonomies/{id}/{id}/levels | write | metadata_taxonomies | Creates new metadata taxonomy levels. |
| PATCH | 2.0/metadata_taxonomies/{id}/{id}/levels/{id} | write | metadata_taxonomies | Updates an existing metadata taxonomy level. |
| POST | 2.0/metadata_taxonomies/{id}/{id}/levels:append | write | metadata_taxonomies | Creates a new metadata taxonomy level and appends it to the existing levels. |
| POST | 2.0/metadata_taxonomies/{id}/{id}/levels:trim | write | metadata_taxonomies | Deletes the last level of the metadata taxonomy. |
| GET | 2.0/metadata_taxonomies/{id}/{id}/nodes | read | metadata_taxonomies | Used to retrieve metadata taxonomy nodes based on the parameters specified. |
| POST | 2.0/metadata_taxonomies/{id}/{id}/nodes | write | metadata_taxonomies | Creates a new metadata taxonomy node. |
| GET | 2.0/metadata_taxonomies/{id}/{id}/nodes/{id} | read | metadata_taxonomies | Retrieves a metadata taxonomy node by its identifier. |
| PATCH | 2.0/metadata_taxonomies/{id}/{id}/nodes/{id} | write | metadata_taxonomies | Updates an existing metadata taxonomy node. |
| DELETE | 2.0/metadata_taxonomies/{id}/{id}/nodes/{id} | write | metadata_taxonomies | Delete a metadata taxonomy node. |
| GET | 2.0/metadata_templates | read | metadata_templates | Finds a metadata template by searching for the ID of an instance of the template. |
| GET | 2.0/metadata_templates/enterprise | read | metadata_templates | Used to retrieve all metadata templates created to be used specifically within the user's enterprise. |
| GET | 2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema | read | metadata_templates | Retrieves the classification metadata template and lists all the classifications available to this enterprise. |
| PUT | 2.0/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema | write | metadata_templates | Adds one or more new classifications to the list of classifications available to the enterprise. |
| GET | 2.0/metadata_templates/global | read | metadata_templates | Used to retrieve all generic, global metadata templates available to all enterprises using Box. |
| POST | 2.0/metadata_templates/schema | write | metadata_templates | Creates a new metadata template that can be applied to files and folders. |
| GET | 2.0/metadata_templates/{id} | read | metadata_templates | Retrieves a metadata template by its ID. |
| GET | 2.0/metadata_templates/{id}/{id}/fields/{id}/options | read | metadata_templates | Used to retrieve metadata taxonomy nodes which are available for the taxonomy field based on its configuration and the parameters specified. |
| GET | 2.0/metadata_templates/{id}/{id}/schema | read | metadata_templates | Retrieves a metadata template by its scope and templateKey values. |
| PUT | 2.0/metadata_templates/{id}/{id}/schema | write | metadata_templates | Updates a metadata template. |
| DELETE | 2.0/metadata_templates/{id}/{id}/schema | write | metadata_templates | Delete a metadata template and its instances. |
| GET | 2.0/recent_items | read | recent_items | Returns information about the recent items accessed by a user, either in the last 90 days or up to the last 1000 items accessed. |
| GET | 2.0/retention_policies | read | retention_policies | Retrieves all of the retention policies for an enterprise. |
| POST | 2.0/retention_policies | write | retention_policies | Creates a retention policy. |
| GET | 2.0/retention_policies/{id} | read | retention_policies | Retrieves a retention policy. |
| PUT | 2.0/retention_policies/{id} | write | retention_policies | Updates a retention policy. |
| DELETE | 2.0/retention_policies/{id} | write | retention_policies | Permanently deletes a retention policy. |
| GET | 2.0/retention_policies/{id}/assignments | read | retention_policies | Returns a list of all retention policy assignments associated with a specified retention policy. |
| POST | 2.0/retention_policy_assignments | write | retention_policy_assignments | Assigns a retention policy to an item. |
| GET | 2.0/retention_policy_assignments/{id} | read | retention_policy_assignments | Retrieves a retention policy assignment. |
| DELETE | 2.0/retention_policy_assignments/{id} | write | retention_policy_assignments | Removes a retention policy assignment applied to content. |
| GET | 2.0/retention_policy_assignments/{id}/file_versions_under_retention | read | retention_policy_assignments | Returns a list of file versions under retention for a retention policy assignment. |
| GET | 2.0/retention_policy_assignments/{id}/files_under_retention | read | retention_policy_assignments | Returns a list of files under retention for a retention policy assignment. |
| GET | 2.0/search | read | search | Searches for files, folders, web links, and shared files across the users content or across the entire enterprise. |
| GET | 2.0/shared_items | read | shared_items | Returns the file represented by a shared link. |
| GET | 2.0/shield_information_barrier_reports | read | shield_information_barrier_reports | Lists shield information barrier reports. |
| POST | 2.0/shield_information_barrier_reports | write | shield_information_barrier_reports | Creates a shield information barrier report for a given barrier. |
| GET | 2.0/shield_information_barrier_reports/{id} | read | shield_information_barrier_reports | Retrieves a shield information barrier report by its ID. |
| GET | 2.0/shield_information_barrier_segment_members | read | shield_information_barrier_segment_members | Lists shield information barrier segment members based on provided segment IDs. |
| POST | 2.0/shield_information_barrier_segment_members | write | shield_information_barrier_segment_members | Creates a new shield information barrier segment member. |
| GET | 2.0/shield_information_barrier_segment_members/{id} | read | shield_information_barrier_segment_members | Retrieves a shield information barrier segment member by its ID. |
| DELETE | 2.0/shield_information_barrier_segment_members/{id} | write | shield_information_barrier_segment_members | Deletes a shield information barrier segment member based on provided ID. |
| GET | 2.0/shield_information_barrier_segment_restrictions | read | shield_information_barrier_segment_restrictions | Lists shield information barrier segment restrictions based on provided segment ID. |
| POST | 2.0/shield_information_barrier_segment_restrictions | write | shield_information_barrier_segment_restrictions | Creates a shield information barrier segment restriction object. |
| GET | 2.0/shield_information_barrier_segment_restrictions/{id} | read | shield_information_barrier_segment_restrictions | Retrieves a shield information barrier segment restriction based on provided ID. |
| DELETE | 2.0/shield_information_barrier_segment_restrictions/{id} | write | shield_information_barrier_segment_restrictions | Delete shield information barrier segment restriction based on provided ID. |
| GET | 2.0/shield_information_barrier_segments | read | shield_information_barrier_segments | Retrieves a list of shield information barrier segment objects for the specified Information Barrier ID. |
| POST | 2.0/shield_information_barrier_segments | write | shield_information_barrier_segments | Creates a shield information barrier segment. |
| GET | 2.0/shield_information_barrier_segments/{id} | read | shield_information_barrier_segments | Retrieves shield information barrier segment based on provided ID.. |
| PUT | 2.0/shield_information_barrier_segments/{id} | write | shield_information_barrier_segments | Updates the shield information barrier segment based on provided ID.. |
| DELETE | 2.0/shield_information_barrier_segments/{id} | write | shield_information_barrier_segments | Deletes the shield information barrier segment based on provided ID. |
| GET | 2.0/shield_information_barriers | read | shield_information_barriers | Retrieves a list of shield information barrier objects for the enterprise of JWT. |
| POST | 2.0/shield_information_barriers | write | shield_information_barriers | Creates a shield information barrier to separate individuals/groups within the same firm and prevents confidential information passing between them. |
| POST | 2.0/shield_information_barriers/change_status | write | shield_information_barriers | Change status of shield information barrier with the specified ID. |
| GET | 2.0/shield_information_barriers/{id} | read | shield_information_barriers | Get shield information barrier based on provided ID. |
| GET | 2.0/sign_requests | read | sign_requests | Gets signature requests created by a user. |
| POST | 2.0/sign_requests | write | sign_requests | Creates a signature request. |
| GET | 2.0/sign_requests/{id} | read | sign_requests | Gets a sign request by ID. |
| POST | 2.0/sign_requests/{id}/cancel | write | sign_requests | Cancels a sign request. |
| POST | 2.0/sign_requests/{id}/resend | write | sign_requests | Resends a signature request email to all outstanding signers. |
| GET | 2.0/sign_templates | read | sign_templates | Gets Box Sign templates created by a user. |
| GET | 2.0/sign_templates/{id} | read | sign_templates | Fetches details of a specific Box Sign template. |
| PUT | 2.0/skill_invocations/{id} | write | skill_invocations | An alternative method that can be used to overwrite and update all Box Skill metadata cards on a file. |
| GET | 2.0/storage_policies | read | storage_policies | Fetches all the storage policies in the enterprise. |
| GET | 2.0/storage_policies/{id} | read | storage_policies | Fetches a specific storage policy. |
| GET | 2.0/storage_policy_assignments | read | storage_policy_assignments | Fetches all the storage policy assignment for an enterprise or user. |
| POST | 2.0/storage_policy_assignments | write | storage_policy_assignments | Creates a storage policy assignment for an enterprise or user. |
| GET | 2.0/storage_policy_assignments/{id} | read | storage_policy_assignments | Fetches a specific storage policy assignment. |
| PUT | 2.0/storage_policy_assignments/{id} | write | storage_policy_assignments | Updates a specific storage policy assignment. |
| DELETE | 2.0/storage_policy_assignments/{id} | write | storage_policy_assignments | Delete a storage policy assignment. |
| POST | 2.0/task_assignments | write | task_assignments | Assigns a task to a user. |
| GET | 2.0/task_assignments/{id} | read | task_assignments | Retrieves information about a task assignment. |
| PUT | 2.0/task_assignments/{id} | write | task_assignments | Updates a task assignment. |
| DELETE | 2.0/task_assignments/{id} | write | task_assignments | Deletes a specific task assignment. |
| POST | 2.0/tasks | write | tasks | Creates a single task on a file. |
| GET | 2.0/tasks/{id} | read | tasks | Retrieves information about a specific task. |
| PUT | 2.0/tasks/{id} | write | tasks | Updates a task. |
| DELETE | 2.0/tasks/{id} | write | tasks | Removes a task from a file. |
| GET | 2.0/tasks/{id}/assignments | read | tasks | Lists all of the assignments for a given task. |
| GET | 2.0/terms_of_service_user_statuses | read | terms_of_service_user_statuses | Retrieves an overview of users and their status for a terms of service, including Whether they have accepted the terms and when. |
| POST | 2.0/terms_of_service_user_statuses | write | terms_of_service_user_statuses | Sets the status for a terms of service for a user. |
| PUT | 2.0/terms_of_service_user_statuses/{id} | write | terms_of_service_user_statuses | Updates the status for a terms of service for a user. |
| GET | 2.0/terms_of_services | read | terms_of_services | Returns the current terms of service text and settings for the enterprise. |
| POST | 2.0/terms_of_services | write | terms_of_services | Creates a terms of service for a given enterprise and type of user. |
| GET | 2.0/terms_of_services/{id} | read | terms_of_services | Fetches a specific terms of service. |
| PUT | 2.0/terms_of_services/{id} | write | terms_of_services | Updates a specific terms of service. |
| GET | 2.0/users | read | users | Returns a list of all users for the Enterprise along with their user_id, public_name, and login. |
| POST | 2.0/users | write | users | Creates a new managed user in an enterprise. |
| GET | 2.0/users/me | read | users | Retrieves information about the user who is currently authenticated. |
| POST | 2.0/users/terminate_sessions | write | users | Validates the roles and permissions of the user, and creates asynchronous jobs to terminate the user's sessions. |
| GET | 2.0/users/{id} | read | users | Retrieves information about a user in the enterprise. |
| PUT | 2.0/users/{id} | write | users | Updates a managed or app user in an enterprise. |
| DELETE | 2.0/users/{id} | write | users | Deletes a user. |
| GET | 2.0/users/{id}/avatar | read | users | Retrieves an image of a the user's avatar. |
| POST | 2.0/users/{id}/avatar | write | users | Adds or updates a user avatar. |
| DELETE | 2.0/users/{id}/avatar | write | users | Removes an existing user avatar. |
| GET | 2.0/users/{id}/email_aliases | read | users | Retrieves all email aliases for a user. |
| POST | 2.0/users/{id}/email_aliases | write | users | Adds a new email alias to a user account.. |
| DELETE | 2.0/users/{id}/email_aliases/{id} | write | users | Removes an email alias from a user. |
| PUT | 2.0/users/{id}/folders/0 | write | users | Move all of the items (files, folders and workflows) owned by a user into another user's account. |
| GET | 2.0/users/{id}/memberships | read | users | Retrieves all the groups for a user. |
| POST | 2.0/web_links | write | web_links | Creates a web link object within a folder. |
| GET | 2.0/web_links/{id} | read | web_links | Retrieve information about a web link. |
| POST | 2.0/web_links/{id} | write | web_links | Restores a web link that has been moved to the trash. |
| PUT | 2.0/web_links/{id} | write | web_links | Updates a web link object. |
| DELETE | 2.0/web_links/{id} | write | web_links | Deletes a web link. |
| GET | 2.0/web_links/{id}/trash | read | web_links | Retrieves a web link that has been moved to the trash. |
| DELETE | 2.0/web_links/{id}/trash | write | web_links | Permanently deletes a web link that is in the trash. |
| GET | 2.0/webhooks | read | webhooks | Returns all defined webhooks for the requesting application. |
| POST | 2.0/webhooks | write | webhooks | Creates a webhook. |
| GET | 2.0/webhooks/{id} | read | webhooks | Retrieves a specific webhook. |
| PUT | 2.0/webhooks/{id} | write | webhooks | Updates a webhook. |
| DELETE | 2.0/webhooks/{id} | write | webhooks | Deletes a webhook. |
| GET | 2.0/workflows | read | workflows | Returns list of workflows that act on a given folder ID, and have a flow with a trigger type of WORKFLOW_MANUAL_START. |
| POST | 2.0/workflows/{id}/start | write | workflows | Initiates a flow with a trigger type of WORKFLOW_MANUAL_START. |
| POST | 2.0/zip_downloads | write | zip_downloads | Creates a request to download multiple files and folders as a single zip archive file. |
| GET | 2.0/zip_downloads/{id}/status | read | zip_downloads | Returns the download status of a zip archive, allowing an application to inspect the progress of the download as well as the number of items that might have been skipped. |
