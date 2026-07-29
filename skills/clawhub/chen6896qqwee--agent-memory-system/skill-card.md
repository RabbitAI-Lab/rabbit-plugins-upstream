## Description: <br>
Agent Memory System describes a local three-layer memory architecture for AI agents, combining a MEMORY.md index, structured JSON memory files, SQLite state, LanceDB semantic search, P0-P3 truth hierarchy, and curation, WAL, buffer, and promotion mechanisms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to design local persistent memory for AI agents using a central MEMORY.md index, structured JSON memory files, and a local vector database. It provides guidance for truth hierarchy, curation, write-ahead logging, context buffering, and memory promotion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can retain sensitive personal or work information if an agent stores it without review. <br>
Mitigation: Review the created memory files and local database contents periodically, minimize sensitive entries, and delete incorrect or unnecessary memories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/agent-memory-system) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, text] <br>
**Output Format:** [Markdown guidance with file and storage architecture descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local-only memory architecture; no code, commands, external APIs, or hidden behavior are included in the release artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
