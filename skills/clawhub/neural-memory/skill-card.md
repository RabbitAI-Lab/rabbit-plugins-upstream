## Description: <br>
Associative memory with spreading activation for persistent recall across agent sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nhadaututtheky](https://clawhub.ai/user/nhadaututtheky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to store, recall, and manage facts, decisions, preferences, errors, TODOs, and project context across sessions through local neural-memory tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation content, including sensitive project details or secrets, may be automatically captured and reused across future sessions. <br>
Mitigation: Disable autoCapture and autoContext unless persistent memory is explicitly desired, and avoid storing secrets, regulated data, or private client content. <br>
Risk: Stored memories may persist locally beyond the session and influence later agent behavior. <br>
Mitigation: Inspect and delete stored memories when needed, use separate brains for unrelated projects, and review recalled context before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nhadaututtheky/skills/neural-memory) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration snippets, and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local memory setup guidance, OpenClaw plugin configuration, MCP configuration, and examples for memory storage and recall.] <br>

## Skill Version(s): <br>
4.60.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
