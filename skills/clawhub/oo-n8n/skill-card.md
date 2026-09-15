## Description:

n8n (n8n.io). Use this skill for ANY n8n request, including reading, creating, updating, and deleting data through the OOMOL-connected n8n connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to manage n8n workflows, executions, data tables, tags, variables, and related metadata through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and destructive operations against n8n workflows, data tables, tags, variables, executions, and metadata.

Mitigation: Confirm the exact target, payload, and expected effect before approving write or destructive actions.

Risk: The setup guidance includes remote installer one-liners for the oo CLI.

Mitigation: Prefer an official, verifiable installation method and avoid running remote installer scripts blindly.

Risk: The oo CLI uses access to the user's connected n8n account.

Mitigation: Install only when the publisher is trusted and the account connection scope is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-n8n)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [n8n homepage](https://n8n.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
