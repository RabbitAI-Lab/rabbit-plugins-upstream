## Description:

Bark (bark.day.app). Use this skill for Bark requests that read server information or send standard, batch, and pre-encrypted notifications through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Bark service through OOMOL, inspect live action schemas, retrieve server information, and send Bark notifications with user confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary code if the installer source is not trusted.

Mitigation: Review the installer source independently or use a pinned, signed, or package-manager installation path before running installation commands.

Risk: Write actions send Bark notifications and may affect connected devices or recipients.

Mitigation: Confirm the action, target device keys, payload, and expected effect with the user before executing write actions.

## Reference(s):

- [Bark homepage](https://bark.day.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Bark skill](https://clawhub.ai/oomol/skills/oo-bark)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before requests; write actions require confirmation before execution.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
