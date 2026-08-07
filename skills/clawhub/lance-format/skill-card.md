## Description: <br>
Deep reference for Lance v10, the open columnar lakehouse format and engine for multimodal AI, covering file and table formats, indexes, schema evolution, time travel, namespaces, object-store configuration, and performance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when building directly on Lance crates or reading .lance datasets and need grounded guidance on Lance formats, APIs, indexing, storage behavior, and performance tradeoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example shell commands may modify local files or datasets when copied into a terminal. <br>
Mitigation: Review commands before execution and run cleanup or mutation examples only in an isolated test directory. <br>
Risk: Unsafe external blob settings can expose untrusted datasets to files outside expected storage bases. <br>
Mitigation: Avoid allow_external_blob_outside_bases for untrusted datasets unless the storage boundary and file paths have been reviewed. <br>
Risk: Cloud credential examples can lead users to paste real secrets into shared prompts or documentation. <br>
Mitigation: Use placeholder credentials in prompts and docs, and keep real cloud credentials in secret stores or local environment configuration. <br>
Risk: The skill tracks a Lance beta tag and describes unstable or experimental format features. <br>
Mitigation: Pin Lance versions explicitly and verify compatibility before using beta or next-format behavior in production workflows. <br>


## Reference(s): <br>
- [Lance Reference](references/lance-reference.md) <br>
- [Lance Performance Reference](references/performance.md) <br>
- [Lance Format Documentation Mirror](references/docs/format/index.md) <br>
- [Lance Object Store Guide](references/docs/guide/object_store.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/lance-format) <br>
- [OpenClaw Skill Homepage](https://github.com/tenequm/skills/tree/main/skills/lance-format) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only reference skill; no hidden execution or data collection reported by server security evidence.] <br>

## Skill Version(s): <br>
0.12.0 (source: server release metadata, SKILL.md frontmatter, and CHANGELOG, released 2026-07-30) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
