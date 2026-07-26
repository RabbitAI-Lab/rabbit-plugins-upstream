## Description: <br>
Memory Lifecycle guides agents through durable memory capture, promotion, compaction, retrieval, and project workspace setup for OpenClaw-style memory files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hanningwang](https://clawhub.ai/user/hanningwang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to maintain durable workspace memory for preferences, corrections, decisions, team facts, research, and project context across sessions. It is intended for workspaces where persistent memory is desired and regularly reviewed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can silently save and reuse conversation details across sessions, including implied preferences or project facts. <br>
Mitigation: Enable it only in workspaces where durable memory is wanted, review the memoryFlush configuration before use, and periodically inspect MEMORY.md and memory/. <br>
Risk: Sensitive information could be retained if conversation content is copied into memory files. <br>
Mitigation: Follow the skill's credential handling rule: do not store credentials, API keys, tokens, or connection strings; replace them with location pointers. <br>
Risk: Stale or incorrect memories can affect future agent responses. <br>
Mitigation: Use the documented promote, compact, conflict-resolution, and verification steps; keep source dates on entries and verify disputed memories against daily files or memory search. <br>


## Reference(s): <br>
- [Memory Lifecycle ClawHub page](https://clawhub.ai/hanningwang/memory-lifecycle) <br>
- [Init execution checklist](references/init.md) <br>
- [Flush prompt configuration](references/flush-prompt.md) <br>
- [Promote and compact checklists](references/promote-compact.md) <br>
- [Workspace init checklist](references/workspace-init.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance, Files] <br>
**Output Format:** [Markdown guidance with configuration snippets and file update instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update MEMORY.md, daily memory files, project workspace files, backups, and lifecycle logs when used by an agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
