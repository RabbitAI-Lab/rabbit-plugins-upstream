## Description:

Helps agents organize long-running, multi-phase projects with a layered directory structure, file placement guidance, project scaffolding, audits, and recoverable deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomuiv](https://clawhub.ai/user/tomuiv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents managing long-lived projects use this skill to create project structures, sort incoming files, audit directory hygiene, and archive or recover work. It is not intended for short-lived tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project files can be moved or deleted during organization and cleanup.

Mitigation: Review proposed moves and deletions before applying them; keep important files outside buffer as the only copy, and confirm irreversible purge operations.

Risk: OpenCode project-record repair may alter local records and optionally perform SSH-based sync cleanup.

Mitigation: Avoid the sync-hub repair option unless you understand the database and remote cleanup it performs.

Risk: Hard-delete options and unrestricted output paths can affect files outside the intended project.

Mitigation: Verify target paths and review any --hard or --out options before execution.

## Reference(s):

- [Project organization operations manual](references/ops-manual.md)
- [Project organization on ClawHub](https://clawhub.ai/tomuiv/skills/project-organization)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance and shell commands; project files and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-management commands can create, move, archive, or delete files.]

## Skill Version(s):

2.5.2 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
