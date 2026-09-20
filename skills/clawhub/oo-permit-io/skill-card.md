## Description:

Permit.io administration skill for reading, creating, updating, and deleting Permit.io data through OOMOL's oo CLI connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Permit.io tenants, users, and role assignments through an OOMOL-connected Permit.io account. It supports read, write, and destructive administrative workflows when the agent first inspects the live connector schema and confirms state-changing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands pipe downloaded scripts directly into a shell.

Mitigation: Prefer official installation steps with verification and avoid allowing an agent to run installer pipe commands directly.

Risk: The Permit.io connector can perform high-impact write and destructive account administration actions.

Mitigation: Inspect the live action schema, verify every payload, and require explicit user approval before write or destructive actions.

## Reference(s):

- [Permit.io ClawHub listing](https://clawhub.ai/oomol/skills/oo-permit-io)
- [Permit.io homepage](https://www.permit.io)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
