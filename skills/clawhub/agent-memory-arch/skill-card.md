## Description: <br>
Three-layer storage plus four mechanisms and a P0-P3 truth hierarchy for AI agent long-term memory using local filesystem storage, SQLite, and LanceDB without external APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to design and maintain persistent local memory for AI agents, including a central memory index, structured fact files, local semantic search, write-ahead logging, and context management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can retain sensitive preferences, project details, or client data in MEMORY.md, memory/, state.db, or the vector index. <br>
Mitigation: Review and limit what the agent writes to local memory stores, avoid storing secrets or regulated data, and periodically inspect or prune retained memory files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/agent-memory-arch) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with filesystem layout, storage rules, and deployment checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No external API dependency; intended outputs describe local MEMORY.md, memory/, SQLite, and LanceDB setup.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
