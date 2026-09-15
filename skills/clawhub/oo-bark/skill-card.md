## Description:

Bark lets an agent inspect live Bark connector schemas and run read or notification-sending actions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect Bark action schemas, fetch Bark server information, and send standard, batch, or pre-encrypted notifications through an OOMOL-connected Bark account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup presents remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer an official package manager or a download-and-verify installation flow before running the oo CLI.

Risk: Write actions can send notifications to connected Bark devices, including batch and pre-encrypted notification payloads.

Mitigation: Confirm the exact payload, target devices or keys, and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Bark Skill](https://clawhub.ai/oomol/skills/oo-bark)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Bark Homepage](https://bark.day.app)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
