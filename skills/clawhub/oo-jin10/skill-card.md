## Description:

Jin10 helps an agent search and read Jin10 market news, quotes, K-line data, supported quote codes, and economic calendar items through OOMOL-connected actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Jin10 financial news, flash updates, quotes, K-line data, supported quote codes, and current-week economic calendar entries from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts for the oo CLI, which the security evidence flags as suspicious if executed without inspection.

Mitigation: Install the CLI only from a trusted source, prefer an official package manager when available, or download and inspect the installer before execution.

Risk: Connector commands depend on an authenticated OOMOL account and a configured Jin10 connection.

Mitigation: Use routine Jin10 read actions after setup, and perform login or connection recovery only when a command fails with an authentication or connection error.

## Reference(s):

- [Jin10 Homepage](https://www.jin10.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-jin10)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented action payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routine actions are read-only; first-time setup may require local CLI installation, sign-in, or connector configuration.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
