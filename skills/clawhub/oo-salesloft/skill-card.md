## Description:

Salesloft (salesloft.com). Use this skill for Salesloft requests involving searching and reading data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and revenue-operations users can have an agent retrieve Salesloft accounts, cadences, people, and current-user data through an OOMOL-connected Salesloft account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants the agent broad authority to run oo CLI commands against an OOMOL-connected Salesloft account.

Mitigation: Install only for accounts where agent access to Salesloft data is acceptable, and keep use scoped to the listed read actions unless the user explicitly approves broader behavior.

Risk: The setup instructions include remote installer commands for the oo CLI.

Mitigation: Review the installer source or use a verified installation method before executing installer commands.

Risk: Connector responses may expose sensitive Salesloft CRM data.

Mitigation: Use the least-privileged Salesloft connection available and avoid sharing retrieved records beyond the intended task.

## Reference(s):

- [ClawHub Salesloft skill page](https://clawhub.ai/oomol/skills/oo-salesloft)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Salesloft homepage](https://www.salesloft.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON data, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
