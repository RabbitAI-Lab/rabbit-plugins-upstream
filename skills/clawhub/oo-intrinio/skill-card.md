## Description:

Intrinio lets agents search Intrinio company and security reference data and retrieve historical end-of-day stock prices through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to access Intrinio market, company, and security data through the OOMOL-connected Intrinio connector instead of calling the Intrinio API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance can lead a user or agent to run a remote oo CLI installer directly without verification.

Mitigation: Review the oo CLI installation source before installing, prefer a versioned installer with checksum or signature verification, and require explicit user approval before running any downloaded script.

## Reference(s):

- [ClawHub Intrinio skill page](https://clawhub.ai/oomol/skills/oo-intrinio)
- [Intrinio homepage](https://intrinio.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include Intrinio data returned through the oo CLI connector.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
