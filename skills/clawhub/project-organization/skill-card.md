## Description:

Organizes long-running, multi-stage projects with hierarchical folders, project scaffolding, structure checks, recoverable trash, and an operation journal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomuiv](https://clawhub.ai/user/tomuiv)

### License/Terms of Use:

MIT

## Use Case:

Developers and other people managing long-running projects use this skill to create and maintain organized project and subproject folders, audit their layout, and move obsolete files into recoverable trash.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trash and restore operations can affect files outside the intended project directory, especially when given absolute paths.

Mitigation: Limit operations to explicitly chosen project directories; do not pass absolute paths outside the project root to trash.py.

Risk: Forced restore can permanently remove an existing destination before restoring a trashed item.

Mitigation: Inspect trash manifests and destination files before restoring; avoid restore --force unless the destination has been verified.

Risk: Permanent purging of trash removes the recovery option.

Mitigation: Review the items to be purged and obtain user confirmation before permanent deletion.

## Reference(s):

- [Project Organization on ClawHub](https://clawhub.ai/tomuiv/skills/project-organization)
- [Publisher profile: tomuiv](https://clawhub.ai/user/tomuiv)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Markdown]

**Output Format:** [Markdown guidance and project files; scripts return JSON status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local project structure and operation logs; trash operations can move, restore, or permanently remove files.]

## Skill Version(s):

2.0.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
