## Description:

Namely (namely.com). Use this skill for ANY Namely request, including searching and reading data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, HR operators, and agents use this skill to read Namely employee profile data, profile fields, and the current connected profile through an OOMOL-connected Namely account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands and the skill can read sensitive HR profile data through Namely/OOMOL scopes.

Mitigation: Review before installing, use a verified or pinned oo CLI installation method, and confirm the connected Namely/OOMOL scopes expose only the employee data the agent is intended to read.

## Reference(s):

- [Namely homepage](https://www.namely.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-namely)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live connector schemas and run read-only Namely connector actions that return JSON data.]

## Skill Version(s):

1.0.3 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
