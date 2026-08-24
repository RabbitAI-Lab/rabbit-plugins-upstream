## Description:

Guides agents working in Go projects to design and implement in-memory caches with samber/hot, including eviction algorithms, TTLs, loaders, sharding, stale-while-revalidate, missing-key caching, and Prometheus metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill when adopting or maintaining samber/hot caches in Go services, especially where repeated access to medium- or low-cardinality resources creates latency or backend pressure. It helps select cache algorithms, generate Go usage patterns, and avoid common production pitfalls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated cache code can introduce stale data, excessive memory use, or backend pressure if TTLs, capacities, and loaders are chosen without production context.

Mitigation: Review cache sizing, TTLs, loader error handling, and hit-rate metrics before deployment; prefer measured working-set data and Prometheus monitoring.

Risk: Incorrect samber/hot configuration can panic or leak behavior into production, such as using SetMissing without a missing cache or combining WithoutLocking with WithJanitor.

Mitigation: Check generated builder chains against the skill references and run project tests before accepting changes.

Risk: Cached mutable Go values can be shared across callers and cause data races or corrupted cached state.

Mitigation: Use CopyOnRead and CopyOnWrite patterns when cached values are pointers, maps, slices, or otherwise mutable.

## Reference(s):

- [Algorithm Selection Guide](references/algorithm-guide.md)
- [API Reference](references/api-reference.md)
- [Production Patterns](references/production-patterns.md)
- [samber/hot Go Package Documentation](https://pkg.go.dev/github.com/samber/hot)
- [samber/hot GitHub Repository](https://github.com/samber/hot)
- [ClawHub Source Homepage](https://github.com/samber/cc-skills-golang)
- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-samber-hot)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Go source edits, cache configuration, and Go tool commands for projects using samber/hot.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
