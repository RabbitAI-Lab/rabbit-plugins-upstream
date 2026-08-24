## Description:

Dependency injection guidance for Go projects using samber/do, covering service containers, lifecycle management, scopes, health checks, graceful shutdown, module organization, and migration from manual constructor injection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when adopting or maintaining samber/do dependency injection in Go applications, especially when organizing service registration, lifecycle behavior, tests, and refactors away from manual constructor wiring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated dependency-injection changes may alter service construction, lifecycles, or shutdown behavior in a Go application.

Mitigation: Review proposed Go diffs, confirm registration lifecycles, and run the project test suite and linting before merging.

Risk: The skill may suggest Go dependency commands or Go-related tooling commands.

Mitigation: Run commands only in a trusted project workspace and review dependency or module file changes before committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-samber-do)
- [Publisher profile](https://clawhub.ai/user/samber)
- [Skill homepage](https://github.com/samber/cc-skills-golang)
- [samber/do package docs](https://pkg.go.dev/github.com/samber/do/v2)
- [samber/do documentation](https://do.samber.dev)
- [samber/do source repository](https://github.com/samber/do)
- [Advanced Usage](references/advanced.md)
- [Testing with samber/do](references/testing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include dependency installation commands, Go code snippets, DI registration patterns, lifecycle guidance, and testing recommendations.]

## Skill Version(s):

1.3.0 (source: server release and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
