## Description:

Opinionated Go development setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to set up or modernize Go projects with linting, formatting, testing, coverage, CI, Justfile workflows, database migrations, and Git hooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Migration recipes and commands using DATABASE_URL can alter the database they target.

Mitigation: Review DATABASE_URL and migration targets before running commands; test migrations against a disposable or development database first.

Risk: Autofix, formatting, and Git hook setup commands can modify source files or repository behavior.

Mitigation: Run commands from a clean worktree, inspect generated Justfile, CI, and lefthook configuration, and review diffs before committing.

## Reference(s):

- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/go-dev)
- [golangci-lint Reference](references/golangci-lint-reference.md)
- [gofumpt Reference](references/gofumpt-reference.md)
- [gotestsum Reference](references/gotestsum-reference.md)
- [Go Testing Reference](references/go-testing-reference.md)
- [golang-migrate Reference](references/go-migrate-reference.md)
- [Justfile Reference for Go Projects](references/justfile-reference.md)
- [Go Official Docs](https://go.dev/doc/)
- [golangci-lint Docs](https://golangci-lint.run/)
- [Go 1.27 Release Notes](https://go.dev/doc/go1.27)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, YAML configuration, Justfile recipes, and CI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project scaffolding guidance, tool installation commands, lint and test recipes, database migration commands, and CI configuration snippets.]

## Skill Version(s):

0.3.0 (source: frontmatter, CHANGELOG, server release metadata; released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
