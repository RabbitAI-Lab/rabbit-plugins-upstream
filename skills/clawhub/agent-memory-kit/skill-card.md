## Description: <br>
Provides a structured AI agent memory system separating episodic, semantic, and procedural memories to preserve knowledge and processes over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryancampbell](https://clawhub.ai/user/ryancampbell) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to set up local long-term memory, record decisions and procedures, and search prior context across memory files. It is most useful for agents that need continuity across sessions, compactions, and repeated workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local memory files can accumulate private notes, sensitive procedures, personal data, or secrets. <br>
Mitigation: Treat memory files as private workspace data and avoid storing passwords, API keys, tokens, raw private conversations, personal data, or sensitive internal procedures. <br>
Risk: Installation and maintenance guidance includes shell commands, PATH changes, and deletion commands. <br>
Mitigation: Review commands before running them, especially PATH edits and file deletion commands, and run them only in the intended workspace. <br>
Risk: Persisted procedures and memories may become stale or encode earlier mistakes. <br>
Mitigation: Review memory entries during normal use, update procedures after successful runs, and use feedback logs to mark failures and corrections. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ryancampbell/skills/agent-memory-kit) <br>
- [README.md](artifact/README.md) <br>
- [SEARCH.md](artifact/SEARCH.md) <br>
- [INSTALLATION.md](artifact/INSTALLATION.md) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, templates, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local memory files; optional search helpers can produce text or JSON results.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release evidence, released 2026-02-04; CHANGELOG.md also lists 2.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
