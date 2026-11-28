# Jira scopes

The OAuth scopes Jira connections can ask for. Pass the ones the task needs with `--scopes` (repeatable or comma-separated) when creating the connection, or to `maton connection reauthorize` to change them later. *Always* scopes are added whatever you pass, *By default* ones are requested when you pass none, and *Optional* ones only when you pass them. Change them only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/jira#permissions.

```bash
maton connection create jira --scopes read:jira-work
```

| Scope | Requested |
| --- | --- |
| `read:jira-work` | By default |
| `write:jira-work` | By default |
| `read:jira-user` | By default |
| `offline_access` | Always |
