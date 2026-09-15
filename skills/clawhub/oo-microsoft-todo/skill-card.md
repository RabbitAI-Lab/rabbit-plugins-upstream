## Description:

Enables an agent to read, create, update, and delete Microsoft To Do task lists, tasks, and checklist items through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Microsoft To Do task lists, tasks, and checklist items through an OOMOL-connected account. It supports read workflows as well as confirmed write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that are not version-pinned or checksum-verified.

Mitigation: Review the OOMOL CLI setup path before installation and prefer official, version-pinned instructions with checksum or signature verification.

Risk: Write and destructive actions can change or delete Microsoft To Do data.

Mitigation: Allow write or delete actions only after the exact target, payload, and expected effect are clear and explicitly approved.

## Reference(s):

- [Microsoft To Do homepage](https://to-do.office.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-microsoft-todo)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; write and destructive actions require clear user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
