# Google Analytics Data access policy

An access policy limits which endpoints Google Analytics Data connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/google-analytics#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Google Analytics Data: its 10 read-only endpoints. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create google-analytics-data --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v1beta/properties/{id}/audienceExports"},
    {"method": "GET", "path": "v1beta/properties/{id}/audienceExports/{id}"},
    {"method": "POST", "path": "v1beta/properties/{id}/audienceExports/{id}:query"},
    {"method": "GET", "path": "v1beta/properties/{id}/metadata"},
    {"method": "POST", "path": "v1beta/properties/{id}:batchRunPivotReports"},
    {"method": "POST", "path": "v1beta/properties/{id}:batchRunReports"},
    {"method": "POST", "path": "v1beta/properties/{id}:checkCompatibility"},
    {"method": "POST", "path": "v1beta/properties/{id}:runPivotReport"},
    {"method": "POST", "path": "v1beta/properties/{id}:runRealtimeReport"},
    {"method": "POST", "path": "v1beta/properties/{id}:runReport"}
  ],
  "deny": []
}
```

## Endpoints

The Google Analytics Data endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v1beta/properties/{id}/audienceExports | read | audienceExports | Lists all audience exports for a property. |
| POST | v1beta/properties/{id}/audienceExports | write | audienceExports | Creates an audience export for later retrieval. |
| GET | v1beta/properties/{id}/audienceExports/{id} | read | audienceExports | Gets configuration metadata about a specific audience export. |
| POST | v1beta/properties/{id}/audienceExports/{id}:query | read | audienceExports | Retrieves an audience export of users. |
| GET | v1beta/properties/{id}/metadata | read | properties | Returns metadata for dimensions and metrics available in reporting methods. |
| POST | v1beta/properties/{id}:batchRunPivotReports | read | properties | Returns multiple pivot reports in a batch. |
| POST | v1beta/properties/{id}:batchRunReports | read | properties | Returns multiple reports in a batch. |
| POST | v1beta/properties/{id}:checkCompatibility | read | properties | This compatibility method lists dimensions and metrics that can be added to a report request and maintain compatibility. |
| POST | v1beta/properties/{id}:runPivotReport | read | properties | Returns a customized pivot report of your Google Analytics event data. |
| POST | v1beta/properties/{id}:runRealtimeReport | read | properties | Returns a customized report of realtime event data for your property. |
| POST | v1beta/properties/{id}:runReport | read | properties | Returns a customized report of your Google Analytics event data. |
