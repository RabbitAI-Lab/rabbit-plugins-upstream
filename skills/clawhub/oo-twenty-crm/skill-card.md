## Description:

This skill supports Twenty CRM (twenty.com) requests for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to manage Twenty CRM workspace records through OOMOL-connected actions, including listing metadata, reading records, and creating, updating, or deleting records with confirmation safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Prefer an official versioned release or package-manager installation path with integrity verification before installing the oo CLI.

Risk: The skill can create, update, and delete CRM records through a connected OOMOL account.

Mitigation: Confirm exact payloads, target records, and expected effects before allowing write or destructive actions.

Risk: Twenty CRM actions are routed through OOMOL as an intermediary.

Mitigation: Install only when use of OOMOL for CRM actions is acceptable for the workspace's data handling requirements.

## Reference(s):

- [Twenty CRM homepage](https://twenty.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twenty-crm)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger Twenty CRM connector actions through the oo CLI when the user has configured OOMOL credentials.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
