## Description: <br>
Helps agents answer questions about JinguYuan Dumpling restaurant information, current and historical queue status, visit timing, pickup, recommended dishes, recipes, news, and confirmed online queue actions through the bundled Node.js CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinguyuan](https://clawhub.ai/user/jinguyuan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and their agents use this skill to get up-to-date JinguYuan Dumpling restaurant details, queue guidance, pickup information, and dining recommendations. With explicit user confirmation, the agent can also guide online queue number, personal queue progress, and queue cancellation flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled CLI contacts JinGuyuan and Meituan/Dianping services for restaurant data and queue actions. <br>
Mitigation: Review the skill before installation and only run live queue, login, cancellation, or prize-binding actions when those account-linked actions are intended. <br>
Risk: Authenticated flows may store local tokens under ~/.jinguyuan. <br>
Mitigation: Avoid sharing token files, use logout on shared machines, and do not expose tokens in chat, logs, or commits. <br>
Risk: Queue booking and cancellation change real account-linked state. <br>
Mitigation: Require explicit same-turn user confirmation before taking a number or canceling an order, and restate the store, party size, and table type or order details before execution. <br>
Risk: The package includes an obfuscated request-signing component. <br>
Mitigation: Treat the vendored signing code as a sensitive dependency and review it before deploying in restricted or high-assurance environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinguyuan/skills/jinguyuan-dumpling-skill) <br>
- [Public API reference](references/api-reference.md) <br>
- [Queue actions reference](references/queue-actions.md) <br>
- [Queue reply contract](references/queue-reply-contract.md) <br>
- [JinguYuan official site](https://jinguyuan.cloud) <br>
- [JinguYuan MCP endpoint](https://mcp.jinguyuan.cloud) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and JSON CLI results when commands are run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18 or higher for bundled CLI operations; authenticated actions may store local tokens under ~/.jinguyuan.] <br>

## Skill Version(s): <br>
3.0.4 (source: SKILL.md frontmatter, skill.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
