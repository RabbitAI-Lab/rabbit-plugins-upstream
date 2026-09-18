## Description:

Operate TalentHR through an OOMOL-connected account to inspect connector schemas and run TalentHR actions, including employee role changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, HR operators, and developers use this skill to operate TalentHR through the OOMOL `oo` CLI. It supports inspecting live action schemas and changing an employee role after confirming the exact employee and target role.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change employee HR roles even though the published description emphasizes searching and reading data.

Mitigation: Require explicit confirmation before any role change, and verify the exact employee and target role before running the action.

Risk: Remote installer shortcuts fetch and execute the `oo` CLI installer.

Mitigation: Avoid remote installer shortcuts unless the installer source has been independently trusted and verified.

Risk: The OOMOL connector can act on TalentHR data through server-side credentials.

Mitigation: Use only intended OOMOL and TalentHR accounts, and review connector permissions before running actions.

## Reference(s):

- [TalentHR homepage](https://www.talenthr.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub TalentHR skill page](https://clawhub.ai/oomol/skills/oo-talenthr)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include data and meta.executionId values returned by the `oo` CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
