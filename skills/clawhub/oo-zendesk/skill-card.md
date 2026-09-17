## Description:

Zendesk (zendesk.com). Use this skill for ANY Zendesk request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, support operators, and developers use this skill to inspect Zendesk schemas and read, create, reply to, or update Zendesk support records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes running a remote installer directly in a shell.

Mitigation: Review the installer path first and prefer a verified, versioned oo CLI installation source or inspect the installer before execution.

Risk: Ticket creation, replies, and updates can change customer-support records.

Mitigation: Confirm the exact Zendesk action payload and expected effect with the user before allowing write actions.

Risk: Zendesk action payloads may drift from the connector contract.

Mitigation: Inspect the live connector schema before constructing payloads for each action.

## Reference(s):

- [ClawHub Zendesk Skill](https://clawhub.ai/oomol/skills/oo-zendesk)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zendesk](https://www.zendesk.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing Zendesk action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence, release metadata, and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
