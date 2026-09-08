## Description:

Provides a deep reference for Lance v12, covering the Lance file and table formats, indexes, schema evolution, object-store behavior, and Rust/Python implementation surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when building directly on Lance crates, pylance, or .lance datasets and need format-level guidance for storage layout, indexing, transactions, versioning, and object-store behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copied tutorial commands may delete, overwrite, or otherwise affect local files.

Mitigation: Review commands before execution and run destructive examples only in disposable directories without important data.

Risk: Object-store examples can interact with external blob storage and credentials.

Mitigation: Scope credentials narrowly to trusted buckets or paths and avoid testing with production storage unless the commands have been reviewed.

Risk: The reference tracks Lance v12.0.0-beta.6 while also documenting v11.0.0 as the stable pin.

Mitigation: Verify guidance against the exact Lance version in use, especially for beta format features, manifest flags, and index behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/lance-format)
- [ClawHub Metadata Homepage](https://github.com/tenequm/skills/tree/main/skills/lance-format)
- [Lance Reference Index](references/lance-reference.md)
- [Lance File Format Reference](references/format-file.md)
- [Lance Table Format Reference](references/format-table.md)
- [Lance Indexes and Distributed Builds](references/indexes.md)
- [Lance Operations Reference](references/ops.md)
- [Lance Performance Reference](references/performance.md)
- [Lance v7 to v12 Changelog](references/changelog-v7-v12.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with technical explanations, code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference answers are version-sensitive and should be checked against the user's exact Lance pin.]

## Skill Version(s):

0.18.0 (source: frontmatter, release evidence, changelog released 2026-09-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
