## Description:

NeetoDesk (neeto.com). Use this skill for ANY NeetoDesk request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support operators use this skill to read, create, and update NeetoDesk tickets, comments, and workspace support data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change customer-support records, including tickets and comments.

Mitigation: Review and confirm the exact payload and intended effect before creating or updating tickets or comments.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live action schema before constructing each payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-neetodesk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [NeetoDesk Homepage](https://www.neeto.com/neetodesk)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; read actions may run directly, while write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
