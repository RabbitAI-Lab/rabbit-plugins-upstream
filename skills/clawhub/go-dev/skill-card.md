## Description:

Opinionated Go setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just. Use when starting a Go project, configuring lint, format, test, coverage or CI, writing a Justfile, wiring migrations, or leaving a Makefile workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to set up and maintain Go project tooling for linting, formatting, testing, coverage, CI, Justfile workflows, database migrations, and Lefthook hooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup examples can install development tools or fetch binaries.

Mitigation: Review commands before execution and prefer pinned package-manager or checksum-verified installation methods over curl-to-shell.

Risk: Some recipes and hook examples can rewrite files or restage changes.

Mitigation: Run formatting, lint fixes, and hook configuration changes in a clean worktree and review diffs before committing.

Risk: Migration examples can alter or drop database state when pointed at the wrong target.

Mitigation: Use migration drop and down commands only against intended, backed-up databases and verify DATABASE_URL before execution.

Risk: Lefthook installation changes Git hook behavior for the repository.

Mitigation: Review the generated hook configuration, validate it in CI, and make hook installation an explicit onboarding step.

## Reference(s):

- [go-dev ClawHub page](https://clawhub.ai/tenequm/skills/go-dev)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/go-dev)
- [golang-migrate Reference](references/go-migrate-reference.md)
- [Go Testing Reference](references/go-testing-reference.md)
- [gofumpt Reference](references/gofumpt-reference.md)
- [golangci-lint v2 Reference](references/golangci-lint-reference.md)
- [gotestsum Reference](references/gotestsum-reference.md)
- [Justfile Reference for Go Projects](references/justfile-reference.md)
- [Lefthook Reference](references/lefthook-reference.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks, shell commands, YAML, Justfile recipes, and Go snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project setup steps, pinned tool versions, CI examples, migration recipes, and hook configuration guidance.]

## Skill Version(s):

0.4.1 (source: frontmatter, changelog released 2026-09-17, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
