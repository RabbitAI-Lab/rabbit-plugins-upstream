## Description: <br>
Helps agents answer JinGuYuan restaurant questions, retrieve current and historical queue information, and perform explicitly confirmed Meituan queue actions for taking, checking, or canceling a user's number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinguyuan](https://clawhub.ai/user/jinguyuan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and restaurant support agents use this skill to query JinGuYuan store information, menu-related guidance, pickup options, queue status, and future queue advice. With explicit user confirmation, the skill can also guide live queue number taking, personal queue progress checks, and queue cancellation. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Live queue actions can create or cancel a real Meituan queue entry. <br>
Mitigation: Require explicit same-turn user confirmation before any take-number or cancel command, and restate the store, party size, table type, or order being changed. <br>
Risk: Meituan authorization can persist local account tokens under ~/.jinguyuan. <br>
Mitigation: Use authorization only for JinGuYuan queue actions, never display tokens, and use the documented logout flow when the user wants local authorization cleared. <br>
Risk: The bundled Meituan signing dependency is security-sensitive and may collect or persist device-identifying information. <br>
Mitigation: Review the clawscan suspicious verdict before installation and avoid invoking the vendored queue dependency for ordinary public restaurant queries. <br>
Risk: Stale queue snapshots or historical observations could be mistaken for current wait conditions. <br>
Mitigation: Check the freshness field before reporting current queue status, label historical or future advice as reference data, and do not convert waiting table counts into exact minutes. <br>


## Reference(s): <br>
- [API reference](references/api-reference.md) <br>
- [Queue reply contract](references/queue-reply-contract.md) <br>
- [Queue actions](references/queue-actions.md) <br>
- [JinGuYuan official site](https://jinguyuan.cloud) <br>
- [JinGuYuan MCP endpoint](https://mcp.jinguyuan.cloud) <br>
- [ClawHub skill page](https://clawhub.ai/jinguyuan/skills/jinguyuan-dumpling-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown or plain text guidance with inline shell commands and JSON CLI results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Public queries return a single JSON object; live queue actions require explicit confirmation and may use local Meituan authorization files under ~/.jinguyuan.] <br>

## Skill Version(s): <br>
3.1.1 (source: evidence release, skill.json, SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
