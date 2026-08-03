## Description: <br>
Provides a local long-term agent memory architecture with a MEMORY.md index, structured core JSON files, SQLite state, LanceDB semantic search, WAL discipline, context buffering, and a P0-P3 truth-source hierarchy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to set up a local memory system that records durable facts, session history, working context, and semantic search data while keeping real-time decisions tied to authoritative state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to persist conversation-derived memory locally, which may include profile details, preferences, session summaries, account or trading context, or sensitive content. <br>
Mitigation: Review or constrain what the agent may write, avoid saving secrets, and require explicit confirmation before storing sensitive information. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown instructions with directory structure, operating rules, and a deployment checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes local filesystem, SQLite, and LanceDB memory components with no external API dependency.] <br>

## Skill Version(s): <br>
8.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
