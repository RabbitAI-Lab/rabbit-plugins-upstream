# Google Drive access policy

An access policy limits which endpoints Google Drive connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/google-drive#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Google Drive: its 27 read-only endpoints, plus deny rules for the 1 write endpoint a read rule would otherwise match. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create google-drive --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "drive/v3/about"},
    {"method": "GET", "path": "drive/v3/files/{id}/accessproposals"},
    {"method": "GET", "path": "drive/v3/files/{id}/accessproposals/{id}"},
    {"method": "GET", "path": "drive/v3/files/{id}/approvals"},
    {"method": "GET", "path": "drive/v3/files/{id}/approvals/{id}"},
    {"method": "GET", "path": "drive/v3/apps"},
    {"method": "GET", "path": "drive/v3/apps/{id}"},
    {"method": "GET", "path": "drive/v3/changes"},
    {"method": "GET", "path": "drive/v3/changes/startPageToken"},
    {"method": "GET", "path": "drive/v3/files/{id}/comments"},
    {"method": "GET", "path": "drive/v3/files/{id}/comments/{id}"},
    {"method": "GET", "path": "drive/v3/drives"},
    {"method": "GET", "path": "drive/v3/drives/{id}"},
    {"method": "GET", "path": "drive/v3/files"},
    {"method": "GET", "path": "drive/v3/files/generateIds"},
    {"method": "GET", "path": "drive/v3/files/{id}"},
    {"method": "GET", "path": "drive/v3/files/{id}/export"},
    {"method": "GET", "path": "drive/v3/files/{id}/listLabels"},
    {"method": "GET", "path": "drive/v3/operations/{id}"},
    {"method": "GET", "path": "drive/v3/files/{id}/permissions"},
    {"method": "GET", "path": "drive/v3/files/{id}/permissions/{id}"},
    {"method": "GET", "path": "drive/v3/files/{id}/comments/{id}/replies"},
    {"method": "GET", "path": "drive/v3/files/{id}/comments/{id}/replies/{id}"},
    {"method": "GET", "path": "drive/v3/files/{id}/revisions"},
    {"method": "GET", "path": "drive/v3/files/{id}/revisions/{id}"},
    {"method": "GET", "path": "drive/v3/teamdrives"},
    {"method": "GET", "path": "drive/v3/teamdrives/{id}"}
  ],
  "deny": [
    {"method": "GET", "path": "drive/v3/files/generateCseToken"}
  ]
}
```

## Endpoints

The Google Drive endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | drive/v3/about | read | about | Gets information about the user, the user's Drive, and system capabilities. |
| GET | drive/v3/files/{id}/accessproposals | read | accessproposals | List the access proposals on a file. |
| GET | drive/v3/files/{id}/accessproposals/{id} | read | accessproposals | Retrieves an access proposal by ID. |
| POST | drive/v3/files/{id}/accessproposals/{id}:resolve | write | accessproposals | Approves or denies an access proposal. |
| GET | drive/v3/files/{id}/approvals | read | approvals | Lists the approvals on a file. |
| GET | drive/v3/files/{id}/approvals/{id} | read | approvals | Gets an approval by ID. |
| POST | drive/v3/files/{id}/approvals/{id}:approve | write | approvals | Approves an approval. |
| POST | drive/v3/files/{id}/approvals/{id}:cancel | write | approvals | Cancels an approval. |
| POST | drive/v3/files/{id}/approvals/{id}:comment | write | approvals | Comments on an approval. |
| POST | drive/v3/files/{id}/approvals/{id}:decline | write | approvals | Declines an approval. |
| POST | drive/v3/files/{id}/approvals/{id}:reassign | write | approvals | Reassigns the reviewers on an approval. |
| POST | drive/v3/files/{id}/approvals:start | write | approvals | Starts an approval on a file. |
| GET | drive/v3/apps | read | apps | Lists a user's installed apps. |
| GET | drive/v3/apps/{id} | read | apps | Gets a specific app. |
| GET | drive/v3/changes | read | changes | Lists the changes for a user or shared drive. |
| GET | drive/v3/changes/startPageToken | read | changes | Gets the starting pageToken for listing future changes. |
| POST | drive/v3/changes/watch | write | changes | Subscribes to changes for a user. |
| POST | drive/v3/channels/stop | write | channels | Stops watching resources through this channel. |
| GET | drive/v3/files/{id}/comments | read | comments | Lists a file's comments. |
| POST | drive/v3/files/{id}/comments | write | comments | Creates a comment on a file. |
| GET | drive/v3/files/{id}/comments/{id} | read | comments | Gets a comment by ID. |
| PATCH | drive/v3/files/{id}/comments/{id} | write | comments | Updates a comment with patch semantics. |
| DELETE | drive/v3/files/{id}/comments/{id} | write | comments | Deletes a comment. |
| GET | drive/v3/drives | read | drives | Lists the user's shared drives. |
| POST | drive/v3/drives | write | drives | Creates a shared drive. |
| GET | drive/v3/drives/{id} | read | drives | Gets a shared drive's metadata by ID. |
| PATCH | drive/v3/drives/{id} | write | drives | Updates the metadata for a shared drive. |
| DELETE | drive/v3/drives/{id} | write | drives | Permanently deletes a shared drive for which the user is an `organizer`. |
| POST | drive/v3/drives/{id}/hide | write | drives | Hides a shared drive from the default view. |
| POST | drive/v3/drives/{id}/unhide | write | drives | Restores a shared drive to the default view. |
| GET | drive/v3/files | read | files | Lists the user's files. |
| POST | drive/v3/files | write | files | Creates a file. |
| GET | drive/v3/files/generateCseToken | write | files | Generates a CSE token which can be used to create or update CSE files. Kept out of read: creates a client-side encryption token. |
| GET | drive/v3/files/generateIds | read | files | Generates a set of file IDs which can be provided in create or copy requests. |
| DELETE | drive/v3/files/trash | write | files | Permanently deletes all of the user's trashed files. |
| GET | drive/v3/files/{id} | read | files | Gets a file's metadata or content by ID. |
| PATCH | drive/v3/files/{id} | write | files | Updates a file's metadata, content, or both. |
| DELETE | drive/v3/files/{id} | write | files | Permanently deletes a file owned by the user without moving it to the trash. |
| POST | drive/v3/files/{id}/copy | write | files | Creates a copy of a file and applies any requested updates with patch semantics. |
| POST | drive/v3/files/{id}/download | write | files | Downloads the content of a file. |
| GET | drive/v3/files/{id}/export | read | files | Exports a Google Workspace document to the requested MIME type and returns exported byte content. |
| GET | drive/v3/files/{id}/listLabels | read | files | Lists the labels on a file. |
| POST | drive/v3/files/{id}/modifyLabels | write | files | Modifies the set of labels applied to a file. |
| POST | drive/v3/files/{id}/watch | write | files | Subscribes to changes to a file. |
| POST | upload/drive/v3/files | write | files | Creates a file. (media upload) |
| PATCH | upload/drive/v3/files/{id} | write | files | Updates a file's metadata, content, or both. (media upload) |
| GET | drive/v3/operations/{id} | read | operations | Gets the latest state of a long-running operation. |
| GET | drive/v3/files/{id}/permissions | read | permissions | Lists a file's or shared drive's permissions. |
| POST | drive/v3/files/{id}/permissions | write | permissions | Creates a permission for a file or shared drive. |
| GET | drive/v3/files/{id}/permissions/{id} | read | permissions | Gets a permission by ID. |
| PATCH | drive/v3/files/{id}/permissions/{id} | write | permissions | Updates a permission with patch semantics. |
| DELETE | drive/v3/files/{id}/permissions/{id} | write | permissions | Deletes a permission. |
| GET | drive/v3/files/{id}/comments/{id}/replies | read | replies | Lists a comment's replies. |
| POST | drive/v3/files/{id}/comments/{id}/replies | write | replies | Creates a reply to a comment. |
| GET | drive/v3/files/{id}/comments/{id}/replies/{id} | read | replies | Gets a reply by ID. |
| PATCH | drive/v3/files/{id}/comments/{id}/replies/{id} | write | replies | Updates a reply with patch semantics. |
| DELETE | drive/v3/files/{id}/comments/{id}/replies/{id} | write | replies | Deletes a reply. |
| GET | drive/v3/files/{id}/revisions | read | revisions | Lists a file's revisions. |
| GET | drive/v3/files/{id}/revisions/{id} | read | revisions | Gets a revision's metadata or content by ID. |
| PATCH | drive/v3/files/{id}/revisions/{id} | write | revisions | Updates a revision with patch semantics. |
| DELETE | drive/v3/files/{id}/revisions/{id} | write | revisions | Permanently deletes a file version. |
| GET | drive/v3/teamdrives | read | teamdrives | Deprecated: Use `drives.list` instead. |
| POST | drive/v3/teamdrives | write | teamdrives | Deprecated: Use `drives.create` instead. |
| GET | drive/v3/teamdrives/{id} | read | teamdrives | Deprecated: Use `drives.get` instead. |
| PATCH | drive/v3/teamdrives/{id} | write | teamdrives | Deprecated: Use `drives.update` instead. |
| DELETE | drive/v3/teamdrives/{id} | write | teamdrives | Deprecated: Use `drives.delete` instead. |
