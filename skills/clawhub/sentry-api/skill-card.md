## Description:

Sentry API integration with managed authentication for monitoring errors, issues, and application performance through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect Sentry organizations, projects, issues, events, teams, and releases through managed Maton authentication. It supports read and list workflows by default and requires explicit user confirmation before new connections or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Sentry access through Maton, so use depends on trusting Maton as an API gateway for the connected Sentry account.

Mitigation: Install only when Maton is trusted for the account and use pinned or locally constrained package installation where appropriate.

Risk: Broad Sentry scopes or ambiguous connections could expose more account data or affect the wrong workspace.

Mitigation: Prefer OAuth with the narrowest Sentry scopes available, specify the intended connection when multiple connections exist, and revoke unused connections.

Risk: Write and delete operations can change or remove Sentry resources.

Mitigation: Default to read/list calls and confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Long-lived API keys or provider tokens can leak through logs, files, command lines, or process environments.

Mitigation: Prefer OAuth via the Maton CLI credential store, never print or persist credentials, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

## Reference(s):

- [ClawHub Sentry Skill](https://clawhub.ai/byungkyu/skills/sentry-api)
- [Maton Homepage](https://maton.ai)
- [Sentry API Documentation](https://docs.sentry.io/api/)
- [Sentry API Authentication](https://docs.sentry.io/api/auth/)
- [Sentry Events API](https://docs.sentry.io/api/events/)
- [Sentry Projects API](https://docs.sentry.io/api/projects/)
- [Sentry Organizations API](https://docs.sentry.io/api/organizations/)
- [Sentry Teams API](https://docs.sentry.io/api/teams/)
- [Sentry Releases API](https://docs.sentry.io/api/releases/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Sentry API request paths, Maton CLI commands, SDK snippets, and operational guidance; Sentry and Maton rate limits apply.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
