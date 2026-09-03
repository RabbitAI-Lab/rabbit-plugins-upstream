## Description:

Vibe Coding Toolkit helps agents initialize and operate a local project-governance workflow with health checks, commit verification, task tracking, and project setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

Developers, project maintainers, and agent operators use this skill to create local governance files, track AI-assisted work, verify local Git commits, and run project health checks. It is intended for repositories where the user wants the agent to manage project-local governance records and version history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task completion can stage and commit all repository changes, which may include secrets or unrelated files.

Mitigation: Use the skill only in repositories intended for local Git management, review the working tree before task completion, and keep secrets or unrelated files outside the repository.

Risk: Rollback workflows can replace workspace files.

Mitigation: Review the recent commit history and selected rollback target before restoring files.

Risk: The skill creates project-local governance files, logs, a commit-msg hook, and local commits.

Mitigation: Install it only where these project-local changes are expected and acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/vibe-coding-toolkit)
- [User guide](docs/USER_GUIDE.md)
- [Project initialization guide](docs/project-init.md)
- [Task manager guide](docs/task-manager.md)
- [Commit check guide](docs/commit-check.md)
- [Health check guide](docs/health-check.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and project-local file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local governance files, logs, Git commits, commit hooks, task records, and health-check reports depending on the selected subcommand.]

## Skill Version(s):

1.2.0 (source: frontmatter, skill.json, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
