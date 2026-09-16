## Description:

Habitica lets an agent read, create, update, score, and delete Habitica tasks and tags through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage a connected Habitica account from an agent, including reading profile and task data and making confirmed task or tag changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Prefer an official, versioned oo CLI package or a download-and-verify installation flow before using the skill.

Risk: Write and destructive Habitica actions can change or delete tasks and tags in the connected account.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Habitica homepage](https://habitica.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-habitica)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing Habitica action payloads.]

## Skill Version(s):

1.0.3 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
