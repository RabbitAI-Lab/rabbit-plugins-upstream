## Description:

Workpath lets an agent search and read Workpath goals, key results, teams, and users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers with access to an OOMOL-connected Workpath account use this skill to retrieve Workpath planning data during agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read Workpath goals, key results, teams, and users visible to the connected OOMOL account.

Mitigation: Confirm the user is comfortable with that read access before installation or first use.

Risk: Setup commands can install the OOMOL CLI, start login, or open account connection and billing flows.

Mitigation: Run setup only after an action fails because the CLI, authentication, Workpath connection, or billing state is missing.

## Reference(s):

- [ClawHub Workpath Skill](https://clawhub.ai/oomol/skills/oo-workpath)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Workpath Homepage](https://www.workpath.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect each live connector schema before sending a JSON payload.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
