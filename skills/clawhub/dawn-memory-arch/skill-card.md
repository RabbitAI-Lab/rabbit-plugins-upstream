## Description: <br>
Dawn Memory Architecture v7 guides agents through a local long-term memory architecture built around a central memory index, structured fact files, semantic retrieval, write-ahead logging, a working buffer, and short-term to long-term promotion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to add durable local memory patterns to an agent workspace, including memory file structure, local vector retrieval, update discipline, and maintenance checklists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to store durable local memory from conversations, including details that may affect future behavior. <br>
Mitigation: Set explicit rules for what may be saved, require confirmation before writing conversation-derived memories, and periodically review or delete created memory files. <br>
Risk: Conversation memory may capture sensitive data or identifiers if boundaries are not configured before use. <br>
Mitigation: Exclude sensitive data, credentials, tokens, and unnecessary identifiers from memory files. <br>
Risk: Automatic updates to future-behavior files can preserve incorrect or stale guidance. <br>
Mitigation: Review memory changes before deployment and keep cleanup routines for outdated, incorrect, or low-value memories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/dawn-memory-arch) <br>
- [memory-architecture-v7-guide.md](artifact/memory-architecture-v7-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Configuration, Guidance, Shell commands] <br>
**Output Format:** [Markdown guidance with directory structures, JSON examples, and setup checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local-memory architecture guidance; it does not call external APIs.] <br>

## Skill Version(s): <br>
7.1.0 (source: server release evidence; artifact text states v7.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
