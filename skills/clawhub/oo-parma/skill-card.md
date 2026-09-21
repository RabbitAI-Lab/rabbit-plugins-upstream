## Description:

Parma lets agents read, create, update, and delete Parma workspace data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Parma workspace from an agent, including listing workspace records and performing approved relationship, note, and group changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and destructive Parma actions that alter or remove workspace data.

Mitigation: Confirm the exact action, target, and payload with the user before approving write or destructive connector calls.

Risk: The first-time setup path can install the oo CLI from a remote installer.

Mitigation: Install the oo CLI only from a trusted OOMOL source and review the installer when appropriate.

Risk: Parma connection state, credentials, scopes, or billing status can block connector execution.

Mitigation: Connect Parma deliberately and resolve authentication, scope, expiration, app readiness, or billing errors before retrying actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-parma)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Parma Homepage](https://parma.ai)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include JSON data and execution metadata when commands run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
