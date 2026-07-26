## Description: <br>
A WorkBuddy bridge skill for lobster-memory that records user preferences, project context, relationships, and feedback as a local long-term graph memory with recall and consolidation commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[littlelollipop](https://clawhub.ai/user/littlelollipop) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and WorkBuddy users use this skill to add a local graph-memory layer for durable preferences, project context, and feedback, then recall or consolidate that memory during later work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation-derived preferences, relationships, emotional signals, project context, and feedback into durable local memory without clear consent controls. <br>
Mitigation: Require explicit user confirmation before memory writes, review extraction JSON before saving, and configure the storage directory deliberately. <br>
Risk: The skill depends on a separately installed lobster-memory engine and Python environment. <br>
Mitigation: Trust and review the separate installation before running it, and set LOBSTER_MEMORY_ENGINE and LOBSTER_MEMORY_PYTHON to the intended local paths. <br>
Risk: Consolidation can modify or forget stored graph-memory entries. <br>
Mitigation: Run consolidation in dry-run mode first and keep backups before allowing changes. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/littlelollipop/skills/wb-lobster-memory) <br>
- [Server-resolved source repository](https://github.com/LittleLollipop/wb-lobster-memory) <br>
- [lobster-memory dependency](https://github.com/LittleLollipop/lobster-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Apple Silicon, Python 3.10 or newer, LOBSTER_MEMORY_ENGINE, and LOBSTER_MEMORY_PYTHON; stores graph memory locally.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
