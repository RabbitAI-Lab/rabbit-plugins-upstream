## Description: <br>
Reference skill for Lance v9, the open columnar lakehouse format for multimodal AI, covering Lance crates, dataset and file formats, indexes, MemWAL, schema evolution, versioning, object-store configuration, and related engineering guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to answer implementation questions about Lance datasets, file and table formats, indexes, versioning, concurrency, performance, and object-store behavior when building directly on Lance crates or bindings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may surface cleanup commands, external blob URI settings, non-TLS object-store options, or trace logging settings that affect data retention or exposure. <br>
Mitigation: Review generated commands and configuration against the data sensitivity, object-store policy, and working directory before applying them. <br>
Risk: Some Lance guidance is version-specific and may describe beta or unstable format behavior. <br>
Mitigation: Pin the intended Lance version and verify reader and writer compatibility before changing persistent datasets or indexes. <br>


## Reference(s): <br>
- [Lance Format ClawHub Skill](https://clawhub.ai/tenequm/skills/lance-format) <br>
- [Lance Format Source Homepage](https://github.com/tenequm/skills/tree/main/skills/lance-format) <br>
- [Lance Reference](references/lance-reference.md) <br>
- [Lance Performance Reference](references/performance.md) <br>
- [Lance Format Documentation Mirror](references/docs/format/index.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; answers should load the relevant bundled reference files before giving version-specific guidance.] <br>

## Skill Version(s): <br>
0.11.1 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
