## Description:

Vibe Coding Toolkit helps agents run local project-governance workflows for project health checks, commit validation, task routing, project initialization, and optional non-Git snapshots without network access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

External developers and project owners use this skill to ask an agent to initialize a project governance structure, check project health, validate commits, route task state, and manage opt-in local snapshots for projects that are not using Git.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently alter local project and agent state by creating governance files, installing a commit-msg hook, appending a memory pointer, and managing snapshot files.

Mitigation: Review the target project changes before and after use, keep the project under version control or backup, and disable HOOK_ENABLED if local Git hook enforcement is not desired.

Risk: Snapshot rollback or cleanup can replace or delete local project files when explicitly invoked.

Mitigation: Require explicit human confirmation before rollback or cleanup and review the snapshot target directories before authorizing the operation.

Risk: The security summary flags broad snapshot routing and an under-scoped review check.

Mitigation: Treat generated checks and reports as review aids, verify the affected files manually, and avoid delegating rollback or cleanup decisions to the agent alone.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/vibe-coding-toolkit)
- [README](README.md)
- [Health check documentation](docs/health-check.md)
- [Commit check documentation](docs/commit-check.md)
- [Project initialization documentation](docs/project-init.md)
- [Task manager documentation](docs/task-manager.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command invocations and local project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local governance files, commit hooks, audit logs, task records, and optional snapshots inside the target project.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
