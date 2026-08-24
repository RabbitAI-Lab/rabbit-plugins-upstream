## Description:

Guides agents in designing, refactoring, and testing Go applications with dependency injection using manual constructor wiring or Go DI libraries such as google/wire, uber-go/dig, uber-go/fx, and samber/do.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to choose an appropriate dependency injection pattern for Go services, generate wiring code, and refactor tightly coupled code toward constructor injection and testable boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refactor mode may read and edit Go files across broad application logic and may use sub-agents to inspect dependency patterns.

Mitigation: Review generated edits and suggested git or Go commands before applying them, then run the project's tests and linters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-dependency-injection)
- [samber Go skills homepage](https://github.com/samber/cc-skills-golang)
- [Manual Constructor Injection](references/manual-di.md)
- [google/wire - Compile-Time Code Generation](references/google-wire.md)
- [uber-go/dig + uber-go/fx - Reflection-Based DI](references/uber-dig-fx.md)
- [samber/do - Generics-Based DI](references/samber-do.md)
- [samber/do documentation](https://do.samber.dev)
- [google/wire user guide](https://github.com/google/wire/blob/main/docs/guide.md)
- [uber-go/fx documentation](https://uber-go.github.io/fx/)
- [uber-go/dig repository](https://github.com/uber-go/dig)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go code examples, decision tables, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to Go source files and dependency wiring during refactor mode.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
