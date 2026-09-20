## Description:

Use SimplyBook.me through the OOMOL oo connector to list services and performers, check availability, and read public company configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators with an OOMOL-connected SimplyBook.me account use this skill to retrieve service, performer, availability, and company information without handling raw SimplyBook.me credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes downloaded shell and PowerShell installer commands.

Mitigation: Review the installer path before installing, prefer trusted and versioned OOMOL documentation, and avoid letting an agent run curl-to-bash or iex setup commands automatically.

Risk: Authentication or connection setup could be triggered unnecessarily if the CLI or SimplyBook.me connection is not already ready.

Mitigation: Run setup steps only after a matching command failure, and do not proactively run account login or connection-opening commands.

## Reference(s):

- [ClawHub SimplyBook.me skill listing](https://clawhub.ai/oomol/skills/oo-simplybook-me)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [SimplyBook.me homepage](https://simplybook.me/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SimplyBook.me action results are returned as JSON through the oo connector after the CLI and account connection are already configured.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
