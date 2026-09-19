## Description:

Sendspark lets agents read, create, and update Sendspark data through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Sendspark dynamic video campaigns and prospects from an agent, including creating campaigns, adding prospects, listing campaigns, and retrieving generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer path before use and prefer a verified, pinned, or package-manager install method for first-time setup.

Risk: Sendspark write actions can change campaign or prospect data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before execution.

## Reference(s):

- [ClawHub Sendspark skill page](https://clawhub.ai/oomol/skills/oo-sendspark)
- [Sendspark homepage](https://sendspark.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
