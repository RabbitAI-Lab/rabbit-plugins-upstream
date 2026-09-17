## Description:

Daffy lets agents use the OOMOL-connected oo CLI to search and read Daffy account, user, nonprofit, donation, contribution, and cause data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Daffy action schemas and run read-only account, nonprofit, donation, contribution, and user-cause queries through an OOMOL-connected Daffy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may direct users to run remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path and prefer an official package manager, pinned release, or installer with checksum or signature verification.

Risk: Read-only Daffy actions can expose account balance, user, contribution, donation, and cause information through the connected Daffy account.

Mitigation: Run actions only for authorized Daffy accounts and limit handling or sharing of returned account data.

## Reference(s):

- [Daffy homepage](https://www.daffy.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-daffy)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before payload construction; documented Daffy actions in this release are read-only.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
