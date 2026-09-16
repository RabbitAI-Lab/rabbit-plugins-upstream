## Description:

Streak (streak.com). Use this skill for ANY Streak request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to search and read Streak CRM data through an OOMOL-connected account, including boxes, pipelines, and the authenticated current user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through a verified safer method and review installer contents before execution.

Risk: The skill grants broad Bash authority for oo CLI commands compared with its read-only Streak purpose.

Mitigation: Use a narrower tool permission than Bash(oo *) when the agent environment supports scoped tool access.

Risk: Using the skill requires trusting OOMOL with access to Streak data through the connected account.

Mitigation: Install only after confirming the OOMOL account, Streak connection, and data access scope are appropriate for the deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-streak)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Streak Homepage](https://www.streak.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before building command payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
