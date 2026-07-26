## Description: <br>
go-dev helps agents set up an opinionated Go development stack with linting, formatting, testing, CI, task runner, and database migration guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineering agents use go-dev when creating or upgrading Go projects that need consistent linting, formatting, testing, CI/CD, Justfile recipes, and database migration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tool installation commands can execute downloaded or newly installed binaries. <br>
Mitigation: Review commands before running them and prefer package managers or verified release artifacts. <br>
Risk: Database migration recipes can modify, revert, or delete database state when DATABASE_URL points at the wrong target. <br>
Mitigation: Confirm DATABASE_URL and the intended environment before running migration, down, force, or drop commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/go-dev) <br>
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/go-dev) <br>
- [golangci-lint Reference](references/golangci-lint-reference.md) <br>
- [gofumpt Reference](references/gofumpt-reference.md) <br>
- [gotestsum Reference](references/gotestsum-reference.md) <br>
- [Go Testing Reference](references/go-testing-reference.md) <br>
- [golang-migrate Reference](references/go-migrate-reference.md) <br>
- [Justfile Reference](references/justfile-reference.md) <br>
- [Go Official Docs](https://go.dev/doc/) <br>
- [golangci-lint Docs](https://golangci-lint.run/) <br>
- [gofumpt](https://github.com/mvdan/gofumpt) <br>
- [gotestsum](https://github.com/gotestyourself/gotestsum) <br>
- [golang-migrate](https://github.com/golang-migrate/migrate) <br>
- [Lefthook](https://github.com/evilmartians/lefthook) <br>
- [just](https://github.com/casey/just) <br>
- [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown prose with fenced shell, YAML, Justfile, Go, and SQL code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes optional DATABASE_URL-dependent migration recipes and tool installation commands that users run manually.] <br>

## Skill Version(s): <br>
0.2.2 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
