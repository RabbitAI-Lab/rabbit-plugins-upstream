## Description:

Workpath (workpath.com). Use this skill for ANY Workpath request - searching and reading data. Whenever a task involves Workpath, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to search and read Workpath goals, key results, teams, and users through an OOMOL-connected Workpath account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts immediately.

Mitigation: Review the setup path before installing and prefer a pinned, signed, or checksum-verified oo CLI installation method.

Risk: The connector can expose Workpath data visible to the connected account.

Mitigation: Connect only a Workpath account whose visible goals, key results, teams, and users are appropriate for agent-mediated access.

## Reference(s):

- [Workpath homepage](https://www.workpath.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Workpath skill page](https://clawhub.ai/oomol/skills/oo-workpath)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs Workpath connector actions through the oo CLI after inspecting the live action schema.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
