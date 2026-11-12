## Description:

xurl CLI for authenticated X posts, replies, reads/search, DMs, media upload, followers, auth status, or raw v2 API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the xurl CLI to make authenticated X API requests, including publishing and managing posts, reading and searching content, messaging, handling media, and calling v2 endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or remove saved authentication settings.

Mitigation: Before installing, consider whether this capability is needed; use `xurl auth status` to check authentication instead of reading the token file.

Risk: Verbose mode can print authentication headers into tool output.

Mitigation: Avoid `--verbose` when handling authenticated requests unless exposing headers is necessary.

## Reference(s):

- [xurl on ClawHub](https://clawhub.ai/hillstreet-ph/skills/xurl)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API results and actions depend on account permissions, app scopes, and rate limits.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
