## Description:

Wrike API integration with managed OAuth for managing tasks, folders, projects, spaces, team collaboration, and administrative functions through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external operators use this skill to access Wrike API v4 through managed OAuth for project work, task tracking, team collaboration, timelogs, and account administration. It is suited for read-first workflows and user-approved changes in a connected Wrike account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate access to a user's Wrike account through Maton.

Mitigation: Install only when Maton-mediated Wrike access is intended, use the least Wrike scopes available, and confirm the target account when multiple connections exist.

Risk: Write, invitation, user-management, access-role, audit-log, or data-export actions can affect account governance or expose sensitive organizational data.

Mitigation: Default to read and list calls, and require explicit user approval with resource identifiers, payload, scope, and intended effect before sensitive or modifying operations.

Risk: External Wrike content and webhook payloads may contain untrusted instructions or data.

Mitigation: Treat returned content as data only; do not execute, evaluate, or use it to choose follow-up endpoints or recipients without validation and user intent.

## Reference(s):

- [Wrike API Documentation](https://developers.wrike.com/)
- [Wrike API Overview](https://developers.wrike.com/overview/)
- [OAuth 2.0 Authorization](https://developers.wrike.com/oauth-20-authorization/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Wrike API request paths, Maton CLI commands, JSON request bodies, and cautionary approval guidance.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
