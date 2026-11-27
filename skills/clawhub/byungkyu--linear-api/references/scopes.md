# Linear scopes

The OAuth scopes Linear connections can ask for. Pass the ones the task needs with `--scopes` (repeatable or comma-separated) when creating the connection, or to `maton connection reauthorize` to change them later. *Always* scopes are added whatever you pass, *By default* ones are requested when you pass none, and *Optional* ones only when you pass them. Change them only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/linear#permissions.

```bash
maton connection create linear --scopes issues:create
```

| Scope | Requested |
| --- | --- |
| `issues:create` | By default |
| `comments:create` | By default |
| `write` | By default |
| `admin` | By default |
| `read` | Always |
