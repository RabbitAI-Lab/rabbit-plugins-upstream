## Description:

Organizes long-lived projects into themed subprojects with scaffolding, file intake, structure checks, activity logs, and recoverable deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomuiv](https://clawhub.ai/user/tomuiv)

### License/Terms of Use:

MIT

## Use Case:

Developers and other project owners use this skill to establish and maintain a clear folder structure for long-running, multi-stage work, including sorting incoming files and archiving or recovering older material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File moves and soft deletion may affect files outside the intended project folder.

Mitigation: Review the dry run, confirm the exact project root and destinations, avoid arbitrary external root or destination combinations, and obtain explicit approval before --apply.

Risk: Purging the trash permanently deletes files.

Mitigation: Review the full deletion list and obtain explicit approval before --confirm.

## Reference(s):

- [Project Organization on ClawHub](https://clawhub.ai/tomuiv/skills/project-organization)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON]

**Output Format:** [Markdown guidance and shell commands; scripts return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Approved operations can create directories and indexes, move files, and record activity.]

## Skill Version(s):

2.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
