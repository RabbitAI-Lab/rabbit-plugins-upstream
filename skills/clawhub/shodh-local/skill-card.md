## Description: <br>
Shodh Local gives AI agents local offline memory with semantic recall, GTD todo and project tracking, proactive context, and knowledge graph support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[doobidoo](https://clawhub.ai/user/doobidoo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Shodh Local to persist local memory, recall prior context, manage todos and projects, and retrieve proactive context from a localhost Shodh-Memory server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist and resurface user information across sessions through a local memory server. <br>
Mitigation: Review stored-memory behavior before installation, avoid saving secrets or sensitive personal data, and confirm how to inspect, disable, and delete stored memories and todos. <br>
Risk: Agent-managed memory may reuse stale or unintended context in future sessions. <br>
Mitigation: Review recalled context before relying on it, and prune or delete outdated memories and todos when they are no longer needed. <br>


## Reference(s): <br>
- [Shodh API Endpoints](reference/api.md) <br>
- [OpenClaw Examples](reference/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls] <br>
**Output Format:** [Markdown with inline curl commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include localhost API endpoints, request headers, memory and todo payloads, and operational guidance for a local memory server.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
