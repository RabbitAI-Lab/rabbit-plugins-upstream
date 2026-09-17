## Description:

Helps agents manage Mobile Text Alerts subscribers through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to read, create, update, list, search, and delete Mobile Text Alerts subscribers from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute directly in a shell.

Mitigation: Review the oo CLI installation path and prefer an official package manager or downloaded installer with a published checksum or signature.

Risk: Subscriber create, update, and delete actions can change or remove Mobile Text Alerts data.

Mitigation: Confirm the exact payload and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mobile-text-alerts)
- [Mobile Text Alerts Homepage](https://mobile-text-alerts.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
