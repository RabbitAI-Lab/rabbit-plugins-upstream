## Description: <br>
金谷园饺子馆信息查询、手机号登录、实体抽奖卡与在线排队取号，通过金谷园官方 API 查询店铺、排队和菜品信息，可揭晓抽奖卡、交付兑奖码、绑定账号并跨设备查询奖品，内置真实排队动作仅用于在线取号、本人排队进度查询、取消排队。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinguyuan](https://clawhub.ai/user/jinguyuan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to answer questions about 金谷园饺子馆, retrieve current restaurant and queue information, handle lottery-card prize flows, and perform user-confirmed online queue actions. The skill is intended for restaurant information lookup and queue workflows tied to 金谷园 services. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The bundled authorization component stores local credentials and performs device-signing or fingerprinting behavior. <br>
Mitigation: Review the skill before installing on a sensitive machine, authorize only accounts you intend to use with this skill, and use the provided logout or token-clearing paths when access is no longer needed. <br>
Risk: Online take-number and cancellation commands can change a live restaurant queue record. <br>
Mitigation: Run those actions only after the user gives explicit same-turn confirmation; the CLI requires --confirm for take-number and cancellation commands. <br>
Risk: Queue snapshots can be stale or unsuitable for personal queue progress. <br>
Mitigation: Check the freshness fields before presenting current queue status and use personal order commands for the user's own queue progress. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinguyuan/skills/jinguyuan-dumpling-skill) <br>
- [Public query API reference](references/api-reference.md) <br>
- [Queue actions reference](references/queue-actions.md) <br>
- [Queue reply contract](references/queue-reply-contract.md) <br>
- [Jinguyuan website](https://jinguyuan.cloud) <br>
- [Jinguyuan MCP service](https://mcp.jinguyuan.cloud) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-backed command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a local QR-code image during Meituan authorization and may store local credentials for authenticated actions.] <br>

## Skill Version(s): <br>
3.0.5 (source: ClawHub release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
