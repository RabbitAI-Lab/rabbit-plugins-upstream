## Description:

Opinionated Go setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just for starting Go projects, configuring lint, format, test, coverage or CI, writing a Justfile, wiring migrations, or leaving a Makefile workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to set up or migrate Go projects with linting, formatting, testing, coverage, CI, Justfile workflows, database migrations, and Git hooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may fetch or execute remote installer content or mutable tool versions on a user's machine.

Mitigation: Review commands before execution and prefer package managers or pinned release artifacts with checksum or signature verification.

Risk: Migration recipes use DATABASE_URL and can affect the configured database.

Mitigation: Use non-production DATABASE_URL values while testing and confirm the target database before running migration recipes.

Risk: Lefthook hooks change repository behavior after installation.

Mitigation: Review hook configuration and commands before installing hooks into a repository.

## Reference(s):

- [go-dev ClawHub page](https://clawhub.ai/tenequm/skills/go-dev)
- [go-dev homepage](https://github.com/tenequm/skills/tree/main/skills/go-dev)
- [Go Testing Reference](references/go-testing-reference.md)
- [golangci-lint v2 Reference](references/golangci-lint-reference.md)
- [Justfile Reference for Go Projects](references/justfile-reference.md)
- [gotestsum Reference](references/gotestsum-reference.md)
- [Lefthook Reference](references/lefthook-reference.md)
- [gofumpt Reference](references/gofumpt-reference.md)
- [golang-migrate Reference](references/go-migrate-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, YAML, Go, SQL, and configuration code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project setup commands, lint/test/CI recipes, migration guidance, and configuration snippets.]

## Skill Version(s):

0.4.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
