## Description: <br>
金谷园饺子馆 Skill helps an agent retrieve restaurant information, queue status, visit guidance, recommendations, pickup details, and explicit Meituan queue actions for the named restaurant. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinguyuan](https://clawhub.ai/user/jinguyuan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and their agents use this skill to answer questions about JinGuYuan Dumpling Restaurant and, after explicit confirmation, take, check, or cancel Meituan queue numbers for supported store locations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meituan account authorization and persistent local token storage are required for real queue actions. <br>
Mitigation: Use authorization only for explicit queue tasks and run logout after use to clear the local Meituan token. <br>
Risk: The bundled Meituan login/signing component is security-sensitive and includes under-disclosed device profiling and signing telemetry. <br>
Mitigation: Review the skill before installation and avoid installing it if that behavior is unacceptable for the environment. <br>
Risk: Taking or canceling a queue number can affect a user's real restaurant queue state. <br>
Mitigation: Confirm the store, party size, table type, and action in the current conversation before executing commands with --confirm. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jinguyuan/skills/jinguyuan-dumpling-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/jinguyuan) <br>
- [Official Restaurant Website](https://jinguyuan.cloud) <br>
- [JinGuYuan MCP Endpoint](https://mcp.jinguyuan.cloud) <br>
- [MCP Access](references/mcp-access.md) <br>
- [MCP Reply Contract](references/mcp-reply-contract.md) <br>
- [Queue Actions](references/queue-actions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and structured JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+ for local queue actions; real queue actions require current-turn user confirmation.] <br>

## Skill Version(s): <br>
2.3.0 (source: SKILL.md frontmatter, skill.json, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
