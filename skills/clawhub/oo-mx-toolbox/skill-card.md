## Description:

MxToolbox lets an agent query MxToolbox through the OOMOL mx_toolbox connector for DNS, email-authentication, HTTP, SMTP, blacklist, monitor, and API-usage diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and operations teams use this skill to inspect live connector schemas and run MxToolbox lookups through an OOMOL-connected account for diagnostics and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that run downloaded scripts directly in a shell.

Mitigation: Prefer an official, versioned installer with checksum or signature verification, and do not run installer commands until the user confirms the source and need.

Risk: The skill uses OOMOL as an intermediary for MxToolbox account access.

Mitigation: Install only when using OOMOL as an intermediary is acceptable, and have the user approve login, account-connection, billing, and credential-refresh steps.

## Reference(s):

- [MxToolbox ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mx-toolbox)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [MxToolbox Homepage](https://mxtoolbox.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return official MxToolbox JSON response payloads when connector actions are run.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
