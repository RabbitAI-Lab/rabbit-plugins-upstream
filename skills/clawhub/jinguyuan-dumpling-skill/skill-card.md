## Description: <br>
This skill helps agents query official Jinguyuan restaurant information and queue status, provide visit guidance, and perform confirmed online queue actions such as taking, checking, or canceling a number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinguyuan](https://clawhub.ai/user/jinguyuan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to answer questions about Jinguyuan restaurant locations, hours, delivery, recommendations, current or historical queue information, and takeout options. With explicit user confirmation, agents can also guide Meituan authorization and perform live queue booking, personal queue checks, or cancellation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use Meituan and Jinguyuan login flows and store local tokens and device or claim state under ~/.jinguyuan. <br>
Mitigation: Install only when this local credential storage is acceptable; do not display tokens, and use the provided logout flows to clear local authorization when needed. <br>
Risk: Authorization may start a temporary background poller and show QR-code or link based login artifacts. <br>
Mitigation: Use the documented auth-start and auth-status flow, present only the generated login link or QR image to the user, and avoid blocking authorization polling in the conversation. <br>
Risk: The skill can perform live queue booking or cancellation for a restaurant account. <br>
Mitigation: Require current, explicit user confirmation before booking or canceling, then execute only the confirmed action with the CLI confirmation flag. <br>
Risk: Security evidence flags under-disclosed prize, lottery, and diagnostic tooling for review before installation. <br>
Mitigation: Review the prize, lottery, and diagnostic scripts before deployment, especially if those features are not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinguyuan/skills/jinguyuan-dumpling-skill) <br>
- [Jinguyuan official website](https://jinguyuan.cloud) <br>
- [Jinguyuan MCP endpoint](https://mcp.jinguyuan.cloud) <br>
- [GitHub repository](https://github.com/JinGuYuan/jinguyuan-dumpling-skill) <br>
- [Gitee repository](https://gitee.com/JinGuYuan/jinguyuan-dumpling-skill) <br>
- [API reference](artifact/references/api-reference.md) <br>
- [Queue reply contract](artifact/references/queue-reply-contract.md) <br>
- [Queue actions reference](artifact/references/queue-actions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and JSON results from bundled Node.js CLI tools] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18 or higher for local CLI actions; live queue booking and cancellation require explicit user confirmation.] <br>

## Skill Version(s): <br>
3.0.0 (source: frontmatter, skill.json, package.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
