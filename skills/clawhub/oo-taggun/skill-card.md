## Description:

Taggun (taggun.io). Use this skill for ANY Taggun request - searching and reading data. Whenever a task involves Taggun, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Taggun through an OOMOL-connected account, including extracting receipt or invoice data from public HTTPS URLs, listing campaign IDs, retrieving campaign settings, and validating receipts against campaign settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote shell installer commands that execute downloaded scripts directly.

Mitigation: Review and verify the OOMOL installer through a trusted channel before installation; avoid curl-to-bash or PowerShell iex execution when verification is not possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-taggun)
- [Taggun Homepage](https://www.taggun.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; responses from connector actions are JSON.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
