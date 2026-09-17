## Description:

Use this skill for Dida365 requests that read, create, update, and delete task, project, and habit data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Dida365 tasks, projects, and habits through an OOMOL-connected account. The skill supports read operations plus confirmed write and destructive actions for task-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes a remote installer executed directly in a shell.

Mitigation: Use a verified installation path when available, or inspect and validate the installer before execution.

Risk: Write and destructive connector actions can change or remove Dida365 tasks, projects, or habit data.

Mitigation: Confirm the exact target, payload, and expected effect before running actions tagged as write or destructive.

## Reference(s):

- [Dida365 homepage](https://dida365.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dida365)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
