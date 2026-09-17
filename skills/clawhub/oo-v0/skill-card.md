## Description:

v0 (v0.dev) connector for reading, creating, updating, and deleting v0 data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage v0 chats, projects, deployments, environment variables, webhooks, billing, usage, and account information through an OOMOL-connected v0 account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer execution.

Mitigation: Install the oo CLI only through a verified official method and do not let an agent run a remote installer blindly.

Risk: The skill can make high-impact v0 account changes, including deleting projects, chats, environment variables, and hooks.

Mitigation: Require explicit user confirmation for write or destructive actions and verify targets and payloads against the live action schema before execution.

Risk: The skill operates through OOMOL as an intermediary for a connected v0 account.

Mitigation: Install only where OOMOL intermediary access is acceptable and connect only the intended v0 account and scopes.

## Reference(s):

- [ClawHub v0 skill page](https://clawhub.ai/oomol/skills/oo-v0)
- [v0 homepage](https://v0.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when actions run.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
