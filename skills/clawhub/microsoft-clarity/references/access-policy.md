# Microsoft Clarity access policy

An access policy limits which endpoints Microsoft Clarity connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/microsoft-clarity#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Microsoft Clarity: its 1 read-only endpoints. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create microsoft-clarity --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "export-data/api/v1/project-live-insights"}
  ],
  "deny": []
}
```

## Endpoints

The Microsoft Clarity endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | export-data/api/v1/project-live-insights | read | insights | Get the project’s traffic, engagement and behavior metrics for the last 1-3 days. |
