## Description:

Manus (manus.im) lets an agent read, create, update, message, stop, confirm, and delete Manus tasks and related Manus resources through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Manus tasks, projects, connectors, skills, browser clients, custom agents, and task messages from a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run unverified internet installer scripts that execute local code.

Mitigation: Install only from trusted OOMOL sources and prefer reviewing or using a verified installer instead of piping remote scripts directly into a shell.

Risk: Write and destructive Manus actions can change or delete account data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-manus)
- [Manus Homepage](https://manus.im)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns oo CLI JSON responses when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
