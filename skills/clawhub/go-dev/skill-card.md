## Description:

Opinionated Go development setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to create or modernize Go project infrastructure, including linting, formatting, testing, coverage, CI, task automation, and database migration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network-fetched installer commands may install unexpected code or versions.

Mitigation: Review installer commands before use and prefer pinned package-manager or verified release installs where possible.

Risk: Migration recipes use DATABASE_URL and can affect sensitive or unintended databases.

Mitigation: Confirm DATABASE_URL points to the intended environment before running migration commands.

Risk: Some migration examples can revert, drop, or otherwise change schema state.

Mitigation: Run destructive migration commands only after backups, environment checks, and explicit operator review.

## Reference(s):

- [go-dev on ClawHub](https://clawhub.ai/tenequm/skills/go-dev)
- [OpenClaw homepage metadata](https://github.com/tenequm/skills/tree/main/skills/go-dev)
- [golangci-lint Reference](artifact/references/golangci-lint-reference.md)
- [gofumpt Reference](artifact/references/gofumpt-reference.md)
- [gotestsum Reference](artifact/references/gotestsum-reference.md)
- [Go Testing Reference](artifact/references/go-testing-reference.md)
- [golang-migrate Reference](artifact/references/go-migrate-reference.md)
- [Justfile Reference for Go Projects](artifact/references/justfile-reference.md)
- [Go Official Docs](https://go.dev/doc/)
- [golangci-lint Docs](https://golangci-lint.run/)
- [gofumpt](https://github.com/mvdan/gofumpt)
- [gotestsum](https://github.com/gotestyourself/gotestsum)
- [golang-migrate](https://github.com/golang-migrate/migrate)
- [Lefthook](https://github.com/evilmartians/lefthook)
- [just](https://github.com/casey/just)
- [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with YAML, Justfile, shell command, and Go project structure examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference optional DATABASE_URL for database migration recipes.]

## Skill Version(s):

0.2.4 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
