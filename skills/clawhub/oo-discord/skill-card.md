## Description:

Enables agents to operate Discord through an OOMOL-connected account for reading, creating, updating, and deleting Discord data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent perform Discord connector actions through OOMOL's oo CLI, including reading user, guild, invite, widget, template, OAuth, Gateway, key, sticker, connection, and entitlement data. It can also manage the current OAuth user's application role connection when the user confirms write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup can execute arbitrary local code if the installer source is compromised or untrusted.

Mitigation: Use an existing trusted oo CLI installation when available; before running installer commands, independently verify the OOMOL install source and prefer the documented install guide.

Risk: Write or destructive Discord actions can change or remove account or application role connection data.

Mitigation: Inspect the live action schema and confirm the exact payload, target, and intended effect with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-discord)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Discord Homepage](https://discord.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON responses from oo CLI connector actions.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
