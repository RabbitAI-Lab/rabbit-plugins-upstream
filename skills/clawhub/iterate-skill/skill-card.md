## Description:

Automates multi-round code review and repair across configurable dimensions, and supports defensive, incremental coding tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to review and improve code quality through repeated review, repair, and validation rounds, or to complete incremental coding tasks with defensive pre-checks and post-checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Updates and removal can follow redirected project folders and overwrite or delete another installation outside the selected project.

Mitigation: Wait for destination-containment fixes before using update or uninstall in untrusted projects.

Risk: Project validation commands and scripts can affect the review or package being produced.

Mitigation: Review validation commands and project scripts, and inspect generated packages before publishing.

Risk: Automatic merge and push can publish changes before they are reviewed.

Mitigation: Keep automatic merge and push disabled unless explicitly needed and reviewed.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Markdown reports]

**Output Format:** [Code edits, shell commands, configuration guidance, and Markdown review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

3.10.0 (source: frontmatter, pyproject.toml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
