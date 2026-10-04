## Description:

Helps developers set up Go projects with consistent linting, formatting, testing, task automation, migrations, and CI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to scaffold or update Go project tooling, generate configuration and commands for quality checks and CI, and manage database migrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute unreviewed code.

Mitigation: Review commands and prefer verified release artifacts over curl-to-shell installers.

Risk: Unpinned tools in automation can change unexpectedly.

Mitigation: Pin Docker/npm-style tool versions before using them in automation.

Risk: Migration commands can modify the wrong database.

Mitigation: Confirm DATABASE_URL points to the intended database before running migrations.

Risk: Installing Git hooks can leave persistent jobs in a repository.

Mitigation: Inspect lefthook jobs before installing hooks.

## Reference(s):

- [go-dev ClawHub release](https://clawhub.ai/tenequm/skills/go-dev)
- [Publisher-listed skill homepage](https://github.com/tenequm/skills/tree/main/skills/go-dev)
- [Go documentation](https://go.dev/doc/)
- [Go testing reference](references/go-testing-reference.md)
- [golangci-lint reference](references/golangci-lint-reference.md)
- [Database migration reference](references/go-migrate-reference.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapt commands and configuration to the target Go project before execution.]

## Skill Version(s):

0.5.0 (source: frontmatter, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
