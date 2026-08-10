## Description:

Opinionated Go development setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to set up or modernize Go project tooling for linting, formatting, testing, CI checks, task automation, and database migrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer examples and generated setup commands may fetch or run external tools.

Mitigation: Prefer verified package-manager installs or pinned releases, and review commands before running them.

Risk: Database migration recipes can change or remove data when pointed at the wrong database.

Mitigation: Double-check DATABASE_URL, review migrate-down, down-all, drop, and production migration commands, and use backups or non-production environments when validating changes.

Risk: Generated Justfile and CI snippets may not match every Go module or organization policy.

Mitigation: Review and adapt configuration snippets before adopting them in a repository or CI pipeline.

## Reference(s):

- [go-dev source homepage](https://github.com/tenequm/skills/tree/main/skills/go-dev)
- [golangci-lint Reference](references/golangci-lint-reference.md)
- [gofumpt Reference](references/gofumpt-reference.md)
- [gotestsum Reference](references/gotestsum-reference.md)
- [Go Testing Reference](references/go-testing-reference.md)
- [golang-migrate Reference](references/go-migrate-reference.md)
- [Justfile Reference](references/justfile-reference.md)
- [Go Official Docs](https://go.dev/doc/)
- [golangci-lint Docs](https://golangci-lint.run/)
- [gofumpt](https://github.com/mvdan/gofumpt)
- [gotestsum](https://github.com/gotestyourself/gotestsum)
- [golang-migrate](https://github.com/golang-migrate/migrate)
- [Lefthook](https://github.com/evilmartians/lefthook)
- [just](https://github.com/casey/just)
- [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, YAML, Justfile, SQL, and Go examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-run setup guidance and project configuration snippets; it does not execute tools directly.]

## Skill Version(s):

0.2.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
