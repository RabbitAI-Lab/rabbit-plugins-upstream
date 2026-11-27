# Google Slides access policy

An access policy limits which endpoints Google Slides connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/google-slides#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Google Slides: its 4 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create google-slides --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v1/presentations/{id}/pages/{id}"},
    {"method": "GET", "path": "v1/presentations/{id}/pages/{id}/thumbnail"},
    {"method": "GET", "path": "v1/presentations/{id}"},
    {"method": "GET", "path": "drive/v3/files"}
  ],
  "deny": []
}
```

## Endpoints

The Google Slides endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v1/presentations/{id}/pages/{id} | read | pages | Gets the latest version of the specified page in the presentation. |
| GET | v1/presentations/{id}/pages/{id}/thumbnail | read | pages | Generates a thumbnail of the latest version of the specified page in the presentation and returns a URL to the thumbnail image. |
| POST | v1/presentations | write | presentations | Creates a blank presentation using the title given in the request. |
| GET | v1/presentations/{id} | read | presentations | Gets the latest version of the specified presentation. |
| POST | v1/presentations/{id}:batchUpdate | write | presentations | Applies one or more updates to the presentation. |
| GET | drive/v3/files | read | drive | Lists your presentations through Drive (needs drive.readonly). |
