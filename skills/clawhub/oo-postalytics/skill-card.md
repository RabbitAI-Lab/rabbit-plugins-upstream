## Description:

Postalytics lets an agent inspect schemas and run read-only Postalytics campaign, contact, and template actions through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Postalytics campaign, delivery, engagement, contact, contact-list, and direct-mail template information from an authenticated Postalytics account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Review the installation path first; prefer a trusted package manager or manually downloaded and verified installer, and do not let an agent run the remote installer automatically.

Risk: Read-only connector actions can expose Postalytics campaign, contact, and template data from the connected account.

Mitigation: Use an appropriate Postalytics account and inspect the live connector schema before each action so requests stay limited to the intended records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-postalytics)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Postalytics Homepage](https://www.postalytics.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running Postalytics actions; connector responses are JSON objects containing data and metadata.]

## Skill Version(s):

1.0.2 (source: skill metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
