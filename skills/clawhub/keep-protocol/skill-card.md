## Description: <br>
Signed Protobuf packets over TCP for AI agent-to-agent communication with MCP tools, ed25519-authenticated messaging, discovery, routing, and memory sharing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nteg-dev](https://clawhub.ai/user/nteg-dev) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let AI agents exchange signed TCP/Protobuf packets, discover peers, route messages, and share optional memory payloads through an MCP or Python SDK workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start server software automatically through Docker or a Go fallback. <br>
Mitigation: Prefer a manually started, pinned, and audited keep server rather than letting an agent call keep_ensure_server. <br>
Risk: Server setup behavior can remove a local Docker container bound to the configured port. <br>
Mitigation: Review the target port and existing containers before using auto-bootstrap behavior. <br>
Risk: Packet bodies or scar data may contain secrets or private memory shared with other agents or logged by the server. <br>
Mitigation: Do not send secrets or private memory in packet bodies or scar data; review server logs and stop background processes after use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nteg-dev/skills/keep-protocol) <br>
- [Skill Instructions](artifact/SKILL.md) <br>
- [Agent Integration Guide](artifact/AGENTS.md) <br>
- [Project README](artifact/README.md) <br>
- [Python Package Metadata](artifact/python/pyproject.toml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration snippets, and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke MCP tools or generate SDK usage that communicates with a local keep server.] <br>

## Skill Version(s): <br>
1.1.1 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
