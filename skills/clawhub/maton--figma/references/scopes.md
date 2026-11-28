# Figma scopes

The OAuth scopes Figma connections can ask for. Pass the ones the task needs with `--scopes` (repeatable or comma-separated) when creating the connection, or to `maton connection reauthorize` to change them later. *Always* scopes are added whatever you pass, *By default* ones are requested when you pass none, and *Optional* ones only when you pass them. Change them only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/figma#permissions.

```bash
maton connection create figma --scopes file_comments:read
```

| Scope | Requested |
| --- | --- |
| `file_comments:read` | By default |
| `file_comments:write` | By default |
| `file_content:read` | By default |
| `file_metadata:read` | By default |
| `file_versions:read` | By default |
| `library_assets:read` | By default |
| `library_content:read` | By default |
| `team_library_content:read` | By default |
| `file_dev_resources:read` | By default |
| `file_dev_resources:write` | By default |
| `current_user:read` | Always |
