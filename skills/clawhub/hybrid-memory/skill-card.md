## Description: <br>
Hybrid Memory helps agents choose between OpenClaw vector memory and Graphiti temporal knowledge graph recall for document, conversation, temporal, and entity-tracking questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawdbrunner](https://clawhub.ai/user/clawdbrunner) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to guide memory recall decisions across OpenClaw's built-in memory search and Graphiti temporal memory. It is intended for agents that need to retrieve past context, answer time-based questions, search memory files, or log durable facts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent Graphiti memory can store personal or project facts that users did not intend to retain. <br>
Mitigation: Before enabling the skill, define what information may be stored and confirm how stored memories can be inspected or deleted. <br>
Risk: The skill depends on external setup and helper scripts for Graphiti memory behavior. <br>
Mitigation: Review the linked setup guide and helper scripts before deployment. <br>


## Reference(s): <br>
- [OpenClaw Graphiti Memory setup guide](https://github.com/clawdbrunner/openclaw-graphiti-memory) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes recall between memory_search, memory_get, and Graphiti helper commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
