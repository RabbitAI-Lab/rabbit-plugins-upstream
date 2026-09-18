## Description:

Operates Workable through an OOMOL-connected account to search and read candidate and job data with the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, recruiters, and recruiting operations teams use this skill to inspect Workable records, list candidates or jobs, and retrieve details without handling raw Workable API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running an unverified remote installer directly in a shell.

Mitigation: Review the setup path before installing and prefer an official or otherwise verified oo CLI installation method.

Risk: The skill relies on OOMOL-mediated access to Workable data.

Mitigation: Use it only when that access path is acceptable for the workspace and confirm any future write or destructive Workable action explicitly.

## Reference(s):

- [ClawHub Workable skill listing](https://clawhub.ai/oomol/skills/oo-workable)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Workable homepage](https://www.workable.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions return JSON data with execution metadata when run through the connector.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
