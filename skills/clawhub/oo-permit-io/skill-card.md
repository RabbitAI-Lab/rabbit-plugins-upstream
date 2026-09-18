## Description:

Permit.io helps agents read, create, update, and delete Permit.io data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Permit.io connector schemas and run oo CLI actions that manage tenants, users, and role assignments in a connected Permit.io account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote oo CLI installer scripts without pinned checksum or signature verification.

Mitigation: Review the installer path before use and prefer a pinned or manually inspected installation method with checksum or signature verification.

Risk: The skill can create, update, or delete Permit.io users and tenants, and assign or remove roles.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write actions, and require explicit approval before destructive actions.

Risk: A connected Permit.io account may grant the agent access to modify sensitive authorization data.

Mitigation: Connect only accounts and scopes whose users, tenants, and role assignments are acceptable for agent-assisted changes after confirmation.

## Reference(s):

- [Permit.io homepage](https://www.permit.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Permit.io app connection](https://console.oomol.com/app-connections?provider=permit_io)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON envelopes containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
