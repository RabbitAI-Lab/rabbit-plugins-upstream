## Description:

MoonClerk (moonclerk.com). Use this skill for MoonClerk searching and read-only data retrieval through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve MoonClerk customers, payment forms, and payments from an OOMOL-connected account after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run remote installer scripts directly in a shell.

Mitigation: Review setup before installation and prefer a verifiable package manager or downloaded, inspected, signed release.

Risk: Connector use can read MoonClerk customer and payment data from the connected account.

Mitigation: Use an account and connection scope appropriate for the task, and run read actions only when the user has requested that data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-moonclerk)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [MoonClerk Homepage](https://moonclerk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
