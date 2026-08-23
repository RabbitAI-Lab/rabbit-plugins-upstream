## Description:

Golang data structures: slices, maps, arrays, container/list/heap/ring, strings.Builder versus bytes.Buffer, generic collections, pointers, and copy semantics for choosing or optimizing Go data structures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when selecting, implementing, reviewing, or optimizing Go data structures, especially where memory layout, allocation behavior, copy semantics, generics, or pointer rules affect correctness and performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can edit Go files and run Go-related or git commands.

Mitigation: Review proposed file changes and command effects before committing or deploying them.

Risk: Guidance involving unsafe.Pointer can affect memory safety and correctness.

Mitigation: Confirm unsafe pointer usage follows Go's documented valid conversion patterns and includes appropriate bounds checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-data-structures)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Container Packages and String Builders](references/containers.md)
- [Writing Generic Data Structures](references/generics.md)
- [Map Internals Deep Dive](references/map-internals.md)
- [Pointer Types Deep Dive](references/pointers.md)
- [Slice Internals](references/slice-internals.md)
- [Go Data Structures](https://research.swtch.com/godata)
- [The Go Memory Model](https://go.dev/ref/mem)
- [Effective Go](https://go.dev/doc/effective_go)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with Go code examples and shell commands when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include edits to Go files and recommendations that should be reviewed before committing]

## Skill Version(s):

1.2.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
