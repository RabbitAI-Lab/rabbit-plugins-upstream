## Description:

Monica CRM (monicahq.com). Use this skill for ANY Monica CRM request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to work with contacts and notes in an authenticated Monica CRM account through the OOMOL Monica CRM connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may install the oo CLI through an optional installer command.

Mitigation: Confirm trust in OOMOL and the oo CLI installer source before installing; prefer reviewing installer scripts or using official verified installation instructions.

Risk: Monica CRM write and destructive actions can create, overwrite, or delete CRM notes.

Mitigation: Approve only exact payloads and targets that are understood, and require explicit confirmation before write or destructive operations.

## Reference(s):

- [ClawHub Monica CRM skill page](https://clawhub.ai/oomol/skills/oo-monica-crm)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Monica CRM homepage](https://www.monicahq.com/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing Monica CRM action payloads.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
