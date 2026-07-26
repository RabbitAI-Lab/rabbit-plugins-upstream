## Description: <br>
Agent & MCP integration. CAN stamps what flows through any pipe. Verify, name, log locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xccx](https://clawhub.ai/user/xccx) <br>

### License/Terms of Use: <br>
Public Domain <br>


## Use Case: <br>
Developers and agent builders use this skill to stamp, verify, and locally log data retrieved through MCP tools or other transports. It supports local audit trails, tamper evidence, and recall of prior tool outputs without requiring MCP server integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill encourages agents to write persistent local records and optionally cached payloads under ~/.can, which can retain secrets, credentials, personal data, regulated data, or sensitive MCP/API results. <br>
Mitigation: Only log data intended for persistent local retention, avoid secrets and sensitive results, and protect or delete ~/.can according to the deployment's data handling requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xccx/skills/can) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local timestamp, hash, and label logging patterns for agent workflows.] <br>

## Skill Version(s): <br>
1.9.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
