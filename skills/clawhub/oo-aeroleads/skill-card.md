## Description:

Runs AeroLeads searches and reads through the OOMOL oo CLI, including prospect-detail lookup from public LinkedIn profile URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve AeroLeads prospect details from public LinkedIn profile URLs through an OOMOL-connected AeroLeads account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified internet installer executed directly from a URL.

Mitigation: Review the setup path before installing and prefer a pinned, verifiable oo CLI release or a package manager with integrity checks.

Risk: AeroLeads credentials and prospect data are brokered through OOMOL connector access.

Mitigation: Connect AeroLeads credentials to OOMOL only after confirming the account owner accepts that service path for prospect data.

## Reference(s):

- [ClawHub AeroLeads skill page](https://clawhub.ai/oomol/skills/oo-aeroleads)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [AeroLeads homepage](https://aeroleads.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
