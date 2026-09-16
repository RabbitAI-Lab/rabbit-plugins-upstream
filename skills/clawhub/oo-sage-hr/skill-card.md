## Description:

Sage HR connector for searching and reading Sage HR data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, HR operators, and supporting agents use this skill to search and read Sage HR employee, position, team, termination, and time off data through a connected OOMOL/Sage HR account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer commands that can execute unverified code.

Mitigation: Review the installer source or use a verified manual oo CLI installation path before running setup commands.

Risk: The skill can access sensitive HR records through the connected OOMOL/Sage HR account.

Mitigation: Use only accounts with appropriate Sage HR permissions and confirm the connected account and scope before requesting employee or time off data.

## Reference(s):

- [ClawHub Sage HR skill page](https://clawhub.ai/oomol/skills/oo-sage-hr)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Sage HR homepage](https://www.sage.com/en-us/sage-business-cloud/people/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; command responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
