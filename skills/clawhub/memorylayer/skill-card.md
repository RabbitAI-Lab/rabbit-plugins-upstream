## Description: <br>
Semantic memory for AI agents. 95% token savings with vector search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[khli01](https://clawhub.ai/user/khli01) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use MemoryLayer to add semantic long-term memory to AI agents, storing and recalling episodic, semantic, and procedural memories through JavaScript or Python wrappers. It helps retrieve relevant memory context for prompts instead of loading full memory files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected memories, metadata, and search queries are sent to MemoryLayer or a configured remote endpoint. <br>
Mitigation: Use a scoped API key, avoid storing secrets, tokens, regulated data, private documents, or sensitive operational procedures, and review what the agent sends. <br>
Risk: Retrieved memories can influence agent actions even when they are stale, irrelevant, or inaccurate. <br>
Mitigation: Review retrieved memories before allowing them to steer important agent actions, and limit stored memories to information appropriate for the use case. <br>


## Reference(s): <br>
- [MemoryLayer homepage](https://memorylayer.clawbot.hk) <br>
- [MemoryLayer documentation](https://memorylayer.clawbot.hk/docs) <br>
- [MemoryLayer API reference](https://memorylayer.clawbot.hk/api) <br>
- [ClawHub skill page](https://clawhub.ai/khli01/skills/memorylayer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Code] <br>
**Output Format:** [Markdown context strings and JSON-like memory API responses from JavaScript or Python wrappers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns relevant memories with relevance scores; stores memory content, memory type, importance, and metadata through a remote service.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
