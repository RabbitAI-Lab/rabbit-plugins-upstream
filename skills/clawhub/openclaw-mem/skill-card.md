## Description: <br>
Guides agents through setup, optimization, and troubleshooting for OpenClaw memory files, memory search, compaction survival, and related configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weareallsatoshin](https://clawhub.ai/user/weareallsatoshin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to set up durable Markdown-based memory, tune retrieval, and troubleshoot memory loss, search relevance, and compaction behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable searchable memory can retain secrets, sensitive personal data, or outdated context across sessions. <br>
Mitigation: Review saved memory files before enabling the workflow, avoid storing secrets or sensitive personal data, and keep a process for inspecting, editing, archiving, or deleting entries. <br>
Risk: Silent automatic writes before compaction can preserve information the user did not intend to make durable. <br>
Mitigation: Review the memoryFlush configuration, writable workspace settings, and memory directory before enabling automatic flush behavior. <br>
Risk: Extra memory paths and embedding provider choices can expand what content is indexed or sent to a provider. <br>
Mitigation: Review configured extraPaths and the selected embedding provider, and use only providers and indexed paths approved for the workspace data. <br>


## Reference(s): <br>
- [OpenClaw Memory skill page](https://clawhub.ai/weareallsatoshin/skills/openclaw-mem) <br>
- [QMD backend project](https://github.com/tobi/qmd) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands] <br>
**Output Format:** [Markdown guidance with configuration snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
2.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
