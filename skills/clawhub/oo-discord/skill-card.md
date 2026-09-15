## Description:

Enables agents to operate Discord through an OOMOL-connected account for reading account and guild data and performing confirmed write or destructive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Discord connector schemas, run Discord actions through the oo CLI, and manage Discord account, guild, invite, widget, entitlement, OAuth, and role-connection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install guidance includes an unverified remote installer pipeline.

Mitigation: Review installation steps before use and prefer official signed or checksum-verified installation methods.

Risk: Discord account, guild, authorization, and linked-connection reads can expose private user data.

Mitigation: Run read actions only for explicit user requests and handle returned Discord data as private.

Risk: Write and destructive Discord actions can change or remove account role-connection data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-discord)
- [Discord Homepage](https://discord.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Discord connector JSON responses through the oo CLI when actions are executed.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
