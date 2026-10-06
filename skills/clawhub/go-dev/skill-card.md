## Description:

Provides an opinionated Go development setup using golangci-lint, gofumpt, gotestsum, golang-migrate, just, and lefthook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache-2.0

## Use Case:

Go developers use this skill to scaffold projects and set up linting, formatting, tests, CI, task recipes, Git hooks, and database migrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation commands can execute remote code that changes over time.

Mitigation: Review commands first; prefer verified release artifacts or a trusted package manager over piping a remote script into a shell.

Risk: Unpinned container images can change between runs.

Mitigation: Pin Docker images to reviewed versions or digests.

Risk: Formatters and installed Git hooks can modify files or persist across project work.

Mitigation: Run formatters and install hooks only when those project changes are intended; review the resulting diff.

Risk: Database migration commands can change or roll back database state.

Mitigation: Confirm the target DATABASE_URL and approve migration commands before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/tenequm/skills/go-dev)
- [Project homepage (publisher-provided)](https://github.com/tenequm/skills/tree/main/skills/go-dev)
- [golangci-lint reference](artifact/references/golangci-lint-reference.md)
- [gofumpt reference](artifact/references/gofumpt-reference.md)
- [gotestsum reference](artifact/references/gotestsum-reference.md)
- [Go testing reference](artifact/references/go-testing-reference.md)
- [golang-migrate reference](artifact/references/go-migrate-reference.md)
- [Justfile reference](artifact/references/justfile-reference.md)
- [Lefthook reference](artifact/references/lefthook-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go, YAML, shell, and Justfile examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and commands may change project files or database state when run.]

## Skill Version(s):

0.6.0 (source: server release, skill metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
