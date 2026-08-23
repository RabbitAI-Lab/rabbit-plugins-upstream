## Description:

Deep reference for Lance v11 - the open columnar lakehouse format for multimodal AI - and its Rust crate workspace plus pylance. Covers the 2.x file format and structural encodings, the table format (manifests, fragments, transactions, OCC), vector / scalar / full-text indexes, MemWAL, schema evolution, time travel, namespaces, and object-store config. Use when building directly on the Lance crates or reading `.lance` datasets; this is the Lance format and engine (`lance-format/lance`), not the LanceDB product built on top of it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill as a deep technical reference for building directly on Lance crates, pylance, or `.lance` datasets, including file and table formats, indexes, schema evolution, object-store behavior, performance, and migration concerns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copied examples may contain inline cloud keys or credential-like placeholders.

Mitigation: Replace credentials with environment variables, IAM or managed identity, or a secret manager before reuse.

Risk: Cleanup commands such as `rm -rf sift* vec_data.lance` can delete local data if copied without review.

Mitigation: Inspect target paths and run cleanup commands only in disposable or confirmed working directories.

Risk: The skill covers Lance v11 beta behavior as well as stable Lance guidance, so applying the wrong version guidance can affect format or migration decisions.

Mitigation: Confirm the Lance version and pin explicit tags before changing production datasets or dependencies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/lance-format)
- [ClawHub metadata homepage](https://github.com/tenequm/skills/tree/main/skills/lance-format)
- [Lance reference](references/lance-reference.md)
- [File format reference](references/format-file.md)
- [Table format reference](references/format-table.md)
- [Indexes reference](references/indexes.md)
- [Performance reference](references/performance.md)
- [Maintenance reference](references/maintenance.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, and file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Developer documentation skill; no executable hooks or hidden runtime behavior were reported by ClawHub security evidence.]

## Skill Version(s):

0.17.1 (source: SKILL.md frontmatter, CHANGELOG.md, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
