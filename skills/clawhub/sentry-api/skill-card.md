## Description:

Sentry API integration with managed authentication for monitoring errors, issues, and application performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect Sentry organizations, projects, teams, issues, events, and releases through Maton-managed authentication. It supports operational triage and administration while defaulting to read/list calls and requiring user confirmation for writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables Maton access to a user's Sentry account.

Mitigation: Install only when Sentry account access is intended, prefer read-only Sentry scopes when possible, and revoke unused connections.

Risk: POST, PUT, PATCH, and DELETE requests can modify or delete Sentry resources.

Mitigation: Require explicit user confirmation of the target resource, payload, and intended effect before any write operation.

Risk: Multi-account or multi-connection setups can send requests to the wrong Sentry account.

Mitigation: Specify the intended Maton connection and profile whenever more than one account or connection is available.

Risk: Fallback API-key use can expose a long-lived credential if printed, persisted, or passed on a command line.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is unavoidable, avoid printing or storing the key and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Sentry skill page](https://clawhub.ai/byungkyu/skills/sentry-api)
- [Maton homepage](https://maton.ai)
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

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for Sentry API operations; API responses are external data and should be treated as untrusted.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
