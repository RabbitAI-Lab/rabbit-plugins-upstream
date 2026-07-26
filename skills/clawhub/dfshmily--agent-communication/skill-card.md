## Description: <br>
Agent Communication provides WebSocket and file-backed messaging, broadcast, status synchronization, offline queues, and shared workspace helpers for coordinating multiple agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[DFshmily](https://clawhub.ai/user/DFshmily) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate multi-agent workflows with direct messages, broadcasts, agent status updates, offline queues, and shared workspace data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The broker can expose real-time agent messaging and shared data in a network-reachable environment. <br>
Mitigation: Bind the broker to localhost unless remote access is required, and add authentication, TLS, or firewall controls before shared or remote use. <br>
Risk: Agent messages and workspace data may persist sensitive information. <br>
Mitigation: Avoid sending secrets through messages or shared workspace data, and review retention and cleanup practices before deployment. <br>
Risk: Server security evidence reports path traversal concerns for agent_id, to, and key inputs. <br>
Mitigation: Inspect and harden path handling for those inputs before using the skill in shared or network-reachable environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/DFshmily/agent-communication) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Test report](artifact/TEST_REPORT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands, Python snippets, and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update message, status, and workspace JSON files under the skill data directory.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
