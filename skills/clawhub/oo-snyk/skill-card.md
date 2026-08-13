## Description:

Snyk (snyk.io). Use this skill for ANY Snyk request - searching and reading data. Whenever a task involves Snyk, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to read Snyk account, organization, project, and issue data through an OOMOL-connected Snyk account. It helps agents inspect Snyk resources without handling raw Snyk tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses OOMOL as an intermediary for access to the user's Snyk account.

Mitigation: Review the oo CLI installer before use and connect only the Snyk account and scopes the agent is intended to read from.

Risk: The connector contract may change or a payload may not match the live action schema.

Mitigation: Fetch the action schema with `oo connector schema` before constructing each payload.

Risk: Authentication, connection, or billing recovery steps could trigger unnecessary account changes if run proactively.

Mitigation: Run setup and recovery commands only after a matching CLI, authentication, connection, scope, or billing error occurs.

## Reference(s):

- [Snyk homepage](https://snyk.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-snyk)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
