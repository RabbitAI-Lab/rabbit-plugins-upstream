## Description: <br>
Automatically monitors and optimizes conversation context by summarizing important information, preserving facts, and reducing older history to prevent context overflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blackworm](https://clawhub.ai/user/blackworm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to keep long OpenClaw conversations within context limits by summarizing prior messages, storing selected facts, and splitting oversized tasks into smaller subtasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation content may be summarized into durable memory files or appended to MEMORY.md. <br>
Mitigation: Use the skill only on conversations suitable for persistence, and disable fact extraction or MEMORY.md updates when handling secrets or sensitive personal or business data. <br>
Risk: Automatic cleanup can remove older context from the active conversation after thresholds are reached. <br>
Mitigation: Review and tune the cleanup thresholds, keep recent-message retention high enough for the workflow, or disable scheduled cleanup until behavior is verified. <br>
Risk: The /optimize-context command reports success using bundled mock messages rather than confirmed live session history. <br>
Mitigation: Verify integration with the real OpenClaw session history before relying on optimization results. <br>


## Reference(s): <br>
- [ClawHub Optimize Context skill page](https://clawhub.ai/blackworm/skills/optimize-context) <br>
- [Context Optimizer package overview](artifact/SKILL.md) <br>
- [Context Optimizer README](artifact/skills/context-optimizer/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Command responses, Markdown summary files, memory updates, and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write context summaries, append remembered facts to MEMORY.md, and return task-splitting status messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact config) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
