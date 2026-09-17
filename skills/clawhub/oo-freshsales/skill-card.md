## Description:

Freshsales (freshworks.com). Use this skill for ANY Freshsales request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent operate Freshsales contacts through an OOMOL-connected account, including reading contact data and creating, updating, or deleting contact records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may involve downloaded shell or PowerShell installer scripts.

Mitigation: Review the OOMOL CLI installation process and installer contents before use, and avoid piping downloaded scripts directly into a shell.

Risk: Write and destructive Freshsales actions can create, update, or delete CRM contact records.

Mitigation: Confirm the exact action, target record, payload, and expected effect before running create, update, or delete operations.

Risk: Freshsales operations are routed through OOMOL's connector service.

Mitigation: Confirm that the organization approves use of OOMOL's connector service and the connected Freshsales credentials before use.

## Reference(s):

- [ClawHub Freshsales skill page](https://clawhub.ai/oomol/skills/oo-freshsales)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Freshsales homepage](https://www.freshworks.com/crm/sales/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Freshsales connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
