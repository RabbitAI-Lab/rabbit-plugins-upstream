## Description:

Deep reference for Lance v11 - the open columnar lakehouse format for multimodal AI - and its Rust crate workspace plus pylance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and data engineers use this skill as a technical reference when building directly on Lance crates or pylance, reading `.lance` datasets, or reasoning about Lance file, table, index, transaction, schema evolution, and object-store behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copy-pasted cleanup commands can remove unintended files if run in the wrong directory.

Mitigation: Run examples in a dedicated test directory and review deletion targets such as rm -rf or shutil.rmtree before execution.

Risk: The reference covers beta and unstable Lance format details whose APIs or encodings can change.

Mitigation: Pin explicit Lance tags or stable format versions and confirm compatibility before applying guidance to production datasets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/lance-format)
- [OpenClaw Homepage](https://github.com/tenequm/skills/tree/main/skills/lance-format)
- [Lance Reference Index](references/lance-reference.md)
- [File Format Reference](references/format-file.md)
- [Table Format Reference](references/format-table.md)
- [Indexes Reference](references/indexes.md)
- [Operations Reference](references/ops.md)
- [Performance Reference](references/performance.md)
- [Lance v7-v11 Changelog](references/changelog-v7-v11.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, configuration details, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only reference; no direct tool calls or credentials required.]

## Skill Version(s):

0.14.1 (source: frontmatter and changelog, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
