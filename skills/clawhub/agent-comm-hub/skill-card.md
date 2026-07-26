## Description: <br>
Local multi-agent communication hub over MCP stdio and HTTP-SSE that provides messaging, task orchestration, shared memory, an evolution engine, 58 MCP tools, and a web management panel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuboacean](https://clawhub.ai/user/liuboacean) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect multiple local AI agents through a hub for message passing, task assignment, shared context retrieval, and operational monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent messages, tasks, or automation triggers may be exposed without enough identity scoping or user review. <br>
Mitigation: Install only where the hub operator and participating agents are trusted, bind the service to localhost or a protected network, require Bearer authentication for SSE and REST endpoints, enforce agent_id matching the authenticated identity, and use a policy gate before automatic task execution. <br>
Risk: Connecting to untrusted hub servers or running maintenance scripts against production data can expose or damage sensitive agent state. <br>
Mitigation: Do not point HUB_URL at untrusted servers, and back up real databases before running tests, migration scripts, or database repair utilities. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liuboacean/skills/agent-comm-hub) <br>
- [Model Context Protocol specification](https://spec.modelcontextprotocol.io) <br>
- [API Reference](docs/API_REFERENCE.md) <br>
- [English README](docs/README_EN.md) <br>
- [Advanced Orchestration Guide](docs/advanced-orchestration-guide.md) <br>
- [ADR-0001: SSE Reliable Delivery](docs/adr/0001-sse-reliable-delivery.md) <br>
- [ADR-0002: Activation State Persistence](docs/adr/0002-activation-state-persistence.md) <br>
- [Hub DB Split Three-Layer Protection](docs/hub-db-split-three-layer-protection.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, API/tool call examples, and status text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local hub data such as messages, tasks, memories, audit records, and attachments when connected to a running Hub.] <br>

## Skill Version(s): <br>
3.0.22 (source: frontmatter, package.json, changelog, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
