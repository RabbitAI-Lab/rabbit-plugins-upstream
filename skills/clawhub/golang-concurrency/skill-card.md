## Description:

Golang concurrency patterns. Use when writing or reviewing concurrent Go code involving goroutines, channels, select, locks, sync primitives, errgroup, singleflight, worker pools, or fan-out/fan-in pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write, review, and audit concurrent Go code for goroutine lifecycle management, channel ownership, synchronization, worker pools, pipelines, and race-prone patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to read and edit Go source files for concurrency work.

Mitigation: Scope use to intended Go paths and review generated changes before applying them.

Risk: Concurrency edits can introduce subtle leaks, races, deadlocks, or behavior changes if applied without verification.

Mitigation: Run project tests, race checks, and relevant Go linters after applying any proposed changes.

Risk: Some guidance is version-sensitive, including loop-variable capture behavior before Go 1.22 and experimental Go 1.26 goroutine leak profiling.

Mitigation: Confirm the target module's Go version and avoid relying on experimental diagnostics unless explicitly enabled.

## Reference(s):

- [Skill homepage](https://github.com/samber/cc-skills-golang)
- [Channels and Select Patterns](references/channels-and-select.md)
- [Pipelines and Worker Pools](references/pipelines.md)
- [Sync Primitives Deep Dive](references/sync-primitives.md)
- [Go Concurrency Patterns: Pipelines](https://go.dev/blog/pipelines)
- [Effective Go: Concurrency](https://go.dev/doc/effective_go#concurrency)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code examples and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to Go source files and commands for Go tooling; generated changes should be reviewed before use.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
