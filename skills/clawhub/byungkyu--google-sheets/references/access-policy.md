# Google Sheets access policy

An access policy limits which endpoints Google Sheets connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/google-sheets#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Google Sheets: its 8 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create google-sheets --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v4/spreadsheets/{id}/developerMetadata/{id}"},
    {"method": "POST", "path": "v4/spreadsheets/{id}/developerMetadata:search"},
    {"method": "GET", "path": "v4/spreadsheets/{id}"},
    {"method": "POST", "path": "v4/spreadsheets/{id}:getByDataFilter"},
    {"method": "GET", "path": "v4/spreadsheets/{id}/values/{id}"},
    {"method": "GET", "path": "v4/spreadsheets/{id}/values:batchGet"},
    {"method": "POST", "path": "v4/spreadsheets/{id}/values:batchGetByDataFilter"},
    {"method": "GET", "path": "drive/v3/files"}
  ],
  "deny": []
}
```

## Endpoints

The Google Sheets endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v4/spreadsheets/{id}/developerMetadata/{id} | read | developerMetadata | Returns the developer metadata with the specified ID. |
| POST | v4/spreadsheets/{id}/developerMetadata:search | read | developerMetadata | Returns all developer metadata matching the specified DataFilter. |
| POST | v4/spreadsheets/{id}/sheets/{id}:copyTo | write | sheets | Copies a single sheet from a spreadsheet to another spreadsheet. |
| POST | v4/spreadsheets | write | spreadsheets | Creates a spreadsheet, returning the newly created spreadsheet. |
| GET | v4/spreadsheets/{id} | read | spreadsheets | Returns the spreadsheet at the given ID. |
| POST | v4/spreadsheets/{id}:batchUpdate | write | spreadsheets | Applies one or more updates to the spreadsheet. |
| POST | v4/spreadsheets/{id}:getByDataFilter | read | spreadsheets | Returns the spreadsheet at the given ID. |
| GET | v4/spreadsheets/{id}/values/{id} | read | values | Returns a range of values from a spreadsheet. |
| PUT | v4/spreadsheets/{id}/values/{id} | write | values | Sets values in a range of a spreadsheet. |
| POST | v4/spreadsheets/{id}/values/{id}:append | write | values | Appends values to a spreadsheet. |
| POST | v4/spreadsheets/{id}/values/{id}:clear | write | values | Clears values from a spreadsheet. |
| POST | v4/spreadsheets/{id}/values:batchClear | write | values | Clears one or more ranges of values from a spreadsheet. |
| POST | v4/spreadsheets/{id}/values:batchClearByDataFilter | write | values | Clears one or more ranges of values from a spreadsheet. |
| GET | v4/spreadsheets/{id}/values:batchGet | read | values | Returns one or more ranges of values from a spreadsheet. |
| POST | v4/spreadsheets/{id}/values:batchGetByDataFilter | read | values | Returns one or more ranges of values that match the specified data filters. |
| POST | v4/spreadsheets/{id}/values:batchUpdate | write | values | Sets values in one or more ranges of a spreadsheet. |
| POST | v4/spreadsheets/{id}/values:batchUpdateByDataFilter | write | values | Sets values in one or more ranges of a spreadsheet. |
| GET | drive/v3/files | read | drive | Lists your spreadsheets through Drive: all of them with drive.readonly, or only those created or opened through Maton with drive.file. |
