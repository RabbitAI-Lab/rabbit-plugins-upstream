## Description:

TalentHR helps an agent operate a TalentHR account through OOMOL's oo CLI, including inspecting connector schemas and changing employee roles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, HR operators, and developers use this skill to let an agent operate TalentHR through an OOMOL-connected account. The skill is most relevant when the agent needs to inspect the live connector schema and submit employee role-change requests with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents itself as read-focused while its listed action can change employee roles.

Mitigation: Require explicit user confirmation of the exact employee, requested role, payload, and expected effect before running any role-change action.

Risk: The setup path suggests remote installer commands that may be difficult to verify when piped directly into a shell.

Mitigation: Prefer a verified oo CLI installation path and validate the installer by checksum or signature before execution.

Risk: Actions run through an OOMOL-connected TalentHR account and may affect live HR data.

Mitigation: Use the least-privileged connected account available, inspect the live connector schema before each request, and limit execution to the intended TalentHR action.

## Reference(s):

- [TalentHR homepage](https://www.talenthr.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub TalentHR skill page](https://clawhub.ai/oomol/skills/oo-talenthr)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-managed credentials and instructs the agent to inspect live action schemas before constructing requests.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
