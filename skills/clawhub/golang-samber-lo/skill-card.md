## Description:

Provides agent guidance for using samber/lo functional programming helpers in Go, including package selection, common patterns, standard-library interop, performance tradeoffs, and safe use of mutable, parallel, iterator, and experimental SIMD variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill when adopting or maintaining Go code that imports github.com/samber/lo, or when choosing between samber/lo package variants for batch collection transformations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated code may use mutable helpers that alter input slices or parallel helpers where goroutine overhead or missing cancellation makes them inappropriate.

Mitigation: Review generated code before applying it, profile before switching to mutable or parallel variants, and use context-aware concurrency patterns for I/O-bound fan-out.

Risk: Suggested package variants have Go version and stability constraints, including Go 1.23+ for lo/it and experimental API stability for lo/exp/simd.

Mitigation: Check the module Go version, pin dependencies when using experimental packages, benchmark performance-sensitive changes, and run the project's normal tests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-samber-lo)
- [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang)
- [samber/lo GitHub repository](https://github.com/samber/lo)
- [samber/lo documentation](https://lo.samber.dev)
- [pkg.go.dev github.com/samber/lo](https://pkg.go.dev/github.com/samber/lo)
- [Package Guide](references/package-guide.md)
- [API Reference](references/api-reference.md)
- [Advanced Patterns](references/advanced-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go code examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May suggest Go dependency commands, code edits, package-selection guidance, and review steps for generated code.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
