## Description:

Sentry API integration with managed authentication for monitoring errors, retrieving events, and managing issues, projects, teams, and releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to access Sentry through Maton-managed authentication, inspect errors and events, and make approved changes to Sentry organizations, projects, teams, issues, and releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Sentry access through Maton-managed authentication.

Mitigation: Install it only where Maton is an approved gateway for the user's Sentry account, and prefer OAuth over long-lived API keys.

Risk: Connected Sentry accounts may expose organization, project, issue, event, team, and release data allowed by the granted scopes.

Mitigation: Grant the narrowest Sentry scopes possible, prefer read-only access when sufficient, and specify the intended connection when multiple accounts are available.

Risk: Write, delete, connection, function, and trigger operations can modify Sentry resources or establish persistent automation.

Mitigation: Require explicit user approval with the target resource, payload, and expected effect before any modifying or automation command.

Risk: Trigger destinations can continuously forward event data outside the platform.

Mitigation: Keep destinations on approved Maton endpoints unless the user explicitly names and approves a third-party host and the data that will be sent.

Risk: The artifact documents CLI and SDK installation without checksum or signature verification.

Mitigation: Use an isolated environment for CLI or SDK installation when supply-chain assurance is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/sentry-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
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
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task-specific instructions and commands for authenticated Sentry API access through Maton; write and automation actions require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
