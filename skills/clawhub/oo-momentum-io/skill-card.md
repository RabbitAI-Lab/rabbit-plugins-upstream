## Description:

Momentum.io connector skill for searching and reading Momentum.io meetings, users, signal prompts, signal definitions, and signal execution history through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Momentum.io data available through an OOMOL-connected account, including meetings, users, signal prompts, definitions, and execution history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Inspect and verify the installer or use a trusted package source before running installation commands.

Risk: The skill can read Momentum.io data available through the connected OOMOL account.

Mitigation: Install only for users who are authorized to access that Momentum.io workspace, and review returned data before sharing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-momentum-io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Momentum.io homepage](https://www.momentum.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when commands run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
