## Description: <br>
Provides commands for interacting with a local Logseq instance through its Plugin API to read, create, update, query, and automate graph content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Logseq users use this skill to generate commands, code snippets, and workflow guidance for automating a locally running Logseq graph through the Plugin API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad reads and edits against a local Logseq graph, including page creation, block updates, deletes, moves, Git commands, and bulk automation. <br>
Mitigation: Use read-only workflows by default, back up the graph before automation, and require explicit user confirmation before any write, delete, move, Git, or bulk operation. <br>
Risk: A generic HTTP bridge can expose Logseq Plugin API actions beyond the intended local automation path. <br>
Mitigation: Avoid generic bridge endpoints unless they are bound to localhost and protected with authentication plus an explicit namespace and method allowlist. <br>
Risk: Automation examples can unintentionally modify many notes or tasks when queries match more graph content than expected. <br>
Mitigation: Preview query matches before mutation, constrain Datalog queries to the intended page or task set, and apply changes in small batches. <br>


## Reference(s): <br>
- [Logseq Plugin API Reference](artifact/references/api-reference.md) <br>
- [Logseq Plugin API Examples](artifact/references/examples.md) <br>
- [Logseq Plugin API Docs](https://logseq.github.io/plugins/) <br>
- [Logseq Plugin Samples](https://github.com/logseq/logseq-plugin-samples) <br>
- [ClawHub Skill Page](https://clawhub.ai/gasgangrene/skills/logseq) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript, TypeScript, Datalog, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local Logseq Plugin API call patterns; require explicit confirmation before writes, deletes, moves, Git commands, or bulk automation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
