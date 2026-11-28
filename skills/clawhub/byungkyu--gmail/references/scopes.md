# Gmail scopes

The OAuth scopes Gmail connections can ask for. Pass the ones the task needs with `--scopes` (repeatable or comma-separated) when creating the connection, or to `maton connection reauthorize` to change them later. *Always* scopes are added whatever you pass, *By default* ones are requested when you pass none, and *Optional* ones only when you pass them. Change them only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/google-mail#permissions.

```bash
maton connection create google-mail --scopes https://www.googleapis.com/auth/gmail.readonly
```

| Scope | Requested |
| --- | --- |
| `https://www.googleapis.com/auth/gmail.modify` | By default |
| `https://www.googleapis.com/auth/gmail.readonly` | Optional |
| `https://www.googleapis.com/auth/gmail.compose` | By default |
| `https://www.googleapis.com/auth/gmail.send` | By default |
| `https://www.googleapis.com/auth/userinfo.profile` | By default |
| `https://www.googleapis.com/auth/userinfo.email` | Always |
